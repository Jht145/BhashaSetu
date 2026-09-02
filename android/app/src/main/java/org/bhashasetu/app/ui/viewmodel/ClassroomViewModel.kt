package org.bhashasetu.app.ui.viewmodel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import org.bhashasetu.app.data.local.AppDatabase
import org.bhashasetu.app.data.local.ConceptEntity
import org.bhashasetu.app.data.remote.SpeechWebSocketClient

data class ClassroomUiState(
    val isRecording: Boolean = false,
    val isPresentationMode: Boolean = false,
    val sourceLanguage: String = "hin",
    val targetLanguage: String = "sat",
    val targetScript: String = "olck",
    val liveSubtitleNative: String = "ᱡᱚᱦᱟᱨ",
    val liveSubtitlePhonetic: String? = "जोहार (Johar)",
    val latencyMs: Float = 65.0f,
    val offlineConcepts: List<ConceptEntity> = emptyList(),
    val isOfflineMode: Boolean = true,
    val errorMessage: String? = null
)

class ClassroomViewModel(application: Application) : AndroidViewModel(application) {
    private val db = AppDatabase.getDatabase(application)
    private val _uiState = MutableStateFlow(ClassroomUiState())
    val uiState: StateFlow<ClassroomUiState> = _uiState.asStateFlow()

    private var wsClient: SpeechWebSocketClient? = null

    init {
        loadOfflineCurriculum(grade = 3, languageCode = "sat")
    }

    fun loadOfflineCurriculum(grade: Int, languageCode: String) {
        viewModelScope.launch {
            db.conceptDao().getConceptsByGradeAndLanguage(grade, languageCode).collect { concepts ->
                _uiState.value = _uiState.value.copy(
                    offlineConcepts = concepts,
                    targetLanguage = languageCode
                )
            }
        }
    }

    fun togglePresentationMode() {
        _uiState.value = _uiState.value.copy(
            isPresentationMode = !_uiState.value.isPresentationMode
        )
    }

    fun setTargetLanguage(languageCode: String, scriptCode: String = "deva") {
        _uiState.value = _uiState.value.copy(
            targetLanguage = languageCode,
            targetScript = if (languageCode == "sat") "olck" else scriptCode
        )
        loadOfflineCurriculum(grade = 3, languageCode = languageCode)
    }

    fun startLiveSpeechTranslation() {
        _uiState.value = _uiState.value.copy(isRecording = true, errorMessage = null)
        wsClient = SpeechWebSocketClient(
            onOutputReceived = { translated, phonetic, _, latency ->
                _uiState.value = _uiState.value.copy(
                    liveSubtitleNative = translated,
                    liveSubtitlePhonetic = phonetic,
                    latencyMs = latency,
                    isRecording = false
                )
            },
            onError = { err ->
                _uiState.value = _uiState.value.copy(
                    isRecording = false,
                    errorMessage = err
                )
            }
        )
        wsClient?.connect(
            sourceLang = _uiState.value.sourceLanguage,
            targetLang = _uiState.value.targetLanguage,
            targetScript = _uiState.value.targetScript
        )
    }

    fun stopLiveSpeechTranslation(sampleUtterance: String? = "नमस्ते बच्चों") {
        wsClient?.triggerEndOfUtterance(sampleUtterance)
        _uiState.value = _uiState.value.copy(isRecording = false)
    }

    override fun onCleared() {
        super.onCleared()
        wsClient?.disconnect()
    }
}
