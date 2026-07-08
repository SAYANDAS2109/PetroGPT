import streamlit as st
from datetime import datetime
import petro_utils.llm as llm
get_response = llm.get_response
from petro_utils.chunking import split_text
from petro_utils.vector_store import create_vector_store
from petro_utils.pdf_reader import extract_text
from petro_utils.retriever import retrieve_context
st.set_page_config(
    page_title="PetroGPT",
    page_icon="🛢️",
    layout = "wide"
)

if "page" not in st.session_state:
    st.session_state.page = "home"
if "petroleum_messages" not in st.session_state:
    st.session_state.petroleum_messages = []
if "pdf_messages" not in st.session_state:
    st.session_state.pdf_messages=[]
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False

if "uploaded_pdf_name" not in st.session_state:
    st.session_state.uploaded_pdf_name = ""


st.sidebar.title("PetroGPT")
st.markdown('---')

if st.session_state.page == "petroleum":
    st.sidebar.subheader("🛢 Petroleum Assistant")
    if st.sidebar.button("🆕 New Chat"):
        st.session_state.petroleum_messages = []
        st.rerun()

    chat_data = ""
    for msg in st.session_state.petroleum_messages:

        chat_data += f"{msg['role'].upper()}\n"

        chat_data += msg["content"]
        if "time" in msg:
            chat_data += f"\nTime: {msg['time']}"

        chat_data += "\n\n----------------------\n\n"
    st.sidebar.download_button(
        "📥 Export Chat",
        data=chat_data,
        file_name="Petroleum_Chat.txt",
        mime="text/plain"
    )
    st.sidebar.markdown('---')

if st.session_state.page == 'pdf':
    st.sidebar.subheader("📄 PDF Assistant")
    if st.sidebar.button("🆕 New Chat"):
        st.session_state.pdf_messages = []
        st.rerun()

    chat_data = ""
    for msg in st.session_state.pdf_messages:
        chat_data += f"{msg['role'].upper()}\n"

        chat_data += msg["content"]
        if "time" in msg:
            chat_data += f"\nTime: {msg['time']}"
        chat_data += "\n\n----------------------\n\n"
    st.sidebar.download_button(
        "📥 Export Chat",
        data=chat_data,
        file_name="PDF_Chat.txt",
        mime="text/plain"
    )

    st.sidebar.markdown("---")

if st.session_state.page != "home":
    if st.sidebar.button("🏠Home"):
        st.session_state.page = "home"
        st.rerun()
st.sidebar.markdown('---')

st.sidebar.subheader("📊 System Status")
st.sidebar.success("🟢 LLM : Gemini 2.5 Flash")
if st.session_state.vector_db is None:
    st.sidebar.warning("🟡 Vector DB : Not Loaded")
else:
    st.sidebar.success("🟢 Vector DB : Loaded")
if st.session_state.pdf_uploaded:
    st.sidebar.success(
        f"🟢 PDF : {st.session_state.uploaded_pdf_name}"
    )
else:
    st.sidebar.info("📄 PDF : None")
st.sidebar.info("🧠 Retrieval : FAISS")

st.sidebar.info("📦 Embeddings : MiniLM-L6-v2")

st.sidebar.info("🚀 Version : PetroGPT v6.0")

st.sidebar.markdown("---")

st.sidebar.caption("Developed by Sayan Das")


if st.session_state.page == "home":
    st.title('PetroGPT')
    st.subheader('AI Assistant for Petroleum Engineering')
    st.markdown("---")

    st.markdown(
        """
Welcome to **PetroGPT Version 6.0**.

Choose how you would like to use PetroGPT.
"""
    )
    st.markdown("")

    col1,col2 = st.columns(2)

    with col1:
        st.info("## 🛢️ Petroleum AI Assistant")

        st.write("""
Ask anything related to Petroleum Engineering.

Examples:

- Reservoir Engineering

- Drilling Engineering

- Production Engineering

- Well Logging

- Petrophysics

- Formation Evaluation

- Geology

- Geophysics

- Petroleum Economics

⚡ Fast responses

⚡ Powered by Gemini

⚡ No PDF required
""")            
        if st.button(
            "Launch Petroleum Assistant",
            use_container_width=True
        ):
            st.session_state.page = "petroleum"
            st.rerun()
    
    with col2:
        st.success("## 📄 PDF Research Assistant")
        st.write("""
Upload Petroleum Engineering PDFs.

Then ask questions directly from them.

Features:

- Semantic Search

- AI Question Answering

- PDF Summarization

- Key Point Extraction

- Research Paper Assistant

⚡ Powered by RAG

⚡ FAISS Vector Database

⚡ AI Retrieval
""")    
        if st.button(
            "Launch PDF Assistant",
            use_container_width=True
        ):
            st.session_state.page = "pdf"
            st.rerun()
if st.session_state.page == "petroleum":
    st.title("🛢️ Petroleum AI Assistant")
    st.caption("Ask anything about Petroleum Engineering")

    st.markdown("---")


    for message in st.session_state.petroleum_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])
            if "time" in message:
                st.caption(message["time"])
    prompt = st.chat_input(
        "Ask PetroGPT...."
    )

    if prompt:
        current_time = datetime.now().strftime("%I:%M %p")
        st.session_state.petroleum_messages.append(
        {
            "role": "user",
            "content": prompt,
            "time":current_time
        }
    )

        with st.chat_message("user"):

            st.markdown(prompt)
            st.caption(current_time)

        conversation=""
        for msg in st.session_state.petroleum_messages:
            conversation += f"{msg['role'].upper()}: {msg['content']}\n\n"
        prompt_for_llm = f"""
You are PetroGPT.

You are a professional Petroleum Engineering AI Assistant.

Continue the following conversation naturally.

Conversation History:

{conversation}

Current Question:

{prompt}
"""
        with st.chat_message('assistant'):
            with st.spinner('Thinking...'):
                response = get_response(prompt_for_llm)
        
            st.markdown(response)
        
        st.session_state.petroleum_messages.append(
            {
                "role":"assistant",
                "content":response,
                "time":current_time
            }
        )

if st.session_state.page == "pdf":
    st.title("📄 PDF Research Assistant")

    st.caption("Upload a Petroleum Engineering PDF and ask questions from it.")

    st.markdown("---")

    uploaded_pdf = st.file_uploader(
        "Upload Petroleum Engineering PDF",
    type=["pdf"])
    with st.expander("📘 Important Instructions (Please Read)", expanded=True):
                st.markdown(
                    """
### 🚀 Tips for Better Results

#### ⏳ 1. Wait for PDF Processing
- Large PDFs may take **5–7 minutes** to process.
- Please wait until you see **'PDF indexed successfully!'** before asking questions.

---

#### 🔍 2. Use Technical Keywords
PetroGPT retrieves information using semantic search.

✅ Better Questions
- Explain porosity
- What is permeability?
- Explain Darcy's Law
- Define water saturation

❌ Less Effective Questions
- What is it?
- Explain it.
- Tell me more.
- Continue.

---

#### 🧠 3. PetroGPT is NOT History Aware

Every question is treated independently.

Instead of:

❌ Explain it

Use:

✅ Explain porosity

✅ Explain permeability

---

#### 📄 4. Ask Questions Related to the Uploaded PDF

PetroGPT only answers from the uploaded document.

If the information is unavailable, it will tell you that it could not find the answer.

---

💡 **Tip:** More specific questions produce better answers.
"""
                )

    if uploaded_pdf is not None:
        if(
            not st.session_state.pdf_uploaded
            or uploaded_pdf.name != st.session_state.uploaded_pdf_name
        ):
            with st.spinner("Reading PDF..."):
                text = extract_text(uploaded_pdf)

            with st.spinner("Creating Chunks..."):
                chunks = split_text(text)

            with st.spinner("Creating Embeddings..."):
                vector_db = create_vector_store(chunks)
            
            st.session_state.vector_db = vector_db

            st.session_state.pdf_uploaded = True

            st.session_state.uploaded_pdf_name = uploaded_pdf.name

            st.success(f"✅ {uploaded_pdf.name} indexed successfully!")

            st.info(f"Created {len(chunks)} semantic chunks.")

            
        else:
            st.success("✅ PDF already indexed.")

            st.info(
            f"Using existing vector database for {st.session_state.uploaded_pdf_name}"
        )
        if st.button('🔄 Upload Another PDF'):
            st.session_state.vector_db = None
            st.session_state.pdf_uploaded = False
            st.session_state.uploaded_pdf_name = ""
            st.session_state.pdf_messages = []

            st.rerun()
        
        
    
        st.markdown("---")
        for message in st.session_state.pdf_messages:
            with st.chat_message(message["role"]):

                st.markdown(message["content"])

                if "time" in message:
                    st.caption(message["time"])

        pdf_prompt = st.chat_input(
            "Ask anything from this PDF..."
        )
        if pdf_prompt:
            current_time= datetime.now().strftime("%I:%M %p")
            st.session_state.pdf_messages.append(
                {
                    "role":"user",
                    "content":pdf_prompt,
                    "time":current_time
                }
            )
            with st.chat_message("user"):
                st.markdown(pdf_prompt)
                st.caption(current_time)
            with st.chat_message("assistant"):
                with st.spinner("Searching Document..."):
                    context = retrieve_context(
                        st.session_state.vector_db,
                        pdf_prompt
                    )
                    conversation = ""

                    for msg in st.session_state.pdf_messages:
                        conversation += (
                            f"{msg['role'].upper()}: "
                            f"{msg['content']}\n\n"
                        )
                    rag_prompt = f"""
You are PetroGPT.

You are a Petroleum Engineering expert.

Answer ONLY using the retrieved context.

If the answer cannot be found inside the retrieved context, reply exactly:

I could not find this information in the uploaded document.

Conversation History:

{conversation}

Retrieved Context:

{context}

Question:

{pdf_prompt}
"""
                    response = get_response(rag_prompt)
                st.markdown(response)
                st.caption(current_time)
            st.session_state.pdf_messages.append(
                    {
                "role": "assistant",
                "content": response,
            "time": current_time
                }
                )
