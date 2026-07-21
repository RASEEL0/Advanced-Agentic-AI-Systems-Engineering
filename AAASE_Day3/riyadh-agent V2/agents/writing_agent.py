from langchain_ollama import ChatOllama
import os 
llm = ChatOllama(
    model="qwen2.5:7b",
    base_url=os.getenv(
        "OLLAMA_HOST",
         "http://localhost:11434"
    )
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