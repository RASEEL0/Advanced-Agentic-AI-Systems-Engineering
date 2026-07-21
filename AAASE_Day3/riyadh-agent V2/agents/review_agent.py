from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b"
)


def review_agent(state):

    response = llm.invoke(
        f"""
Review the report.

Improve grammar.

Improve readability.

Return the improved report.

{state["draft_report"]}
"""
    )

    return {

        "final_report": response.content

    }