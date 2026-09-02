"""
Web Frontend API Endpoints for BhashaSetu
Provides dictionary, translation, stories, quizzes, and script data for the web UI.
"""

from typing import Optional, List
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel

from backend.data.languages import LANGUAGES
from backend.data.dictionary import CATEGORIES, VOCABULARY
from backend.data.stories import STORIES
from backend.data.quizzes import QUIZZES, MATCH_GAMES
from backend.data.scripts_data import OL_CHIKI_CHARS, WARANG_CITI_CHARS
from backend.services.translator import translator_service

router = APIRouter()


class TranslationRequest(BaseModel):
    text: str
    target_language: str = "santhali"
    source_language: Optional[str] = "hin_Deva"
    translate_all: bool = False


@router.get("/languages", tags=["Web Frontend"])
def get_languages():
    """Returns metadata for all 9 supported tribal and regional languages."""
    return {
        "count": len(LANGUAGES),
        "tribal_count": sum(1 for l in LANGUAGES.values() if l["type"] == "tribal"),
        "regional_count": sum(1 for l in LANGUAGES.values() if l["type"] == "regional"),
        "languages": LANGUAGES
    }


@router.post("/translate", tags=["Web Frontend"])
def translate(req: TranslationRequest):
    """
    Translates input Hindi/English text to a target language or all 9 languages.
    """
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if req.translate_all:
        return translator_service.translate_all_languages(req.text)
    else:
        return translator_service.translate_single(req.text, req.target_language, req.source_language)


@router.get("/categories", tags=["Web Frontend"])
def get_categories():
    """Returns all dictionary categories."""
    return {"categories": CATEGORIES}


@router.get("/dictionary", tags=["Web Frontend"])
def get_dictionary(category: Optional[str] = None):
    """Returns vocabulary words, optionally filtered by category."""
    items = translator_service.get_category_items(category)
    return {
        "category": category or "all",
        "total": len(items),
        "items": items
    }


@router.get("/dictionary/search", tags=["Web Frontend"])
def search_dictionary(q: str = Query(..., min_length=1)):
    """Search for terms across Hindi and target languages."""
    results = translator_service.search_dictionary(q)
    return {
        "query": q,
        "count": len(results),
        "results": results
    }


@router.get("/stories", tags=["Web Frontend"])
def get_stories():
    """Returns bilingual illustrated folk stories."""
    return {"stories": STORIES}


@router.get("/quizzes", tags=["Web Frontend"])
def get_quizzes():
    """Returns gamified quizzes and word-match pairs."""
    return {
        "quizzes": QUIZZES,
        "match_games": MATCH_GAMES
    }


@router.get("/scripts", tags=["Web Frontend"])
def get_scripts():
    """Returns script character cards for Ol Chiki and Warang Citi."""
    return {
        "ol_chiki": {
            "name": "Ol Chiki (ᱚᱞ ᱪᱤᱠᱤ)",
            "language": "Santhali",
            "creator": "Pandit Raghunath Murmu (1925)",
            "characters": OL_CHIKI_CHARS
        },
        "warang_citi": {
            "name": "Warang Citi (𑢹𑣗𑢭 𑢔𑢫𑢵𑢸)",
            "language": "Ho",
            "creator": "Lako Bodra (1940s)",
            "characters": WARANG_CITI_CHARS
        }
    }
