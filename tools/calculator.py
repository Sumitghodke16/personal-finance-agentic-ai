"""
General financial calculator tool.

This module contains deterministic mathematical calculations
that can later be exposed to the LangChain agent.
"""


def calculate_percentage(value: float, percentage: float) -> float:
    """
    Calculate a percentage of a given value.

    Example:
        calculate_percentage(85000, 20)
        -> 17000
    """

    if value < 0:
        raise ValueError("Value cannot be negative.")

    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    return value * (percentage / 100)


def calculate_percentage_change(
    original_value: float,
    new_value: float
) -> float:
    """
    Calculate percentage change between two values.

    Example:
        original = 100
        new = 120
        result = 20%
    """

    if original_value <= 0:
        raise ValueError("Original value must be greater than zero.")

    return ((new_value - original_value) / original_value) * 100