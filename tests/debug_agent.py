from agent.finance_agent import create_finance_agent


agent = create_finance_agent()

query = "Calculate EMI for a ₹10,00,000 loan at 8% annual interest for 20 years."

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

print("\n========== AGENT TRACE ==========\n")

for message in response["messages"]:
    print("MESSAGE TYPE:", message.type)

    if hasattr(message, "tool_calls") and message.tool_calls:
        print("TOOL CALLS:")
        print(message.tool_calls)

    print("CONTENT:")
    print(message.content)

    print("-" * 60)