"""
Unit tests for BhashaSetu Translation Engine & API
"""

import unittest
from backend.services.translator import translator_service
from backend.data.languages import LANGUAGES
from backend.data.dictionary import VOCABULARY, CATEGORIES

class TestBhashaSetu(unittest.TestCase):
    def test_languages_count(self):
        # 5 tribal + 4 regional = 9 languages
        self.assertEqual(len(LANGUAGES), 9)
        tribal = [l for l in LANGUAGES.values() if l["type"] == "tribal"]
        regional = [l for l in LANGUAGES.values() if l["type"] == "regional"]
        self.assertEqual(len(tribal), 5)
        self.assertEqual(len(regional), 4)

    def test_vocabulary_completeness(self):
        self.assertGreater(len(VOCABULARY), 20)
        self.assertGreater(len(CATEGORIES), 10)

        # Check each vocabulary item has translations for all 9 languages
        for item in VOCABULARY:
            self.assertIn("hindi", item)
            self.assertIn("category", item)
            self.assertIn("translations", item)
            for lang_id in LANGUAGES.keys():
                self.assertIn(lang_id, item["translations"], f"Missing {lang_id} in {item['hindi']}")

    def test_santhali_translation(self):
        res = translator_service.translate_single("नमस्ते", "santhali")
        self.assertTrue(res["success"])
        self.assertEqual(res["target_lang"], "santhali")
        self.assertIn("जोहार", res["devanagari"])
        self.assertIn("ᱡᱚᱦᱟᱨ", res["native_script"])

    def test_mundari_translation(self):
        res = translator_service.translate_single("हाथी", "mundari")
        self.assertTrue(res["success"])
        self.assertIn("हाती", res["devanagari"])

    def test_nagpuri_translation(self):
        res = translator_service.translate_single("माँ", "nagpuri")
        self.assertTrue(res["success"])
        self.assertIn("माय", res["devanagari"])

    def test_all_languages_translation(self):
        res = translator_service.translate_all_languages("पानी")
        self.assertEqual(len(res["translations"]), 9)
        for lang_id in LANGUAGES.keys():
            self.assertIn(lang_id, res["translations"])
            self.assertTrue(res["translations"][lang_id]["success"])

    def test_search(self):
        results = translator_service.search_dictionary("सूरज")
        self.assertGreater(len(results), 0)

if __name__ == "__main__":
    unittest.main()
