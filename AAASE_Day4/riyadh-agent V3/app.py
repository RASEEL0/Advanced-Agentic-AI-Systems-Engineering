from graph import app
import os 
result = app.invoke(
    {
        "user_request": "Who won the World Cup?",
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
reports_dir = os.getenv("REPORTS_DIR", "reports")
os.makedirs(reports_dir, exist_ok=True)

path = os.path.join(reports_dir, "final_report.md")

with open(path, "w", encoding="utf-8") as f:
    f.write(result["final_report"])

print(f"Report saved to: {path}")
print("Report saved to report.md")
#print graph
# print(
#     app.get_graph().draw_ascii()
# )