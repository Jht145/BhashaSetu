package org.bhashasetu.app.data.local

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "offline_concepts")
data class ConceptEntity(
    @PrimaryKey val id: Int,
    val grade: Int,
    val subjectCode: String,
    val title: String,
    val standardText: String,
    val vernacularTitle: String,
    val vernacularText: String,
    val languageCode: String,
    val scriptCode: String,
    val culturalMetaphor: String? = null,
    val localAudioPath: String? = null,
    val isCompleted: Boolean = false,
    val lastAccessedTimestamp: Long = System.currentTimeMillis()
)
