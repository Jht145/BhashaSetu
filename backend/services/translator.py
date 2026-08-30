"""
Translation & Linguistic Engine for BhashaSetu
Handles Hindi -> 9 Indigenous & Regional Languages translation,
token-based matching, phrase breakdown, and multi-script transliteration.
"""

import re
from typing import Dict, List, Any, Optional
from backend.data.languages import LANGUAGES
from backend.data.dictionary import VOCABULARY, CATEGORIES
from backend.data.scripts_data import devanagari_to_olchiki

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
        """Index dictionary by normalized Hindi keys and token keywords."""
        self.phrase_index = {}
        self.word_index = {}

        for item in self.vocabulary:
            hindi_raw = item["hindi"]
            # Split variants like "नमस्ते / जोहार" or "गाय (गौमाता)"
            variants = re.split(r'[/,()]', hindi_raw)
            for var in variants:
                clean_var = self._clean_text(var)
                if clean_var:
                    if clean_var not in self.phrase_index:
                        self.phrase_index[clean_var] = item
                    # Also index single words
                    words = clean_var.split()
                    for w in words:
                        if len(w) > 1:
                            if w not in self.word_index:
                                self.word_index[w] = []
                            if item not in self.word_index[w]:
                                self.word_index[w].append(item)

    def translate_single(self, text: str, target_lang: str) -> Dict[str, Any]:
        """
        Translates a Hindi text query to a specific target language.
        Returns translations with native script, devanagari, phonetics, and word breakdown.
        """
        target_lang = target_lang.lower().strip()
        if target_lang not in self.languages:
            target_lang = "santhali"

        clean_query = self._clean_text(text)
        lang_meta = self.languages[target_lang]

        # 1. Exact phrase lookup
        if clean_query in self.phrase_index:
            item = self.phrase_index[clean_query]
            tr = item["translations"].get(target_lang, {})
            return {
                "success": True,
                "match_type": "exact",
                "source_text": text,
                "matched_entry": item["hindi"],
                "target_lang": target_lang,
                "target_lang_name": lang_meta["name_hi"],
                "emoji": item.get("emoji", "✨"),
                "category": item.get("category", "general"),
                "devanagari": tr.get("dev", ""),
                "native_script": tr.get("native", tr.get("dev", "")),
                "phonetic": tr.get("phonetic", ""),
                "script_name": lang_meta["primary_script"],
                "words_breakdown": self._breakdown_phrase(item, target_lang)
            }

        # 2. Substring / partial match lookup
        for phrase, item in self.phrase_index.items():
            if phrase in clean_query or clean_query in phrase:
                tr = item["translations"].get(target_lang, {})
                return {
                    "success": True,
                    "match_type": "partial",
                    "source_text": text,
                    "matched_entry": item["hindi"],
                    "target_lang": target_lang,
                    "target_lang_name": lang_meta["name_hi"],
                    "emoji": item.get("emoji", "✨"),
                    "category": item.get("category", "general"),
                    "devanagari": tr.get("dev", ""),
                    "native_script": tr.get("native", tr.get("dev", "")),
                    "phonetic": tr.get("phonetic", ""),
                    "script_name": lang_meta["primary_script"],
                    "words_breakdown": self._breakdown_phrase(item, target_lang)
                }

        # 3. Token-by-token composition
        tokens = [t for t in re.split(r'\s+', text.strip()) if t]
        translated_dev = []
        translated_native = []
        translated_phonetic = []
        breakdowns = []
        found_any = False

        for token in tokens:
            clean_tok = self._clean_text(token)
            if clean_tok in self.word_index and len(self.word_index[clean_tok]) > 0:
                found_any = True
                matched_item = self.word_index[clean_tok][0]
                tr = matched_item["translations"].get(target_lang, {})
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
                translated_dev.append(token)
                if target_lang == "santhali":
                    translated_native.append(devanagari_to_olchiki(token))
                else:
                    translated_native.append(token)
                translated_phonetic.append(token)
                breakdowns.append({
                    "original": token,
                    "devanagari": token,
                    "native": token,
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
            "target_lang": target_lang,
            "target_lang_name": lang_meta["name_hi"],
            "emoji": "✨",
            "category": "general",
            "devanagari": dev_result,
            "native_script": native_result,
            "phonetic": phonetic_result,
            "script_name": lang_meta["primary_script"],
            "words_breakdown": breakdowns
        }

    def _breakdown_phrase(self, item: Dict[str, Any], target_lang: str) -> List[Dict[str, str]]:
        tr = item["translations"].get(target_lang, {})
        return [{
            "original": item["hindi"],
            "devanagari": tr.get("dev", ""),
            "native": tr.get("native", tr.get("dev", "")),
            "phonetic": tr.get("phonetic", ""),
            "emoji": item.get("emoji", "✨")
        }]

    def translate_all_languages(self, text: str) -> Dict[str, Any]:
        """
        Translates the given Hindi query across all 9 languages simultaneously!
        Delightful for kids to compare.
        """
        results = {}
        for lang_id in self.languages:
            results[lang_id] = self.translate_single(text, lang_id)
        return {
            "source_text": text,
            "translations": results
        }

    def get_category_items(self, category_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns vocabulary items, optionally filtered by category."""
        if not category_id or category_id == "all":
            return self.vocabulary
        return [item for item in self.vocabulary if item.get("category") == category_id]

    def search_dictionary(self, query: str) -> List[Dict[str, Any]]:
        """Searches vocabulary in Hindi or any target language phonetic/script."""
        q = self._clean_text(query)
        if not q:
            return self.vocabulary[:12]

        results = []
        for item in self.vocabulary:
            if q in self._clean_text(item["hindi"]):
                results.append(item)
                continue
            # Search translations
            for lang_id, tr in item["translations"].items():
                if q in self._clean_text(tr.get("dev", "")) or q in tr.get("phonetic", "").lower():
                    results.append(item)
                    break
        return results

# Singleton instance
translator_service = BhashaSetuTranslator()
