from os import system, name


def read_option() -> str:
    return input("Enter option number:\n")


def show_menu() -> None:
    print(f"======MENU======")
    print("[1] Hiragana")
    print("[2] Katakana")
    print("[3] Exit")


def clear_console() -> None:
    system('cls') if name == "nt" else system('clear')


def notice_message(notice: str) -> None:
    print(notice)
    input()
    clear_console()
