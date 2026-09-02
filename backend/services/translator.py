"""
Translation & Linguistic Engine for BhashaSetu
Handles Hindi / English / Hinglish -> 9 Indigenous & Regional Languages translation,
greedy phrase chunking, token-based matching, name transliteration, and multi-script transliteration.
"""

import re
from typing import Dict, List, Any, Optional, Tuple
from backend.data.languages import LANGUAGES
from backend.data.dictionary import VOCABULARY, CATEGORIES
from backend.data.scripts_data import devanagari_to_olchiki
from backend.app.services.ai.indic_processor import IndicTextProcessor, HINGLISH_TO_HINDI, ENGLISH_TO_HINDI


# Common sentence phrases and idioms mapped across all 9 languages
COMMON_PHRASES: List[Dict[str, Any]] = [
    {
        "patterns": ["hello", "hi", "namaste", "pranam", "johar", "नमस्ते", "प्रणाम", "जोहार"],
        "translations": {
            "santhali": {"native": "ᱡᱚᱦᱟᱨ", "dev": "जोहार", "phonetic": "Johar"},
            "mundari": {"native": "जोहार", "dev": "जोहार", "phonetic": "Johar"},
            "ho": {"native": "𑢪𑣉𑢦𑢬𑣂", "dev": "जोहार", "phonetic": "Johar"},
            "kurukh": {"native": "गोड़े", "dev": "गोड़े / जोहार", "phonetic": "Godey / Johar"},
            "kharia": {"native": "जोहार", "dev": "जोहार", "phonetic": "Johar"},
            "khortha": {"native": "प्रनाम", "dev": "प्रनाम / जोहार", "phonetic": "Pranam / Johar"},
            "nagpuri": {"native": "जोहार", "dev": "जोहार / पायलागी", "phonetic": "Johar / Paylagi"},
            "panchpargania": {"native": "जोहार", "dev": "जोहार / नमस्कार", "phonetic": "Johar / Namaskar"},
            "kurmali": {"native": "जोहार", "dev": "जोहार / पांय लागों", "phonetic": "Johar / Pay Lagon"},
        }
    },
    {
        "patterns": [
            "my name is", "my name", "mera naam hai", "mera naam", "mor naav", "mor nam",
            "मेरा नाम है", "मेरा नाम", "हमर नाम", "मोर नाम"
        ],
        "translations": {
            "santhali": {"native": "ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ ᱫᱚ", "dev": "इञाः ञुतुम दो", "phonetic": "Injań ñutum do"},
            "mundari": {"native": "आइं रेन नुतुम", "dev": "आइं रेन नुतुम", "phonetic": "Aing ren nutum"},
            "ho": {"native": "अंगा नुतुम", "dev": "अंगा नुतुम", "phonetic": "Anga nutum"},
            "kurukh": {"native": "एन नामे", "dev": "एन नामे", "phonetic": "En naame"},
            "kharia": {"native": "इंग नाम", "dev": "इंग नाम", "phonetic": "Ing nam"},
            "khortha": {"native": "हमर नाम", "dev": "हमर नाम", "phonetic": "Hamar naam"},
            "nagpuri": {"native": "मोर नाव", "dev": "मोर नाव", "phonetic": "Mor naav"},
            "panchpargania": {"native": "मोर नाम", "dev": "मोर नाम", "phonetic": "Mor nam"},
            "kurmali": {"native": "मोर नाम", "dev": "मोर नाम", "phonetic": "Mor nam"},
        }
    },
    {
        "patterns": [
            "what is your name", "aapka naam kya hai", "tumhara naam kya hai", "tora naam ki",
            "आपका नाम क्या है", "तुम्हारा नाम क्या है", "तोहर नाम का हे"
        ],
        "translations": {
            "santhali": {"native": "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ ᱫᱚ ᱪᱮᱫ?", "dev": "आमाः ञुतुम दो चेद?", "phonetic": "Amag ñutum do chet?"},
            "mundari": {"native": "अमाः नुतुम चिनाः?", "dev": "अमाः नुतुम चिनाः?", "phonetic": "Amah nutum chinah?"},
            "ho": {"native": "अमा नुतुम चिना?", "dev": "अमा नुतुम चिना?", "phonetic": "Ama nutum china?"},
            "kurukh": {"native": "निंघाई नामे इन्द्रा?", "dev": "निंघाई नामे इन्द्रा?", "phonetic": "Ninghai naame indra?"},
            "kharia": {"native": "अम नाम चिन?", "dev": "अम नाम चिन?", "phonetic": "Am nam chin?"},
            "khortha": {"native": "तोहर नाम का लागय?", "dev": "तोहर नाम का लागय?", "phonetic": "Tohar naam ka lagay?"},
            "nagpuri": {"native": "रउरे कर नाव का हेके?", "dev": "रउरे कर नाव का हेके?", "phonetic": "Raure kar naav ka heke?"},
            "panchpargania": {"native": "तोर नाम का?", "dev": "तोर नाम का?", "phonetic": "Tor nam ka?"},
            "kurmali": {"native": "तोर नाम का हेके?", "dev": "तोर नाम का हेके?", "phonetic": "Tor nam ka heke?"},
        }
    },
    {
        "patterns": [
            "how are you", "tum kaise ho", "aap kaise hain", "tu kaisa hai", "kese ho",
            "तुम कैसे हो", "आप कैसे हैं", "तू कैसा है", "केसे हो"
        ],
        "translations": {
            "santhali": {"native": "ᱪᱮᱫ ᱞᱮᱠᱟ ᱢᱮᱱᱟᱢᱟ?", "dev": "चेद लेका मेनामा?", "phonetic": "Chet leka menama?"},
            "mundari": {"native": "चिलका मेनामा?", "dev": "चिलका मेनामा?", "phonetic": "Chilka menama?"},
            "ho": {"native": "अम चेकना?", "dev": "अम चेकना?", "phonetic": "Am chekana?"},
            "kurukh": {"native": "नीन एकन तरा रअदाय?", "dev": "नीन एकन तरा रअदाय?", "phonetic": "Neen ekan tara raday?"},
            "kharia": {"native": "अम चेलके आत?", "dev": "अम चेलके आत?", "phonetic": "Am chelke aat?"},
            "khortha": {"native": "तोहे कैसन हा?", "dev": "तोहे कैसन हा?", "phonetic": "Tohe kaisan ha?"},
            "nagpuri": {"native": "रउरे कैसन हई?", "dev": "रउरे कैसन हई?", "phonetic": "Raure kaisan hayi?"},
            "panchpargania": {"native": "तुइ केमन आछिस?", "dev": "तुइ केमन आछिस?", "phonetic": "Tui kemon achis?"},
            "kurmali": {"native": "तुइ केमने आछिस?", "dev": "तुइ केमने आछिस?", "phonetic": "Tui kemne achis?"},
        }
    },
    {
        "patterns": ["thank you", "thanks", "dhanyawad", "dhanyavad", "shukriya", "धन्यवाद", "शुक्रिया", "बहुत धन्यवाद"],
        "translations": {
            "santhali": {"native": "ᱥᱟᱨᱦᱟᱣ", "dev": "सारहाव", "phonetic": "Sarhaw"},
            "mundari": {"native": "जोहार / धनबाद", "dev": "जोहार / धनबाद", "phonetic": "Johar / Dhanbad"},
            "ho": {"native": "जोहार", "dev": "जोहार", "phonetic": "Johar"},
            "kurukh": {"native": "धनबाद", "dev": "धनबाद", "phonetic": "Dhanbad"},
            "kharia": {"native": "जोहार", "dev": "जोहार", "phonetic": "Johar"},
            "khortha": {"native": "धनबाद", "dev": "धनबाद", "phonetic": "Dhanbad"},
            "nagpuri": {"native": "धनबाद", "dev": "धनबाद", "phonetic": "Dhanbad"},
            "panchpargania": {"native": "धन्यबाद", "dev": "धन्यबाद", "phonetic": "Dhanyabad"},
            "kurmali": {"native": "धन्यबाद", "dev": "धन्यबाद", "phonetic": "Dhanyabad"},
        }
    },
    {
        "patterns": ["water is life", "pani jeevan hai", "जल ही जीवन है", "पानी जीवन है"],
        "translations": {
            "santhali": {"native": "ᱫᱟᱜ ᱜᱮ ᱡᱤᱭᱚᱱ", "dev": "दाग गे जियोन", "phonetic": "Daak ge jiyon"},
            "mundari": {"native": "दाः गे जीवन", "dev": "दाः गे जीवन", "phonetic": "Dah ge jeevan"},
            "ho": {"native": "दाः गे जीवन", "dev": "दाः गे जीवन", "phonetic": "Dah ge jeevan"},
            "kurukh": {"native": "अम्म गे उज्जना", "dev": "अम्म गे उज्जना", "phonetic": "Amm ge ujjna"},
            "kharia": {"native": "दाअ गे जीवन", "dev": "दाअ गे जीवन", "phonetic": "Daa ge jeevan"},
            "khortha": {"native": "पानीए जीवन लागे", "dev": "पानीए जीवन लागे", "phonetic": "Paniye jeevan lage"},
            "nagpuri": {"native": "पानीए जिनगी हेके", "dev": "पानीए जिनगी हेके", "phonetic": "Paniye jingi heke"},
            "panchpargania": {"native": "जलटाए जीवन", "dev": "जलटाए जीवन", "phonetic": "Jaltae jeevan"},
            "kurmali": {"native": "पानीए जीवन हेके", "dev": "पानीए जीवन हेके", "phonetic": "Paniye jeevan heke"},
        }
    },
    {
        "patterns": ["good morning", "shubh prabhat", "सुप्रभात", "शुभ प्रभात"],
        "translations": {
            "santhali": {"native": "ᱥᱟᱹᱜᱩᱱ ᱥᱮᱛᱟᱜ", "dev": "सागुन सेताः", "phonetic": "Sagun setak"},
            "mundari": {"native": "बुगिन सेताः", "dev": "बुगिन सेताः", "phonetic": "Bugin setah"},
            "ho": {"native": "बुगि सेताः", "dev": "बुगि सेताः", "phonetic": "Bugi setah"},
            "kurukh": {"native": "दाव पैरी", "dev": "दाव पैरी", "phonetic": "Daw pairi"},
            "kharia": {"native": "बेसे बेड़ा", "dev": "बेसे बेड़ा", "phonetic": "Bese bera"},
            "khortha": {"native": "सुभ बिहान", "dev": "सुभ बिहान", "phonetic": "Subh bihan"},
            "nagpuri": {"native": "सुभ बिहान", "dev": "सुभ बिहान", "phonetic": "Subh bihan"},
            "panchpargania": {"native": "सुभ बिहान", "dev": "सुभ बिहान", "phonetic": "Subh bihan"},
            "kurmali": {"native": "सुभ बिहान", "dev": "सुभ बिहान", "phonetic": "Subh bihan"},
        }
    }
]


class BhashaSetuTranslator:
    def __init__(self):
        self.languages = LANGUAGES
        self.vocabulary = VOCABULARY
        self.categories = CATEGORIES
        self._build_indexes()

    def _clean_text(self, text: str) -> str:
        if not text:
            return ""
        text = text.strip()
        cleaned = re.sub(r'[\?\.!,।\n\r]+', ' ', text)
        return re.sub(r'\s+', ' ', cleaned).strip().lower()

    def _build_indexes(self):
        """Build phrase and token indices for high-precision lookups."""
        self.phrase_index = {}
        self.word_index = {}

        # 1. Index common phrases & idioms first
        for item in COMMON_PHRASES:
            for pat in item["patterns"]:
                clean_pat = self._clean_text(pat)
                if clean_pat:
                    self.phrase_index[clean_pat] = {
                        "hindi": pat,
                        "english": pat,
                        "translations": item["translations"],
                        "category": "conversation",
                        "emoji": "💬"
                    }

        # 2. Index dictionary vocabulary
        for item in self.vocabulary:
            hindi_raw = item.get("hindi", "")
            for var in re.split(r'[/,()]', hindi_raw):
                clean_var = self._clean_text(var)
                if clean_var:
                    if clean_var not in self.phrase_index:
                        self.phrase_index[clean_var] = item
                    for w in clean_var.split():
                        if len(w) > 1:
                            if w not in self.word_index:
                                self.word_index[w] = []
                            if item not in self.word_index[w]:
                                self.word_index[w].append(item)

            english_raw = item.get("english", "")
            for var in re.split(r'[/,()]', english_raw):
                clean_var = self._clean_text(var)
                if clean_var:
                    if clean_var not in self.phrase_index:
                        self.phrase_index[clean_var] = item
                    for w in clean_var.split():
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

    def _match_single_phrase_or_token(self, chunk: str, target_lang_id: str) -> Optional[Tuple[str, str, str]]:
        """
        Attempts to translate a single phrase chunk or token into (native, dev, phonetic).
        Returns None if not found in dictionary.
        """
        clean = self._clean_text(chunk)
        if not clean:
            return None

        # 1. Exact match in phrase index
        if clean in self.phrase_index:
            item = self.phrase_index[clean]
            tr = item["translations"].get(target_lang_id, {})
            d = tr.get("dev", chunk)
            n = tr.get("native", d)
            p = tr.get("phonetic", d)
            return (n, d, p)

        # 2. Normalized English/Hinglish phrase match
        if IndicTextProcessor.is_latin_text(chunk):
            hi_norm = IndicTextProcessor.convert_english_or_hinglish_to_hindi(chunk)
            clean_hi = self._clean_text(hi_norm)
            if clean_hi in self.phrase_index:
                item = self.phrase_index[clean_hi]
                tr = item["translations"].get(target_lang_id, {})
                d = tr.get("dev", hi_norm)
                n = tr.get("native", d)
                p = tr.get("phonetic", d)
                return (n, d, p)

        # 3. Single word dictionary lookup
        if clean in self.word_index and len(self.word_index[clean]) > 0:
            item = self.word_index[clean][0]
            tr = item["translations"].get(target_lang_id, {})
            d = tr.get("dev", chunk)
            n = tr.get("native", d)
            p = tr.get("phonetic", d)
            return (n, d, p)

        return None

    def translate_single(self, text: str, target_lang: str, source_lang: Optional[str] = "hin_Deva") -> Dict[str, Any]:
        """
        Translates Hindi, English, or Hinglish text query (words, phrases, sentences)
        to a specific target language with high precision greedy phrase segmentation.
        """
        target_lang_clean = target_lang.lower().strip()
        target_lang_id = self.CODE_MAP.get(target_lang_clean, target_lang_clean)
        if target_lang_id not in self.languages:
            target_lang_id = "santhali"

        clean_query = self._clean_text(text)
        lang_meta = self.languages[target_lang_id]
        is_latin = IndicTextProcessor.is_latin_text(text)

        # 1. Exact full-sentence match
        exact_match = self._match_single_phrase_or_token(text, target_lang_id)
        if exact_match:
            native_val, dev_val, phonetic_val = exact_match
            return {
                "success": True,
                "match_type": "exact",
                "source_text": text,
                "target_lang": target_lang_id,
                "target_lang_name": lang_meta["name_hi"],
                "emoji": "✨",
                "category": "general",
                "devanagari": dev_val,
                "native_script": native_val,
                "translated_text": native_val or dev_val,
                "phonetic": phonetic_val,
                "transliteration": phonetic_val,
                "script_name": lang_meta["primary_script"],
                "translation_method": "direct_dictionary",
                "quality_flags": [],
                "warnings": [],
                "words_breakdown": [{"original": text, "devanagari": dev_val, "native": native_val, "phonetic": phonetic_val, "emoji": "✨"}]
            }

        # 2. Greedy multi-word phrase segmentation for sentences (e.g. 'Hello My name is adarsh sharma')
        # Tokenize by words and punctuation
        tokens = re.findall(r'[a-zA-Z0-9\u0900-\u097F]+|[^\w\s]', text, re.UNICODE)
        translated_native = []
        translated_dev = []
        translated_phonetic = []
        breakdowns = []
        
        i = 0
        n = len(tokens)
        while i < n:
            tok = tokens[i]
            if re.match(r'^[^\w\s]$', tok):
                # Punctuation
                translated_native.append(tok)
                translated_dev.append(tok)
                translated_phonetic.append(tok)
                i += 1
                continue

            # Try multi-word window: 4 words -> 3 words -> 2 words -> 1 word
            matched_chunk = False
            for window in range(min(4, n - i), 1, -1):
                chunk_words = tokens[i:i + window]
                # Filter out pure punctuation chunks
                if any(re.match(r'^[^\w\s]$', w) for w in chunk_words):
                    continue
                chunk_str = " ".join(chunk_words)
                res = self._match_single_phrase_or_token(chunk_str, target_lang_id)
                if res:
                    n_val, d_val, p_val = res
                    translated_native.append(n_val)
                    translated_dev.append(d_val)
                    translated_phonetic.append(p_val)
                    breakdowns.append({
                        "original": chunk_str,
                        "devanagari": d_val,
                        "native": n_val,
                        "phonetic": p_val,
                        "emoji": "🔹"
                    })
                    i += window
                    matched_chunk = True
                    break

            if matched_chunk:
                continue

            # Single word lookup or transliteration
            res_single = self._match_single_phrase_or_token(tok, target_lang_id)
            if res_single:
                n_val, d_val, p_val = res_single
                translated_native.append(n_val)
                translated_dev.append(d_val)
                translated_phonetic.append(p_val)
                breakdowns.append({
                    "original": tok,
                    "devanagari": d_val,
                    "native": n_val,
                    "phonetic": p_val,
                    "emoji": "🔹"
                })
            else:
                # Name / Out-of-vocabulary transliteration
                tok_dev = IndicTextProcessor.convert_english_or_hinglish_to_hindi(tok) if is_latin else tok
                tok_native = devanagari_to_olchiki(tok_dev) if target_lang_id == "santhali" else tok_dev
                tok_phonetic = tok.capitalize() if is_latin else tok_dev

                translated_native.append(tok_native)
                translated_dev.append(tok_dev)
                translated_phonetic.append(tok_phonetic)
                breakdowns.append({
                    "original": tok,
                    "devanagari": tok_dev,
                    "native": tok_native,
                    "phonetic": tok_phonetic,
                    "emoji": "🔹"
                })

            i += 1

        # Join results cleanly
        native_result = re.sub(r'\s+([,।\.!?;:॥᱾᱿])', r'\1', " ".join(translated_native))
        dev_result = re.sub(r'\s+([,।\.!?;:॥᱾᱿])', r'\1', " ".join(translated_dev))
        phonetic_result = re.sub(r'\s+([,।\.!?;:॥᱾᱿])', r'\1', " ".join(translated_phonetic))

        return {
            "success": True,
            "match_type": "segmented_sentence",
            "source_text": text,
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
            "translation_method": "greedy_phrase_segmenter",
            "quality_flags": [],
            "warnings": [],
            "words_breakdown": breakdowns
        }

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
