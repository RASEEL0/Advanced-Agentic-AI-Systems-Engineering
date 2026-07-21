from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

from state import AgentState
from tools import search_activities


llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.7
)

# Node 1: extract preference from user input
def preference_node(state: AgentState):

    response = llm.invoke(
        f"""
        You are a tourism preference extraction system.

        Extract information from the user request.

        Return ONLY valid JSON.

        Fields:

        {{
          "category": "type of activity",
          "audience": "who is going",
          "budget": number or null,
          "style": "relaxing/adventure/cultural/etc"
        }}

        User request:
        {state['question']}
        """
    )


    import json
    import re


    json_text = re.search(
        r"\{.*\}",
        response.content,
        re.DOTALL
    ).group()


    preferences = json.loads(json_text)


    print("Preferences extracted:")
    print(preferences)


    return {
        "preferences": preferences
    }
# Node 2: Search our database

def research_node(state: AgentState):

    preferences = state["preferences"]


    activities = search_activities(
        category=preferences.get("category"),
        audience=preferences.get("audience"),
        max_price=preferences.get("budget"),
         style=preferences.get("style")
)
    if not activities:
        return {
        "activities": [],
    }
    return {
        "activities": activities
    }




# Node 3: Generate recommendation

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
    "preference",
    preference_node
)

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
    "preference"
)


graph.add_edge(
    "preference",
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