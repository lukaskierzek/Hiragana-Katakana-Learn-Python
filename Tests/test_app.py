from random import choice

from Application.Hiragana.hiragana import Hiragana as h
from Application.Katakana.katakana import Katakana as k


def test_get_random_syllable_from_katakana_gojuuon_list():
    katakana_gojuuon_list = k.syllabary_gojuuon_list()
    random_katakana_syllable = k.random_syllable()
    assert random_katakana_syllable in katakana_gojuuon_list


def test_get_random_syllable_from_hiragana_gojuuon_list():
    hiragana_gojuuon_list = h.syllabary_gojuuon_list()
    random_katakana_syllable = choice(hiragana_gojuuon_list)
    assert random_katakana_syllable in hiragana_gojuuon_list
