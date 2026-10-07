"""
LangChain Personal Finance Agent.

The agent receives a natural-language financial question
and automatically selects the appropriate financial tool.
"""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.calculator import (
    calculate_percentage,
    calculate_percentage_change,
)
from tools.emi_calculator import calculate_emi
from tools.sip_calculator import calculate_sip_future_value
from tools.budget_planner import calculate_budget


# Load environment variables from .env
load_dotenv()


# -------------------------------------------------------------------
# Tool wrappers
# -------------------------------------------------------------------

def percentage_tool(value: float, percentage: float) -> float:
    """Calculate a percentage of a value."""
    return calculate_percentage(value, percentage)


def percentage_change_tool(
    original_value: float,
    new_value: float
) -> float:
    """Calculate percentage change."""
    return calculate_percentage_change(
        original_value,
        new_value
    )


def emi_tool(
    principal: float,
    annual_interest_rate: float,
    tenure_years: int
) -> float:
    """Calculate monthly loan EMI."""
    return calculate_emi(
        principal,
        annual_interest_rate,
        tenure_years
    )


def sip_tool(
    monthly_investment: float,
    annual_return_rate: float,
    tenure_years: int
) -> float:
    """Calculate SIP future value."""
    return calculate_sip_future_value(
        monthly_investment,
        annual_return_rate,
        tenure_years
    )


def budget_tool(monthly_income: float) -> dict:
    """Calculate budget using the 50/30/20 rule."""
    return calculate_budget(monthly_income)


# All tools available to the agent
tools = [
    percentage_tool,
    percentage_change_tool,
    emi_tool,
    sip_tool,
    budget_tool,
]


# -------------------------------------------------------------------
# Agent creation
# -------------------------------------------------------------------

def create_finance_agent():
    """
    Create and return the LangChain finance agent.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not configured. "
            "Please add it to your .env file."
        )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        google_api_key=api_key,
    )

    system_prompt = """
You are a Personal Finance Assistant.

Your job is to help users with basic financial calculations.

You have access to these tools:

1. percentage_tool
   - Calculate a percentage of a value.

2. percentage_change_tool
   - Calculate percentage change.

3. emi_tool
   - Calculate monthly loan EMI.

4. sip_tool
   - Calculate SIP future value.

5. budget_tool
   - Calculate a monthly budget using the 50/30/20 rule.

IMPORTANT RULES:

- Use the appropriate tool whenever a calculation matches
  one of the available tools.
- Do not perform financial arithmetic yourself when a tool
  is available.
- Clearly explain the final result.
- Show important input values in the response.
- Investment calculations are estimates and should be
  presented as such.
- Do not provide personalized financial advice.
"""

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent