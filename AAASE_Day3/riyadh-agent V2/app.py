from graph import app

result = app.invoke(
    {
        "user_request": "Generate a report about family entertainment activities in Riyadh.",
        "topic": "",
        "research_notes": "",
        "summary": "",
        "draft_report": "",
        "final_report": ""
    }
)

print("\n========== FINAL STATE ==========")
print(result)

# print(
#     app.get_graph().draw_ascii()
# )