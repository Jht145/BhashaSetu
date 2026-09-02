import base64
import time
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.translation import TranslationLog
from app.schemas.translation import (
    TTSRequest,
    TTSResponse,
    SpeechTranslateRequest,
    SpeechTranslateResponse,
)
from app.services.ai.asr_service import ASRService
from app.services.ai.nmt_service import NMTService
from app.services.ai.tts_service import TTSService

router = APIRouter()


@router.post("/tts", response_model=TTSResponse)
async def generate_speech(req: TTSRequest):
    """
    Synthesizes speech audio for vernacular text (e.g. Santhali in Ol Chiki or Devanagari).
    """
    audio_url, duration, file_size = TTSService.synthesize_speech(
        text=req.text,
        language_code=req.language_code,
        script_code=req.script_code,
        speed=req.speed,
    )
    return {
        "audio_url": audio_url,
        "duration_seconds": duration,
        "language_code": req.language_code,
        "file_size_bytes": file_size,
    }


@router.post("/duplex-translate", response_model=SpeechTranslateResponse)
async def classroom_duplex_speech_translate(
    req: SpeechTranslateRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Real-time Duplex Classroom Speech Translation Layer:
    Takes teacher/student spoken audio (or simulated stream), performs ASR, NMT, and TTS synthesis.
    Target latency: < 2.0s.
    """
    start_time = time.time()
    
    # 1. ASR - Speech to Text
    audio_bytes = b""
    if req.audio_base64:
        try:
            audio_bytes = base64.b64decode(req.audio_base64)
        except Exception:
            pass
            
    recognized_text, asr_latency = ASRService.transcribe(
        audio_data=audio_bytes,
        source_language=req.source_language
    )

    # 2. NMT - Vernacular Translation
    translated_text, phonetic_deva, nmt_latency, _ = NMTService.translate(
        text=recognized_text,
        source_language=req.source_language,
        target_language=req.target_language,
        target_script=req.target_script,
    )

    # 3. TTS - Speech Synthesis (if requested)
    audio_url = None
    if req.generate_speech_output:
        audio_url, _, _ = TTSService.synthesize_speech(
            text=translated_text,
            language_code=req.target_language,
            script_code=req.target_script,
        )

    total_latency = (time.time() - start_time) * 1000 + asr_latency + nmt_latency

    # Log translation
    log = TranslationLog(
        source_language=req.source_language,
        target_language=req.target_language,
        target_script=req.target_script,
        source_text=recognized_text,
        translated_text=translated_text,
        mode="SPEECH_TO_SPEECH",
        latency_ms=round(total_latency, 2),
    )
    db.add(log)
    await db.commit()

    return {
        "recognized_text": recognized_text,
        "source_language": req.source_language,
        "translated_text": translated_text,
        "target_language": req.target_language,
        "target_script": req.target_script,
        "phonetic_transcription": phonetic_deva,
        "audio_url": audio_url,
        "latency_ms": round(total_latency, 2),
    }
