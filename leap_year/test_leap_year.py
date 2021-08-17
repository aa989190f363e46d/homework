import pytest
from leap_year import is_leap_year


def test_year_not_divisible_by_4():
    assert not is_leap_year(2021)


def test_year_divisible_by_2_but_not_by_4():
    assert not is_leap_year(1970)


def test_year_divisible_by_4_not_by_100():
    assert is_leap_year(1996)


def test_year_divisible_by_100_not_divisible_by_400():
    assert not is_leap_year(1900)


def test_year_divisible_by_400():
    assert is_leap_year(2000)


def test_year_is_1582():
    """year of estatinf leap year rules"""
    assert not is_leap_year(15_82)


def test_year_is_1584():
    """first leap yeir in hostory"""
    assert is_leap_year(15_84)


def test_year_is_less_1582():
    """year of estatinf leap year rules"""
    with pytest.raises(ValueError):
        assert is_leap_year(15_81)
        assert is_leap_year(0)
