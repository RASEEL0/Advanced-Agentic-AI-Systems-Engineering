from graph import app


result = app.invoke(
    {
        "question":
        "I am visiting Riyadh with my family. "
        "What entertainment activities do you recommend?"
    }
)


print(result["answer"])