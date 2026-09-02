# 🌉 भाषा सेतु (BhashaSetu)

> **AI-Powered Vernacular Pedagogy Engine & Duplex Translation Layer**  
> *Project Code: SIH26042 | Category: Smart Education / Software*  
> *Target Region: Low-resource schools in Jharkhand (Offline-First Android + Web Portal)*

---

## 🌟 Overview

In linguistically diverse states like Jharkhand, primary school children face high dropout rates and low comprehension because the medium of instruction often does not match their mother tongue. 

**BhashaSetu** provides:
1. **Vernacular Pedagogy Engine:** Converts standard NCERT/JCERT curricula into culturally grounded metaphors (e.g. Sarhul, Karma, Sal tree) paired with synchronized audio and text.
2. **Duplex Classroom Translation Layer:** Bi-directional Speech-to-Speech (S2S) and Speech-to-Text (S2T) between standard Hindi/English and tribal languages.
3. **Native Script Engine (Ol Chiki):** Embedded Unicode engine with instant dynamic script switching (Devanagari <-> Ol Chiki <-> Latin).
4. **Offline-First Delta Sync:** Compressed offline concept packs (< 50MB) and queued Android WorkManager delta synchronization.
5. **Human-in-the-Loop (HITL) Linguist Portal:** Language experts verify, score, and correct automated translations to generate active learning LoRA datasets.
6. **Interactive Web App & Learning Arena:** Child-friendly bilingual learning platform with visual dictionaries, quizzes, stories, and speech synthesis.

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

## ✨ Features & Child-Friendly Experience

- 🎨 **Playful Kid-Friendly UI**: Vibrant pastels, cheerful icons, bubbly cards, and confetti celebrations.
- 🐘 **Interactive Mascot "Setu Bhaiya"**: Animated companion providing cheerful guidance and voice praise.
- 🎙️ **Multi-Modal Voice & Sound**:
  - Speech-to-Text: Speak Hindi using the mic button.
  - Web Audio API Sound Synthesizer: Playful chimes, pops, and fanfares without needing external audio files.
  - Pronunciation guide & Text-to-Speech playback.
- 🌈 **Compare All 9 Languages**: See how any word or sentence looks across all 9 indigenous languages simultaneously!
- 📚 **Visual Picture Dictionary**: 12+ categories (Animals, Nature, Food, Family, Colors, Numbers, Actions, School, Feelings) with emojis and instant audio.
- 🎮 **Kids Fun Arena (खेल-खेल में सीखें)**:
  - **Quiz Master**: Interactive multiple choice questions with rewards and badges (🌟 जोहार मास्टर, ⭐ जल सेतु सितारा).
  - **Word Match**: Match Hindi words to tribal words with sound effects and star confetti.
- 📖 **Story Corner**: Illustrated bilingual short stories ("सरहुल का त्योहार", "हाथी और चतुर खरगोश").
- 🔤 **Script Explorer**: Explore Ol Chiki (Santali) and Warang Citi (Ho) alphabets with interactive pronunciation.

---

## 🚀 How to Run

### 1. Web Application & Frontend
```bash
# Install dependencies
pip install -r requirements.txt

# Launch Application
python3 run.py
```
Navigate to [http://localhost:8000](http://localhost:8000).

### 2. Backend API Service
```bash
cd backend
pip install -r requirements.txt
python -m scripts.seed_data
uvicorn app.main:app --reload --port 8000
```
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 🧪 Running Tests

```bash
# Translation test suite
PYTHONPATH=. python3 backend/tests/test_translation.py

# Backend pytest suite
cd backend && pytest -v
```
