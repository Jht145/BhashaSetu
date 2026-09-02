# BhashaSetu (भाषासेतु)

**AI-Powered Vernacular Pedagogy Engine & Duplex Translation Layer**
*Project Code: SIH26042 | Category: Smart Education / Software*
*Target Region: Low-resource schools in Jharkhand (Offline-First Android + Web Portal)*

---

## 🌟 Overview

In linguistically diverse states like Jharkhand, primary school children face high dropout rates and low comprehension because the medium of instruction often does not match their mother tongue. 

**BhashaSetu** provides:
1. **Vernacular Pedagogy Engine:** Converts standard NCERT/JCERT curricula into culturally grounded metaphors (e.g. Sarhul, Karma, Sal tree) paired with synchronized audio and text.
2. **Duplex Classroom Translation Layer:** Bi-directional Speech-to-Speech (S2S) and Speech-to-Text (S2T) between standard Hindi/English and tribal languages.
3. **Native Script Engine (Ol Chiki):** Embedded Unicode engine with instant dynamic script switching (Devanagari <-> Ol Chiki <-> Latin).
4. **Offline-First Delta Sync:** Compressed offline concept packs (< 50MB) and queued Android WorkManager delta synchronization.
5. **Human-in-the-Loop (HITL) Linguist Portal:** Language experts verify, score, and correct automated translations to generate active learning LoRA datasets.

---

## 🌐 Supported Languages & Scripts Matrix

| Language | Code | Type | Native Script | Supported Scripts |
| --- | --- | --- | --- | --- |
| **Santhali** | `sat` | Tribal | **Ol Chiki (ᱚᱞ ᱪᱤᱠᱤ)** | Ol Chiki, Devanagari, Latin |
| **Mundari** | `unr` | Tribal | Devanagari / Mundari Bani | Devanagari, Latin |
| **Ho** | `hoc` | Tribal | Warang Citi | Warang Citi, Devanagari, Latin |
| **Kurukh (Oraon)** | `kru` | Tribal | Tolong Siki | Tolong Siki, Devanagari, Latin |
| **Kharia** | `khr` | Tribal | Devanagari | Devanagari, Latin |
| **Khortha** | `kht` | Regional | Devanagari | Devanagari |
| **Nagpuri (Sadri)** | `sck` | Regional | Devanagari | Devanagari |
| **Panchpargania** | `tdb` | Regional | Devanagari | Devanagari |
| **Kurmali** | `kyw` | Regional | Devanagari | Devanagari |
| **Hindi** | `hin` | Bridge | Devanagari | Devanagari |
| **English** | `eng` | Bridge | Latin | Latin |

---

## 🚀 Quick Start (Backend)

### 1. Prerequisites
- Python 3.10+
- (Optional) Docker & Docker Compose

### 2. Setup Virtual Environment & Install Dependencies
```bash
cd backend
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Seed Initial Jharkhand Curriculum & Pilot Data
```bash
python -m scripts.seed_data
```

### 4. Run the Server
```bash
uvicorn app.main:app --reload --port 8000
```

### 5. Access Interactive Documentation
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
- **Health Check:** `http://localhost:8000/health`

---

## 🧪 Running Tests
```bash
cd backend
pytest -v
```

---

## 🐳 Docker Deployment
```bash
cd backend
docker-compose up --build
```