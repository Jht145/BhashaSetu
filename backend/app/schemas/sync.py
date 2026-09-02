from typing import List, Optional, Any, Dict
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class OfflinePackageCreate(BaseModel):
    pack_identifier: str
    grade: int
    subject_code: str
    language_code: str
    version: str = "1.0.0"


class OfflinePackageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    pack_identifier: str
    grade: int
    subject_code: str
    language_code: str
    version: str
    file_path: str
    file_size_mb: float
    checksum_sha256: str
    download_count: int
    is_active: bool
    created_at: datetime


class DeltaSyncItem(BaseModel):
    table_name: str
    action: str  # INSERT, UPDATE, DELETE
    client_id: str
    data: Dict[str, Any]
    client_timestamp: datetime


class DeltaSyncUploadRequest(BaseModel):
    device_id: str
    user_id: Optional[int] = None
    app_version: str
    sync_items: List[DeltaSyncItem] = []


class DeltaSyncResponse(BaseModel):
    sync_id: int
    status: str
    records_processed: int
    server_timestamp: datetime
    message: str


class DeviceTelemetryPayload(BaseModel):
    device_id: str
    app_version: str
    android_sdk: Optional[int] = 29
    ram_mb: Optional[int] = 2048
    battery_level: Optional[float] = 85.0
    offline_usage_seconds: int = 0
    speech_translations_count: int = 0
    audio_play_count: int = 0
