# from langchain_ollama import OllamaLLM
# import streamlit as st

# # Load LLaMA via Ollama
# llm = OllamaLLM(model="llama3.2")
# st.title("Research Tool 🤖🧠")

# user_input = st.text_input("Ask a question")

# if st.button("Submit"):
#     with st.spinner("Thinking..."):
#         result = llm.invoke(user_input)
#     st.success("Here's the response:")
#     st.write(result)



from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

# Initialize Ollama LLaMA 3.2 model
llm = OllamaLLM(model="llama3.2")

# Load custom prompt template from JSON file
template = load_prompt("/Users/sanghvi/Desktop/Coding/LangChain/4_LangChain_Prompts/template.json")

# Streamlit UI
st.header('📚 Research Summary Tool (LLaMA 3.2)')

# User selections
paper_input = st.selectbox(
    "📄 Select Research Paper",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers",
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "🧠 Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "📏 Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# When Submit button is pressed
if st.button("Submit"):
    chain = template | llm  # Create a runnable chain with prompt + LLM

    with st.spinner("🧠 Thinking..."):
        try:
            # Invoke the chain with input values
            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            })

            # Display the generated summary
            st.markdown(result)

        except Exception as e:
            st.error(f"❌ Error: {e}")
