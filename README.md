# 🛢️ PetroGPT v6.0
### AI-Powered Petroleum Engineering Assistant using Google Gemini + RAG

<p align="center">

An intelligent AI assistant built specifically for **Petroleum Engineering** that combines **Large Language Models (LLMs)** with **Retrieval-Augmented Generation (RAG)** to answer both general petroleum engineering questions and questions from uploaded technical PDFs.

</p>

---

# 🚀 Live Demo

> **🔗 Streamlit Application**



*[(link.)](https://petrogpt-kbrbehhbrbjceebhxgqph2.streamlit.app/)*

---

# 📖 Overview

PetroGPT is an AI-powered assistant designed for Petroleum Engineering students, researchers, and professionals.

Unlike a general chatbot, PetroGPT provides two dedicated assistants:

### 🛢️ Petroleum AI Assistant

Provides instant answers to Petroleum Engineering questions using Google's Gemini model.

### 📄 PDF Research Assistant

Allows users to upload Petroleum Engineering PDFs and ask questions directly from the document using **Retrieval-Augmented Generation (RAG)**.

The project combines:

- Google Gemini
- FAISS Vector Database
- Sentence Transformers
- Semantic Search
- LangChain
- Streamlit

to create a specialized engineering assistant.

---

# ✨ Features

## 🛢️ Petroleum AI Assistant

- Instant Petroleum Engineering chatbot
- Conversation Memory
- New Chat
- Export Chat
- Fast responses
- Powered by Google Gemini

Topics include:

- Reservoir Engineering
- Drilling Engineering
- Production Engineering
- Well Logging
- Petrophysics
- Formation Evaluation
- Enhanced Oil Recovery
- Petroleum Economics
- Geology
- Geophysics

---

## 📄 PDF Research Assistant

- Upload Petroleum Engineering PDFs
- Automatic PDF text extraction
- Intelligent text chunking
- Semantic embeddings
- FAISS Vector Database
- Retrieval-Augmented Generation (RAG)
- AI-powered PDF Question Answering
- Upload Another PDF
- New Chat
- Export Chat

---

# 🧠 Architecture

```
                        PetroGPT

                    Home Interface
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼

 Petroleum AI Assistant         PDF Research Assistant

          │                             │
          ▼                             ▼

   Google Gemini                 Upload PDF

                                        │
                                        ▼

                              PDF Text Extraction

                                        │
                                        ▼

                                 Text Chunking

                                        │
                                        ▼

                             Sentence Embeddings

                                        │
                                        ▼

                             FAISS Vector Database

                                        │
                                        ▼

                              Semantic Retrieval

                                        │
                                        ▼

                               Google Gemini LLM

                                        │
                                        ▼

                                 Final AI Response
```

---

# 🛠️ Technology Stack

## Frontend

- Streamlit

## Programming Language

- Python

## Large Language Model

- Google Gemini 2.5 Flash

## Embedding Model

- all-MiniLM-L6-v2

## Vector Database

- FAISS

## RAG Framework

- LangChain

## PDF Processing

- PyPDF

---

# 📂 Project Structure

```
PetroGPT/

│
├── app.py
│
├── data/
│
├── petro_utils/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── pdf_reader.py
│   ├── retriever.py
│   └── vector_store.py
│
├── vector_db/
│
├── versions/
│   ├── v1.py
│   ├── v2.py
│   ├── v3.py
│   ├── v4.py
│   └── v5.py
│
├── requirements.txt
└── README.md
```

---

# 📈 Development Journey

PetroGPT was built incrementally through multiple versions.

| Version | Description |
|----------|-------------|
| **Version 1** | Initial Petroleum Engineering chatbot powered by Google Gemini. |
| **Version 2** | Introduced conversation memory, improved chat interface, and export functionality. |
| **Version 3** | Added PDF upload, document summarization, and key point extraction. |
| **Version 4** | Built the first Retrieval-Augmented Generation (RAG) pipeline using semantic embeddings and FAISS vector search. |
| **Version 5** | Improved retrieval accuracy, optimized indexing, modularized the architecture, and enhanced the UI. |
| **Version 6 (Current)** | Complete redesign featuring two independent assistants, optimized PDF workflow, Upload Another PDF functionality, Home navigation, faster responses, and an improved user experience. |

---

# 📚 How PetroGPT Works

## Petroleum Assistant

```
User Question

↓

Google Gemini

↓

Petroleum Engineering Answer
```

---

## PDF Assistant

```
Upload PDF

↓

Extract Text

↓

Split into Chunks

↓

Generate Embeddings

↓

Create FAISS Vector Database

↓

Retrieve Relevant Chunks

↓

Google Gemini

↓

Final Response
```

---

# ⚠️ Important Notes

## PDF Processing

When uploading a PDF for the first time, PetroGPT performs the following steps:

- Reads the PDF
- Extracts text
- Splits the document into semantic chunks
- Generates embeddings
- Creates a FAISS vector database

Depending on the size of the document, this process may take **5–7 minutes**.

The vector database is created **only once** for each uploaded PDF, preventing repeated indexing during the session.

---

## Asking Questions

For the best retrieval performance:

✅ Preferred

- Explain porosity
- Darcy's Law
- Relative permeability
- Formation evaluation
- Water saturation

❌ Less Effective

- Explain it
- Tell me more
- Continue
- What is it?

Using technical keywords significantly improves semantic retrieval quality.

---

## Conversation Awareness

The **Petroleum AI Assistant** supports conversational interactions.

The **PDF Research Assistant** treats each query independently and is **not conversation-aware** in the current version. Each question should clearly reference the desired topic.

---

## API Usage

PetroGPT uses the **Google Gemini API**.

If the application displays a quota-related message, it indicates that the free API request limit has been reached. Users should wait until the quota resets or use another valid Gemini API key.

---


# 🚀 Future Improvements

- Multi-PDF support
- Conversation-aware Retrieval
- Streaming responses
- Voice interaction
- Authentication system

---

# 👨‍💻 Author

**Sayan Das**

Undergraduate Student  
Department of Petroleum Engineering  
Indian Institute of Technology (ISM) Dhanbad

---
