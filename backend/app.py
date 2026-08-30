"""
BhashaSetu FastAPI Application Server
"""

import os
from fastapi import FastAPI, Query, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

from backend.data.languages import LANGUAGES
from backend.data.dictionary import CATEGORIES, VOCABULARY
from backend.data.stories import STORIES
from backend.data.quizzes import QUIZZES, MATCH_GAMES
from backend.data.scripts_data import OL_CHIKI_CHARS, WARANG_CITI_CHARS
from backend.services.translator import translator_service

app = FastAPI(
    title="BhashaSetu API",
    description="Language translation & learning web app for Hindi to Tribal & Regional Languages",
    version="1.0.0"
)

# Enable CORS for development flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str = "santhali"
    translate_all: bool = False

@app.get("/api/languages")
def get_languages():
    """Returns metadata for all 9 supported tribal and regional languages."""
    return {
        "count": len(LANGUAGES),
        "tribal_count": sum(1 for l in LANGUAGES.values() if l["type"] == "tribal"),
        "regional_count": sum(1 for l in LANGUAGES.values() if l["type"] == "regional"),
        "languages": LANGUAGES
    }

@app.post("/api/translate")
def translate(req: TranslationRequest):
    """
    Translates input Hindi text to a target language or all 9 languages.
    """
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if req.translate_all:
        return translator_service.translate_all_languages(req.text)
    else:
        return translator_service.translate_single(req.text, req.target_language)

@app.get("/api/categories")
def get_categories():
    """Returns all dictionary categories."""
    return {"categories": CATEGORIES}

@app.get("/api/dictionary")
def get_dictionary(category: Optional[str] = None):
    """Returns vocabulary words, optionally filtered by category."""
    items = translator_service.get_category_items(category)
    return {
        "category": category or "all",
        "total": len(items),
        "items": items
    }

@app.get("/api/dictionary/search")
def search_dictionary(q: str = Query(..., min_length=1)):
    """Search for terms across Hindi and target languages."""
    results = translator_service.search_dictionary(q)
    return {
        "query": q,
        "count": len(results),
        "results": results
    }

@app.get("/api/stories")
def get_stories():
    """Returns bilingual illustrated folk stories."""
    return {"stories": STORIES}

@app.get("/api/quizzes")
def get_quizzes():
    """Returns gamified quizzes and word-match pairs."""
    return {
        "quizzes": QUIZZES,
        "match_games": MATCH_GAMES
    }

@app.get("/api/scripts")
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

# Mount static frontend files
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
