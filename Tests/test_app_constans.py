import pytest
import Application.app_constans as appc


@pytest.mark.parametrize(
    "expected_string, actual_string",
    [
        ("Wrong option!\nEnter any key to continue", appc.Strings.WRONG_OPTION),
        ("N", appc.Strings.AGAIN_NO),
        ("Y", appc.Strings.AGAIN_YES),
        ("Again? [Y/N]", appc.Strings.AGAIN_QUESTION),
        ("Enter option number:\n", appc.Strings.OPTION_NUMBER),
    ]
)
def test_constans_string(expected_string: str, actual_string: str):
    assert expected_string == actual_string


@pytest.mark.parametrize(
    "expected_japanese_string, actual_japanese_string",
    [
        ("行ってきます！", appc.Strings.JAPANESE_SEE_YOU_LATER),
        ("せいかい！", appc.Strings.JAPANESE_CORRECT_ANSWER),
    ]
)
def test_constans_japanese_string(expected_japanese_string: str, actual_japanese_string: str):
    assert expected_japanese_string == actual_japanese_string


def test_maximum_number_of_answers():
    expected_maximum_number_of_answers: int = 4
    assert expected_maximum_number_of_answers == appc.Numbers.MAX_NUMBER_OF_ANSWERS
