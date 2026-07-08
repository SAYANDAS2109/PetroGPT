# 🛢️ PetroGPT

> **An AI-powered Petroleum Engineering Assistant built using Google Gemini, Streamlit, FAISS, Sentence Transformers, and Retrieval-Augmented Generation (RAG).**

PetroGPT is an intelligent AI assistant designed specifically for Petroleum Engineering students, researchers, and professionals. It combines Large Language Models (LLMs) with semantic document retrieval to answer petroleum engineering questions, understand uploaded PDF documents, and provide accurate, context-aware responses.

---

# 🌐 Live Demo

🚀 **Try PetroGPT Online**

**Live App:**  
https://petrogpt-orcp5r2adjbeapjctlwadg.streamlit.app/

> **Note:** PetroGPT uses the free Google Gemini API. During periods of heavy usage, you may occasionally experience slower responses or temporary quota (HTTP 429) errors. Simply wait a minute and try again.

---

# 🚀 Project Evolution

PetroGPT was developed incrementally, with each version introducing new capabilities and architectural improvements.

| Version | Description |
|----------|-------------|
| **Version 1** | Basic Petroleum Engineering chatbot powered by Google Gemini. Capable of answering petroleum engineering questions without document support. |
| **Version 2** | Introduced conversation memory and improved prompt engineering for more natural interactions. |
| **Version 3** | Added PDF upload, text extraction, PDF summarization, key point extraction, and chat export functionality. |
| **Version 4** | Improved user interface, better conversation handling, enhanced PDF workflow, and overall application stability. |
| **Version 5 (Current)** | Complete Retrieval-Augmented Generation (RAG) implementation using document chunking, semantic embeddings, FAISS vector database, and semantic retrieval for highly accurate PDF question answering. |

Older versions are included in the repository to showcase the complete development journey of PetroGPT.

---

# ✨ Features

## 🤖 AI Petroleum Engineering Assistant

- Ask technical petroleum engineering questions
- Professional AI responses powered by Google Gemini 2.5 Flash
- Specialized prompt engineering for engineering concepts

---

## 📄 PDF Question Answering

Upload petroleum engineering PDFs and interact with them naturally.

Supported documents include:

- Reservoir Engineering
- Drilling Engineering
- Production Engineering
- Petrophysics
- Well Logging
- Formation Evaluation
- Research Papers
- Lecture Notes

---

## 🧠 Retrieval-Augmented Generation (RAG)

PetroGPT follows a modern Retrieval-Augmented Generation workflow:

1. Upload PDF
2. Extract Text
3. Split into Semantic Chunks
4. Generate Embeddings
5. Store in FAISS Vector Database
6. Retrieve Relevant Context
7. Generate AI Response using Gemini

Benefits:

- Improved answer accuracy
- Faster retrieval
- Reduced token usage
- Scalable document understanding

---

## 🔍 Semantic Search

Uses semantic similarity instead of keyword matching to retrieve the most relevant sections of uploaded documents.

---

## 💾 Local Vector Database

Embeddings are stored locally using **FAISS**, allowing efficient semantic search across indexed documents.

---

## 💬 Conversation Memory

Maintains conversation history during the current chat session for contextual follow-up questions.

---

## 📥 Export Chat

Download the complete conversation history for future reference.

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

# ⚙️ Tech Stack

### Frontend

- Streamlit

### AI Model

- Google Gemini 2.5 Flash

### Retrieval-Augmented Generation

- LangChain
- FAISS
- Sentence Transformers

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
├── versions/
│   ├── PetroGPT_v1/
│   ├── PetroGPT_v2/
│   ├── PetroGPT_v3/
│   └── PetroGPT_v4/
│
├── vector_db/
│
└── screenshots/
```


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

- PetroGPT currently uses the **Google Gemini Free API**, which has request and token rate limits.
- Large PDF documents require additional processing time during the first upload because embeddings and the FAISS vector database must be generated.
- If you encounter temporary **HTTP 429 (Quota Exceeded)** errors, simply wait a short period before trying again.
- This project is intended for educational and research purposes and should not replace professional engineering judgement for real-world petroleum operations.

---

# 🚀 Future Roadmap

- Multi-document knowledge base
- Source citations with page numbers
- PDF preview
- Streaming AI responses
- Knowledge base management
- Petroleum engineering calculators
- Reservoir simulation integration
- Well log interpretation
- Multi-user support

---

# 👨‍💻 Author

**Sayan Das**

Petroleum Engineering Undergraduate  
AI & Machine Learning Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star**.

Your support motivates future development.
