from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.core.database import Base


class OfflinePackage(Base):
    __tablename__ = "offline_packages"

    id = Column(Integer, primary_key=True, index=True)
    pack_identifier = Column(String(100), unique=True, index=True, nullable=False)  # e.g. "G1_EVS_SAT_v1.0"
    grade = Column(Integer, nullable=False)
    subject_code = Column(String(50), nullable=False)
    language_code = Column(String(10), nullable=False)  # sat, unr, etc.
    version = Column(String(20), default="1.0.0")
    
    file_path = Column(String(500), nullable=False)
    file_size_mb = Column(Float, nullable=False)  # Under 50MB per requirement
    checksum_sha256 = Column(String(64), nullable=False)
    download_count = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class DeltaSyncLog(Base):
    __tablename__ = "delta_sync_logs"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(100), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    sync_status = Column(String(20), default="SUCCESS")  # SUCCESS, PARTIAL, FAILED
    records_uploaded = Column(Integer, default=0)
    records_downloaded = Column(Integer, default=0)
    payload_size_kb = Column(Float, default=0.0)
    synced_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="sync_logs")


class DeviceTelemetry(Base):
    __tablename__ = "device_telemetry"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(100), index=True, nullable=False)
    app_version = Column(String(20), nullable=False)
    android_sdk = Column(Integer, nullable=True)
    ram_mb = Column(Integer, nullable=True)
    battery_level = Column(Float, nullable=True)
    
    offline_usage_seconds = Column(Integer, default=0)
    speech_translations_count = Column(Integer, default=0)
    audio_play_count = Column(Integer, default=0)
    
    recorded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
