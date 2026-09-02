from datetime import datetime, timezone
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.app.core.database import get_db
from backend.app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    oauth2_scheme,
    decode_token,
)
from backend.app.models.user import User, UserRole, District, School
from backend.app.schemas.auth import (
    Token,
    UserCreate,
    UserResponse,
    DistrictCreate,
    DistrictResponse,
    SchoolCreate,
    SchoolResponse,
)

router = APIRouter()


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    payload = decode_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalars().first()
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )
    return user


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user_in.username))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    user = User(
        username=user_in.username,
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
        role=user_in.role,
        preferred_language=user_in.preferred_language,
        preferred_script=user_in.preferred_script,
        school_id=user_in.school_id,
        grade=user_in.grade,
        is_active=True,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User).where(User.username == form_data.username))
    user = result.scalars().first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user.last_login = datetime.now(timezone.utc)
    await db.commit()

    access_token = create_access_token(
        subject=user.id,
        role=user.role.value,
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role.value,
        "user_id": user.id,
        "username": user.username,
        "full_name": user.full_name,
        "preferred_language": user.preferred_language,
        "preferred_script": user.preferred_script,
    }


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/districts", response_model=List[DistrictResponse])
async def list_districts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(District))
    return result.scalars().all()


@router.post("/districts", response_model=DistrictResponse, status_code=status.HTTP_201_CREATED)
async def create_district(district_in: DistrictCreate, db: AsyncSession = Depends(get_db)):
    district = District(**district_in.model_dump())
    db.add(district)
    await db.commit()
    await db.refresh(district)
    return district


@router.get("/schools", response_model=List[SchoolResponse])
async def list_schools(district_id: int = None, db: AsyncSession = Depends(get_db)):
    query = select(School)
    if district_id:
        query = query.where(School.district_id == district_id)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/schools", response_model=SchoolResponse, status_code=status.HTTP_201_CREATED)
async def create_school(school_in: SchoolCreate, db: AsyncSession = Depends(get_db)):
    school = School(**school_in.model_dump())
    db.add(school)
    await db.commit()
    await db.refresh(school)
    return school
