import utils
from exo3_1 import print_sign

MSG_POSITIVE = 'Le nombre est positif.'
MSG_NEGATIVE = 'Le nombre est négatif.'
MSG_NOTHING = ''


def test_positive_number_sould_be_positive() -> None:
    expectedOutput = MSG_POSITIVE
    print_sign(12)
    assert utils.stdout_equals(expectedOutput)


def test_negative_number_sould_be_negative() -> None:
    expectedOutput = MSG_NEGATIVE
    print_sign(-1.02)
    assert utils.stdout_equals(expectedOutput)


def test_zero_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_sign(0.0)
    assert utils.stdout_equals(expectedOutput)


def test_negative_zero_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_sign(-0.0)
    assert utils.stdout_equals(expectedOutput)
