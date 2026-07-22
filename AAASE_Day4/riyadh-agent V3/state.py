from typing import TypedDict

class ReportState(TypedDict):
    user_request: str
    topic: str
    research_notes: str
    summary: str
    draft_report: str
    final_report: str