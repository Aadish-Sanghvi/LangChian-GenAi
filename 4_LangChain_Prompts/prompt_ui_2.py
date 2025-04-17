from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt, PromptTemplate

# Load .env
load_dotenv()

# Initialize LLM
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

# Load prompt template
template = load_prompt("/Users/sanghvi/Desktop/Coding/LangChain/4_LangChain_Prompts/template.json")

# template = PromptTemplate.from_template(
#     """
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input}  

# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  

# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
#     """
# )

# Streamlit UI
st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name", 
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

if st.button("Submit"):
    # Combine prompt + model into a runnable chain
    chain = template | llm

    with st.spinner("Thinking..."):
        try:
            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            })

            st.markdown(result)  # Use markdown to show formatted text

        except Exception as e:
            st.error(f"Error: {e}")