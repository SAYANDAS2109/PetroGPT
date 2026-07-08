import streamlit as st
from petro_utils.llm import get_response
from datetime import datetime

st.set_page_config(
    page_title="PetroGPT",
    page_icon="🛢️",
    layout='wide'
)

st.sidebar.title("PetroGPT")

st.sidebar.markdown("---")

if st.sidebar.button('New Chat'):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("About")

st.sidebar.write("""
**Version:** 2.0

**Powered by**
- Google Gemini 2.5 Flash

**Specialized In**
- Reservoir Engineering
- Drilling Engineering
- Production Engineering
- Formation Evaluation
- Petrophysics
- Well Logging
- Geology
- Geophysics
""")

st.sidebar.markdown("---")
st.sidebar.success("Developed by Sayan Das")

st.title('PetroGPT')

st.subheader("AI Assistant for Petroleum Engineering")
st.info("""
Welcome to **PetroGPT**!

Ask questions related to:

- Reservoir Engineering
- Drilling Engineering
- Production Engineering
- Petrophysics
- Formation Evaluation
- Well Logging
- Geology
- Oil & Gas Exploration

Current Version: **2.0**
""")

st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if "time" in message:
            st.caption(message["time"])

prompt = st.chat_input(
    "Ask PetroGPT anything about Petroleum Engineering..."
)

if prompt:

    current_time = datetime.now().strftime("%I:%M %p")

    st.session_state.messages.append(
        {"role":"user",
        "content":prompt,
        "time":current_time}
    )

    with st.chat_message("user"):

        st.markdown(prompt)
        st.caption(current_time)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_response(prompt)

        st.markdown(response)
        st.caption(current_time)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "time": current_time
        }
    )
st.markdown("---")

st.caption("PetroGPT Version 2.0 | Built with Streamlit + Gemini")