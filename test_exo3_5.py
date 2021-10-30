import utils

from exo3_5 import print_age_group
from exo3_5 import print_age_group_alt1
from exo3_5 import print_age_group_alt2
from exo3_5 import print_age_group_alt3

AGE_GROUP_POUSSIN = 'Poussin'
AGE_GROUP_PUPILLE = 'Pupille'
AGE_GROUP_MINIME = 'Minime'
AGE_GROUP_CADET = 'Cadet'
AGE_GROUP_NOTHING = ''


def test_five_should_be_age_group_nothing() -> None:
    expectedOutput = AGE_GROUP_NOTHING
    print_age_group(5)
    assert utils.stdout_equals(expectedOutput)


def test_six_should_be_age_group_poussin() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group(6)
    assert utils.stdout_equals(expectedOutput)


def test_seven_should_be_age_group_poussin() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group(7)
    assert utils.stdout_equals(expectedOutput)


def test_eight_should_be_age_group_pupille() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group(8)
    assert utils.stdout_equals(expectedOutput)


def test_nine_should_be_age_group_pupille() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group(9)
    assert utils.stdout_equals(expectedOutput)


def test_ten_should_be_age_group_minime() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group(10)
    assert utils.stdout_equals(expectedOutput)


def test_eleven_should_be_age_group_minime() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group(11)
    assert utils.stdout_equals(expectedOutput)


def test_twelve_should_be_age_group_cadet() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group(12)
    assert utils.stdout_equals(expectedOutput)


def test_thirteen_should_be_age_group_cadet() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group(13)
    assert utils.stdout_equals(expectedOutput)


# alt 1


def test_five_should_be_age_group_nothing_alt1() -> None:
    expectedOutput = AGE_GROUP_NOTHING
    print_age_group_alt1(5)
    assert utils.stdout_equals(expectedOutput)


def test_six_should_be_age_group_poussin_alt1() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group_alt1(6)
    assert utils.stdout_equals(expectedOutput)


def test_seven_should_be_age_group_poussin_alt1() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group_alt1(7)
    assert utils.stdout_equals(expectedOutput)


def test_eight_should_be_age_group_pupille_alt1() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group_alt1(8)
    assert utils.stdout_equals(expectedOutput)


def test_nine_should_be_age_group_pupille_alt1() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group_alt1(9)
    assert utils.stdout_equals(expectedOutput)


def test_ten_should_be_age_group_minime_alt1() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group_alt1(10)
    assert utils.stdout_equals(expectedOutput)


def test_eleven_should_be_age_group_minime_alt1() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group_alt1(11)
    assert utils.stdout_equals(expectedOutput)


def test_twelve_should_be_age_group_cadet_alt1() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group_alt1(12)
    assert utils.stdout_equals(expectedOutput)


def test_thirteen_should_be_age_group_cadet_alt1() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group_alt1(13)
    assert utils.stdout_equals(expectedOutput)


# alt 2


def test_five_should_be_age_group_nothing_alt2() -> None:
    expectedOutput = AGE_GROUP_NOTHING
    print_age_group_alt2(5)
    assert utils.stdout_equals(expectedOutput)


def test_six_should_be_age_group_poussin_alt2() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group_alt2(6)
    assert utils.stdout_equals(expectedOutput)


def test_seven_should_be_age_group_poussin_alt2() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group_alt2(7)
    assert utils.stdout_equals(expectedOutput)


def test_eight_should_be_age_group_pupille_alt2() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group_alt2(8)
    assert utils.stdout_equals(expectedOutput)


def test_nine_should_be_age_group_pupille_alt2() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group_alt2(9)
    assert utils.stdout_equals(expectedOutput)


def test_ten_should_be_age_group_minime_alt2() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group_alt2(10)
    assert utils.stdout_equals(expectedOutput)


def test_eleven_should_be_age_group_minime_alt2() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group_alt2(11)
    assert utils.stdout_equals(expectedOutput)


def test_twelve_should_be_age_group_cadet_alt2() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group_alt2(12)
    assert utils.stdout_equals(expectedOutput)


def test_thirteen_should_be_age_group_cadet_alt2() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group_alt2(13)
    assert utils.stdout_equals(expectedOutput)


# alt 3


def test_five_should_be_age_group_nothing_alt3() -> None:
    expectedOutput = AGE_GROUP_NOTHING
    print_age_group_alt3(5)
    assert utils.stdout_equals(expectedOutput)


def test_six_should_be_age_group_poussin_alt3() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group_alt3(6)
    assert utils.stdout_equals(expectedOutput)


def test_seven_should_be_age_group_poussin_alt3() -> None:
    expectedOutput = AGE_GROUP_POUSSIN
    print_age_group_alt3(7)
    assert utils.stdout_equals(expectedOutput)


def test_eight_should_be_age_group_pupille_alt3() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group_alt3(8)
    assert utils.stdout_equals(expectedOutput)


def test_nine_should_be_age_group_pupille_alt3() -> None:
    expectedOutput = AGE_GROUP_PUPILLE
    print_age_group_alt3(9)
    assert utils.stdout_equals(expectedOutput)


def test_ten_should_be_age_group_minime_alt3() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group_alt3(10)
    assert utils.stdout_equals(expectedOutput)


def test_eleven_should_be_age_group_minime_alt3() -> None:
    expectedOutput = AGE_GROUP_MINIME
    print_age_group_alt3(11)
    assert utils.stdout_equals(expectedOutput)


def test_twelve_should_be_age_group_cadet_alt3() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group_alt3(12)
    assert utils.stdout_equals(expectedOutput)


def test_thirteen_should_be_age_group_cadet_alt3() -> None:
    expectedOutput = AGE_GROUP_CADET
    print_age_group_alt3(13)
    assert utils.stdout_equals(expectedOutput)
