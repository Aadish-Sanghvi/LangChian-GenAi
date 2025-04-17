from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} assistant.'),
    ('human', 'Explain in brief and simple terms, What is {topic}?'),
])

prompt = chat_template.invoke({"domain": "Skin Expert", "topic": "Cause of Acne"})

print(prompt)