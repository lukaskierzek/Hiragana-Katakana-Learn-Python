from Application.syllabary import Syllabary
from Application.Hiragana.hiragana_syllables import Gojuuon as hg


class Hiragana(Syllabary):

    @staticmethod
    def syllabary_gojuuon_list():
        return list(map(str, hg))
