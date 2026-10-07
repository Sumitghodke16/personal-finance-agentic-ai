import pytest

from tools.sip_calculator import calculate_sip_future_value


def test_calculate_sip_future_value():
    result = calculate_sip_future_value(
        monthly_investment=7_000,
        annual_return_rate=10,
        tenure_years=15
    )

    assert round(result, 2) == 2901292.42


def test_zero_return():
    result = calculate_sip_future_value(
        monthly_investment=3_000,
        annual_return_rate=0,
        tenure_years=5
    )

    assert result == 180_000


def test_invalid_monthly_investment():
    with pytest.raises(ValueError):
        calculate_sip_future_value(0, 10, 15)


def test_negative_return_rate():
    with pytest.raises(ValueError):
        calculate_sip_future_value(7_000, -10, 15)


def test_invalid_tenure():
    with pytest.raises(ValueError):
        calculate_sip_future_value(7_000, 10, 0)