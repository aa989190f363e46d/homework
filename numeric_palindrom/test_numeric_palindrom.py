import pytest
from numeric_palindrom import is_palindrom


def test_12321():
    assert is_palindrom(12321)
    assert is_palindrom(123321)
    assert is_palindrom(1)


def test_wrong_numbers():
    with pytest.raises(ValueError):    
        assert is_palindrom(-12321)
        assert is_palindrom(1232.1)
