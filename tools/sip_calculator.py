"""
SIP Investment Calculator Tool

Calculates the future value of a monthly SIP investment
using the standard SIP future-value formula.
"""


def calculate_sip_future_value(
    monthly_investment: float,
    annual_return_rate: float,
    tenure_years: int
) -> float:
    """
    Calculate the future value of a monthly SIP.

    Args:
        monthly_investment: Monthly amount invested.
        annual_return_rate: Expected annual return in percentage.
        tenure_years: Investment duration in years.

    Returns:
        Estimated future value of the investment.
    """

    if monthly_investment <= 0:
        raise ValueError("Monthly investment must be greater than zero.")

    if annual_return_rate < 0:
        raise ValueError("Return rate cannot be negative.")

    if tenure_years <= 0:
        raise ValueError("Tenure must be greater than zero.")

    monthly_rate = annual_return_rate / (12 * 100)
    number_of_months = tenure_years * 12

    # Special case: 0% return
    if monthly_rate == 0:
        return monthly_investment * number_of_months

    future_value = (
        monthly_investment
        * ((1 + monthly_rate) ** number_of_months - 1)
        / monthly_rate
    )

    return future_value