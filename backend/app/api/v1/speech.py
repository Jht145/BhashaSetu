import base64
import time
import json
import asyncio
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.core.database import get_db, AsyncSessionLocal
from backend.app.models.translation import TranslationLog
from backend.app.schemas.translation import (
    TTSRequest,
    TTSResponse,
    SpeechTranslateRequest,
    SpeechTranslateResponse,
)
from backend.app.services.ai.asr_service import ASRService
from backend.app.services.ai.nmt_service import NMTService
from backend.app.services.ai.tts_service import TTSService

router = APIRouter()


@router.post("/tts", response_model=TTSResponse)
async def generate_speech(req: TTSRequest):
    """
    Synthesizes speech audio for vernacular text (e.g. Santhali in Ol Chiki or Devanagari).
    """
    audio_url, duration, file_size = TTSService.synthesize_speech(
        text=req.text,
        language_code=req.language_code,
        script_code=req.script_code,
        speed=req.speed,
    )
    return {
        "audio_url": audio_url,
        "duration_seconds": duration,
        "language_code": req.language_code,
        "file_size_bytes": file_size,
    }


@router.post("/duplex-translate", response_model=SpeechTranslateResponse)
async def classroom_duplex_speech_translate(
    req: SpeechTranslateRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Real-time Duplex Classroom Speech Translation Layer (REST):
    Takes teacher/student spoken audio, performs ASR, NMT, and TTS synthesis.
    Target latency: < 2.0s.
    """
    start_time = time.time()
    
    # 1. ASR - Speech to Text
    audio_bytes = b""
    if req.audio_base64:
        try:
            audio_bytes = base64.b64decode(req.audio_base64)
        except Exception:
            pass
            
    recognized_text, asr_latency = ASRService.transcribe(
        audio_data=audio_bytes,
        source_language=req.source_language
    )

    # 2. NMT - Vernacular Translation
    translated_text, phonetic_deva, nmt_latency, _ = await NMTService.translate_async(
        text=recognized_text,
        source_language=req.source_language,
        target_language=req.target_language,
        target_script=req.target_script,
    )

    # 3. TTS - Speech Synthesis (if requested)
    audio_url = None
    if req.generate_speech_output:
        audio_url, _, _ = TTSService.synthesize_speech(
            text=translated_text,
            language_code=req.target_language,
            script_code=req.target_script,
        )

    total_latency = (time.time() - start_time) * 1000 + asr_latency + nmt_latency

    # Log translation
    log = TranslationLog(
        source_language=req.source_language,
        target_language=req.target_language,
        target_script=req.target_script,
        source_text=recognized_text,
        translated_text=translated_text,
        mode="SPEECH_TO_SPEECH",
        latency_ms=round(total_latency, 2),
    )
    db.add(log)
    await db.commit()

    return {
        "recognized_text": recognized_text,
        "source_language": req.source_language,
        "translated_text": translated_text,
        "target_language": req.target_language,
        "target_script": req.target_script,
        "phonetic_transcription": phonetic_deva,
        "audio_url": audio_url,
        "latency_ms": round(total_latency, 2),
    }


@router.websocket("/ws/classroom-speech")
async def websocket_classroom_speech(websocket: WebSocket):
    """
    Duplex Audio WebSocket Stream: Ingests live PCM microphone chunks from classroom teachers/students
    and streams back real-time recognized subtitles, phonetic guides, and synthesized audio URL.
    """
    await websocket.accept()
    
    # Default streaming session parameters
    source_lang = "hin"
    target_lang = "sat"
    target_script = "olck"
    audio_buffer = bytearray()

    try:
        # 1. Send connection handshake
        await websocket.send_json({
            "type": "HANDSHAKE_READY",
            "message": "BhashaSetu Duplex Speech Stream Active",
            "status": "connected"
        })

        while True:
            message = await websocket.receive()

            if "text" in message:
                data = json.loads(message["text"])
                msg_type = data.get("type", "")

                # Configuration update
                if msg_type == "CONFIG":
                    source_lang = data.get("source_language", source_lang)
                    target_lang = data.get("target_language", target_lang)
                    target_script = data.get("target_script", target_script)
                    await websocket.send_json({
                        "type": "CONFIG_ACK",
                        "source_language": source_lang,
                        "target_language": target_lang,
                        "target_script": target_script
                    })

                # Explicit end of speech turn
                elif msg_type == "END_OF_UTTERANCE":
                    if audio_buffer or data.get("text_fallback"):
                        t_start = time.time()
                        text_to_process = data.get("text_fallback")
                        asr_lat = 0.0
                        if not text_to_process:
                            text_to_process, asr_lat = ASRService.transcribe(bytes(audio_buffer), source_lang)
                        
                        translated, phonetic_deva, nmt_lat, conf = await NMTService.translate_async(
                            text=text_to_process,
                            source_language=source_lang,
                            target_language=target_lang,
                            target_script=target_script
                        )

                        audio_url, dur, _ = TTSService.synthesize_speech(
                            text=translated,
                            language_code=target_lang,
                            script_code=target_script
                        )

                        total_lat = (time.time() - t_start) * 1000 + asr_lat + nmt_lat

                        await websocket.send_json({
                            "type": "TRANSLATION_OUTPUT",
                            "recognized_text": text_to_process,
                            "translated_text": translated,
                            "phonetic_transcription": phonetic_deva,
                            "audio_url": audio_url,
                            "duration_seconds": dur,
                            "target_language": target_lang,
                            "target_script": target_script,
                            "latency_ms": round(total_lat, 2)
                        })
                        audio_buffer.clear()

            elif "bytes" in message:
                # Append raw binary audio chunk
                audio_buffer.extend(message["bytes"])
                # Real-time chunk ping
                await websocket.send_json({
                    "type": "CHUNK_RECEIVED",
                    "buffer_size_bytes": len(audio_buffer)
                })

    except WebSocketDisconnect:
        pass
    except Exception as e:
        try:
            await websocket.send_json({"type": "ERROR", "detail": str(e)})
            await websocket.close()
        except Exception:
            pass
