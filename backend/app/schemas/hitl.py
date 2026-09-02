from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.hitl import ReviewStatus


class ReviewTaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    task_type: str
    language_code: str
    script_code: str
    source_text: str
    machine_translation: str
    corrected_translation: Optional[str] = None
    audio_asset_path: Optional[str] = None
    status: ReviewStatus
    accuracy_score: Optional[float] = None
    cultural_appropriateness_score: Optional[float] = None
    notes: Optional[str] = None
    reviewer_id: Optional[int] = None
    created_at: datetime


class ReviewTaskSubmit(BaseModel):
    task_id: int
    status: ReviewStatus  # APPROVED, REJECTED, CORRECTED
    corrected_translation: Optional[str] = None
    accuracy_score: float  # 1.0 - 5.0
    cultural_appropriateness_score: float  # 1.0 - 5.0
    notes: Optional[str] = None
    reviewer_audio_feedback: Optional[str] = None


class LoRADatasetExportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    version_tag: str
    language_code: str
    sample_count: int
    file_path: str
    is_exported: bool
    exported_at: datetime
