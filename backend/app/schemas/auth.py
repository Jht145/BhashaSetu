from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from backend.app.models.user import UserRole


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    user_id: int
    username: str
    full_name: str
    preferred_language: str
    preferred_script: str


class TokenPayload(BaseModel):
    sub: Optional[str] = None
    role: Optional[str] = None
    exp: Optional[int] = None


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str
    email: Optional[EmailStr] = None
    role: UserRole = UserRole.TEACHER
    preferred_language: str = "sat"
    preferred_script: str = "olck"
    school_id: Optional[int] = None
    grade: Optional[int] = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    full_name: str
    email: Optional[str] = None
    role: UserRole
    preferred_language: str
    preferred_script: str
    school_id: Optional[int] = None
    grade: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None


class DistrictCreate(BaseModel):
    name: str
    state: str = "Jharkhand"
    is_palash_pilot: bool = False
    primary_tribal_languages: str = "sat,unr"


class DistrictResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    state: str
    is_palash_pilot: bool
    primary_tribal_languages: str


class SchoolCreate(BaseModel):
    code: str
    name: str
    block: str
    district_id: int


class SchoolResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    name: str
    block: str
    district_id: int
