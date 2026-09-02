"""
Translation & Linguistic Engine for BhashaSetu
Handles Hindi / English / Hinglish -> 9 Indigenous & Regional Languages translation,
token-based matching, phrase breakdown, and multi-script transliteration.
"""

import re
from typing import Dict, List, Any, Optional
from backend.data.languages import LANGUAGES
from backend.data.dictionary import VOCABULARY, CATEGORIES
from backend.data.scripts_data import devanagari_to_olchiki
from backend.app.services.ai.indic_processor import IndicTextProcessor


class BhashaSetuTranslator:
    def __init__(self):
        self.languages = LANGUAGES
        self.vocabulary = VOCABULARY
        self.categories = CATEGORIES
        self._build_indexes()

    def _clean_text(self, text: str) -> str:
        if not text:
            return ""
        # Remove excess whitespace and common punctuation for matching
        text = text.strip()
        cleaned = re.sub(r'[\?\.!,।\n\r]+', ' ', text)
        return re.sub(r'\s+', ' ', cleaned).strip().lower()

    def _build_indexes(self):
        """Index dictionary by normalized Hindi & English keys and token keywords."""
        self.phrase_index = {}
        self.word_index = {}

        for item in self.vocabulary:
            # 1. Hindi indexing
            hindi_raw = item.get("hindi", "")
            hindi_variants = re.split(r'[/,()]', hindi_raw)
            for var in hindi_variants:
                clean_var = self._clean_text(var)
                if clean_var:
                    if clean_var not in self.phrase_index:
                        self.phrase_index[clean_var] = item
                    words = clean_var.split()
                    for w in words:
                        if len(w) > 1:
                            if w not in self.word_index:
                                self.word_index[w] = []
                            if item not in self.word_index[w]:
                                self.word_index[w].append(item)

            # 2. English indexing
            english_raw = item.get("english", "")
            english_variants = re.split(r'[/,()]', english_raw)
            for var in english_variants:
                clean_var = self._clean_text(var)
                if clean_var:
                    if clean_var not in self.phrase_index:
                        self.phrase_index[clean_var] = item
                    words = clean_var.split()
                    for w in words:
                        if len(w) > 1:
                            if w not in self.word_index:
                                self.word_index[w] = []
                            if item not in self.word_index[w]:
                                self.word_index[w].append(item)

    CODE_MAP = {
        "sat_olck": "santhali", "sat": "santhali", "santhali": "santhali",
        "unr_deva": "mundari", "unr": "mundari", "mundari": "mundari",
        "hoc_wara": "ho", "hoc_deva": "ho", "hoc": "ho", "ho": "ho",
        "kru_deva": "kurukh", "kru": "kurukh", "kurukh": "kurukh",
        "khr_deva": "kharia", "khr": "kharia", "kharia": "kharia",
        "kht_deva": "khortha", "kht": "khortha", "khortha": "khortha",
        "sck_deva": "nagpuri", "sck": "nagpuri", "nagpuri": "nagpuri",
        "tdb_deva": "panchpargania", "tdb": "panchpargania", "panchpargania": "panchpargania",
        "kyw_deva": "kurmali", "kyw": "kurmali", "kurmali": "kurmali",
        "hin_deva": "hindi", "hin": "hindi", "hindi": "hindi",
        "eng_latn": "english", "eng": "english", "english": "english",
    }

    def translate_single(self, text: str, target_lang: str, source_lang: Optional[str] = "hin_Deva") -> Dict[str, Any]:
        """
        Translates Hindi, English, or Hinglish text query to a specific target language.
        Returns translations with native script, devanagari, phonetics, and word breakdown.
        """
        target_lang_clean = target_lang.lower().strip()
        target_lang_id = self.CODE_MAP.get(target_lang_clean, target_lang_clean)
        if target_lang_id not in self.languages:
            target_lang_id = "santhali"

        clean_query = self._clean_text(text)
        lang_meta = self.languages[target_lang_id]
        
        is_latin = IndicTextProcessor.is_latin_text(text)
        translation_method = "direct_dictionary"
        if is_latin:
            translation_method = "hinglish_english_auto_transducer"

        # 1. Exact phrase lookup in dictionary
        if clean_query in self.phrase_index:
            item = self.phrase_index[clean_query]
            tr = item["translations"].get(target_lang_id, {})
            native_val = tr.get("native", tr.get("dev", ""))
            return {
                "success": True,
                "match_type": "exact",
                "source_text": text,
                "matched_entry": item.get("hindi", "") + " (" + item.get("english", "") + ")",
                "target_lang": target_lang_id,
                "target_lang_name": lang_meta["name_hi"],
                "emoji": item.get("emoji", "✨"),
                "category": item.get("category", "general"),
                "devanagari": tr.get("dev", ""),
                "native_script": native_val,
                "translated_text": native_val or tr.get("dev", ""),
                "phonetic": tr.get("phonetic", ""),
                "transliteration": tr.get("phonetic", ""),
                "script_name": lang_meta["primary_script"],
                "translation_method": translation_method,
                "quality_flags": [],
                "warnings": [],
                "words_breakdown": self._breakdown_phrase(item, target_lang_id)
            }

        # 2. Check if normalized Hinglish / English maps to an exact phrase in dictionary
        if is_latin:
            hindi_normalized = IndicTextProcessor.convert_english_or_hinglish_to_hindi(text)
            clean_hindi = self._clean_text(hindi_normalized)
            if clean_hindi in self.phrase_index:
                item = self.phrase_index[clean_hindi]
                tr = item["translations"].get(target_lang_id, {})
                native_val = tr.get("native", tr.get("dev", ""))
                return {
                    "success": True,
                    "match_type": "exact_normalized",
                    "source_text": text,
                    "matched_entry": item.get("hindi", "") + " (" + item.get("english", "") + ")",
                    "target_lang": target_lang_id,
                    "target_lang_name": lang_meta["name_hi"],
                    "emoji": item.get("emoji", "✨"),
                    "category": item.get("category", "general"),
                    "devanagari": tr.get("dev", ""),
                    "native_script": native_val,
                    "translated_text": native_val or tr.get("dev", ""),
                    "phonetic": tr.get("phonetic", ""),
                    "transliteration": tr.get("phonetic", ""),
                    "script_name": lang_meta["primary_script"],
                    "translation_method": translation_method,
                    "quality_flags": [],
                    "warnings": [],
                    "words_breakdown": self._breakdown_phrase(item, target_lang_id)
                }

        # 3. Substring / partial match lookup
        for phrase, item in self.phrase_index.items():
            if phrase in clean_query or (len(clean_query) >= 3 and clean_query in phrase):
                tr = item["translations"].get(target_lang_id, {})
                native_val = tr.get("native", tr.get("dev", ""))
                return {
                    "success": True,
                    "match_type": "partial",
                    "source_text": text,
                    "matched_entry": item.get("hindi", "") + " (" + item.get("english", "") + ")",
                    "target_lang": target_lang_id,
                    "target_lang_name": lang_meta["name_hi"],
                    "emoji": item.get("emoji", "✨"),
                    "category": item.get("category", "general"),
                    "devanagari": tr.get("dev", ""),
                    "native_script": native_val,
                    "translated_text": native_val or tr.get("dev", ""),
                    "phonetic": tr.get("phonetic", ""),
                    "transliteration": tr.get("phonetic", ""),
                    "script_name": lang_meta["primary_script"],
                    "translation_method": translation_method,
                    "quality_flags": [],
                    "warnings": [],
                    "words_breakdown": self._breakdown_phrase(item, target_lang_id)
                }

        # 4. Token-by-token composition with English / Hinglish transliteration support
        raw_tokens = [t for t in re.split(r'\s+', text.strip()) if t]
        translated_dev = []
        translated_native = []
        translated_phonetic = []
        breakdowns = []
        found_any = False

        for token in raw_tokens:
            clean_tok = self._clean_text(token)
            
            # Check if token is in dictionary
            if clean_tok in self.word_index and len(self.word_index[clean_tok]) > 0:
                found_any = True
                matched_item = self.word_index[clean_tok][0]
                tr = matched_item["translations"].get(target_lang_id, {})
                d_val = tr.get("dev", token)
                n_val = tr.get("native", d_val)
                p_val = tr.get("phonetic", token)
                translated_dev.append(d_val)
                translated_native.append(n_val)
                translated_phonetic.append(p_val)
                breakdowns.append({
                    "original": token,
                    "devanagari": d_val,
                    "native": n_val,
                    "phonetic": p_val,
                    "emoji": matched_item.get("emoji", "🔹")
                })
            else:
                # If Latin, convert token to Hindi Devanagari first
                tok_dev = IndicTextProcessor.convert_english_or_hinglish_to_hindi(token) if is_latin else token
                clean_tok_dev = self._clean_text(tok_dev)

                if clean_tok_dev in self.word_index and len(self.word_index[clean_tok_dev]) > 0:
                    found_any = True
                    matched_item = self.word_index[clean_tok_dev][0]
                    tr = matched_item["translations"].get(target_lang_id, {})
                    d_val = tr.get("dev", tok_dev)
                    n_val = tr.get("native", d_val)
                    p_val = tr.get("phonetic", token)
                    translated_dev.append(d_val)
                    translated_native.append(n_val)
                    translated_phonetic.append(p_val)
                    breakdowns.append({
                        "original": token,
                        "devanagari": d_val,
                        "native": n_val,
                        "phonetic": p_val,
                        "emoji": matched_item.get("emoji", "🔹")
                    })
                else:
                    translated_dev.append(tok_dev)
                    if target_lang_id == "santhali":
                        translated_native.append(devanagari_to_olchiki(tok_dev))
                    else:
                        translated_native.append(tok_dev)
                    translated_phonetic.append(token)
                    breakdowns.append({
                        "original": token,
                        "devanagari": tok_dev,
                        "native": devanagari_to_olchiki(tok_dev) if target_lang_id == "santhali" else tok_dev,
                        "phonetic": token,
                        "emoji": "🔹"
                    })

        dev_result = " ".join(translated_dev)
        native_result = " ".join(translated_native)
        phonetic_result = " ".join(translated_phonetic)

        return {
            "success": True,
            "match_type": "tokenized" if found_any else "transliterated",
            "source_text": text,
            "matched_entry": None,
            "target_lang": target_lang_id,
            "target_lang_name": lang_meta["name_hi"],
            "emoji": "✨",
            "category": "general",
            "devanagari": dev_result,
            "native_script": native_result,
            "translated_text": native_result or dev_result,
            "phonetic": phonetic_result,
            "transliteration": phonetic_result,
            "script_name": lang_meta["primary_script"],
            "translation_method": translation_method,
            "quality_flags": [] if found_any else ["transliterated"],
            "warnings": [],
            "words_breakdown": breakdowns
        }

    def _breakdown_phrase(self, item: Dict[str, Any], target_lang: str) -> List[Dict[str, str]]:
        tr = item["translations"].get(target_lang, {})
        d_val = tr.get("dev", "")
        n_val = tr.get("native", d_val)
        p_val = tr.get("phonetic", "")

        return [{
            "original": item.get("hindi", ""),
            "devanagari": d_val,
            "native": n_val,
            "phonetic": p_val,
            "emoji": item.get("emoji", "✨")
        }]

    def translate_all_languages(self, text: str, source_lang: Optional[str] = "hin_Deva") -> Dict[str, Any]:
        """Translates a single text into all 9 tribal and regional languages simultaneously."""
        results = {}
        for lang_id in self.languages:
            results[lang_id] = self.translate_single(text, lang_id, source_lang)

        return {
            "source_text": text,
            "source_lang": source_lang,
            "translations": results
        }

    def get_category_items(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns vocabulary items, optionally filtered by category."""
        if not category or category.lower() == "all":
            return self.vocabulary
        return [
            item for item in self.vocabulary
            if item.get("category", "").lower() == category.lower()
        ]

    def search_dictionary(self, query: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Searches vocabulary dictionary across Hindi, English, and tribal words."""
        clean_q = self._clean_text(query)
        if not clean_q:
            return self.vocabulary[:limit]

        results = []
        for item in self.vocabulary:
            h = self._clean_text(item.get("hindi", ""))
            e = self._clean_text(item.get("english", ""))
            if clean_q in h or clean_q in e:
                results.append(item)
                if len(results) >= limit:
                    break

        return results


# Global singleton instance
translator_service = BhashaSetuTranslator()
