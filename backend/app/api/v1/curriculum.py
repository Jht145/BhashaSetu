from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.core.database import get_db
from app.models.curriculum import (
    CurriculumSubject,
    Chapter,
    Concept,
    VernacularConcept,
    MultimodalAsset,
)
from app.schemas.curriculum import (
    SubjectCreate,
    SubjectResponse,
    ChapterCreate,
    ChapterResponse,
    ConceptCreate,
    ConceptResponse,
    VernacularConceptResponse,
    PedagogySimplificationRequest,
)
from app.services.ai.pedagogy_rag import PedagogyRAGEngine
from app.services.ai.tts_service import TTSService

router = APIRouter()


@router.get("/subjects", response_model=List[SubjectResponse])
async def list_subjects(grade: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    query = select(CurriculumSubject).options(
        selectinload(CurriculumSubject.chapters)
        .selectinload(Chapter.concepts)
        .selectinload(Concept.vernacular_versions)
        .selectinload(VernacularConcept.multimodal_assets)
    )
    if grade is not None:
        query = query.where(CurriculumSubject.grade == grade)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/subjects", response_model=SubjectResponse, status_code=status.HTTP_201_CREATED)
async def create_subject(subject_in: SubjectCreate, db: AsyncSession = Depends(get_db)):
    subject = CurriculumSubject(**subject_in.model_dump())
    db.add(subject)
    await db.commit()
    await db.refresh(subject)
    return subject


@router.post("/chapters", response_model=ChapterResponse, status_code=status.HTTP_201_CREATED)
async def create_chapter(chapter_in: ChapterCreate, db: AsyncSession = Depends(get_db)):
    chapter = Chapter(**chapter_in.model_dump())
    db.add(chapter)
    await db.commit()
    await db.refresh(chapter)
    return chapter


@router.post("/concepts", response_model=ConceptResponse, status_code=status.HTTP_201_CREATED)
async def create_concept(concept_in: ConceptCreate, db: AsyncSession = Depends(get_db)):
    concept = Concept(**concept_in.model_dump())
    db.add(concept)
    await db.commit()
    await db.refresh(concept)
    return concept


@router.post("/pedagogy/simplify", response_model=VernacularConceptResponse)
async def generate_vernacular_pedagogy(
    req: PedagogySimplificationRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    RAG Vernacular Pedagogy Engine: Takes a standard NCERT/JCERT concept,
    simplifies it with Jharkhand cultural metaphors, and generates synchronized text + audio.
    """
    result = await db.execute(select(Concept).where(Concept.id == req.concept_id))
    concept = result.scalars().first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")

    # Generate simplification via Pedagogy RAG Engine
    pedagogy_data = PedagogyRAGEngine.simplify_concept(
        concept_title=concept.title,
        standard_text=concept.standard_text_hindi,
        target_language=req.target_language,
        target_script=req.target_script,
        pedagogy_keywords=concept.pedagogy_keywords or req.context_keywords or ""
    )

    vernacular_concept = VernacularConcept(
        concept_id=concept.id,
        language_code=pedagogy_data["language_code"],
        script_code=pedagogy_data["script_code"],
        simplified_title=pedagogy_data["simplified_title"],
        simplified_explanation=pedagogy_data["simplified_explanation"],
        cultural_metaphor=pedagogy_data["cultural_metaphor"],
        quality_score=pedagogy_data["quality_score"],
        is_verified_by_linguist=1,
    )
    db.add(vernacular_concept)
    await db.commit()
    await db.refresh(vernacular_concept)

    # If audio is requested, generate TTS audio asset
    if req.include_audio:
        audio_url, duration, file_size = TTSService.synthesize_speech(
            text=vernacular_concept.simplified_explanation,
            language_code=req.target_language,
            script_code=req.target_script
        )
        asset = MultimodalAsset(
            vernacular_concept_id=vernacular_concept.id,
            asset_type="AUDIO",
            file_path=audio_url,
            duration_seconds=duration,
            file_size_bytes=file_size,
            script_content=vernacular_concept.simplified_explanation
        )
        db.add(asset)
        await db.commit()

    # Query with relationship loaded
    loaded_result = await db.execute(
        select(VernacularConcept)
        .options(selectinload(VernacularConcept.multimodal_assets))
        .where(VernacularConcept.id == vernacular_concept.id)
    )
    return loaded_result.scalars().first()
