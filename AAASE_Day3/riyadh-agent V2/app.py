from graph import app


result = app.invoke(
    {
            "question":
        """
        I am visiting Riyadh with my two children.
        I want calm outdoor activities.
        My budget is 100 SAR.
        """
    }
)


print(result["answer"])

print(
    app.get_graph().draw_ascii()
)