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
#save report
with open("report.md", "w", encoding="utf-8") as f:
    f.write(result["final_report"])

print("Report saved to report.md")
#print graph
print(
    app.get_graph().draw_ascii()
)