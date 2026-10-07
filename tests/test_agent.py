from agent.finance_agent import create_finance_agent


def test_agent_creation():
    agent = create_finance_agent()

    assert agent is not None