import json


def search_activities(
    category=None,
    audience=None,
    max_price=None,
    style=None
):

    with open(
        "data/activities.json",
        "r",
        encoding="utf-8"
    ) as file:

        activities = json.load(file)


    results = []


    for activity in activities:

        if category:
            if category.lower() not in activity["category"].lower():
                continue


        if audience:
            if audience.lower() not in activity["audience"].lower():
                continue


        if max_price:
            if activity["price"] > max_price:
                continue


        if style:
            if style.lower() not in activity["style"].lower():
                continue


        results.append(activity)


    return results