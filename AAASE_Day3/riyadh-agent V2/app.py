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

print("\n" + "=" * 60)
print("FINAL REPORT")
print("=" * 60)
print(result["final_report"])

# print(
#     app.get_graph().draw_ascii()
# )