from random import choice

import Application.app_constans as appc
from Application.Katakana.katakana_syllables import Gojuuon as kg
from Application.app import App
from Application.syllabary import Syllabary


class Katakana(Syllabary):

    @staticmethod
    def not_the_same_syllable_from_list(syllable_list):
        syllable = Katakana.random_syllable()
        syllable_list.remove(syllable)
        return syllable

    @staticmethod
    def random_syllable() -> str:
        return choice(Katakana.syllabary_gojuuon_list())

    @staticmethod
    def syllabary_gojuuon_list():
        return list(map(str, kg))

    @staticmethod
    def question_syllabary_gojuuon(answer_list,
                                   syllabary_gojuuon_list,
                                   syllable_correct_answer):
        for i in range(appc.Numbers.MAX_NUMBER_OF_ANSWERS):
            answer_list.append(Katakana.not_the_same_syllable_from_list(syllabary_gojuuon_list))
        syllable_correct_answer.append(choice(answer_list))

    @staticmethod
    def learn_syllabary():
        return_to_menu: bool = False
        new_question: bool = False
        answer_list: list[str] = []
        syllabary_gojuuon_list = Katakana.syllabary_gojuuon_list()
        syllable_correct_answer = []

        Katakana.question_syllabary_gojuuon(answer_list, syllabary_gojuuon_list, syllable_correct_answer)

        while True:
            if new_question:
                answer_list.clear()
                syllabary_gojuuon_list.clear()
                syllable_correct_answer.clear()
                syllabary_gojuuon_list = Katakana.syllabary_gojuuon_list()
                Katakana.question_syllabary_gojuuon(answer_list, syllabary_gojuuon_list, syllable_correct_answer)

            App.header_with_answers(answer_list, syllable_correct_answer[0])
            option = input().upper()
            syllable_correct_answer_name = kg(syllable_correct_answer[0]).name

            if option != syllable_correct_answer_name:
                App.notice_message(appc.Strings.ENTER_KEY_AGAIN)
                App.clear_console()
                new_question = False
            elif option == syllable_correct_answer_name:
                App.notice_good_answer()
                while True:
                    continue_option = input().upper()
                    if continue_option == appc.Strings.AGAIN_YES:
                        App.clear_console()
                        new_question = True
                        break
                    elif continue_option == appc.Strings.AGAIN_NO:
                        return_to_menu = True
                        break

            if return_to_menu:
                break

        App.notice_message(appc.Strings.ENTER_KEY_TO_RETURN_TO_MENU)
        App.clear_console()
