# RAGfolio

<p align="center">
  <h3 align="center">AI Portfolio Assistant powered by Retrieval-Augmented Generation (RAG)</h3>
  <p align="center">
    Answer questions about a professional profile using semantic search, vector embeddings, and Google Gemini.
  </p>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented--Generation-2563EB?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![ChromaDB](https://img.shields.io/badge/ChromaDB-5B4BDB?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</p>

---

## Overview

RAGfolio is an AI-powered portfolio assistant built using Retrieval-Augmented Generation (RAG). It answers natural language questions about a professional profile—including skills, projects, work experience, education, certifications, and achievements—by retrieving relevant information from a personalized knowledge base.

Instead of relying solely on a language model's pretrained knowledge, RAGfolio performs semantic search over indexed documents, retrieves the most relevant information, and uses Google Gemini to generate accurate, context-aware responses.

This project demonstrates the implementation of a production-style RAG pipeline using LangChain, Hugging Face embeddings, ChromaDB, and Google Gemini.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic search over portfolio documents
* Context-aware responses using Google Gemini
* Hugging Face sentence embeddings
* ChromaDB vector database
* Interactive Streamlit interface
* Modular and extensible architecture
* Refreshable knowledge base

---

## Architecture

```text
                    User Question
                          │
                          ▼
              Generate Query Embedding
                          │
                          ▼
               ChromaDB Vector Search
                          │
                          ▼
           Retrieve Relevant Documents
                          │
                          ▼
            Prompt Augmentation (RAG)
                          │
                          ▼
                  Google Gemini
                          │
                          ▼
                  Generated Response
```

---

## Technology Stack

| Category        | Technology                                              |
| --------------- | ------------------------------------------------------- |
| Language        | Python                                                  |
| Framework       | LangChain                                               |
| LLM             | Google Gemini                                           |
| Embeddings      | Hugging Face (`all-MiniLM-L6-v2`)                       |
| Vector Database | ChromaDB                                                |
| Frontend        | Streamlit                                               |
| Environment     | python-dotenv                                           |

---

## Project Structure

```text
RAGfolio/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── data/
│   ├── education.txt
│   ├── experience.txt
│   ├── projects.txt
│   └── skills.txt
│
├── src/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── rag.py
│   └── vectordb.py
│
├── tests/
│   ├── test_setup.py
│   └── test_data_loading.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CHECKLIST.md
│   ├── CONFIG_GUIDE.md
│   ├── EXAMPLE_DATA.md
│   ├── PROJECT_SUMMARY.md
│   └── QUICKSTART.md
│
└── chroma_db/ 
```

---

## Getting Started

### Prerequisites

* Python 3.10 or later
* Google AI Studio API Key

### Clone the Repository

```bash
git clone https://github.com/<kaviyadharshini2805>/RAGfolio.git

cd RAGfolio
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key

MODEL_NAME=gemini-2.5-flash

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

---

## Knowledge Base

RAGfolio retrieves information from text documents stored in the `data/` directory.

```text
data/
├── education.txt
├── experience.txt
├── projects.txt
└── skills.txt
```

Update these files with your latest information and refresh the knowledge base from the application to rebuild the vector index.

---

## Running the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

Initialize or refresh the knowledge base from the sidebar before interacting with the chatbot.

---

## Example Questions

```text
Tell me about your projects.

What programming languages do you know?

Describe your technical skills.

What is your educational background?

Summarize your work experience.

Have you built any machine learning projects?

Which frameworks have you worked with?

What certifications do you have?
```

---

## How It Works

### Document Indexing

1. Load portfolio documents.
2. Split documents into overlapping chunks.
3. Generate embeddings using Hugging Face (`all-MiniLM-L6-v2`).
4. Store embeddings in ChromaDB.

### Query Processing

1. Convert the user's question into a vector embedding.
2. Retrieve the most relevant document chunks from ChromaDB.
3. Construct a Retrieval-Augmented prompt.
4. Generate a response using Google Gemini.

---

## Future Improvements

* PDF and DOCX document support
* Conversation memory
* Source citations for retrieved documents
* Resume upload interface
* Voice interaction
* Docker support
* Cloud deployment
* Authentication and user management
* Hybrid keyword and semantic search

---

## License

This project is licensed under the MIT License.
