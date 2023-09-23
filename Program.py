from Application import app_constans as appc
from Application.Hiragana.hiragana import Hiragana as h
from Application.Katakana.katakana import Katakana as k
from Application.app import App


def main():
    while True:
        App.show_menu()
        option = App.read_option()
        match option:
            case "1":
                App.clear_console()
                h.learn_syllabary()
            case "2":
                App.clear_console()
                k.learn_syllabary()
            case "3":
                print(appc.Strings.JAPANESE_SEE_YOU_LATER)
                return
            case _:
                App.notice_message(appc.Strings.WRONG_OPTION)


if __name__ == '__main__':
    main()
