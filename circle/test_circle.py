from math import pi

import pytest
from circle import perimeter, aria


def float_eq(real, expected):
    """
    Helper function to compare floats
    """
    return abs(real - expected) < 0.001


def test_perimeter():
    d = 3
    assert float_eq(perimeter(d), pi * d)


def test_aria():
    d = 4.2
    assert float_eq(aria(d), pi * (d / 2) ** 2)


def test_invalid_diameter_perimeter():
    with pytest.raises(ValueError):
        perimeter(-2)


def test_invalid_diameter_aria():
    with pytest.raises(ValueError):
        aria(-2)


def test_invalid_types():
    with pytest.raises(TypeError):
        perimeter("2")
