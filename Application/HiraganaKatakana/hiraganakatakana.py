from random import choice

from Application import app_constans
from Application.Syllables.hiragana_syllables import HiraganaGojuuon as hg
from Application.Syllables.katakana_syllables import KatakanaGojuuon as kg
from Application.app import App
from Application.syllabary import Syllabary


class HiraganaKatakana(Syllabary):

    @staticmethod
    def header_with_answers(answer_list, syllable, syllabary) -> None:
        print(f"======= {syllable} =======")
        if syllabary == app_constans.Syllabaries.HIRAGANA_SYLLABARY:
            for syllable in answer_list:
                print(f"> {hg(syllable).name}")
        else:
            for syllable in answer_list:
                print(f"> {kg(syllable).name}")
        print(app_constans.Strings.ENTER_ANSWER)

    @staticmethod
    def random_syllable(syllable_list) -> str:
        return choice(syllable_list)

    @staticmethod
    def not_the_same_syllable_from_list(syllable_list):
        syllable = HiraganaKatakana.random_syllable(syllable_list)
        syllable_list.remove(syllable)
        return syllable

    @staticmethod
    def question_syllabary_gojuuon(answer_list,
                                   syllabary_gojuuon_list,
                                   syllable_correct_answer) -> None:
        for i in range(app_constans.Numbers.MAX_NUMBER_OF_ANSWERS):
            answer_list.append(HiraganaKatakana.not_the_same_syllable_from_list(syllabary_gojuuon_list))
        syllable_correct_answer.append(choice(answer_list))

    @staticmethod
    def syllabary_gojuuon_list(syllabary):
        if syllabary == app_constans.Syllabaries.HIRAGANA_SYLLABARY:
            return list(map(str, hg))
        else:
            return list(map(str, kg))

    @staticmethod
    def learn_syllabary(syllabary) -> None:
        return_to_menu: bool = False
        new_question: bool = False
        answer_list: list[str] = []
        syllabary_gojuuon_list: list[str] = HiraganaKatakana.syllabary_gojuuon_list(syllabary)
        syllable_correct_answer: list[str] = []

        HiraganaKatakana.question_syllabary_gojuuon(answer_list, syllabary_gojuuon_list, syllable_correct_answer)

        while True:
            if new_question:
                answer_list.clear()
                syllabary_gojuuon_list.clear()
                syllable_correct_answer.clear()
                syllabary_gojuuon_list = HiraganaKatakana.syllabary_gojuuon_list(syllabary)
                HiraganaKatakana.question_syllabary_gojuuon(answer_list, syllabary_gojuuon_list,
                                                            syllable_correct_answer)

            HiraganaKatakana.header_with_answers(answer_list, syllable_correct_answer[0], syllabary)
            option = input().upper()

            syllable_correct_answer_name = ''

            if syllabary == app_constans.Syllabaries.HIRAGANA_SYLLABARY:
                syllable_correct_answer_name = hg(syllable_correct_answer[0]).name
            else:
                syllable_correct_answer_name = kg(syllable_correct_answer[0]).name

            if option != syllable_correct_answer_name:
                App.notice_message(app_constans.Strings.ENTER_KEY_AGAIN)
                App.clear_console()
                new_question = False
            elif option == syllable_correct_answer_name:
                App.notice_good_answer()
                while True:
                    continue_option = input().upper()
                    if continue_option == app_constans.Strings.AGAIN_YES:
                        App.clear_console()
                        new_question = True
                        break
                    elif continue_option == app_constans.Strings.AGAIN_NO:
                        return_to_menu = True
                        break

            if return_to_menu:
                break

        App.notice_message(app_constans.Strings.ENTER_KEY_TO_RETURN_TO_MENU)
        App.clear_console()
