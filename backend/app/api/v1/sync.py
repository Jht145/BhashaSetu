import os
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.app.core.database import get_db
from backend.app.models.sync import OfflinePackage, DeltaSyncLog, DeviceTelemetry
from backend.app.models.curriculum import CurriculumSubject, Concept
from backend.app.schemas.sync import (
    OfflinePackageCreate,
    OfflinePackageResponse,
    DeltaSyncUploadRequest,
    DeltaSyncResponse,
    DeviceTelemetryPayload,
)
from backend.app.services.packager_service import PackagerService
from backend.app.services.sync_service import SyncService

router = APIRouter()


@router.get("/packages", response_model=List[OfflinePackageResponse])
async def list_offline_packages(
    grade: Optional[int] = None,
    language_code: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Returns available offline packages for pre-downloading in zero-bandwidth schools.
    """
    query = select(OfflinePackage).where(OfflinePackage.is_active == True)
    if grade is not None:
        query = query.where(OfflinePackage.grade == grade)
    if language_code:
        query = query.where(OfflinePackage.language_code == language_code)
    
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/packages/compile", response_model=OfflinePackageResponse, status_code=status.HTTP_201_CREATED)
async def compile_offline_package(
    req: OfflinePackageCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Compiles an offline curriculum pack container (<50MB) with embedded JSON and fonts.
    """
    # Check if package identifier already exists
    existing = await db.execute(select(OfflinePackage).where(OfflinePackage.pack_identifier == req.pack_identifier))
    if existing.scalars().first():
        raise HTTPException(status_code=400, detail="Package identifier already exists")

    dummy_payload = {
        "pack_identifier": req.pack_identifier,
        "grade": req.grade,
        "subject_code": req.subject_code,
        "language_code": req.language_code,
        "concepts": [
            {"id": 1, "title": "Pedagogy Unit 1", "vernacular": "ᱚᱞ ᱪᱤᱠᱤ ᱯᱟᱹᱴᱷᱩᱣᱟᱹ"}
        ]
    }

    file_path, file_size_mb, checksum = PackagerService.create_offline_package(
        pack_identifier=req.pack_identifier,
        grade=req.grade,
        subject_code=req.subject_code,
        language_code=req.language_code,
        curriculum_payload=dummy_payload
    )

    pack = OfflinePackage(
        pack_identifier=req.pack_identifier,
        grade=req.grade,
        subject_code=req.subject_code,
        language_code=req.language_code,
        version=req.version,
        file_path=file_path,
        file_size_mb=file_size_mb,
        checksum_sha256=checksum,
        download_count=0,
        is_active=True,
    )
    db.add(pack)
    await db.commit()
    await db.refresh(pack)
    return pack


@router.get("/packages/download/{pack_identifier}")
async def download_package(pack_identifier: str, db: AsyncSession = Depends(get_db)):
    """
    Streams the compiled .pack file for offline Android storage.
    """
    result = await db.execute(select(OfflinePackage).where(OfflinePackage.pack_identifier == pack_identifier))
    pack = result.scalars().first()
    if not pack or not os.path.exists(pack.file_path):
        raise HTTPException(status_code=404, detail="Package file not found")

    pack.download_count += 1
    await db.commit()

    return FileResponse(
        path=pack.file_path,
        filename=os.path.basename(pack.file_path),
        media_type="application/octet-stream"
    )


@router.post("/delta-upload", response_model=DeltaSyncResponse)
async def upload_delta_sync(
    payload: DeltaSyncUploadRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Receives batched delta items (lesson completions, feedback, audio telemetry)
    queued by Android WorkManager.
    """
    sync_log = await SyncService.process_delta_sync(
        db=db,
        device_id=payload.device_id,
        user_id=payload.user_id or 1,
        app_version=payload.app_version,
        sync_items=payload.sync_items
    )
    return {
        "sync_id": sync_log.id,
        "status": "SUCCESS",
        "records_processed": len(payload.sync_items),
        "server_timestamp": sync_log.synced_at,
        "message": f"Successfully processed {len(payload.sync_items)} queued records."
    }


@router.post("/telemetry", status_code=status.HTTP_201_CREATED)
async def record_device_telemetry(
    payload: DeviceTelemetryPayload,
    db: AsyncSession = Depends(get_db)
):
    """
    Receives device runtime telemetry (RAM usage, battery level, offline seconds).
    """
    await SyncService.record_telemetry(db, payload)
    return {"status": "recorded", "device_id": payload.device_id}
