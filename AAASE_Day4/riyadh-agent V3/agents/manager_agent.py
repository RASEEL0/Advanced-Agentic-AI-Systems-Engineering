from langchain_ollama import ChatOllama
import os

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url=os.getenv(
        "OLLAMA_HOST",
         "http://localhost:11434"
    )
)

def manager_agent(state):
    """
    Determines the report topic from the user's request.
    """

    response = llm.invoke(
        f"""
You are the Report Manager.

Your job is to understand the user's request.

Return ONLY the report topic.

User request:
{state["user_request"]}
"""
    )

    print("\n========== MANAGER AGENT ==========")
    print(response.content)

    return {
        "topic": response.content.strip()
    }