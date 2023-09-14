from Application.app import App
from Application import app_constans as appc


def main():
    while True:
        App.show_menu()
        option = App.read_option()
        match option:
            case "1":
                App.clear_console()
            case "2":
                App.clear_console()
            case "3":
                print(appc.Strings.JAPANESE_SEE_YOU_LATER)
                return
            case _:
                App.notice_message(appc.Strings.WRONG_OPTION)


if __name__ == '__main__':
    main()
