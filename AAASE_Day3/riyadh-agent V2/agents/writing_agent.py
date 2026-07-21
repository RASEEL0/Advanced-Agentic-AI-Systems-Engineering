from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b"
)


def writing_agent(state):
    """
    Generates the first report draft.
    """

    response = llm.invoke(
        f"""
You are a professional report writer.

Write a structured report.

Topic:

{state["topic"]}

Summary:

{state["summary"]}

Include:

# Executive Summary

# Research Findings

# Recommendations

# Conclusion
"""
    )

    print("\n========== WRITING AGENT ==========")

    return {
        "draft_report": response.content
    }