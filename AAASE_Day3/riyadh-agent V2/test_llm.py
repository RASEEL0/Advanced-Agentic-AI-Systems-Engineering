from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.7
)


response = llm.invoke(
    "You are a Riyadh tourism expert. "
    "Tell me about Boulevard World."
)


print(response.content)
