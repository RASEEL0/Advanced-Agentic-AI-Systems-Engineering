from langgraph.graph import StateGraph, START, END

from state import ReportState

from agents.manager_agent import manager_agent
from agents.research_agent import research_agent


graph = StateGraph(ReportState)

# Add nodes
graph.add_node("manager", manager_agent)
graph.add_node("research", research_agent)

# Connect nodes
graph.add_edge(START, "manager")
graph.add_edge("manager", "research")
graph.add_edge("research", END)

# Compile graph
app = graph.compile()