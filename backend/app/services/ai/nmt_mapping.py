"""
IndicTrans2 Language & Script Tag Resolver for Jharkhand Dialects
Maps internal BhashaSetu language codes to standard AI4Bharat IndicTrans2 BCP-47 tags
and handles execution strategies (Native IndicTrans2, Transliterated, or Lexicon fallback).
"""

from enum import Enum
from typing import Tuple, Optional, Dict

class TranslationBackend(str, Enum):
    INDICTRANS2 = "indictrans2"
    INDICTRANS2_WITH_OLCHIKI_TRANSLITERATION = "it2_olck_translit"
    VERNACULAR_LEXICON = "lexicon_fallback"


# Officially supported IndicTrans2 language tags for BhashaSetu routing
INDICTRANS2_TAGS: Dict[str, str] = {
    "hin": "hin_Deva",
    "eng": "eng_Latn",
    "sat_olck": "sat_Olck",
    # Regional dialect proxies (Indo-Aryan branch)
    "kht": "mag_Deva",  # Khortha -> Magahi proxy
    "sck": "bho_Deva",  # Nagpuri / Sadri -> Bhojpuri proxy
    "tdb": "ben_Deva",  # Panchpargania -> Bengali / Devanagari proxy
    "kyw": "hin_Deva",  # Kurmali -> Hindi proxy
}

LANGUAGE_ALIASES: Dict[str, str] = {
    "santhali": "sat",
    "mundari": "unr",
    "ho": "hoc",
    "kurukh": "kru",
    "kharia": "khr",
    "khortha": "kht",
    "nagpuri": "sck",
    "panchpargania": "tdb",
    "kurmali": "kyw",
    "hindi": "hin",
    "english": "eng",
}


def normalize_code(code: str) -> str:
    """Normalizes language/script string."""
    if not code:
        return ""
    cleaned = code.strip().lower()
    if "_" in cleaned:
        cleaned = cleaned.split("_")[0]
    return LANGUAGE_ALIASES.get(cleaned, cleaned)


def resolve_translation_strategy(
    source_lang: str,
    target_lang: str,
    target_script: str = "deva"
) -> Tuple[TranslationBackend, Optional[str], Optional[str]]:
    """
    Returns the execution backend and corresponding IndicTrans2 source and target tags.

    Handles the 3 critical architectural constraints:
    1. Santhali in Ol Chiki -> Native IndicTrans2 ('sat_Olck')
    2. Santhali in Devanagari -> IndicTrans2 ('sat_Olck') + OlChikiService transliteration
    3. Regional dialects -> IndicTrans2 proxies (Khortha->mag_Deva, Nagpuri->bho_Deva, etc.)
    4. Non-scheduled tribal tongues (Mundari, Ho, Kurukh, Kharia) -> Vernacular Lexicon fallback
    """
    src_key = normalize_code(source_lang)
    tgt_key = normalize_code(target_lang)
    script = target_script.strip().lower() if target_script else "deva"

    src_tag = INDICTRANS2_TAGS.get(src_key, "hin_Deva")

    # Case 1: Native Santhali in Ol Chiki
    if tgt_key == "sat" and script in ["olck", "sat_olck"]:
        return TranslationBackend.INDICTRANS2, src_tag, "sat_Olck"

    # Case 2: Santhali requested in Devanagari (Translate to Ol Chiki -> Transliterate to Devanagari)
    if tgt_key == "sat" and script in ["deva", "sat_deva", "latn"]:
        return TranslationBackend.INDICTRANS2_WITH_OLCHIKI_TRANSLITERATION, src_tag, "sat_Olck"

    # Case 3: Regional Dialects mapped to IndicTrans2 proxies
    if tgt_key in ["kht", "sck", "tdb", "kyw"]:
        return TranslationBackend.INDICTRANS2, src_tag, INDICTRANS2_TAGS[tgt_key]

    # Case 4: Non-scheduled tribal tongues (Mundari, Ho, Kurukh, Kharia) -> Lexicon / Rule Engine
    if tgt_key in ["unr", "hoc", "kru", "khr"]:
        return TranslationBackend.VERNACULAR_LEXICON, None, None

    # Bridge translations: Hindi or English target
    if tgt_key == "hin":
        return TranslationBackend.INDICTRANS2, src_tag, "hin_Deva"
    if tgt_key == "eng":
        return TranslationBackend.INDICTRANS2, src_tag, "eng_Latn"

    # Default fallback
    return TranslationBackend.VERNACULAR_LEXICON, None, None
