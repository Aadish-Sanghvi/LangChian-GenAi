from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = llm

st.header('Reasearch Tool')

user_input = st.text_input("Ask a question")

if st.button("Submit"):
    with st.spinner("Thinking..."):
        result = llm.invoke(user_input)
    st.success("Here's the response:")
    st.write(result)