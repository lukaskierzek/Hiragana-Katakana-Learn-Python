from abc import ABC, abstractmethod
from Application.app_constans import Syllabaries

class Syllabary(ABC):

    @staticmethod
    @abstractmethod
    def syllabary_gojuuon_list(syllabary: Syllabaries) -> list[str]:
        pass

    @staticmethod
    @abstractmethod
    def random_syllable(syllable_list: list[str]) -> str:
        pass

    @staticmethod
    @abstractmethod
    def not_the_same_syllable_from_list(syllable_list: list[str]) -> str:
        pass

    @staticmethod
    @abstractmethod
    def question_syllabary_gojuuon(answer_list: list[str],
                                   syllabary_gojuuon_list: list[str],
                                   syllable_correct_answer: list[str]) -> None:
        pass

    @staticmethod
    @abstractmethod
    def header_with_answers(answer_list: list[str], syllable: str, syllabary: Syllabaries) -> None:
        pass

    @staticmethod
    @abstractmethod
    def learn_syllabary(syllabary: Syllabaries) -> None:
        pass
