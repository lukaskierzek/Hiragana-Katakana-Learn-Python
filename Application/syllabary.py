from abc import ABC, abstractmethod


class Syllabary(ABC):

    @staticmethod
    @abstractmethod
    def syllabary_gojuuon_list() -> list[str]:
        pass

    @staticmethod
    @abstractmethod
    def random_syllable() -> str:
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
    def learn_syllabary() -> None:
        pass
