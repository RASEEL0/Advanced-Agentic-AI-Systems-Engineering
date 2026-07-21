from typing import TypedDict, List


class AgentState(TypedDict):

    question: str

    preferences: dict

    activities: List[dict]

    answer: str