"""
Lightweight Indic Text Processor for IndicTrans2 Normalization,
English-to-Hindi Translation, and Hinglish / Romanized Hindi Transliteration.
"""

import re
from typing import List, Dict, Tuple, Optional

# Common Indic unicode replacements
INDIC_PUNCT_MAP = {
    "।": "।",
    "॥": "॥",
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
}

# High-frequency English to Hindi dictionary
ENGLISH_TO_HINDI: Dict[str, str] = {
    "hello": "नमस्ते",
    "hi": "नमस्ते",
    "namaste": "नमस्ते",
    "welcome": "स्वागत",
    "thanks": "धन्यवाद",
    "thank you": "धन्यवाद",
    "water": "पानी",
    "tree": "पेड़",
    "trees": "पेड़",
    "school": "स्कूल",
    "teacher": "शिक्षक",
    "student": "छात्र",
    "students": "छात्र",
    "book": "किताब",
    "books": "किताबें",
    "sun": "सूरज",
    "moon": "चाँद",
    "house": "घर",
    "home": "घर",
    "village": "गाँव",
    "forest": "जंगल",
    "jungle": "जंगल",
    "food": "खाना",
    "flower": "फूल",
    "flowers": "फूल",
    "bird": "पक्षी",
    "birds": "पक्षी",
    "animal": "जानवर",
    "animals": "जानवर",
    "plant": "पौधा",
    "plants": "पौधे",
    "nature": "प्रकृति",
    "math": "गणित",
    "maths": "गणित",
    "count": "गिनती",
    "counting": "गिनती",
    "add": "जोड़",
    "addition": "जोड़",
    "subtract": "घटाव",
    "friend": "दोस्त",
    "friends": "दोस्त",
    "mother": "माँ",
    "father": "पिता",
    "brother": "भाई",
    "sister": "बहन",
    "good morning": "शुभ प्रभात",
    "good evening": "शुभ संध्या",
    "good night": "शुभ रात्रि",
    "how are you": "तुम कैसे हो",
    "my name": "मेरा नाम",
    "my name is": "मेरा नाम",
    "what is your name": "तुम्हारा नाम क्या है",
    "earth": "धरती",
    "soil": "मिट्टी",
    "sky": "आसमान",
    "river": "नदी",
    "mountain": "पहाड़",
    "rain": "बारिश",
    "fire": "आग",
    "wind": "हवा",
    "boy": "लड़का",
    "girl": "लड़की",
    "child": "बच्चा",
    "children": "बच्चे",
    "good": "अच्छा",
    "bad": "बुरा",
    "big": "बड़ा",
    "small": "छोटा",
    "eat": "खाना",
    "drink": "पीना",
    "read": "पढ़ना",
    "write": "लिखना",
    "learn": "सीखना",
    "play": "खेलना",
    "sing": "गाना",
    "dance": "नाचना",
    "day": "दिन",
    "night": "रात",
    "today": "आज",
    "tomorrow": "कल",
    "yesterday": "कल",
    "is": "है",
    "are": "हैं",
    "am": "हूँ",
    "and": "और",
    "the": "",
    "a": "एक",
    "an": "एक",
}

# High-frequency Hinglish / Romanized Hindi word dictionary
HINGLISH_TO_HINDI: Dict[str, str] = {
    "namaste": "नमस्ते",
    "pranam": "प्रणाम",
    "johar": "जोहार",
    "dhanyawad": "धन्यवाद",
    "dhanyavad": "धन्यवाद",
    "shukriya": "धन्यवाद",
    "swagat": "स्वागत",
    "pani": "पानी",
    "paani": "पानी",
    "jal": "पानी",
    "ped": "पेड़",
    "per": "पेड़",
    "vriksh": "पेड़",
    "jungle": "जंगल",
    "ban": "जंगल",
    "van": "जंगल",
    "ghar": "घर",
    "gaon": "गाँव",
    "gaav": "गाँव",
    "kitab": "किताब",
    "pustak": "किताब",
    "school": "स्कूल",
    "shikshak": "शिक्षक",
    "guru": "शिक्षक",
    "master": "शिक्षक",
    "chhatra": "छात्र",
    "bachha": "बच्चा",
    "bachhe": "बच्चे",
    "sooraj": "सूरज",
    "suraj": "सूरज",
    "surya": "सूरज",
    "chand": "चाँद",
    "chanda": "चाँद",
    "pahar": "पहाड़",
    "parvat": "पहाड़",
    "khana": "खाना",
    "bhojan": "खाना",
    "phool": "फूल",
    "pushp": "फूल",
    "pakshi": "पक्षी",
    "chidiya": "पक्षी",
    "janwar": "जानवर",
    "pashu": "जानवर",
    "paudha": "पौधा",
    "podha": "पौधा",
    "ganit": "गणित",
    "ginti": "गिनती",
    "dost": "दोस्त",
    "mitra": "दोस्त",
    "yar": "दोस्त",
    "yaar": "दोस्त",
    "mata": "माँ",
    "maa": "माँ",
    "mummy": "माँ",
    "pita": "पिता",
    "baap": "पिता",
    "papa": "पिता",
    "bhai": "भाई",
    "behan": "बहन",
    "mera": "मेरा",
    "meri": "मेरी",
    "mere": "मेरे",
    "tera": "तेरा",
    "teri": "तेरी",
    "tere": "तेरे",
    "apna": "अपना",
    "apni": "अपनी",
    "naam": "नाम",
    "nam": "नाम",
    "kya": "क्या",
    "kyon": "क्यों",
    "kaise": "कैसे",
    "kaisi": "कैसी",
    "kaisa": "कैसा",
    "kaha": "कहाँ",
    "kahan": "कहाँ",
    "hai": "है",
    "hain": "हैं",
    "ho": "हो",
    "hu": "हूँ",
    "hoon": "हूँ",
    "tha": "था",
    "thi": "थी",
    "the": "थे",
    "hoga": "होगा",
    "hogi": "होगी",
    "tum": "तुम",
    "aap": "आप",
    "tu": "तू",
    "hum": "हम",
    "ham": "हम",
    "wo": "वह",
    "woh": "वह",
    "ye": "यह",
    "yeh": "यह",
    "achha": "अच्छा",
    "acha": "अच्छा",
    "theek": "ठीक",
    "badhiya": "बढ़िया",
    "bura": "बुरा",
    "bada": "बड़ा",
    "chhota": "छोटा",
    "chota": "छोटा",
    "aur": "और",
    "bhi": "भी",
    "to": "तो",
    "lekin": "लेकिन",
    "par": "पर",
    "me": "में",
    "mein": "में",
    "se": "से",
    "ko": "को",
    "ka": "का",
    "ke": "के",
    "ki": "की",
    "nahi": "नहीं",
    "nahin": "नहीं",
    "ha": "हाँ",
    "haan": "हाँ",
    "peena": "पीना",
    "padhna": "पढ़ना",
    "likhna": "लिखना",
    "dekhna": "देखना",
    "bolna": "बोलना",
    "sunna": "सुनना",
    "jana": "जाना",
    "aana": "आना",
    "karna": "करना",
    "raha": "रहा",
    "rahi": "रही",
    "rahe": "रहे",
    "dev": "देव",
    "rahul": "राहुल",
    "amit": "अमित",
    "gaandu": "गांडू",
    "gandu": "गांडू",
    "pagal": "पागल",
    "bhasha": "भाषा",
    "setu": "सेतु",
    "jharkhand": "झारखंड",
    "ranchi": "राँची",
}

# Phonetic Latin to Devanagari multi-char rules
LATIN_TO_DEVA_RULES = [
    ("shh", "ष्"), ("kh", "ख"), ("gh", "घ"), ("ch", "च"), ("chh", "छ"),
    ("jh", "झ"), ("th", "थ"), ("dh", "ध"), ("ph", "फ"), ("bh", "भ"),
    ("sh", "श"), ("gn", "ज्ञ"), ("gy", "ज्ञ"), ("tr", "त्र"), ("shr", "श्र"),
    ("aa", "ा"), ("ee", "ी"), ("oo", "ू"), ("ai", "ै"), ("au", "ौ"),
    ("a", "ा"), ("i", "ि"), ("u", "ु"), ("e", "े"), ("o", "ो"),
    ("k", "क"), ("g", "ग"), ("j", "ज"), ("t", "त"), ("d", "द"),
    ("n", "न"), ("p", "प"), ("b", "ब"), ("m", "म"), ("y", "य"),
    ("r", "र"), ("l", "ल"), ("v", "व"), ("w", "व"), ("s", "स"),
    ("h", "ह"), ("z", "ज़"), ("f", "फ़"),
]


class IndicTextProcessor:
    @staticmethod
    def is_latin_text(text: str) -> bool:
        """Checks if input text contains Latin/ASCII alphabetical characters."""
        return bool(re.search(r'[a-zA-Z]', text))

    @staticmethod
    def transliterate_latin_word_to_devanagari(word: str) -> str:
        """Phonetically transliterates an unknown Latin/Hinglish word to Devanagari."""
        w = word.lower().strip()
        if not w:
            return ""
        if w in HINGLISH_TO_HINDI:
            return HINGLISH_TO_HINDI[w]
        if w in ENGLISH_TO_HINDI:
            return ENGLISH_TO_HINDI[w]

        # Syllable transducer
        res = ""
        i = 0
        n = len(w)
        while i < n:
            matched = False
            for pat, repl in LATIN_TO_DEVA_RULES:
                if w.startswith(pat, i):
                    res += repl
                    i += len(pat)
                    matched = True
                    break
            if not matched:
                res += w[i]
                i += 1

        # Fix leading vowel signs to independent vowels
        vowel_map = {
            "ा": "आ", "ि": "इ", "ी": "ई", "ु": "उ", "ू": "ऊ",
            "े": "ए", "ै": "ऐ", "ो": "ओ", "ौ": "औ"
        }
        if res and res[0] in vowel_map:
            res = vowel_map[res[0]] + res[1:]

        return res

    @classmethod
    def convert_english_or_hinglish_to_hindi(cls, text: str) -> str:
        """
        Translates or transliterates English/Hinglish text to standard Devanagari Hindi.
        Example: 'dev gaandu hai' -> 'देव गांडू है'
        Example: 'water and tree' -> 'पानी और पेड़'
        Example: 'hello my friend' -> 'नमस्ते मेरा दोस्त'
        """
        if not cls.is_latin_text(text):
            return text.strip()

        clean_lower = text.strip().lower()
        # 1. Exact phrase check in English or Hinglish dictionary
        if clean_lower in ENGLISH_TO_HINDI:
            return ENGLISH_TO_HINDI[clean_lower]
        if clean_lower in HINGLISH_TO_HINDI:
            return HINGLISH_TO_HINDI[clean_lower]

        # 2. Token-by-token transformation
        tokens = re.findall(r'[a-zA-Z0-9\u0900-\u097F]+|[^\w\s]', text, re.UNICODE)
        translated_tokens = []

        for tok in tokens:
            if not tok.strip():
                continue
            tok_lower = tok.lower()
            if tok_lower in ENGLISH_TO_HINDI and ENGLISH_TO_HINDI[tok_lower]:
                translated_tokens.append(ENGLISH_TO_HINDI[tok_lower])
            elif tok_lower in HINGLISH_TO_HINDI:
                translated_tokens.append(HINGLISH_TO_HINDI[tok_lower])
            elif re.match(r'^[a-zA-Z]+$', tok):
                # Out-of-vocabulary phonetic conversion
                translated_tokens.append(cls.transliterate_latin_word_to_devanagari(tok_lower))
            else:
                translated_tokens.append(tok)

        result = " ".join(translated_tokens)
        return re.sub(r'\s+([,।\.!?;:॥᱾᱿])', r'\1', result)

    @staticmethod
    def normalize_text(text: str, lang_tag: str = "hin_Deva") -> str:
        """Normalizes whitespaces, non-standard unicode spaces, and punctuation."""
        if not text:
            return ""
        
        # Replace zero-width chars and special spaces
        cleaned = text.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
        cleaned = re.sub(r'[\r\n\t]+', ' ', cleaned)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()

        for k, v in INDIC_PUNCT_MAP.items():
            cleaned = cleaned.replace(k, v)

        return cleaned

    @staticmethod
    def format_input_for_indictrans2(text: str, src_tag: str, tgt_tag: str) -> str:
        """
        Formats normalized text with IndicTrans2 source and target prefix tags.
        Example: '__hin_Deva__ __sat_Olck__ नमस्ते'
        """
        clean_text = IndicTextProcessor.normalize_text(text, src_tag)
        return f"__{src_tag}__ __{tgt_tag}__ {clean_text}"

    @staticmethod
    def postprocess_output(raw_output: str, tgt_tag: str) -> str:
        """Cleans special tokens and artifacts from CTranslate2 generation."""
        if not raw_output:
            return ""
        
        # Strip any language tag remnants
        cleaned = re.sub(r'__\w+_\w+__', '', raw_output)
        cleaned = re.sub(r'<unk>', '', cleaned)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        # Format spacing before punctuation
        cleaned = re.sub(r'\s+([,।\.!?;:॥᱾᱿])', r'\1', cleaned)
        return cleaned
