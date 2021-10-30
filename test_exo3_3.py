import utils
from exo3_3 import print_sorted

MSG_SORTED = 'Ordre alphabétique.'
MSG_UNSORTED = 'Ordre non-alphabétique.'


def test_tata_titi_toto_sould_be_sorted() -> None:
    expectedOutput = MSG_SORTED
    print_sorted('tata', 'titi', 'toto')
    assert utils.stdout_equals(expectedOutput)


def test_tata_titi_titi_sould_be_sorted() -> None:
    expectedOutput = MSG_SORTED
    print_sorted('tata', 'titi', 'titi')
    assert utils.stdout_equals(expectedOutput)


def test_three_same_names_sould_be_sorted() -> None:
    expectedOutput = MSG_SORTED
    print_sorted('toto', 'toto', 'toto')
    assert utils.stdout_equals(expectedOutput)


def test_toto_titi_tata_sould_be_unsorted() -> None:
    expectedOutput = MSG_UNSORTED
    print_sorted('toto', 'titi', 'tata')
    assert utils.stdout_equals(expectedOutput)


def test_toto_titi_titi_sould_be_unsorted() -> None:
    expectedOutput = MSG_UNSORTED
    print_sorted('toto', 'titi', 'tata')
    assert utils.stdout_equals(expectedOutput)
