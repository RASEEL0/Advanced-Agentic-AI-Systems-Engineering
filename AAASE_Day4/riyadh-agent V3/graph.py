from langgraph.graph import StateGraph, START, END

from state import ReportState

from agents.manager_agent import manager_agent
from agents.research_agent import research_agent
from agents.summarization_agent import summarization_agent
from agents.writing_agent import writing_agent
from agents.review_agent import review_agent


graph = StateGraph(ReportState)

# Add nodes
graph.add_node("manager", manager_agent)
graph.add_node("research", research_agent)
graph.add_node("summary", summarization_agent)
graph.add_node("writer", writing_agent)
graph.add_node("review", review_agent)

# Connect nodes
graph.add_edge(START, "manager")
# Decide whether to continue or stop.
def manager_router(state):
    """
    Decide whether to continue or stop.
    """

    if state["topic"] == "REFUSE":
        return "end"

    return "research"


graph.add_conditional_edges(
    "manager",
    manager_router,
    {
        "research": "research",
        "end": END,
    },
)
graph.add_edge("research", "summary")
graph.add_edge("summary", "writer")
graph.add_edge("writer", "review")
graph.add_edge("review", END)

# Compile graph
app = graph.compile()