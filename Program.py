from Application import app
from Application import app_constans as appc


def main():
    while True:
        app.show_menu()
        option = app.read_option()
        match option:
            case "1":
                app.clear_console()
            case "2":
                app.clear_console()
            case "3":
                print(appc.JAPANESE_SEE_YOU_LATER)
                return
            case _:
                app.notice_message(appc.WRONG_OPTION)


if __name__ == '__main__':
    main()
