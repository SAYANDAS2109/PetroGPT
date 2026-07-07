import petro_utils.pdf_reader as pdf_reader
extract_text = pdf_reader.extract_text
import streamlit as st
from datetime import datetime
import petro_utils.llm as llm
from petro_utils.chunking import split_text
from petro_utils.vector_store import create_vector_store
from petro_utils.retriever import retrieve_context
from petro_utils.vector_store import load_vector_store
import os


get_response = llm.get_response

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
## PetroGPT v5.0

### Features

✅ Petroleum Engineering AI Chat

✅ Conversation Memory

✅ PDF Upload

✅ Semantic Search (RAG)

✅ Vector Database

✅ Download Chat

### Specialized In

• Reservoir Engineering

• Drilling Engineering

• Production Engineering

• Formation Evaluation

• Petrophysics

• Well Logging

• Geology

• Geophysics

• Enhanced Oil Recovery

• Petroleum Economics

### Powered By

• Google Gemini 2.5 Flash

• Streamlit

• PyPDF
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Export Chat")

chat_data = ""

for msg in st.session_state.get("messages", []):

    chat_data += f"{msg['role'].upper()}\n"

    chat_data += f"{msg['content']}\n"

    if "time" in msg:
        chat_data += f"Time: {msg['time']}\n"

    chat_data += "\n----------------------------------------\n\n"

st.sidebar.download_button(

    label="📥 Download Chat",

    data=chat_data,

    file_name=f"PetroGPT_Chat_{datetime.now().strftime('%Y-%m-%d')}.txt",

    mime="text/plain"

)
st.markdown("---")
st.sidebar.success("Developed by Sayan Das")

st.title('PetroGPT')

st.subheader("AI Assistant for Petroleum Engineering")
st.info("""
# 👋 Welcome to PetroGPT

Your AI Assistant for Petroleum Engineering.

### You can:

🛢️ Ask Petroleum Engineering questions

📄 Upload Petroleum PDFs

❓ Ask questions from uploaded PDFs

📚 Generate professional PDF summaries

🧠 Continue conversations with memory

📥 Download complete chat history
        
🗝️ Generate Key Points

---

### Current Version

**PetroGPT v5.0**
""")

st.markdown("---")

if "vector_db" not in st.session_state:
    if os.path.exists("vector_db/index.faiss"):
        st.session_state.vector_db = load_vector_store()
    else:
        st.session_state.vector_db = None

uploaded_pdf = st.file_uploader(
    "📄 Upload a Petroleum PDF",
    type=["pdf"]
)

if uploaded_pdf is not None:

    with st.spinner("Reading PDF..."):
        text = extract_text(uploaded_pdf)
    with st.spinner("Splitting Documents into chunks..."):
        chunks = split_text(text)
    with st.spinner("Create semantic embeddings..."):
        st.session_state.vector_db = create_vector_store(chunks)

    st.success(f"✅ {uploaded_pdf.name} indexed successfully!")

    st.info(f"📚 Created {len(chunks)} semantic chunks.")

        
st.markdown("---")



if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if "time" in message:
            st.caption(message["time"])

prompt = st.chat_input(
    "Ask PetroGPT..."
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
            if st.session_state.vector_db is not None:


                context = retrieve_context(
                st.session_state.vector_db,
                prompt
                )

                conversation = ""

                for msg in st.session_state.messages:
                    conversation += f"{msg['role'].upper()}: {msg['content']}\n\n"

                pdf_prompt = f"""
You are PetroGPT.

You are answering questions ONLY from the retrieved context below.

If the answer is NOT available inside the context, reply exactly:

'I could not find this information in the uploaded document.'

---------------- Conversation ----------------

{conversation}

---------------- Retrieved Context ----------------

{context}

---------------- Current Question ----------------

{prompt}
"""

                response = get_response(pdf_prompt)

            else:
                conversation = ""

                for msg in st.session_state.messages:
                    conversation += f"{msg['role'].upper()}: {msg['content']}\n\n"
                
                full_prompt = f"""
You are PetroGPT.

No PDF is currently loaded.

Conversation History:

{conversation}

Current Question:

{prompt}
"""
                response = get_response(full_prompt)
           

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

st.caption("PetroGPT Version 5.0")

