from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b"
)


def summarization_agent(state):
    """
    Summarizes the research findings.
    """

    response = llm.invoke(
        f"""
You are a research summarization agent.

Summarize the following research notes into concise bullet points.

Research Notes:

{state["research_notes"]}

Keep only the most important information.
"""
    )

    print("\n========== SUMMARIZATION AGENT ==========")
    print(response.content)

    return {
        "summary": response.content
    }