from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

from state import AgentState
from tools import search_activities


llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.7
)


# Node 1: Search our database

def research_node(state: AgentState):

    activities = search_activities(
        category="Nature",
        max_price=100
    )

    return {
        "activities": activities
    }



# Node 2: Generate recommendation

def recommendation_node(state: AgentState):

    activities_text = "\n".join(
        [
            f"- {a['name']}: {a['description']}"
            for a in state["activities"]
        ]
    )


    response = llm.invoke(
        f"""
        You are a Riyadh tourism expert.

        User request:
        {state['question']}

        Recommend activities from this database:

        {activities_text}

        Explain why they are suitable.
        """
    )


    return {
        "answer": response.content
    }



# Create graph

graph = StateGraph(AgentState)


graph.add_node(
    "research",
    research_node
)


graph.add_node(
    "recommend",
    recommendation_node
)



graph.add_edge(
    START,
    "research"
)


graph.add_edge(
    "research",
    "recommend"
)


graph.add_edge(
    "recommend",
    END
)



app = graph.compile()