import pytest
from pizza import find_entrance, find_floor

F = 5  # этажей
# 4 квартиры на каждый этаж


def test_first_flat():
    n = 1

    assert find_entrance(F, n) == 1
    assert find_floor(F, n) == 1


def test_first_entrance_middle_1():
    n = 13

    assert find_entrance(F, n) == 1
    assert find_floor(F, n) == 4


def test_first_entrance_middle_2():
    n = 16

    assert find_entrance(F, n) == 1
    assert find_floor(F, n) == 4


def test_first_entrance_last_flat():
    n = F * 4

    assert find_entrance(F, n) == 1
    assert find_floor(F, n) == 5


def test_first_flat_of_entrance():
    # первая квартира 2 подъезда
    n = F * 4 + 1

    assert find_entrance(F, n) == 2
    assert find_floor(F, n) == 1


def test_somewhere_in_the_middle():
    # 2 подъезд, 2 этаж
    n = 25

    assert find_entrance(F, n) == 2
    assert find_floor(F, n) == 2


def test_last_flat_of_entrance():
    # последняя квартира 2 подъезда
    n = 2 * F * 4

    assert find_entrance(F, n) == 2
    assert find_floor(F, n) == F


def test_zero_height_find_entrance():
    with pytest.raises(ValueError):
        find_entrance(0, 1)


def test_negative_height_find_entrance():
    with pytest.raises(ValueError):
        find_entrance(-1, 1)


def test_zero_height_find_floor():
    with pytest.raises(ValueError):
        find_entrance(F, 0)


def test_negative_height_find_floor():
    with pytest.raises(ValueError):
        find_entrance(F, -1)
