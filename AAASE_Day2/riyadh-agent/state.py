from typing import TypedDict, List


class AgentState(TypedDict):

    question: str

    activities: List[dict]

    answer: str