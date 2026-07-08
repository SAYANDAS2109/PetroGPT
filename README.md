# 🛢️ PetroGPT

> **An AI-powered Petroleum Engineering Assistant built using Google Gemini, Streamlit, FAISS, Sentence Transformers, and Retrieval-Augmented Generation (RAG).**

PetroGPT is an intelligent AI assistant specifically designed for Petroleum Engineering students, researchers, and professionals. It combines Large Language Models (LLMs) with semantic search to provide accurate, context-aware answers from uploaded petroleum engineering documents while also serving as a specialized petroleum engineering chatbot.

---

# 📌 Features

## 🤖 AI Petroleum Engineering Assistant

- Ask technical questions related to Petroleum Engineering.
- Professional responses powered by **Google Gemini 2.5 Flash**.
- Specialized prompt engineering for petroleum engineering concepts.

---

## 📄 PDF Question Answering

Upload petroleum engineering documents and interact with them using natural language.

Supported documents include:

- Reservoir Engineering notes
- Drilling Engineering manuals
- Production Engineering reports
- Petrophysics notes
- Well Logging documents
- Research papers
- Lecture notes

---

## 🧠 Retrieval-Augmented Generation (RAG)

Instead of sending the complete PDF to the language model, PetroGPT follows a modern RAG workflow:

1. Extract text from the uploaded PDF
2. Split the document into semantic chunks
3. Generate vector embeddings
4. Store embeddings inside a FAISS vector database
5. Retrieve only the most relevant chunks
6. Generate accurate context-aware responses using Gemini

This significantly improves:

- Response quality
- Scalability
- Token efficiency
- Retrieval accuracy

---

## 🔍 Semantic Search

PetroGPT performs semantic similarity search rather than simple keyword matching, enabling it to understand the meaning behind user queries and retrieve the most relevant information.

---

## 💾 Persistent Vector Database

Document embeddings are stored locally using **FAISS**, allowing previously processed documents to be reused without recreating embeddings every time.

---

## 💬 Conversation Memory

Maintains conversation history throughout the current session, enabling more natural follow-up questions.

---

## 📥 Chat Export

Download the complete chat history for future reference.

---

# 🏗️ System Architecture

```text
                Upload PDF
                     │
                     ▼
             Text Extraction
                     │
                     ▼
             Document Chunking
                     │
                     ▼
          Sentence Embeddings
                     │
                     ▼
             FAISS Vector Store
                     │
          Semantic Similarity Search
                     │
                     ▼
        Retrieved Relevant Context
                     │
                     ▼
          Google Gemini 2.5 Flash
                     │
                     ▼
              Final AI Response
```

---

# ⚙️ Technologies Used

### Frontend
- Streamlit

### AI Model
- Google Gemini 2.5 Flash

### Retrieval-Augmented Generation
- FAISS
- Sentence Transformers
- LangChain

### PDF Processing
- PyPDF

### Programming Language
- Python

---

# 📂 Project Structure

```text
PetroGPT/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── petro_utils/
│   ├── llm.py
│   ├── pdf_reader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── prompts.py
│
├── vector_db/

```

---

# 🎯 Current Capabilities

- ✅ Petroleum Engineering AI Assistant
- ✅ PDF Question Answering
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Semantic Search
- ✅ FAISS Vector Database
- ✅ Conversation Memory
- ✅ Chat Export

---

# ⚠️ Important Notes

- PetroGPT currently uses the **Google Gemini Free API**, which is subject to request and token rate limits.
- If you upload very large PDF files or repeatedly ask many questions within a short period, you may encounter temporary **quota exceeded (HTTP 429)** errors.
- Large documents require chunking, embedding generation, and vector indexing, so the **first upload may take some time** depending on the document size and your internet connection.
- Once a document has been indexed, semantic retrieval becomes significantly faster.
- This project is intended for **educational and research purposes** and should not replace professional engineering judgement for critical field operations.

---

# 📈 Future Improvements

- Multi-document knowledge base
- Page-level citations
- PDF preview
- Streaming AI responses
- Knowledge base management
- Petroleum engineering calculators
- Well log interpretation
- Reservoir engineering utilities

---

# 👨‍💻 Author

**Sayan Das**

Petroleum Engineering Undergraduate | AI & Machine Learning Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star**.
