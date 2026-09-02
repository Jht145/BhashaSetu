package org.bhashasetu.app.data.importer

import android.content.Context
import org.bhashasetu.app.data.local.AppDatabase
import org.bhashasetu.app.data.local.ConceptEntity
import org.json.JSONObject
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.util.zip.ZipInputStream

object PackImporter {
    /**
     * Unpacks a downloaded .pack file, reads curriculum metadata,
     * and synchronizes concepts into local Room DB.
     */
    suspend fun importPackFile(context: Context, packFile: File): Boolean {
        return try {
            val db = AppDatabase.getDatabase(context)
            val conceptsToInsert = mutableListOf<ConceptEntity>()
            var grade = 1
            var subjectCode = "EVS"
            var languageCode = "sat"
            var scriptCode = "olck"

            ZipInputStream(FileInputStream(packFile)).use { zis ->
                var entry = zis.nextEntry
                while (entry != null) {
                    when (entry.name) {
                        "manifest.json" -> {
                            val content = zis.bufferedReader().readText()
                            val json = JSONObject(content)
                            grade = json.optInt("grade", 1)
                            subjectCode = json.optString("subject_code", "EVS")
                            languageCode = json.optString("language_code", "sat")
                            scriptCode = json.optString("script_code", "olck")
                        }
                        "curriculum_data.json" -> {
                            val content = zis.bufferedReader().readText()
                            val json = JSONObject(content)
                            val array = json.optJSONArray("concepts")
                            if (array != null) {
                                for (i in 0 until array.length()) {
                                    val obj = array.getJSONObject(i)
                                    val entity = ConceptEntity(
                                        id = obj.optInt("id", i + 1),
                                        grade = grade,
                                        subjectCode = subjectCode,
                                        title = obj.optString("title", ""),
                                        standardText = obj.optString("standard_text", ""),
                                        vernacularTitle = obj.optString("vernacular", obj.optString("title")),
                                        vernacularText = obj.optString("vernacular_text", ""),
                                        languageCode = languageCode,
                                        scriptCode = scriptCode,
                                        culturalMetaphor = obj.optString("cultural_metaphor", null)
                                    )
                                    conceptsToInsert.add(entity)
                                }
                            }
                        }
                    }
                    entry = zis.nextEntry
                }
            }

            if (conceptsToInsert.isNotEmpty()) {
                db.conceptDao().insertAll(conceptsToInsert)
            }
            true
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }
}
