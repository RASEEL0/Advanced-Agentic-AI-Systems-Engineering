from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b"
)


def writing_agent(state):

    response = llm.invoke(
        f"""
Write a professional report.

Topic:

{state["topic"]}

Research summary:

{state["summary"]}

Sections:

Executive Summary

Research Findings

Recommendations

Conclusion
"""
    )

    return {

        "draft_report": response.content

    }