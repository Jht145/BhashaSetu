package org.bhashasetu.app.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable

private val LightColorScheme = lightColorScheme(
    primary = ForestGreen,
    secondary = BrightGold,
    tertiary = OlChikiAccent,
    background = WarmSand,
    surface = CardSurface,
    onPrimary = CardSurface,
    onSecondary = TextDark,
    onBackground = TextDark,
    onSurface = TextDark,
)

@Composable
fun BhashaSetuTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = LightColorScheme,
        content = content
    )
}
