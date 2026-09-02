package org.bhashasetu.app.data.local

import androidx.room.*
import kotlinx.coroutines.flow.Flow

@Dao
interface ConceptDao {
    @Query("SELECT * FROM offline_concepts WHERE grade = :grade AND languageCode = :languageCode ORDER BY id ASC")
    fun getConceptsByGradeAndLanguage(grade: Int, languageCode: String): Flow<List<ConceptEntity>>

    @Query("SELECT * FROM offline_concepts WHERE id = :conceptId")
    suspend fun getConceptById(conceptId: Int): ConceptEntity?

    @Query("SELECT * FROM offline_concepts WHERE title LIKE '%' || :query || '%' OR vernacularTitle LIKE '%' || :query || '%'")
    suspend fun searchConcepts(query: String): List<ConceptEntity>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(concepts: List<ConceptEntity>)

    @Update
    suspend fun update(concept: ConceptEntity)

    @Query("SELECT COUNT(*) FROM offline_concepts")
    suspend fun getConceptCount(): Int

    @Query("SELECT * FROM offline_concepts WHERE isCompleted = 1")
    suspend fun getCompletedConcepts(): List<ConceptEntity>
}
