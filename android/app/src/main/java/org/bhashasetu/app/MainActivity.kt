package org.bhashasetu.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Class_
import androidx.compose.material.icons.filled.MenuBook
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import org.bhashasetu.app.ui.screens.ClassroomScreen
import org.bhashasetu.app.ui.screens.OfflineCurriculumScreen
import org.bhashasetu.app.ui.theme.BhashaSetuTheme
import org.bhashasetu.app.ui.theme.ForestGreen
import org.bhashasetu.app.ui.viewmodel.ClassroomViewModel

class MainActivity : ComponentActivity() {
    private val classroomViewModel: ClassroomViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            BhashaSetuTheme {
                var selectedTab by remember { mutableStateOf(0) }

                Scaffold(
                    modifier = Modifier.fillMaxSize(),
                    bottomBar = {
                        NavigationBar(
                            containerColor = MaterialTheme.colorScheme.surface
                        ) {
                            NavigationBarItem(
                                selected = selectedTab == 0,
                                onClick = { selectedTab = 0 },
                                icon = { Icon(Icons.Default.Class_, contentDescription = "Classroom") },
                                label = { Text("कक्षा अनुवाद (Live)") }
                            )
                            NavigationBarItem(
                                selected = selectedTab == 1,
                                onClick = { selectedTab = 1 },
                                icon = { Icon(Icons.Default.MenuBook, contentDescription = "Curriculum") },
                                label = { Text("पाठ्य सामग्री (Packs)") }
                            )
                        }
                    }
                ) { innerPadding ->
                    Surface(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(innerPadding)
                    ) {
                        when (selectedTab) {
                            0 -> ClassroomScreen(viewModel = classroomViewModel)
                            1 -> OfflineCurriculumScreen(viewModel = classroomViewModel)
                        }
                    }
                }
            }
        }
    }
}
