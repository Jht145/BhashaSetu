from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.core.database import get_db
from backend.app.models.translation import TranslationLog
from backend.app.schemas.translation import (
    TranslationRequest,
    TranslationResponse,
    TransliterationRequest,
    TransliterationResponse,
)
from backend.app.services.ai.nmt_service import NMTService
from backend.app.services.ai.olchiki_service import OlChikiService

router = APIRouter()


@router.post("/translate", response_model=TranslationResponse)
async def translate_text(
    req: TranslationRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Translates classroom discourse text between Hindi/English and 9 Jharkhand languages.
    Supports Ol Chiki output for Santhali.
    """
    translated_text, phonetic_deva, latency_ms, confidence = NMTService.translate(
        text=req.text,
        source_language=req.source_language,
        target_language=req.target_language,
        target_script=req.target_script,
    )

    # Log translation for audit & HITL continuous learning
    log = TranslationLog(
        source_language=req.source_language,
        target_language=req.target_language,
        source_script=req.source_script,
        target_script=req.target_script,
        source_text=req.text,
        translated_text=translated_text,
        mode="TEXT",
        latency_ms=latency_ms,
        confidence_score=confidence,
    )
    db.add(log)
    await db.commit()

    return {
        "source_text": req.text,
        "source_language": req.source_language,
        "target_language": req.target_language,
        "target_script": req.target_script,
        "translated_text": translated_text,
        "phonetic_devanagari": phonetic_deva,
        "latency_ms": latency_ms,
        "confidence_score": confidence,
        "model_version": "IndicTrans2-Tribal-v1.0"
    }


@router.post("/transliterate", response_model=TransliterationResponse)
async def transliterate_script(req: TransliterationRequest):
    """
    Dynamic Script Switching: Convert between Devanagari, Ol Chiki, and Latin script.
    """
    converted = OlChikiService.transliterate(
        text=req.text,
        source_script=req.source_script,
        target_script=req.target_script,
    )
    return {
        "original_text": req.text,
        "source_script": req.source_script,
        "target_script": req.target_script,
        "converted_text": converted,
    }
