from graph import app


result = app.invoke(
    {
         "question":
        "I want family activities in Riyadh."
    }
)


print(result["answer"])

print(
    app.get_graph().draw_ascii()
)