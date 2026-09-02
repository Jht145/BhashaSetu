from fastapi import APIRouter
from backend.app.api.v1 import (
    auth,
    curriculum,
    translation,
    speech,
    sync,
    hitl,
    analytics,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication & Roles"])
api_router.include_router(curriculum.router, prefix="/curriculum", tags=["Vernacular Pedagogy & Curriculum"])
api_router.include_router(translation.router, prefix="/translation", tags=["NMT & Script Transliteration"])
api_router.include_router(speech.router, prefix="/speech", tags=["ASR, TTS & Duplex Speech"])
api_router.include_router(sync.router, prefix="/sync", tags=["Offline Packaging & Delta Sync"])
api_router.include_router(hitl.router, prefix="/hitl", tags=["Human-in-the-Loop Linguist Portal"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics & KPIs"])
