import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.database import init_db
from app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables
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

# Serve media files (TTS audio assets, fonts, packs)
if os.path.exists(settings.MEDIA_DIR):
    app.mount("/media", StaticFiles(directory=settings.MEDIA_DIR), name="media")

# Register API Router
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "project_code": settings.PROJECT_CODE,
        "version": "1.0.0",
        "supported_tribal_languages": list(settings.SUPPORTED_LANGUAGES.keys()),
    }


@app.get("/", tags=["System"])
async def root():
    return {
        "message": "Welcome to BhashaSetu Backend API",
        "docs": "/docs",
        "health": "/health",
        "api_v1": settings.API_V1_STR,
    }
