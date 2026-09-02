import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.core.database import init_db
from scripts.seed_data import seed


@pytest_asyncio.fixture(autouse=True)
async def prepare_database():
    await init_db()
    await seed()


@pytest.mark.asyncio
async def test_health_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["project_code"] == "SIH26042"


@pytest.mark.asyncio
async def test_auth_login():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/auth/login",
            data={"username": "teacher_santhali", "password": "teacher123"}
        )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["role"] == "TEACHER"
    assert data["preferred_language"] == "sat"


@pytest.mark.asyncio
async def test_curriculum_subjects():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/curriculum/subjects?grade=3")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["code"] == "G3_EVS_JCERT"


@pytest.mark.asyncio
async def test_translation_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/translation/translate",
            json={
                "text": "नमस्ते पानी और पेड़",
                "source_language": "hin",
                "target_language": "sat",
                "target_script": "olck"
            }
        )
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert data["latency_ms"] < 200.0  # NFR requirement


@pytest.mark.asyncio
async def test_speech_duplex_translation():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/speech/duplex-translate",
            json={
                "source_language": "hin",
                "target_language": "sat",
                "target_script": "olck",
                "generate_speech_output": True
            }
        )
    assert response.status_code == 200
    data = response.json()
    assert data["audio_url"] is not None
    assert data["latency_ms"] < 2000.0  # NFR requirement < 2.0s


import time


@pytest.mark.asyncio
async def test_offline_package_compilation():
    unique_id = f"TEST_G1_MATH_SAT_{int(time.time() * 1000)}"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/sync/packages/compile",
            json={
                "pack_identifier": unique_id,
                "grade": 1,
                "subject_code": "G1_MATH",
                "language_code": "sat",
                "version": "1.0.0"
            }
        )
    assert response.status_code == 201
    data = response.json()
    assert data["pack_identifier"] == unique_id
    assert data["file_size_mb"] < 50.0  # NFR requirement < 50MB
    assert data["checksum_sha256"] != ""


@pytest.mark.asyncio
async def test_analytics_summary():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/analytics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "kpis" in data
    assert "teacher_adoption_rate" in data["kpis"]
