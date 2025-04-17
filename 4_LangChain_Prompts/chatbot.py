from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = OllamaLLM(model="llama3.2")

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("User: ")

    chat_history.append(HumanMessage(content=user_input))

    if user_input == "exit":
        break

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result))

    print("AI: ", result)

print("Chat history:", chat_history)