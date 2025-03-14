from os import system, name

from Application import app_constans


class App:

    @staticmethod
    def read_option() -> str:
        return input(app_constans.Strings.OPTION_NUMBER)

    @staticmethod
    def show_menu() -> None:
        print("======= MENU =======")
        print("[ 1 ] Hiragana")
        print("[ 2 ] Katakana")
        print("[ 3 ] Exit")

    @staticmethod
    def clear_console() -> None:
        system('cls') if name == "nt" else system('clear')

    @staticmethod
    def notice_message(notice: str) -> None:
        print(notice)
        input()
        App.clear_console()

    @staticmethod
    def notice_good_answer():
        print(app_constans.Strings.JAPANESE_CORRECT_ANSWER)
        print(app_constans.Strings.AGAIN_QUESTION)
