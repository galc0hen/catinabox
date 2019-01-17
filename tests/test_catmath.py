import pytest
from catinabox import catmath


@pytest.mark.parametrize('age, expected_result', [(7, 35), (0.5, 2.5), (0, 0)])
def test__cat_years_to_hooman_years__succeeds(age, expected_result):
    assert catmath.cat_years_to_hooman_years(age) == expected_result


"""
def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 7
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.5
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0

# BONUS MATERIAL FOR STEP 2


def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True

"""
