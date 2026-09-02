package org.bhashasetu.app.data.remote

import retrofit2.Response
import retrofit2.http.*

data class TranslationRequestDto(
    val text: String,
    val source_language: String = "hin",
    val target_language: String = "sat",
    val target_script: String = "olck"
)

data class TranslationResponseDto(
    val source_text: String,
    val translated_text: String,
    val phonetic_devanagari: String?,
    val latency_ms: Float
)

data class PackageResponseDto(
    val id: Int,
    val pack_identifier: String,
    val grade: Int,
    val subject_code: String,
    val language_code: String,
    val file_size_mb: Float,
    val checksum_sha256: String
)

interface BhashaSetuApiService {
    @POST("/api/v1/translation/translate")
    suspend fun translateText(@Body request: TranslationRequestDto): Response<TranslationResponseDto>

    @GET("/api/v1/sync/packages")
    suspend fun getAvailablePackages(
        @Query("grade") grade: Int?,
        @Query("language_code") languageCode: String?
    ): Response<List<PackageResponseDto>>
}
