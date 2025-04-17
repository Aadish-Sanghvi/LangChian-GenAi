from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India") # invoke method is used to call the LLM with given prompt.

print(result)

# All the LLMs are inherited from BaseLLM class whereas all the Chat Models are inherited from BaseChatModel class.
# The main difference between LLMs and Chat Models is that LLMs are used for text generation while Chat Models are used for chat-based interactions.