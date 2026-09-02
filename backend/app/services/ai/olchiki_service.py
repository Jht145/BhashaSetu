"""
Ol Chiki (ᱚᱞ ᱪᱤᱠᱤ) Script Engine
Provides bi-directional transliteration between Ol Chiki (Unicode U+1C50 - U+1C7F),
Devanagari, and Latin (Roman) scripts for Santhali.
"""

import re
from typing import Dict

# Direct character map from Latin/Devanagari to Ol Chiki
LATIN_TO_OLCHIKI: Dict[str, str] = {
    # Vowels
    "a": "ᱚ", "la": "ᱚ",
    "aa": "ᱟ", "ā": "ᱟ", "laa": "ᱟ",
    "i": "ᱤ", "li": "ᱤ",
    "u": "ᱩ", "lu": "ᱩ",
    "e": "ᱮ", "le": "ᱮ",
    "o": "ᱳ", "lo": "ᱳ",
    
    # Consonants
    "t": "ᱛ", "at": "ᱛ",
    "g": "ᱜ", "ag": "ᱜ",
    "ng": "ᱝ", "ang": "ᱝ",
    "l": "ᱞ", "al": "ᱞ",
    "k": "ᱠ", "aak": "ᱠ",
    "j": "ᱡ", "aaj": "ᱡ",
    "m": "ᱢ", "aam": "ᱢ",
    "w": "ᱣ", "aaw": "ᱣ",
    "s": "ᱥ", "is": "ᱥ",
    "h": "ᱦ", "ih": "ᱦ",
    "ny": "ᱧ", "iny": "ᱧ",
    "r": "ᱨ", "ir": "ᱨ",
    "ch": "ᱪ", "c": "ᱪ", "uch": "ᱪ",
    "d": "ᱫ", "ud": "ᱫ",
    "nn": "ᱬ", "unn": "ᱬ",
    "y": "ᱭ", "uy": "ᱭ",
    "p": "ᱯ", "ep": "ᱯ",
    "dd": "ᱰ", "ḍ": "ᱰ", "edd": "ᱰ",
    "n": "ᱱ", "en": "ᱱ",
    "rr": "ᱲ", "ṛ": "ᱲ", "err": "ᱲ",
    "tt": "ᱴ", "ṭ": "ᱴ", "ott": "ᱴ",
    "b": "ᱵ", "ob": "ᱵ",
    "v": "ᱶ", "ov": "ᱶ",
    "oh": "ᱷ",
    
    # Modifiers & Punctuations
    ".": "᱾",
    "..": "᱿",
    "|": "᱾",
    "||": "᱿",
}

# Digits
DIGIT_TO_OLCHIKI = {
    "0": "᱐", "1": "᱑", "2": "᱒", "3": "᱓", "4": "᱔",
    "5": "᱕", "6": "᱖", "7": "᱗", "8": "᱘", "9": "᱙"
}

OLCHIKI_TO_DIGIT = {v: k for k, v in DIGIT_TO_OLCHIKI.items()}

# Devanagari to Ol Chiki basic mapping table
DEVA_TO_OLCHIKI: Dict[str, str] = {
    "अ": "ᱚ", "आ": "ᱟ", "इ": "ᱤ", "ई": "ᱤ", "उ": "ᱩ", "ऊ": "ᱩ", "ए": "ᱮ", "ऐ": "ᱮ", "ओ": "ᱳ", "औ": "ᱳ",
    "ा": "ᱟ", "ि": "ᱤ", "ी": "ᱤ", "ु": "ᱩ", "ू": "ᱩ", "े": "ᱮ", "ै": "ᱮ", "ो": "ᱳ", "ौ": "ᱳ",
    "क": "ᱠ", "ख": "ᱠᱷ", "ग": "ᱜ", "घ": "ᱜᱷ", "ङ": "ᱝ",
    "च": "ᱪ", "छ": "ᱪᱷ", "ज": "ᱡ", "झ": "ᱡᱷ", "ञ": "ᱧ",
    "ट": "ᱴ", "ठ": "ᱴᱷ", "ड": "ᱰ", "ढ": "ᱰᱷ", "ण": "ᱬ",
    "त": "ᱛ", "थ": "ᱛᱷ", "द": "ᱫ", "ध": "ᱫᱷ", "न": "ᱱ",
    "प": "ᱯ", "फ": "ᱯᱷ", "ब": "ᱵ", "भ": "ᱵᱷ", "म": "ᱢ",
    "य": "ᱭ", "र": "ᱨ", "ल": "ᱞ", "व": "ᱣ", "श": "ᱥ", "ष": "ᱥ", "स": "ᱥ", "ह": "ᱦ",
    "ड़": "ᱲ", "ढ़": "ᱲᱷ",
    "ं": "ᱸ", "्": "", "।": "᱾", "॥": "᱿",
    "०": "᱐", "१": "᱑", "२": "᱒", "३": "᱓", "४": "᱔",
    "५": "᱕", "६": "᱖", "७": "᱗", "८": "᱘", "९": "᱙"
}

# Inverted mapping for Ol Chiki -> Devanagari
OLCHIKI_TO_DEVA: Dict[str, str] = {
    "᱐": "0", "᱑": "1", "᱒": "2", "᱓": "3", "᱔": "4",
    "᱕": "5", "᱖": "6", "᱗": "7", "༨": "8", "᱙": "9",
    "ᱚ": "अ", "ᱛ": "त", "ᱜ": "ग", "ᱝ": "ं", "ᱞ": "ल",
    "ᱟ": "आ", "ᱠ": "क", "ᱡ": "ज", "ᱢ": "म", "ᱣ": "व",
    "ᱤ": "इ", "ᱥ": "स", "ᱦ": "ह", "ᱧ": "ञ", "ᱨ": "र",
    "ᱩ": "उ", "ᱪ": "च", "ᱫ": "द", "ᱬ": "ण", "ᱭ": "य",
    "ᱮ": "ए", "ᱯ": "प", "ᱰ": "ड", "ᱱ": "न", "ᱲ": "ड़",
    "ᱳ": "ओ", "ᱴ": "ट", "ᱵ": "ब", "ᱶ": "ंव", "ᱷ": "ह",
    "ᱸ": "ं", "ᱹ": "़", "ᱺ": "ँ", "ᱼ": "-", "᱾": "।", "᱿": "॥"
}

OLCHIKI_TO_LATIN: Dict[str, str] = {
    "᱐": "0", "᱑": "1", "᱒": "2", "₃": "3", "᱔": "4",
    "᱕": "5", "᱖": "6", "᱗": "7", "᱘": "8", "᱙": "9",
    "ᱚ": "o", "ᱛ": "t", "ᱜ": "g", "ᱝ": "ng", "ᱞ": "l",
    "ᱟ": "a", "ᱠ": "k", "ᱡ": "j", "ᱢ": "m", "ᱣ": "w",
    "ᱤ": "i", "ᱥ": "s", "ᱦ": "h", "ᱧ": "ny", "ᱨ": "r",
    "ᱩ": "u", "ᱪ": "c", "ᱫ": "d", "ᱬ": "n", "ᱭ": "y",
    "ᱮ": "e", "ᱯ": "p", "ᱰ": "d", "ᱱ": "n", "ᱲ": "r",
    "ᱳ": "o", "ᱴ": "t", "ᱵ": "b", "ᱶ": "w", "ᱷ": "h",
    "ᱸ": "n", "᱾": ".", "᱿": ".."
}


class OlChikiService:
    @staticmethod
    def devanagari_to_olchiki(text: str) -> str:
        """Converts Devanagari text into native Ol Chiki Unicode script."""
        result = []
        i = 0
        while i < len(text):
            char = text[i]
            # Check two-character aspirated consonants or ligatures
            if i + 1 < len(text):
                two_char = text[i:i+2]
                if two_char in DEVA_TO_OLCHIKI:
                    result.append(DEVA_TO_OLCHIKI[two_char])
                    i += 2
                    continue
            
            if char in DEVA_TO_OLCHIKI:
                result.append(DEVA_TO_OLCHIKI[char])
            elif char in DIGIT_TO_OLCHIKI:
                result.append(DIGIT_TO_OLCHIKI[char])
            else:
                result.append(char)
            i += 1
        return "".join(result)

    @staticmethod
    def olchiki_to_devanagari(text: str) -> str:
        """Converts Ol Chiki text into Devanagari script for non-tribal teacher assistance."""
        result = []
        for char in text:
            if char in OLCHIKI_TO_DEVA:
                result.append(OLCHIKI_TO_DEVA[char])
            else:
                result.append(char)
        return "".join(result)

    @staticmethod
    def olchiki_to_latin(text: str) -> str:
        """Converts Ol Chiki to standard romanized phonetics."""
        result = []
        for char in text:
            if char in OLCHIKI_TO_LATIN:
                result.append(OLCHIKI_TO_LATIN[char])
            else:
                result.append(char)
        return "".join(result)

    @staticmethod
    def transliterate(text: str, source_script: str, target_script: str) -> str:
        """General transliteration router between olck, deva, and latn."""
        source = source_script.lower()
        target = target_script.lower()

        if source == target:
            return text

        if source == "deva" and target == "olck":
            return OlChikiService.devanagari_to_olchiki(text)
        elif source == "olck" and target == "deva":
            return OlChikiService.olchiki_to_devanagari(text)
        elif source == "olck" and target == "latn":
            return OlChikiService.olchiki_to_latin(text)
        elif source == "deva" and target == "latn":
            olchiki = OlChikiService.devanagari_to_olchiki(text)
            return OlChikiService.olchiki_to_latin(olchiki)
        
        return text
