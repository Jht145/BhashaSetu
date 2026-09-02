"""
Unit tests for Duplex Audio WebSocket streaming endpoint (/ws/classroom-speech)
"""

import pytest
from starlette.testclient import TestClient
from backend.app.main import app


def test_duplex_websocket_speech_stream():
    client = TestClient(app)
    with client.websocket_connect("/ws/classroom-speech") as websocket:
        # 1. Receive Handshake
        handshake = websocket.receive_json()
        assert handshake["type"] == "HANDSHAKE_READY"
        assert handshake["status"] == "connected"

        # 2. Send Config Update
        websocket.send_json({
            "type": "CONFIG",
            "source_language": "hin",
            "target_language": "sat",
            "target_script": "olck"
        })
        config_ack = websocket.receive_json()
        assert config_ack["type"] == "CONFIG_ACK"
        assert config_ack["target_language"] == "sat"
        assert config_ack["target_script"] == "olck"

        # 3. Stream binary audio chunks
        dummy_pcm_chunk = b"\x00\x01\x00\x02" * 128
        websocket.send_bytes(dummy_pcm_chunk)
        chunk_ack = websocket.receive_json()
        assert chunk_ack["type"] == "CHUNK_RECEIVED"
        assert chunk_ack["buffer_size_bytes"] == len(dummy_pcm_chunk)

        # 4. End of utterance trigger
        websocket.send_json({
            "type": "END_OF_UTTERANCE",
            "text_fallback": "नमस्ते"
        })
        output = websocket.receive_json()
        assert output["type"] == "TRANSLATION_OUTPUT"
        assert "ᱡᱚᱦᱟᱨ" in output["translated_text"]
        assert output["audio_url"] is not None
        assert output["latency_ms"] < 2000.0
