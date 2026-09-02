import os
from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "BhashaSetu API"
    PROJECT_CODE: str = "SIH26042"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "bhashasetu-super-secret-key-for-jwt-signing-jharkhand-sih2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days for low connectivity teachers

    # Database
    # Defaults to async SQLite for out-of-the-box local operation; easily configured for PostgreSQL/pgvector
    DATABASE_URL: str = "sqlite+aiosqlite:///./bhashasetu.db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Storage Paths
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    MEDIA_DIR: str = os.path.join(BASE_DIR, "data", "media")
    OFFLINE_PACKS_DIR: str = os.path.join(BASE_DIR, "data", "packs")
    FONTS_DIR: str = os.path.join(BASE_DIR, "data", "fonts")

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:5173",
        "*"
    ]

    # Target Languages Matrix in Jharkhand
    SUPPORTED_LANGUAGES: dict = {
        "sat": {"name": "Santhali", "scripts": ["olck", "deva", "latn"], "type": "tribal"},
        "unr": {"name": "Mundari", "scripts": ["deva", "latn"], "type": "tribal"},
        "hoc": {"name": "Ho", "scripts": ["warang", "deva", "latn"], "type": "tribal"},
        "kru": {"name": "Kurukh (Oraon)", "scripts": ["tolong", "deva", "latn"], "type": "tribal"},
        "khr": {"name": "Kharia", "scripts": ["deva", "latn"], "type": "tribal"},
        "kht": {"name": "Khortha", "scripts": ["deva"], "type": "regional"},
        "sck": {"name": "Nagpuri (Sadri)", "scripts": ["deva"], "type": "regional"},
        "tdb": {"name": "Panchpargania", "scripts": ["deva"], "type": "regional"},
        "kyw": {"name": "Kurmali", "scripts": ["deva"], "type": "regional"},
        "hin": {"name": "Hindi", "scripts": ["deva"], "type": "bridge"},
        "eng": {"name": "English", "scripts": ["latn"], "type": "bridge"},
    }

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env", extra="allow")


settings = Settings()

# Ensure critical directories exist
os.makedirs(settings.MEDIA_DIR, exist_ok=True)
os.makedirs(settings.OFFLINE_PACKS_DIR, exist_ok=True)
os.makedirs(settings.FONTS_DIR, exist_ok=True)
