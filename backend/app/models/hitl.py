import enum
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.app.core.database import Base


class ReviewStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    CORRECTED = "CORRECTED"


class ReviewTask(Base):
    __tablename__ = "review_tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_type = Column(String(50), default="TRANSLATION_VERIFICATION")  # TRANSLATION_VERIFICATION, PHONETIC_AUDIO, SCRIPT_CHECK
    language_code = Column(String(10), nullable=False)
    script_code = Column(String(10), default="olck")
    
    source_text = Column(Text, nullable=False)
    machine_translation = Column(Text, nullable=False)
    corrected_translation = Column(Text, nullable=True)
    
    audio_asset_path = Column(String(500), nullable=True)
    reviewer_audio_feedback = Column(Text, nullable=True)
    
    status = Column(Enum(ReviewStatus), default=ReviewStatus.PENDING, nullable=False)
    accuracy_score = Column(Float, nullable=True)  # 1.0 to 5.0
    cultural_appropriateness_score = Column(Float, nullable=True)  # 1.0 to 5.0
    notes = Column(Text, nullable=True)
    
    reviewer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    reviewed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    reviewer = relationship("User", back_populates="reviews")
    corrections = relationship("CorrectionHistory", back_populates="review_task", cascade="all, delete-orphan")


class CorrectionHistory(Base):
    __tablename__ = "correction_histories"

    id = Column(Integer, primary_key=True, index=True)
    review_task_id = Column(Integer, ForeignKey("review_tasks.id"), nullable=False)
    previous_text = Column(Text, nullable=False)
    new_text = Column(Text, nullable=False)
    field_modified = Column(String(50), default="translation")
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    review_task = relationship("ReviewTask", back_populates="corrections")


class LoRADatasetExport(Base):
    __tablename__ = "lora_dataset_exports"

    id = Column(Integer, primary_key=True, index=True)
    version_tag = Column(String(50), unique=True, index=True, nullable=False)  # e.g., "sat-lora-dataset-v1.1"
    language_code = Column(String(10), nullable=False)
    sample_count = Column(Integer, default=0)
    file_path = Column(String(500), nullable=False)
    is_exported = Column(Boolean, default=True)
    exported_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
