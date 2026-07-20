import json


def search_activities(
    category=None,
    max_price=None
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


        if max_price:
            if activity["price"] > max_price:
                continue


        results.append(activity)


    return results