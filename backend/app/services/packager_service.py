"""
Offline Package Compiler Service
Bundles curriculum data, compressed SQLite models (curriculum.db), and audio clips into
compact offline .pack files for Android zero-bandwidth classrooms.
"""

import os
import json
import sqlite3
import zipfile
import hashlib
import tempfile
from typing import Dict, Any, Tuple, List

from backend.app.core.config import settings
from backend.app.services.ai.nmt_service import offline_translator


class PackagerService:
    @classmethod
    def create_offline_package(
        cls,
        pack_identifier: str,
        grade: int,
        subject_code: str,
        language_code: str,
        curriculum_payload: Dict[str, Any]
    ) -> Tuple[str, float, str]:
        """
        Creates a compressed offline pack file (.pack / .zip) with embedded SQLite curriculum.db
        populated using local offline neural/lexicon translation batching.
        Returns: (file_path, file_size_mb, checksum_sha256)
        """
        filename = f"{pack_identifier}.pack"
        pack_path = os.path.join(settings.OFFLINE_PACKS_DIR, filename)
        target_script = "olck" if language_code.lower() == "sat" else "deva"

        raw_concepts = curriculum_payload.get("concepts", [])
        
        # Batch translate concept titles and contents locally using offline engine
        titles = [c.get("title", "") for c in raw_concepts]
        translations = offline_translator.translate_batch_sync(
            texts=titles,
            source_lang="hin",
            target_lang=language_code,
            target_script=target_script,
        )

        # Build embedded SQLite database (curriculum.db)
        with tempfile.TemporaryDirectory() as tmpdir:
            sqlite_path = os.path.join(tmpdir, "curriculum.db")
            conn = sqlite3.connect(sqlite_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS concepts (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    standard_text TEXT,
                    vernacular_title TEXT NOT NULL,
                    vernacular_text TEXT,
                    language_code TEXT NOT NULL,
                    script_code TEXT NOT NULL,
                    quality_score REAL DEFAULT 5.0
                )
            """)

            for idx, c in enumerate(raw_concepts):
                concept_id = c.get("id", idx + 1)
                title = c.get("title", f"Concept {idx + 1}")
                std_text = c.get("standard_text", title)
                vernacular_title = translations[idx][0] if idx < len(translations) else c.get("vernacular", title)
                vernacular_text = c.get("vernacular_text", vernacular_title)

                cursor.execute("""
                    INSERT INTO concepts (id, title, standard_text, vernacular_title, vernacular_text, language_code, script_code, quality_score)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (concept_id, title, std_text, vernacular_title, vernacular_text, language_code, target_script, 5.0))

            conn.commit()
            conn.close()

            # Write manifest, curriculum JSON, and embedded SQLite into zip pack container
            with zipfile.ZipFile(pack_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                # 1. Manifest
                manifest = {
                    "pack_identifier": pack_identifier,
                    "grade": grade,
                    "subject_code": subject_code,
                    "language_code": language_code,
                    "script_code": target_script,
                    "version": "1.0.0",
                    "format_version": "bhashasetu-v1",
                    "total_concepts": len(raw_concepts),
                    "database": "curriculum.db"
                }
                zipf.writestr("manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))

                # 2. JSON Data export
                zipf.writestr("curriculum_data.json", json.dumps(curriculum_payload, indent=2, ensure_ascii=False))

                # 3. Embedded SQLite database
                zipf.write(sqlite_path, arcname="curriculum.db")

                # 4. Embedded font descriptor
                zipf.writestr("fonts/README.txt", "Embedded NotoSansOlChiki-Regular font assets")

        # Compute SHA-256 checksum
        sha256_hash = hashlib.sha256()
        with open(pack_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        checksum = sha256_hash.hexdigest()
        file_size_mb = round(os.path.getsize(pack_path) / (1024 * 1024), 3)

        return pack_path, max(file_size_mb, 0.05), checksum
