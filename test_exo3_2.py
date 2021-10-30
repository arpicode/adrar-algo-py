import utils
from exo3_2 import print_product_sign

MSG_POSITIVE = 'Le produit est positif.'
MSG_NEGATIVE = 'Le produit est négatif.'
MSG_NOTHING = ''


def test_plus_by_plus_sould_be_positive() -> None:
    expectedOutput = MSG_POSITIVE
    print_product_sign(12, 2.6)
    assert utils.stdout_equals(expectedOutput)


def test_minus_by_minus_sould_be_positive() -> None:
    expectedOutput = MSG_POSITIVE
    print_product_sign(-20, -2.6)
    assert utils.stdout_equals(expectedOutput)


def test_plus_by_minus_sould_be_negative() -> None:
    expectedOutput = MSG_NEGATIVE
    print_product_sign(16.0, -2.6)
    assert utils.stdout_equals(expectedOutput)


def test_minus_by_plus_sould_be_negative() -> None:
    expectedOutput = MSG_NEGATIVE
    print_product_sign(-2.03, 0.1)
    assert utils.stdout_equals(expectedOutput)


def test_plus_by_zero_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_product_sign(0.9, 0)
    assert utils.stdout_equals(expectedOutput)


def test_zero_by_plus_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_product_sign(0, 2.3)
    assert utils.stdout_equals(expectedOutput)


def test_minus_by_zero_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_product_sign(-20, 0.0)
    assert utils.stdout_equals(expectedOutput)


def test_zero_by_minus_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_product_sign(0, -36.0)
    assert utils.stdout_equals(expectedOutput)


def test_zero_by_zero_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_product_sign(0, 0)
    assert utils.stdout_equals(expectedOutput)


def test_minus_zero_by_minus_zero_sould_be_nothing() -> None:
    expectedOutput = MSG_NOTHING
    print_product_sign(-0, -0.0)
    assert utils.stdout_equals(expectedOutput)
