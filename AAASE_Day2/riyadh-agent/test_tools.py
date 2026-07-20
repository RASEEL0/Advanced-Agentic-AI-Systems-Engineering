from tools import search_activities


results = search_activities(
    category="Nature",
    max_price=50
)


for item in results:
    print(item["name"])