from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean
from app.core.database import Base


class TranslationLog(Base):
    __tablename__ = "translation_logs"

    id = Column(Integer, primary_key=True, index=True)
    source_language = Column(String(10), nullable=False)
    target_language = Column(String(10), nullable=False)
    source_script = Column(String(10), default="deva")
    target_script = Column(String(10), default="olck")
    
    source_text = Column(Text, nullable=False)
    translated_text = Column(Text, nullable=False)
    
    mode = Column(String(20), default="TEXT")  # TEXT, SPEECH_TO_TEXT, SPEECH_TO_SPEECH
    latency_ms = Column(Float, nullable=True)
    model_version = Column(String(50), default="IndicTrans2-Tribal-v1.0")
    confidence_score = Column(Float, default=0.95)
    
    is_reviewed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class PhoneticGlossary(Base):
    __tablename__ = "phonetic_glossaries"

    id = Column(Integer, primary_key=True, index=True)
    language_code = Column(String(10), nullable=False)  # sat, unr, hoc, etc.
    word_hindi = Column(String(100), nullable=False)
    word_native_script = Column(String(100), nullable=False)  # e.g., Ol Chiki
    word_devanagari_phonetic = Column(String(100), nullable=False)
    ipa_phonetics = Column(String(100), nullable=True)
    category = Column(String(50), default="science")  # science, math, nature, daily
