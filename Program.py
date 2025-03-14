from Application import app_constans
from Application.HiraganaKatakana.hiraganakatakana import HiraganaKatakana
from Application.app import App


def main():
    while True:
        App.show_menu()
        option = App.read_option()
        match option:
            case "1":
                App.clear_console()
                HiraganaKatakana.learn_syllabary(app_constans.Syllabaries.HIRAGANA_SYLLABARY)
            case "2":
                App.clear_console()
                HiraganaKatakana.learn_syllabary(app_constans.Syllabaries.KATAKANA_SYLLABARY)
            case "3":
                print(app_constans.Strings.JAPANESE_SEE_YOU_LATER)
                return
            case _:
                App.notice_message(app_constans.Strings.WRONG_OPTION)


if __name__ == '__main__':
    main()
