import pytest
from fibonacci import fibonacci


def test_first_3():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1


def test_neganacci():
    assert fibonacci(-1) == 1
    assert fibonacci(-2) == -1
    assert fibonacci(-3) == 2


def test_not_integer_error():
    with pytest.raises(ValueError):
        fibonacci(.1)
