"""
Unit and Integration Tests for IndicTrans2 Offline Translation Engine & Packager
"""

import os
import sqlite3
import zipfile
import pytest
from backend.app.services.ai.nmt_mapping import (
    TranslationBackend,
    resolve_translation_strategy,
    INDICTRANS2_TAGS,
)
from backend.app.services.ai.indic_processor import IndicTextProcessor
from backend.app.services.ai.nmt_service import (
    offline_translator,
    NMTService,
    OfflineIndicTransService,
)
from backend.app.services.packager_service import PackagerService


def test_language_strategy_routing_santhali_olchiki():
    """Santhali in Ol Chiki should route to native IndicTrans2 sat_Olck."""
    strategy, src_tag, tgt_tag = resolve_translation_strategy("hin", "sat", "olck")
    assert strategy == TranslationBackend.INDICTRANS2
    assert src_tag == "hin_Deva"
    assert tgt_tag == "sat_Olck"


def test_language_strategy_routing_santhali_devanagari():
    """Santhali in Devanagari should route to IndicTrans2 sat_Olck + transliteration."""
    strategy, src_tag, tgt_tag = resolve_translation_strategy("hin", "sat", "deva")
    assert strategy == TranslationBackend.INDICTRANS2_WITH_OLCHIKI_TRANSLITERATION
    assert src_tag == "hin_Deva"
    assert tgt_tag == "sat_Olck"


def test_language_strategy_routing_regional_proxies():
    """Regional dialects should route to Indo-Aryan proxies."""
    # Khortha -> Magahi
    strat, _, tgt = resolve_translation_strategy("hin", "kht", "deva")
    assert strat == TranslationBackend.INDICTRANS2
    assert tgt == "mag_Deva"

    # Nagpuri -> Bhojpuri
    strat, _, tgt = resolve_translation_strategy("hin", "sck", "deva")
    assert strat == TranslationBackend.INDICTRANS2
    assert tgt == "bho_Deva"

    # Panchpargania -> Bengali
    strat, _, tgt = resolve_translation_strategy("hin", "tdb", "deva")
    assert strat == TranslationBackend.INDICTRANS2
    assert tgt == "ben_Deva"

    # Kurmali -> Hindi
    strat, _, tgt = resolve_translation_strategy("hin", "kyw", "deva")
    assert strat == TranslationBackend.INDICTRANS2
    assert tgt == "hin_Deva"


def test_language_strategy_routing_non_scheduled_tribal():
    """Mundari, Ho, Kurukh, Kharia must route to VERNACULAR_LEXICON to avoid CTranslate2 OOV crashes."""
    for lang in ["unr", "hoc", "kru", "khr"]:
        strat, src, tgt = resolve_translation_strategy("hin", lang, "deva")
        assert strat == TranslationBackend.VERNACULAR_LEXICON
        assert src is None
        assert tgt is None


def test_indic_processor_formatting():
    """Tests prefix token formatting and post-processing."""
    raw = "  नमस्ते   दुनिया! "
    formatted = IndicTextProcessor.format_input_for_indictrans2(raw, "hin_Deva", "sat_Olck")
    assert formatted == "__hin_Deva__ __sat_Olck__ नमस्ते दुनिया!"

    # Test clean post-processing
    model_output = "__sat_Olck__ ᱡᱚᱦᱟᱨ  ᱫᱟᱜ ᱾"
    cleaned = IndicTextProcessor.postprocess_output(model_output, "sat_Olck")
    assert "__" not in cleaned
    assert cleaned == "ᱡᱚᱦᱟᱨ ᱫᱟᱜ᱾"


@pytest.mark.asyncio
async def test_offline_nmt_service_async():
    """Tests async translation wrapper without event loop locking."""
    translated, phonetic, latency, conf = await NMTService.translate_async(
        text="नमस्ते",
        source_language="hin",
        target_language="sat",
        target_script="olck"
    )
    assert "ᱡᱚᱦᱟᱨ" in translated
    assert latency > 0
    assert conf > 0.8


def test_offline_packager_sqlite_generation():
    """Integration test verifying PackagerService creates SQLite curriculum.db inside .pack."""
    test_identifier = "TEST_INTEG_G2_EVS_SAT_v1"
    curriculum_payload = {
        "concepts": [
            {"id": 101, "title": "पेड़ और जंगल", "standard_text": "पेड़ हमें फल और छाया देते हैं।"},
            {"id": 102, "title": "पानी का चक्र", "standard_text": "पानी से बादल बनते हैं।"}
        ]
    }

    file_path, size_mb, checksum = PackagerService.create_offline_package(
        pack_identifier=test_identifier,
        grade=2,
        subject_code="G2_EVS",
        language_code="sat",
        curriculum_payload=curriculum_payload
    )

    assert os.path.exists(file_path)
    assert size_mb < 50.0
    assert len(checksum) == 64

    # Unpack and verify embedded SQLite database
    with zipfile.ZipFile(file_path, "r") as zipf:
        file_list = zipf.namelist()
        assert "curriculum.db" in file_list
        assert "manifest.json" in file_list

        # Read SQLite database directly from unpacked archive
        sqlite_bytes = zipf.read("curriculum.db")
        assert len(sqlite_bytes) > 0

        # Extract to check table data
        tmp_db = os.path.join(os.path.dirname(file_path), f"temp_{test_identifier}.db")
        with open(tmp_db, "wb") as f:
            f.write(sqlite_bytes)

        conn = sqlite3.connect(tmp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, vernacular_title, language_code, script_code FROM concepts")
        rows = cursor.fetchall()
        conn.close()
        os.remove(tmp_db)

        assert len(rows) == 2
        assert rows[0][0] == 101
        assert rows[0][3] == "sat"
        assert rows[0][4] == "olck"
