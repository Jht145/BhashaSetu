from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MultimodalAssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    asset_type: str
    file_path: str
    duration_seconds: Optional[float] = None
    file_size_bytes: Optional[int] = None
    script_content: Optional[str] = None


class VernacularConceptCreate(BaseModel):
    concept_id: int
    language_code: str
    script_code: str = "olck"
    simplified_title: str
    simplified_explanation: str
    cultural_metaphor: Optional[str] = None


class VernacularConceptResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    concept_id: int
    language_code: str
    script_code: str
    simplified_title: str
    simplified_explanation: str
    cultural_metaphor: Optional[str] = None
    is_verified_by_linguist: int
    quality_score: float
    multimodal_assets: List[MultimodalAssetResponse] = []


class ConceptCreate(BaseModel):
    title: str
    standard_text_hindi: str
    standard_text_english: Optional[str] = None
    pedagogy_keywords: Optional[str] = None
    chapter_id: int


class ConceptResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    standard_text_hindi: str
    standard_text_english: Optional[str] = None
    pedagogy_keywords: Optional[str] = None
    chapter_id: int
    vernacular_versions: List[VernacularConceptResponse] = []


class ChapterCreate(BaseModel):
    chapter_number: int
    title: str
    summary: Optional[str] = None
    subject_id: int


class ChapterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chapter_number: int
    title: str
    summary: Optional[str] = None
    subject_id: int
    concepts: List[ConceptResponse] = []


class SubjectCreate(BaseModel):
    code: str
    name: str
    grade: int
    curriculum_source: str = "JCERT/NCERT"


class SubjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    name: str
    grade: int
    curriculum_source: str
    chapters: List[ChapterResponse] = []


class PedagogySimplificationRequest(BaseModel):
    concept_id: int
    target_language: str = "sat"
    target_script: str = "olck"
    include_audio: bool = True
    context_keywords: Optional[str] = None
