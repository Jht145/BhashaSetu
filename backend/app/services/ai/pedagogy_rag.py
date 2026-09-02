"""
Vernacular Pedagogy Engine & Culturally Grounded Metaphor Generator
Transforms standard NCERT/JCERT textbook concepts into intuitive explanations
grounded in Jharkhand tribal folklore, festivals, and local nature.
"""

from typing import Dict, Any
from backend.app.services.ai.nmt_service import NMTService
from backend.app.services.ai.olchiki_service import OlChikiService

CULTURAL_METAPHORS = {
    "plants_trees": "जैसे सरहुल (Sarhul) में हम साल (सखुआ) के फूलों की पूजा कर प्रकृति का सम्मान करते हैं, वैसे ही हर पौधा और पेड़ हमें सांस लेने के लिए हवा और फल देता है।",
    "water_conservation": "हमारे गांव के दाड़ी-कुंआ और जाहेर थान के पास की नदियां जैसे हमें जीवन देती हैं, उसी तरह पानी की हर बूंद को बचाना हमारा कर्तव्य है।",
    "community_work": "जैसे करम (Karma) और सोहराय (Sohrai) में पूरा गांव एक साथ मिलकर मांदर की थाप पर काम और उत्सव करता है, वैसे ही मिलजुलकर रहने से समाज मजबूत बनता है।",
    "counting_math": "साल के पत्तों की पत्तल बनाते समय या करम की डालियों की पत्तियों को गिनकर आसानी से जोड़ और घटाव सीखा जा सकता है।",
    "animals_nature": "सोहराय पर्व में हम अपने बैलों और गायों को सजाते हैं क्योंकि वे हमारी खेती और जीवन के सबसे सच्चे साथी हैं।"
}


class PedagogyRAGEngine:
    @classmethod
    def simplify_concept(
        cls,
        concept_title: str,
        standard_text: str,
        target_language: str = "sat",
        target_script: str = "olck",
        pedagogy_keywords: str = ""
    ) -> Dict[str, Any]:
        """
        Generates simplified vernacular curriculum concept with tribal cultural grounding.
        """
        # Determine appropriate cultural metaphor based on keywords
        selected_metaphor = CULTURAL_METAPHORS["plants_trees"]
        kw_lower = (pedagogy_keywords + " " + concept_title + " " + standard_text).lower()

        if any(w in kw_lower for w in ["पानी", "जल", "नदी", "water", "rain", "बरसात"]):
            selected_metaphor = CULTURAL_METAPHORS["water_conservation"]
        elif any(w in kw_lower for w in ["गणित", "गिनती", "संख्या", "math", "count", "number"]):
            selected_metaphor = CULTURAL_METAPHORS["counting_math"]
        elif any(w in kw_lower for w in ["जानवर", "पशु", "गाय", "animal", "sohrai"]):
            selected_metaphor = CULTURAL_METAPHORS["animals_nature"]
        elif any(w in kw_lower for w in ["समाज", "गाँव", "त्योहार", "community", "festival"]):
            selected_metaphor = CULTURAL_METAPHORS["community_work"]

        # Formulate simplified foundational explanation
        simplified_hindi = f"{concept_title}: {standard_text[:120]}... {selected_metaphor}"
        
        # Translate to targeted vernacular
        translated_title, _, _, _ = NMTService.translate(
            concept_title, "hin", target_language, target_script
        )
        translated_explanation, _, _, _ = NMTService.translate(
            simplified_hindi, "hin", target_language, target_script
        )

        return {
            "simplified_title": translated_title,
            "simplified_explanation": translated_explanation,
            "cultural_metaphor": selected_metaphor,
            "language_code": target_language,
            "script_code": target_script,
            "quality_score": 4.8
        }
