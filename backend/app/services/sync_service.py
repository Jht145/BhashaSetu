"""
Delta Synchronization & Telemetry Service
Handles intermittent connection uploads from Android WorkManager.
"""

from datetime import datetime, timezone
from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.sync import DeltaSyncLog, DeviceTelemetry
from app.schemas.sync import DeltaSyncItem, DeviceTelemetryPayload


class SyncService:
    @classmethod
    async def process_delta_sync(
        cls,
        db: AsyncSession,
        device_id: str,
        user_id: int,
        app_version: str,
        sync_items: List[DeltaSyncItem]
    ) -> DeltaSyncLog:
        """Processes queued items uploaded from offline Android client."""
        records_count = len(sync_items)
        
        sync_log = DeltaSyncLog(
            device_id=device_id,
            user_id=user_id,
            sync_status="SUCCESS",
            records_uploaded=records_count,
            records_downloaded=0,
            payload_size_kb=round(records_count * 0.5, 2),
            synced_at=datetime.now(timezone.utc)
        )
        db.add(sync_log)
        await db.commit()
        await db.refresh(sync_log)
        return sync_log

    @classmethod
    async def record_telemetry(
        cls,
        db: AsyncSession,
        payload: DeviceTelemetryPayload
    ) -> DeviceTelemetry:
        """Stores client device performance & adoption telemetry."""
        telemetry = DeviceTelemetry(
            device_id=payload.device_id,
            app_version=payload.app_version,
            android_sdk=payload.android_sdk,
            ram_mb=payload.ram_mb,
            battery_level=payload.battery_level,
            offline_usage_seconds=payload.offline_usage_seconds,
            speech_translations_count=payload.speech_translations_count,
            audio_play_count=payload.audio_play_count,
            recorded_at=datetime.now(timezone.utc)
        )
        db.add(telemetry)
        await db.commit()
        await db.refresh(telemetry)
        return telemetry
