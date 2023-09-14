from enum import StrEnum, IntEnum


class Strings(StrEnum):
    WRONG_OPTION = "Wrong option!\nEnter any key to continue"
    AGAIN_NO = "N"
    AGAIN_YES = "Y"
    AGAIN_QUESTION = f"Again? [{AGAIN_YES}/{AGAIN_NO}]"
    OPTION_NUMBER = "Enter option number:\n"
    # region Japanese
    JAPANESE_SEE_YOU_LATER = "行ってきます！"
    JAPANESE_CORRECT_ANSWER = "せいかい！"
    # endregion


class Numbers(IntEnum):
    MAX_NUMBER_OF_ANSWERS = 4
