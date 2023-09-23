from random import choice

import Application.app_constans as appc
from Application.Hiragana.hiragana_syllables import HiraganaGojuuon as hg
from Application.app import App
from Application.syllabary import Syllabary


class Hiragana(Syllabary):

    @staticmethod
    def header_with_answers(answer_list, syllable) -> None:
        print(f"======= {syllable} =======")
        for syllable in answer_list:
            print(f"> {hg(syllable).name}")
        print(appc.Strings.ENTER_ANSWER)

    @staticmethod
    def random_syllable(syllable_list) -> str:
        return choice(syllable_list)

    @staticmethod
    def not_the_same_syllable_from_list(syllable_list):
        syllable = Hiragana.random_syllable(syllable_list)
        syllable_list.remove(syllable)
        return syllable

    @staticmethod
    def question_syllabary_gojuuon(answer_list,
                                   syllabary_gojuuon_list,
                                   syllable_correct_answer) -> None:
        for i in range(appc.Numbers.MAX_NUMBER_OF_ANSWERS):
            answer_list.append(Hiragana.not_the_same_syllable_from_list(syllabary_gojuuon_list))
        syllable_correct_answer.append(choice(answer_list))

    @staticmethod
    def syllabary_gojuuon_list():
        return list(map(str, hg))

    @staticmethod
    def learn_syllabary() -> None:
        return_to_menu: bool = False
        new_question: bool = False
        answer_list: list[str] = []
        syllabary_gojuuon_list = Hiragana.syllabary_gojuuon_list()
        syllable_correct_answer = []

        Hiragana.question_syllabary_gojuuon(answer_list, syllabary_gojuuon_list, syllable_correct_answer)

        while True:
            if new_question:
                answer_list.clear()
                syllabary_gojuuon_list.clear()
                syllable_correct_answer.clear()
                syllabary_gojuuon_list = Hiragana.syllabary_gojuuon_list()
                Hiragana.question_syllabary_gojuuon(answer_list, syllabary_gojuuon_list, syllable_correct_answer)

            Hiragana.header_with_answers(answer_list, syllable_correct_answer[0])
            option = input().upper()
            syllable_correct_answer_name = hg(syllable_correct_answer[0]).name

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
