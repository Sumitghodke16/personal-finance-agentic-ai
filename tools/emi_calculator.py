"""
EMI Calculator Tool

Calculates the monthly EMI for a loan using the standard
reducing-balance EMI formula.
"""


def calculate_emi(
    principal: float,
    annual_interest_rate: float,
    tenure_years: int
) -> float:
    """
    Calculate monthly loan EMI.

    Args:
        principal: Loan amount.
        annual_interest_rate: Annual interest rate in percentage.
        tenure_years: Loan tenure in years.

    Returns:
        Monthly EMI amount.
    """

    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")

    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    if tenure_years <= 0:
        raise ValueError("Tenure must be greater than zero.")

    monthly_rate = annual_interest_rate / (12 * 100)
    number_of_months = tenure_years * 12

    # Special case: 0% interest
    if monthly_rate == 0:
        return principal / number_of_months

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** number_of_months
        / ((1 + monthly_rate) ** number_of_months - 1)
    )

    return emi