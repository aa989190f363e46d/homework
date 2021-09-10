import pytest
from fibonacci import fibonacci
from math import log10


def test_first_3():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2


def test_neganacci():
    assert fibonacci(-1) == 1
    assert fibonacci(-2) == -1
    assert fibonacci(-3) == 2


def test_huge_fib():
    assert sum(map(int, str(fibonacci(150_000)))) == 139_626


def test_not_integer_error():
    with pytest.raises(ValueError):
        fibonacci(.1)
