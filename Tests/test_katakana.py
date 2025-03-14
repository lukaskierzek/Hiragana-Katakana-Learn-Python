import pytest

from Application.HiraganaKatakana.hiraganakatakana import HiraganaKatakana as hk
from Application.Syllables.katakana_syllables import KatakanaGojuuon as kg
from Application import app_constans


@pytest.fixture
def number_of_vowels_of_katakana_gojuuon():
    vowels_of_katakana_gojuuon: list[str] = [kg.A, kg.I, kg.U, kg.E, kg.O, kg.N]
    return len(vowels_of_katakana_gojuuon)


@pytest.fixture
def number_of_katakana_gojuuon():
    return len(kg)


@pytest.fixture
def katakana_syllabary_gojuuon_list():
    return hk.syllabary_gojuuon_list(app_constans.Syllabaries.KATAKANA_SYLLABARY)


@pytest.mark.parametrize(
    "excepted_katakana_syllable, actual_katakana_syllable",
    [
        # region syllables vowels
        ("ア", kg.A),
        ("イ", kg.I),
        ("ウ", kg.U),
        ("エ", kg.E),
        ("オ", kg.O),
        ("ン", kg.N),
        # endregion
        # region constant K
        ("カ", kg.KA),
        ("キ", kg.KI),
        ("ク", kg.KU),
        ("ケ", kg.KE),
        ("コ", kg.KO),
        # endregion
        # region constant S
        ("サ", kg.SA),
        ("シ", kg.SHI),
        ("ス", kg.SU),
        ("セ", kg.SE),
        ("ソ", kg.SO),
        # endregion
        # region constant T
        ("タ", kg.TA),
        ("チ", kg.CHI),
        ("ツ", kg.TSU),
        ("テ", kg.TE),
        ("ト", kg.TO),
        # endregion
        # region constant N
        ("ナ", kg.NA),
        ("ニ", kg.NI),
        ("ヌ", kg.NU),
        ("ネ", kg.NE),
        ("ノ", kg.NO),
        # endregion
        # region constant H
        ("ハ", kg.HA),
        ("ヒ", kg.HI),
        ("フ", kg.FU),
        ("ヘ", kg.HE),
        ("ホ", kg.HO),
        # endregion
        # region constant M
        ("マ", kg.MA),
        ("ミ", kg.MI),
        ("ム", kg.MU),
        ("メ", kg.ME),
        ("モ", kg.MO),
        # endregion
        # region constant Y
        ("ヤ", kg.YA),
        ("ユ", kg.YU),
        ("ヨ", kg.YO),
        # endregion
        # region constant R
        ("ラ", kg.RA),
        ("リ", kg.RI),
        ("ル", kg.RU),
        ("レ", kg.RE),
        ("ロ", kg.RO),
        # endregion
        # region constant W
        ("ワ", kg.WA),
        ("ヰ", kg.WI),
        ("ヱ", kg.WE),
        ("ヲ", kg.WO),
        # endregion
    ]
)
def test_katakana_gojuuon(excepted_katakana_syllable: str, actual_katakana_syllable: str):
    assert excepted_katakana_syllable == actual_katakana_syllable


def test_number_of_katakana_gojuuon_is_48(number_of_katakana_gojuuon):
    expected_number_of_katakana_gojuuon: int = 48
    actual_number_of_katakana_gojuuon: int = number_of_katakana_gojuuon
    assert expected_number_of_katakana_gojuuon == actual_number_of_katakana_gojuuon


def test_number_of_vowels_of_katakana_gojuuon_is_6(number_of_vowels_of_katakana_gojuuon):
    expected_number_of_vowels_of_katakana_gojuuon: int = 6
    actual_number_of_vowels_of_katakana_gojuuon: int = number_of_vowels_of_katakana_gojuuon
    assert expected_number_of_vowels_of_katakana_gojuuon == actual_number_of_vowels_of_katakana_gojuuon


def test_number_of_contants_of_katakana_gojuuon_is_42(number_of_katakana_gojuuon, number_of_vowels_of_katakana_gojuuon):
    expected_number_of_contants_of_katakana_gojuuon: int = 42
    actual_number_of_contants_of_katakana_gojuuon: int = number_of_katakana_gojuuon - number_of_vowels_of_katakana_gojuuon
    assert expected_number_of_contants_of_katakana_gojuuon == actual_number_of_contants_of_katakana_gojuuon


def test_katakana_syllabary_gojuuon_list_contains_all_katakana_gojuuon(katakana_syllabary_gojuuon_list):
    expected_list: list[str] = list(map(str, kg))
    actual_list: list[str] = katakana_syllabary_gojuuon_list
    assert expected_list == actual_list


def test_get_not_the_same_syllable_from_syllable_list(katakana_syllabary_gojuuon_list):
    syllable: str = hk.not_the_same_syllable_from_list(katakana_syllabary_gojuuon_list)
    assert syllable not in katakana_syllabary_gojuuon_list


def test_get_random_syllable_from_katkana_syllable_list_is_in_katakana_syllable_list(katakana_syllabary_gojuuon_list):
    syllable: str = hk.random_syllable(katakana_syllabary_gojuuon_list)
    assert syllable in katakana_syllabary_gojuuon_list
