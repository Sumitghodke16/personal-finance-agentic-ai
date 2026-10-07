import pytest

from tools.calculator import (
    calculate_percentage,
    calculate_percentage_change,
)


def test_calculate_percentage():
    result = calculate_percentage(85000, 20)

    assert result == 17000


def test_calculate_percentage_change():
    result = calculate_percentage_change(100, 120)

    assert result == 20


def test_negative_value():
    with pytest.raises(ValueError):
        calculate_percentage(-1000, 20)


def test_negative_percentage():
    with pytest.raises(ValueError):
        calculate_percentage(1000, -20)


def test_invalid_original_value():
    with pytest.raises(ValueError):
        calculate_percentage_change(0, 100)