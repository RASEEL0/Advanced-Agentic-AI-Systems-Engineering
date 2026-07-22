from tools import search_activities


results = search_activities(
    audience="Family",
    max_price=100,
    style="Relaxing"
)


for activity in results:
    print(activity["name"])