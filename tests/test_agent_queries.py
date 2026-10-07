from agent.finance_agent import create_finance_agent


def run_query(agent, query: str):
    """Send a natural-language query to the finance agent."""

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query,
                }
            ]
        }
    )

    return response


def get_final_message(response):
    """Extract the final AI response."""

    messages = response["messages"]

    for message in reversed(messages):
        if getattr(message, "type", None) == "ai":
            return message.content

    return None


def test_emi_query():
    agent = create_finance_agent()

    response = run_query(
        agent,
        "Calculate EMI for a ₹10,00,000 loan at 8% annual interest for 20 years."
    )

    answer = get_final_message(response)

    assert answer is not None
    assert len(answer) > 0


def test_sip_query():
    agent = create_finance_agent()

    response = run_query(
        agent,
        "If I invest ₹7,000 every month for 15 years at 10% annual return, what will be the future value?"
    )

    answer = get_final_message(response)

    assert answer is not None
    assert len(answer) > 0


def test_budget_query():
    agent = create_finance_agent()

    response = run_query(
        agent,
        "My monthly income is ₹90,000. Create a 50/30/20 budget."
    )

    answer = get_final_message(response)

    assert answer is not None
    assert len(answer) > 0


def test_percentage_query():
    agent = create_finance_agent()

    response = run_query(
        agent,
        "What is 20% of ₹85,000?"
    )

    answer = get_final_message(response)

    assert answer is not None
    assert len(answer) > 0