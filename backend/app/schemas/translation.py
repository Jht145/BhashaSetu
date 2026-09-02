from typing import Optional, List
from pydantic import BaseModel


class TranslationRequest(BaseModel):
    text: str
    source_language: str = "hin"
    target_language: str = "sat"
    source_script: str = "deva"
    target_script: str = "olck"
    domain: str = "education"  # education, general, math, science


class TranslationResponse(BaseModel):
    source_text: str
    source_language: str
    target_language: str
    target_script: str
    translated_text: str
    phonetic_devanagari: Optional[str] = None
    latency_ms: float
    confidence_score: float
    model_version: str


class TransliterationRequest(BaseModel):
    text: str
    source_script: str  # e.g., 'deva' or 'olck' or 'latn'
    target_script: str  # e.g., 'olck' or 'deva' or 'latn'
    language_code: str = "sat"


class TransliterationResponse(BaseModel):
    original_text: str
    source_script: str
    target_script: str
    converted_text: str


class SpeechTranslateRequest(BaseModel):
    source_language: str = "hin"
    target_language: str = "sat"
    target_script: str = "olck"
    audio_base64: Optional[str] = None  # Raw audio input
    generate_speech_output: bool = True


class SpeechTranslateResponse(BaseModel):
    recognized_text: str
    source_language: str
    translated_text: str
    target_language: str
    target_script: str
    phonetic_transcription: Optional[str] = None
    audio_url: Optional[str] = None
    latency_ms: float


class TTSRequest(BaseModel):
    text: str
    language_code: str = "sat"
    script_code: str = "olck"
    speed: float = 1.0


class TTSResponse(BaseModel):
    audio_url: str
    duration_seconds: float
    language_code: str
    file_size_bytes: int
