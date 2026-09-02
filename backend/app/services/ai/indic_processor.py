"""
Lightweight Indic Text Processor for IndicTrans2 Normalization
Provides standard Indic script normalization, digit normalization,
and prefix token preparation without heavy external dependencies.
"""

import re
from typing import List

# Common Indic unicode replacements
INDIC_PUNCT_MAP = {
    "।": "।",
    "॥": "॥",
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
}


class IndicTextProcessor:
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
