import pytest
from Application.Hiragana.hiragana_syllables import Gojuuon as hg


@pytest.mark.parametrize(
    "excepted_syllable, actual_syllable",
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
        ("し", hg.SI),
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
def test_hiragana_gojuuon(excepted_syllable: str, actual_syllable: str):
    assert excepted_syllable == actual_syllable
