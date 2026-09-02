import enum
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class UserRole(str, enum.Enum):
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"
    LINGUIST_REVIEWER = "LINGUIST_REVIEWER"
    ADMIN = "ADMIN"


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    state = Column(String(100), default="Jharkhand")
    is_palash_pilot = Column(Boolean, default=False)  # 8 PALASH operational districts
    primary_tribal_languages = Column(String(255), default="sat,unr")  # comma-separated codes

    schools = relationship("School", back_populates="district")


class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)  # UDISE+ Code
    name = Column(String(255), nullable=False)
    block = Column(String(100), nullable=False)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)

    district = relationship("District", back_populates="schools")
    users = relationship("User", back_populates="school")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.TEACHER, nullable=False)
    preferred_language = Column(String(10), default="hin")  # e.g., 'sat', 'unr', 'hin'
    preferred_script = Column(String(10), default="olck")  # e.g., 'olck', 'deva', 'latn'
    is_active = Column(Boolean, default=True)
    
    school_id = Column(Integer, ForeignKey("schools.id"), nullable=True)
    grade = Column(Integer, nullable=True)  # For student/teacher assigned grade (1-5)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_login = Column(DateTime, nullable=True)

    school = relationship("School", back_populates="users")
    sync_logs = relationship("DeltaSyncLog", back_populates="user")
    reviews = relationship("ReviewTask", back_populates="reviewer")
