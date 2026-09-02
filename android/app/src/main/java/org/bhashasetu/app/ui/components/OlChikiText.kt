package org.bhashasetu.app.ui.components

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import org.bhashasetu.app.ui.theme.ForestGreen
import org.bhashasetu.app.ui.theme.OlChikiAccent

@Composable
fun OlChikiText(
    text: String,
    devanagariPhonetic: String? = null,
    modifier: Modifier = Modifier,
    fontSize: TextUnit = 24.sp,
    isLargePresentation: Boolean = false,
    showScriptToggle: Boolean = true
) {
    var showDevanagari by remember { mutableStateOf(false) }

    Column(modifier = modifier) {
        if (showScriptToggle && devanagariPhonetic != null) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween,
                modifier = Modifier.fillMaxWidth().padding(bottom = 4.dp)
            ) {
                Text(
                    text = if (showDevanagari) "🔤 देवनागरी मोड" else "🔤 ᱚᱞ ᱪᱤᱠᱤ (Ol Chiki)",
                    fontSize = 12.sp,
                    color = OlChikiAccent,
                    fontWeight = FontWeight.Bold
                )
                TextButton(
                    onClick = { showDevanagari = !showDevanagari },
                    contentPadding = PaddingValues(horizontal = 8.dp, vertical = 2.dp)
                ) {
                    Text(
                        text = if (showDevanagari) "Switch to Ol Chiki ⇄" else "देवनागरी में देखें ⇄",
                        fontSize = 12.sp,
                        color = ForestGreen
                    )
                }
            }
        }

        val displayText = if (showDevanagari && devanagariPhonetic != null) devanagariPhonetic else text
        Text(
            text = displayText,
            fontSize = if (isLargePresentation) 32.sp else fontSize,
            fontWeight = FontWeight.SemiBold,
            lineHeight = if (isLargePresentation) 40.sp else (fontSize.value * 1.3f).sp
        )

        if (!showDevanagari && devanagariPhonetic != null && !isLargePresentation) {
            Text(
                text = "उच्चारण: $devanagariPhonetic",
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.7f),
                modifier = Modifier.padding(top = 2.dp)
            )
        }
    }
}
