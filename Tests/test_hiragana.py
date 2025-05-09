import pytest

from Application.HiraganaKatakana.hiraganakatakana import HiraganaKatakana as hk
from Application.Syllables.hiragana_syllables import HiraganaGojuuon as hg
from Application import app_constans


@pytest.fixture
def number_of_vowels_of_hiragana_gojuuon():
    vowels_of_hiragana_gojuuon: list[str] = [hg.A, hg.I, hg.U, hg.E, hg.O, hg.N]
    return len(vowels_of_hiragana_gojuuon)


@pytest.fixture
def number_of_hiragana_gojuuon():
    return len(hg)


@pytest.fixture
def hiragana_syllabary_gojuuon_list():
    return hk.syllabary_gojuuon_list(app_constans.Syllabaries.HIRAGANA_SYLLABARY)


@pytest.mark.parametrize(
    "expected_hiragana_syllable, actual_hiragana_syllable",
    [
        # region syllables vowels
        ("あ", hg.A),
        ("い", hg.I),
        ("う", hg.U),
        ("え", hg.E),
        ("お", hg.O),
        ("ん", hg.N),
        # endregion
        # region constant K
        ("か", hg.KA),
        ("き", hg.KI),
        ("く", hg.KU),
        ("け", hg.KE),
        ("こ", hg.KO),
        # endregion
        # region constant S
        ("さ", hg.SA),
        ("し", hg.SHI),
        ("す", hg.SU),
        ("せ", hg.SE),
        ("そ", hg.SO),
        # endregion
        # region constant T
        ("た", hg.TA),
        ("ち", hg.CHI),
        ("つ", hg.TSU),
        ("て", hg.TE),
        ("と", hg.TO),
        # endregion
        # region constant N
        ("な", hg.NA),
        ("に", hg.NI),
        ("ぬ", hg.NU),
        ("ね", hg.NE),
        ("の", hg.NO),
        # endregion
        # region constant H
        ("は", hg.HA),
        ("ひ", hg.HI),
        ("ふ", hg.FU),
        ("へ", hg.HE),
        ("ほ", hg.HO),
        # endregion
        # region constant M
        ("ま", hg.MA),
        ("み", hg.MI),
        ("む", hg.MU),
        ("め", hg.ME),
        ("も", hg.MO),
        # endregion
        # region constant Y
        ("や", hg.YA),
        ("ゆ", hg.YU),
        ("よ", hg.YO),
        # endregion
        # region constant R
        ("ら", hg.RA),
        ("り", hg.RI),
        ("る", hg.RU),
        ("れ", hg.RE),
        ("ろ", hg.RO),
        # endregion
        # region constant W
        ("わ", hg.WA),
        ("ゐ", hg.WI),
        ("ゑ", hg.WE),
        ("を", hg.WO),
        # endregion
    ]
)
def test_hiragana_gojuuon(expected_hiragana_syllable: str, actual_hiragana_syllable: str):
    assert expected_hiragana_syllable == actual_hiragana_syllable


def test_number_of_hiragana_gojuuon_is_48(number_of_hiragana_gojuuon):
    expected_number_of_hiragana_gojuuon: int = 48
    actual_number_of_hiragana_gojuuon: int = number_of_hiragana_gojuuon
    assert expected_number_of_hiragana_gojuuon == actual_number_of_hiragana_gojuuon


def test_number_of_vowels_of_hiragana_gojuuon_is_6(number_of_vowels_of_hiragana_gojuuon):
    expected_number_of_vowels_of_hiragana_gojuuon: int = 6
    actual_number_of_vowels_of_hiragana_gojuuon: int = number_of_vowels_of_hiragana_gojuuon
    assert expected_number_of_vowels_of_hiragana_gojuuon == actual_number_of_vowels_of_hiragana_gojuuon


def test_number_of_contants_of_hiragana_gojuuon_is_42(number_of_hiragana_gojuuon, number_of_vowels_of_hiragana_gojuuon):
    expected_number_of_contants_of_hiragana_gojuuon: int = 42
    actual_number_of_contants_of_hiragana_gojuuon: int = number_of_hiragana_gojuuon - number_of_vowels_of_hiragana_gojuuon
    assert expected_number_of_contants_of_hiragana_gojuuon == actual_number_of_contants_of_hiragana_gojuuon


def test_hiragana_syllabary_gojuuon_list_contains_all_hiragana_gojuuon():
    expected_list: list[str] = list(map(str, hg))
    actual_list: list[str] = hk.syllabary_gojuuon_list(app_constans.Syllabaries.HIRAGANA_SYLLABARY)
    assert expected_list == actual_list


def test_get_not_the_same_syllable_from_syllable_list(hiragana_syllabary_gojuuon_list):
    syllable: str = hk.not_the_same_syllable_from_list(hiragana_syllabary_gojuuon_list)
    assert syllable not in hiragana_syllabary_gojuuon_list


def test_get_random_syllable_from_katkana_syllable_list_is_in_hiragana_syllable_list(hiragana_syllabary_gojuuon_list):
    syllable = hk.random_syllable(hiragana_syllabary_gojuuon_list)
    assert syllable in hiragana_syllabary_gojuuon_list
