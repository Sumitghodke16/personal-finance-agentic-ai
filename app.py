import streamlit as st

from agent.finance_agent import create_finance_agent


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Personal Finance AI Agent",
    page_icon="💰",
    layout="centered",
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("💰 Personal Finance AI Agent")

st.markdown(
    """
    Ask financial calculation questions in natural language.

    The AI agent automatically selects the appropriate
    financial tool to calculate the answer.
    """
)


# --------------------------------------------------
# Initialize Agent
# --------------------------------------------------

@st.cache_resource
def load_agent():
    return create_finance_agent()


try:
    agent = load_agent()

except Exception as e:
    st.error(
        "Unable to initialize the finance agent. "
        "Please check your Gemini API configuration."
    )
    st.stop()


# --------------------------------------------------
# Example Queries
# --------------------------------------------------

st.subheader("💡 Example Questions")

examples = [
    "Calculate EMI for a ₹10,00,000 loan at 8% annual interest for 20 years.",
    "If I invest ₹7,000 every month for 15 years at 10% annual return, what will be the future value?",
    "My monthly income is ₹90,000. Create a 50/30/20 budget.",
    "What is 20% of ₹85,000?",
]


for example in examples:
    st.caption(f"• {example}")


# --------------------------------------------------
# User Input
# --------------------------------------------------

st.subheader("Ask Your Question")

query = st.text_area(
    "Enter your financial question:",
    placeholder="Example: Calculate EMI for a ₹10 lakh loan at 8% for 20 years.",
    height=120,
)


# --------------------------------------------------
# Run Agent
# --------------------------------------------------

if st.button("Calculate", type="primary"):

    if not query.strip():
        st.warning("Please enter a financial question.")

    else:

        with st.spinner("Analyzing your question..."):

            try:

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

                # Get final AI response
                final_message = None

                for message in reversed(response["messages"]):

                    if getattr(message, "type", None) == "ai":

                        if message.content:
                            final_message = message.content
                            break

                # Display result
                if final_message:

                    st.subheader("📊 Result")

                    if isinstance(final_message, list):

                        for item in final_message:

                            if (
                                isinstance(item, dict)
                                and item.get("type") == "text"
                            ):
                                st.markdown(item["text"])

                    else:
                        st.markdown(final_message)

                else:

                    st.warning(
                        "The agent did not return a final response."
                    )

            except Exception as e:

                st.error(
                    f"Something went wrong while processing your request:\n\n{e}"
                )


# --------------------------------------------------
# Disclaimer
# --------------------------------------------------

st.divider()

st.caption(
    "⚠️ This application provides mathematical calculations "
    "and general financial information for educational purposes. "
    "It is not personalized financial advice."
)