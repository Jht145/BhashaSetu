package org.bhashasetu.app.sync

import android.content.Context
import android.os.BatteryManager
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.bhashasetu.app.data.local.AppDatabase
import org.json.JSONArray
import org.json.JSONObject
import java.util.concurrent.TimeUnit

class DeltaSyncWorker(
    appContext: Context,
    workerParams: WorkerParameters
) : CoroutineWorker(appContext, workerParams) {

    private val client = OkHttpClient.Builder()
        .connectTimeout(15, TimeUnit.SECONDS)
        .readTimeout(20, TimeUnit.SECONDS)
        .build()

    override suspend fun doWork(): Result {
        return try {
            val db = AppDatabase.getDatabase(applicationContext)
            val completed = db.conceptDao().getCompletedConcepts()
            val serverBaseUrl = inputData.getString("server_url") ?: "http://10.0.2.2:8000"

            val syncArray = JSONArray()
            completed.forEach { concept ->
                val item = JSONObject().apply {
                    put("table_name", "offline_concepts")
                    put("action", "UPDATE")
                    put("client_id", "concept_${concept.id}")
                    put("data", JSONObject().apply {
                        put("concept_id", concept.id)
                        put("is_completed", true)
                        put("last_accessed", concept.lastAccessedTimestamp)
                    })
                    put("client_timestamp", System.currentTimeMillis())
                }
                syncArray.put(item)
            }

            val payload = JSONObject().apply {
                put("device_id", android.provider.Settings.Secure.getString(
                    applicationContext.contentResolver,
                    android.provider.Settings.Secure.ANDROID_ID
                ) ?: "unknown_device")
                put("app_version", "1.0.0")
                put("sync_items", syncArray)
            }

            val requestBody = payload.toString().toRequestBody("application/json; charset=utf-8".toMediaType())
            val request = Request.Builder()
                .url("$serverBaseUrl/api/v1/sync/delta-upload")
                .post(requestBody)
                .build()

            val response = client.newCall(request).execute()
            if (response.isSuccessful) {
                Result.success()
            } else {
                Result.retry()
            }
        } catch (e: Exception) {
            e.printStackTrace()
            Result.retry()
        }
    }
}
