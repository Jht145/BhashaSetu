package org.bhashasetu.app.data.remote

import okhttp3.*
import okio.ByteString
import org.json.JSONObject
import java.util.concurrent.TimeUnit

class SpeechWebSocketClient(
    private val serverWsUrl: String = "ws://10.0.2.2:8000/ws/classroom-speech",
    private val onOutputReceived: (translated: String, phonetic: String?, audioUrl: String?, latencyMs: Float) -> Unit,
    private val onError: (String) -> Unit
) {
    private val client = OkHttpClient.Builder()
        .readTimeout(0, TimeUnit.MILLISECONDS)
        .build()

    private var webSocket: WebSocket? = null
    var isConnected = false
        private set

    fun connect(sourceLang: String = "hin", targetLang: String = "sat", targetScript: String = "olck") {
        val request = Request.Builder().url(serverWsUrl).build()
        webSocket = client.newWebSocket(request, object : WebSocketListener() {
            override fun onOpen(ws: WebSocket, response: Response) {
                isConnected = true
                val config = JSONObject().apply {
                    put("type", "CONFIG")
                    put("source_language", sourceLang)
                    put("target_language", targetLang)
                    put("target_script", targetScript)
                }
                ws.send(config.toString())
            }

            override fun onMessage(ws: WebSocket, text: String) {
                try {
                    val json = JSONObject(text)
                    when (json.optString("type")) {
                        "TRANSLATION_OUTPUT" -> {
                            val translated = json.optString("translated_text", "")
                            val phonetic = json.optString("phonetic_transcription", null)
                            val audioUrl = json.optString("audio_url", null)
                            val latency = json.optDouble("latency_ms", 0.0).toFloat()
                            onOutputReceived(translated, phonetic, audioUrl, latency)
                        }
                        "ERROR" -> onError(json.optString("detail", "Stream error"))
                    }
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }

            override fun onFailure(ws: WebSocket, t: Throwable, response: Response?) {
                isConnected = false
                onError(t.message ?: "WebSocket connection failed")
            }

            override fun onClosed(ws: WebSocket, code: Int, reason: String) {
                isConnected = false
            }
        })
    }

    fun sendAudioChunk(pcmBytes: ByteArray) {
        webSocket?.send(ByteString.of(*pcmBytes))
    }

    fun triggerEndOfUtterance(textFallback: String? = null) {
        val msg = JSONObject().apply {
            put("type", "END_OF_UTTERANCE")
            if (textFallback != null) put("text_fallback", textFallback)
        }
        webSocket?.send(msg.toString())
    }

    fun disconnect() {
        webSocket?.close(1000, "Client closed")
        isConnected = false
    }
}
