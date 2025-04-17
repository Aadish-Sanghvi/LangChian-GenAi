from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about langchain."),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result))

print(messages)