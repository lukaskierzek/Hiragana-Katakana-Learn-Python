from Application import app_constans


def test_read_option():
    expected: str = "Enter option number:\n"
    actual: str = app_constans.Strings.OPTION_NUMBER
    assert expected == actual
