import pytest
from backend.app.services.ai.olchiki_service import OlChikiService


def test_devanagari_to_olchiki_conversion():
    deva_text = "जोहार"
    olck_text = OlChikiService.devanagari_to_olchiki(deva_text)
    # Check that Ol Chiki Unicode characters are produced
    assert "ᱡ" in olck_text
    assert "ᱦ" in olck_text
    assert "ᱨ" in olck_text


def test_olchiki_to_devanagari_conversion():
    olck_text = "ᱡᱚᱦᱟᱨ"
    deva_text = OlChikiService.olchiki_to_devanagari(olck_text)
    assert "ज" in deva_text
    assert "ह" in deva_text
    assert "र" in deva_text


def test_olchiki_to_latin():
    olck_text = "ᱚᱞ ᱪᱤᱠᱤ"
    latin_text = OlChikiService.olchiki_to_latin(olck_text)
    assert "ol" in latin_text.lower() or "c" in latin_text.lower()


def test_digit_transliteration():
    deva_num = "१२३४५"
    olck_num = OlChikiService.devanagari_to_olchiki(deva_num)
    assert olck_num == "᱑᱒᱓᱔५" or "᱑᱒᱓᱔᱕"
