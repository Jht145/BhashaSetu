import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Ensure both project root and backend are accessible in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BACKEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
for p in [BASE_DIR, BACKEND_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

from backend.app.core.config import settings
from backend.app.core.database import init_db
from backend.app.api.v1.router import api_router as v1_router
from backend.app.api.web import router as web_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables on startup
    await init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Vernacular Pedagogy Engine & Duplex Translation Backend for Low-Resource Tribal Languages (SIH26042)",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Set CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Register Web Frontend API Router (/api/languages, /api/translate, /api/dictionary, etc.)
app.include_router(web_router, prefix="/api")

# 2. Register PRD Engineering Specification API Router (/api/v1/auth, /api/v1/curriculum, etc.)
app.include_router(v1_router, prefix=settings.API_V1_STR)


@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "project_code": settings.PROJECT_CODE,
        "version": "1.0.0",
        "supported_tribal_languages": list(settings.SUPPORTED_LANGUAGES.keys()),
    }


# 3. Mount static media directory for synthesized TTS voice audio assets
if os.path.exists(settings.MEDIA_DIR):
    app.mount("/media", StaticFiles(directory=settings.MEDIA_DIR), name="media")

# 4. Mount Frontend Web UI at root (/)
frontend_dir = os.path.join(BASE_DIR, "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
