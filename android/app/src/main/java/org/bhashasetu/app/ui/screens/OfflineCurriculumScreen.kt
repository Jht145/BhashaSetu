package org.bhashasetu.app.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import org.bhashasetu.app.data.local.ConceptEntity
import org.bhashasetu.app.ui.components.OlChikiText
import org.bhashasetu.app.ui.theme.ForestGreen
import org.bhashasetu.app.ui.theme.OlChikiAccent
import org.bhashasetu.app.ui.theme.SubtitleGray
import org.bhashasetu.app.ui.viewmodel.ClassroomViewModel

@Composable
fun OfflineCurriculumScreen(viewModel: ClassroomViewModel) {
    val state by viewModel.uiState.collectAsState()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "📚 ऑफ़लाइन पाठ्य सामग्री (Offline Concepts)",
            fontSize = 20.sp,
            fontWeight = FontWeight.Bold,
            color = ForestGreen
        )
        Text(
            text = "कक्षा ३ • पर्यावरण अध्ययन (EVS) • ${state.offlineConcepts.size} संकल्पनाएँ",
            fontSize = 14.sp,
            color = SubtitleGray,
            modifier = Modifier.padding(top = 2.dp, bottom = 12.dp)
        )

        if (state.offlineConcepts.isEmpty()) {
            Card(
                modifier = Modifier.fillMaxWidth().padding(top = 24.dp),
                shape = RoundedCornerShape(12.dp)
            ) {
                Column(modifier = Modifier.padding(24.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(text = "📦 कोई ऑफ़लाइन पैक नहीं मिला", fontWeight = FontWeight.Bold)
                    Text(
                        text = "सर्वर से .pack फ़ाइल डाउनलोड करें या शिक्षक डेस्क से सिंक्रनाइज़ करें।",
                        fontSize = 13.sp,
                        color = SubtitleGray,
                        modifier = Modifier.padding(top = 6.dp)
                    )
                }
            }
        } else {
            LazyColumn(
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                items(state.offlineConcepts) { concept ->
                    ConceptCard(concept = concept)
                }
            }
        }
    }
}

@Composable
fun ConceptCard(concept: ConceptEntity) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(14.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = concept.title,
                    fontWeight = FontWeight.Bold,
                    fontSize = 16.sp
                )
                if (concept.isCompleted) {
                    Icon(imageVector = Icons.Default.CheckCircle, contentDescription = "Completed", tint = ForestGreen)
                }
            }

            Spacer(modifier = Modifier.height(8.dp))

            OlChikiText(
                text = concept.vernacularTitle,
                devanagariPhonetic = null,
                fontSize = 20.sp,
                showScriptToggle = false
            )

            if (concept.culturalMetaphor != null) {
                Spacer(modifier = Modifier.height(6.dp))
                Surface(
                    shape = RoundedCornerShape(8.dp),
                    color = MaterialTheme.colorScheme.background,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text(
                        text = "🌱 सांस्कृतिक संदर्भ: ${concept.culturalMetaphor}",
                        fontSize = 13.sp,
                        color = ForestGreen,
                        modifier = Modifier.padding(8.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(10.dp))

            Row(horizontalArrangement = Arrangement.End, modifier = Modifier.fillMaxWidth()) {
                FilledTonalButton(
                    onClick = { /* Play local audio */ },
                    contentPadding = PaddingValues(horizontal = 12.dp, vertical = 6.dp)
                ) {
                    Icon(imageVector = Icons.Default.PlayArrow, contentDescription = "Play audio", modifier = Modifier.size(18.dp))
                    Spacer(modifier = Modifier.width(4.dp))
                    Text(text = "ऑडियो सुनें", fontSize = 12.sp)
                }
            }
        }
    }
}
