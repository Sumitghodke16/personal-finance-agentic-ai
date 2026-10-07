import pytest

from tools.budget_planner import calculate_budget


def test_calculate_budget():
    result = calculate_budget(90_000)

    assert result["income"] == 90_000
    assert result["needs"] == 45_000
    assert result["wants"] == 27_000
    assert result["savings"] == 18_000


def test_budget_total():
    result = calculate_budget(90_000)

    total = (
        result["needs"]
        + result["wants"]
        + result["savings"]
    )

    assert total == result["income"]


def test_small_income():
    result = calculate_budget(10_000)

    assert result["needs"] == 5_000
    assert result["wants"] == 3_000
    assert result["savings"] == 2_000


def test_zero_income():
    with pytest.raises(ValueError):
        calculate_budget(0)


def test_negative_income():
    with pytest.raises(ValueError):
        calculate_budget(-50_000)