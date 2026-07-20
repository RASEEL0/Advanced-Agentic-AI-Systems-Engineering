from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

from state import AgentState


llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.7
)


def tourist_agent(state: AgentState):

    response = llm.invoke(
        f"""
        You are a Riyadh tourism expert.

        Answer the user's question:
        
        {state['question']}

        Give useful recommendations.
        """
    )

    return {
        "answer": response.content
    }



graph = StateGraph(AgentState)


graph.add_node(
    "tourist_agent",
    tourist_agent
)


graph.add_edge(
    START,
    "tourist_agent"
)


graph.add_edge(
    "tourist_agent",
    END
)


app = graph.compile()