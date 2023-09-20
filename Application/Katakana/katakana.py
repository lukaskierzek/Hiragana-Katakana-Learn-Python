from Application.syllabary import Syllabary
from Application.Katakana.katakana_syllables import Gojuuon as kg


class Katakana(Syllabary):

    @staticmethod
    def syllabary_gojuuon_list():
        return list(map(str, kg))
