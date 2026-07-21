from tools import search_activities


def research_agent(state):
    """
    Collects information from the JSON database.
    """

    activities = search_activities()

    notes = ""

    for activity in activities:

        notes += f"""
Name: {activity["name"]}
Category: {activity["category"]}
Audience: {activity["audience"]}
Price: {activity["price"]}
Description: {activity["description"]}

"""

    print("\n========== RESEARCH AGENT ==========")
    print(notes)

    return {
        "research_notes": notes
    }