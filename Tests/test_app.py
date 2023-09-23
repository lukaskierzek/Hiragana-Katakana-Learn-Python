import Application.app_constans as appc


def test_read_option():
    expected: str = "Enter option number:\n"
    actual: str = appc.Strings.OPTION_NUMBER
    assert expected == actual
