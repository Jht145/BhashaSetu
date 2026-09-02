import os
import json
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.app.core.config import settings
from backend.app.core.database import get_db
from backend.app.models.hitl import ReviewTask, ReviewStatus, CorrectionHistory, LoRADatasetExport
from backend.app.models.user import User, UserRole
from backend.app.schemas.hitl import (
    ReviewTaskResponse,
    ReviewTaskSubmit,
    LoRADatasetExportResponse,
)
from backend.app.api.v1.auth import get_current_user

router = APIRouter()


@router.get("/tasks", response_model=List[ReviewTaskResponse])
async def list_review_tasks(
    language_code: Optional[str] = None,
    status_filter: Optional[ReviewStatus] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Linguist Portal Task Queue: List translation / phonetic verification items.
    """
    query = select(ReviewTask)
    if language_code:
        query = query.where(ReviewTask.language_code == language_code)
    if status_filter:
        query = query.where(ReviewTask.status == status_filter)
    
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/tasks/submit", response_model=ReviewTaskResponse)
async def submit_linguist_review(
    review_in: ReviewTaskSubmit,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Certified linguist verifies, scores (BLEU/accuracy), and corrects automated translations.
    """
    result = await db.execute(select(ReviewTask).where(ReviewTask.id == review_in.task_id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Review task not found")

    # If linguist corrected the translation, log correction history
    if review_in.corrected_translation and review_in.corrected_translation != task.machine_translation:
        history = CorrectionHistory(
            review_task_id=task.id,
            previous_text=task.machine_translation,
            new_text=review_in.corrected_translation,
            field_modified="translation",
        )
        db.add(history)
        task.corrected_translation = review_in.corrected_translation

    task.status = review_in.status
    task.accuracy_score = review_in.accuracy_score
    task.cultural_appropriateness_score = review_in.cultural_appropriateness_score
    task.notes = review_in.notes
    task.reviewer_audio_feedback = review_in.reviewer_audio_feedback
    task.reviewer_id = current_user.id
    task.reviewed_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(task)
    return task


@router.post("/export-lora-dataset", response_model=LoRADatasetExportResponse)
async def export_lora_dataset(
    language_code: str = "sat",
    db: AsyncSession = Depends(get_db)
):
    """
    Active Learning Export: Compiles approved linguist corrections into a LoRA fine-tuning JSONL dataset.
    """
    query = select(ReviewTask).where(
        ReviewTask.language_code == language_code,
        ReviewTask.status.in_([ReviewStatus.APPROVED, ReviewStatus.CORRECTED])
    )
    result = await db.execute(query)
    tasks = result.scalars().all()

    export_samples = []
    for t in tasks:
        target_text = t.corrected_translation if t.corrected_translation else t.machine_translation
        export_samples.append({
            "instruction": f"Translate into {t.language_code} ({t.script_code}):",
            "input": t.source_text,
            "output": target_text,
            "accuracy_score": t.accuracy_score or 5.0
        })

    version_tag = f"{language_code}-lora-{int(datetime.now(timezone.utc).timestamp())}"
    file_name = f"{version_tag}.jsonl"
    file_path = os.path.join(settings.BASE_DIR, "data", file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        for s in export_samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    dataset_export = LoRADatasetExport(
        version_tag=version_tag,
        language_code=language_code,
        sample_count=len(export_samples),
        file_path=file_path,
        is_exported=True,
    )
    db.add(dataset_export)
    await db.commit()
    await db.refresh(dataset_export)
    return dataset_export
