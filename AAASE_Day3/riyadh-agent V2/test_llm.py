from langchain_ollama import ChatOllama
import os

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.7,
    base_url="http://host.docker.internal:11434"
    
)
llm = ChatOllama(
    model="qwen2.5:7b",
    base_url=os.getenv(
        "OLLAMA_HOST",
        "http://host.docker.internal:11434"
    )
)


response = llm.invoke(
    "You are a Riyadh tourism expert. "
    "Tell me about Boulevard World."
)


print(response.content)
