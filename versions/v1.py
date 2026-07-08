# import petro_utils.llm
# & "C:\Users\Sayan Das\AppData\Local\Python\pythoncore-3.11-64\python.exe" -m streamlit run app.py
# print("Imported from:", petro_utils.llm.__file__)
# print("Functions:", dir(petro_utils.llm))

# from petro_utils.llm import get_response
# import sys
# import os

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import petro_utils.llm

# print("LLM FILE:", petro_utils.llm.__file__)
# print("ATTRIBUTES:", dir(petro_utils.llm))

import streamlit as st
from petro_utils.llm import get_response

st.set_page_config(
    page_title="PetroGPT",
    page_icon="🛢️",
    layout="wide"
)
with st.sidebar:
    st.title("🛢️ PetroGPT")
    st.write("AI Assistant for Petroleum Engineering")

    st.markdown("---")

    st.write("### Features")
    st.write("✔ Reservoir Engineering")
    st.write("✔ Drilling")
    st.write("✔ Production")
    st.write("✔ Geology")
    st.write("✔ Well Logging")

    st.markdown("---")

    if st.sidebar.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()


st.title("PetroGPT")
st.caption("AI Assistant for Petroleum Engineering")

st.markdown("---")

st.info("""
Welcome to PetroGPT!

This chatbot is powered by Google's Gemini AI.

Current Version:
- AI Chat
- Petroleum Engineering Assistant

Future Updates:
- PDF Question Answering
- RAG
- Reservoir Knowledge Base
- Oil & Gas Dataset Support
""")

st.markdown("### Example Questions")

col1, col2 = st.columns(2)

with col1:
    st.write("- What is porosity?")
    st.write("- Explain Darcy's Law.")
    st.write("- What is shale gas?")
    st.write("- What is permeability?")

with col2:
    st.write("- Explain well logging.")
    st.write("- Difference between sandstone and shale.")
    st.write("- What is water saturation?")
    st.write("- Explain reservoir rocks.")

st.markdown("---")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask PetroGPT anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_response(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )