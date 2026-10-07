import pytest

from tools.emi_calculator import calculate_emi


def test_calculate_emi():
    result = calculate_emi(
        principal=1_000_000,
        annual_interest_rate=8,
        tenure_years=20
    )

    assert round(result, 2) == 8364.40


def test_zero_interest_emi():
    result = calculate_emi(
        principal=120_000,
        annual_interest_rate=0,
        tenure_years=1
    )

    assert result == 10_000


def test_invalid_principal():
    with pytest.raises(ValueError):
        calculate_emi(0, 8, 20)


def test_negative_interest_rate():
    with pytest.raises(ValueError):
        calculate_emi(1_000_000, -8, 20)


def test_invalid_tenure():
    with pytest.raises(ValueError):
        calculate_emi(1_000_000, 8, 0)