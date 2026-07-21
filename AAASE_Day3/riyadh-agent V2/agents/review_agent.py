from langchain_ollama import ChatOllama
import os 
llm = ChatOllama(
    model="qwen2.5:7b",
    base_url=os.getenv(
        "OLLAMA_HOST",
         "http://localhost:11434"
    )
)


def review_agent(state):
    """
    Reviews and improves the report.
    """

    response = llm.invoke(
        f"""
You are a professional editor.

Review the report.

Improve:

- Grammar
- Clarity
- Professional tone
- Formatting

Return the improved report only.

Report:

{state["draft_report"]}
"""
    )

    print("\n========== REVIEW AGENT ==========")

    return {
        "final_report": response.content
    }