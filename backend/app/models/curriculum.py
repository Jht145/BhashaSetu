from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.core.database import Base


class CurriculumSubject(Base):
    __tablename__ = "curriculum_subjects"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)  # e.g., 'G1_EVS', 'G3_MATH'
    name = Column(String(100), nullable=False)  # e.g., 'Environmental Studies (Aas Paas)'
    grade = Column(Integer, nullable=False)  # Grades 1 to 5
    curriculum_source = Column(String(50), default="JCERT/NCERT")  # JCERT, NCERT, PALASH

    chapters = relationship("Chapter", back_populates="subject", cascade="all, delete-orphan")


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    chapter_number = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=True)
    subject_id = Column(Integer, ForeignKey("curriculum_subjects.id"), nullable=False)

    subject = relationship("CurriculumSubject", back_populates="chapters")
    concepts = relationship("Concept", back_populates="chapter", cascade="all, delete-orphan")


class Concept(Base):
    __tablename__ = "concepts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    standard_text_hindi = Column(Text, nullable=False)
    standard_text_english = Column(Text, nullable=True)
    pedagogy_keywords = Column(String(255), nullable=True)  # e.g. "trees, water cycle, Sarhul"
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)

    chapter = relationship("Chapter", back_populates="concepts")
    vernacular_versions = relationship("VernacularConcept", back_populates="concept", cascade="all, delete-orphan")


class VernacularConcept(Base):
    __tablename__ = "vernacular_concepts"

    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey("concepts.id"), nullable=False)
    language_code = Column(String(10), nullable=False)  # sat, unr, hoc, kru, khr, kht, sck, etc.
    script_code = Column(String(10), default="olck")  # olck (Ol Chiki), deva, latn, warang, tolong
    
    simplified_title = Column(String(255), nullable=False)
    simplified_explanation = Column(Text, nullable=False)
    cultural_metaphor = Column(Text, nullable=True)  # Local Jharkhand context/metaphor (e.g. Sal tree, Karma festival)
    
    is_verified_by_linguist = Column(Integer, default=0)  # 0=Pending, 1=Verified, -1=Flagged
    quality_score = Column(Float, default=0.0)  # 0.0 - 5.0

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    concept = relationship("Concept", back_populates="vernacular_versions")
    multimodal_assets = relationship("MultimodalAsset", back_populates="vernacular_concept", cascade="all, delete-orphan")


class MultimodalAsset(Base):
    __tablename__ = "multimodal_assets"

    id = Column(Integer, primary_key=True, index=True)
    vernacular_concept_id = Column(Integer, ForeignKey("vernacular_concepts.id"), nullable=False)
    asset_type = Column(String(20), default="AUDIO")  # AUDIO, STORY_IMAGE, SUBTITLE_SRT
    file_path = Column(String(500), nullable=False)
    duration_seconds = Column(Float, nullable=True)
    file_size_bytes = Column(Integer, nullable=True)
    script_content = Column(Text, nullable=True)  # Transcript in native script

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    vernacular_concept = relationship("VernacularConcept", back_populates="multimodal_assets")
