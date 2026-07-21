from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b"
)


def summarization_agent(state):

    response = llm.invoke(
        f"""
Summarize these research notes.

{state["research_notes"]}

Use bullet points.
"""
    )

    return {

        "summary": response.content

    }