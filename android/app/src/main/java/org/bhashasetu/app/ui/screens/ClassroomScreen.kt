package org.bhashasetu.app.ui.screens

import androidx.compose.animation.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import org.bhashasetu.app.ui.components.OlChikiText
import org.bhashasetu.app.ui.theme.*
import org.bhashasetu.app.ui.viewmodel.ClassroomViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ClassroomScreen(viewModel: ClassroomViewModel) {
    val state by viewModel.uiState.collectAsState()

    val targetLanguages = listOf(
        "sat" to "संताली (Santhali)",
        "unr" to "मुंडारी (Mundari)",
        "hoc" to "हो (Ho)",
        "kru" to "कुड़ुख़ (Kurukh)",
        "khr" to "खड़िया (Kharia)",
        "kht" to "खोरठा (Khortha)",
        "sck" to "नागपुरी (Nagpuri)"
    )

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(if (state.isPresentationMode) DarkGreen else MaterialTheme.colorScheme.background)
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        // Top Classroom Controls
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = if (state.isPresentationMode) "📺 प्रस्तुति मोड (Presentation)" else "🏫 BhashaSetu Classroom",
                fontSize = 18.sp,
                fontWeight = FontWeight.Bold,
                color = if (state.isPresentationMode) Color.White else MaterialTheme.colorScheme.onBackground
            )

            IconButton(onClick = { viewModel.togglePresentationMode() }) {
                Icon(
                    imageVector = if (state.isPresentationMode) Icons.Default.FullscreenExit else Icons.Default.Fullscreen,
                    contentDescription = "Toggle Presentation",
                    tint = if (state.isPresentationMode) BrightGold else ForestGreen
                )
            }
        }

        Spacer(modifier = Modifier.height(12.dp))

        // Target Language Selector Bar
        ScrollableTabRow(
            selectedTabIndex = targetLanguages.indexOfFirst { it.first == state.targetLanguage }.coerceAtLeast(0),
            edgePadding = 0.dp,
            containerColor = Color.Transparent,
            contentColor = ForestGreen
        ) {
            targetLanguages.forEach { (code, name) ->
                Tab(
                    selected = state.targetLanguage == code,
                    onClick = { viewModel.setTargetLanguage(code) },
                    text = { Text(text = name, fontWeight = FontWeight.SemiBold) }
                )
            }
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Live Subtitle Display Card (High Contrast for low-end phone & projector screens)
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .weight(1f),
            shape = RoundedCornerShape(16.dp),
            colors = CardDefaults.cardColors(
                containerColor = if (state.isPresentationMode) Color(0xFF001F00) else MaterialTheme.colorScheme.surface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
        ) {
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(24.dp),
                contentAlignment = Alignment.Center
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    OlChikiText(
                        text = state.liveSubtitleNative,
                        devanagariPhonetic = state.liveSubtitlePhonetic,
                        fontSize = if (state.isPresentationMode) 36.sp else 28.sp,
                        isLargePresentation = state.isPresentationMode,
                        showScriptToggle = true
                    )

                    Spacer(modifier = Modifier.height(12.dp))
                    Text(
                        text = "⚡ Latency: ${state.latencyMs} ms",
                        fontSize = 12.sp,
                        color = if (state.isPresentationMode) Color.LightGray else SubtitleGray
                    )
                }
            }
        }

        Spacer(modifier = Modifier.height(24.dp))

        // Large Touch Voice Activation Button
        Button(
            onClick = {
                if (state.isRecording) {
                    viewModel.stopLiveSpeechTranslation("साल का पेड़ हमारे जंगलों की जान है।")
                } else {
                    viewModel.startLiveSpeechTranslation()
                }
            },
            modifier = Modifier
                .size(90.dp),
            shape = CircleShape,
            colors = ButtonDefaults.buttonColors(
                containerColor = if (state.isRecording) Color.Red else ForestGreen
            ),
            elevation = ButtonDefaults.buttonElevation(defaultElevation = 8.dp)
        ) {
            Icon(
                imageVector = if (state.isRecording) Icons.Default.Stop else Icons.Default.Mic,
                contentDescription = "Microphone",
                tint = Color.White,
                modifier = Modifier.size(44.dp)
            )
        }

        Text(
            text = if (state.isRecording) "🎤 शिक्षक बोल रहे हैं (Listening...)" else "🎙️ बोलने के लिए बटन दबाएं (Tap to Speak)",
            fontSize = 14.sp,
            fontWeight = FontWeight.Medium,
            color = if (state.isPresentationMode) Color.White else MaterialTheme.colorScheme.onBackground,
            modifier = Modifier.padding(top = 8.dp)
        )
    }
}
