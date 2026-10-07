"""
Budget Planner Tool

Calculates a recommended budget using the 50/30/20 rule:

50% -> Needs
30% -> Wants
20% -> Savings
"""


def calculate_budget(monthly_income: float) -> dict:
    """
    Calculate budget allocation using the 50/30/20 rule.

    Args:
        monthly_income: Monthly take-home income.

    Returns:
        Dictionary containing recommended allocations.
    """

    if monthly_income <= 0:
        raise ValueError("Monthly income must be greater than zero.")

    needs = monthly_income * 0.50
    wants = monthly_income * 0.30
    savings = monthly_income * 0.20

    return {
        "income": monthly_income,
        "needs": needs,
        "wants": wants,
        "savings": savings,
    }