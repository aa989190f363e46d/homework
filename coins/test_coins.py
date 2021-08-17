import pytest
from itertools import permutations

from coins import max_sum_of_2


def test_2_3_6():
    coins = [2, 3, 6]

    for perm in permutations(coins):
        assert max_sum_of_2(*perm) == 9


def test_3_2_2():
    coins = [3, 2, 2]

    for perm in permutations(coins):
        assert max_sum_of_2(*perm) == 5


def test_invalid_values():
    coins = [-2, 3, 6]
    with pytest.raises(ValueError):
        for perm in permutations(coins):
            assert max_sum_of_2(*perm)


def test_invalid_types():
    coins = ["2", 3, 6]
    with pytest.raises(ValueError):
        for perm in permutations(coins):
            assert max_sum_of_2(*perm)


def test_invalid_coin_count():
    two_coins = [3, 6]
    four_coins = [3, 6]
    with pytest.raises(ValueError):
        assert max_sum_of_2(two_coins)
        assert max_sum_of_2(four_coins)
