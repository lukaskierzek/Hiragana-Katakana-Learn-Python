from abc import ABC, abstractmethod


class Syllabary(ABC):

    @staticmethod
    @abstractmethod
    def syllabary_gojuuon_list():
        pass
