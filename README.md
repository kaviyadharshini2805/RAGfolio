# RAGfolio

<p align="center">
  <h3 align="center">AI Portfolio Assistant powered by Retrieval-Augmented Generation (RAG)</h3>
  <p align="center">
    Answer questions about your resume, skills, projects, education, and experience using semantic search and Large Language Models.
  </p>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-121212?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-412991?style=for-the-badge&logo=openai&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-5B4BDB?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

## Overview

RAGfolio is a Retrieval-Augmented Generation (RAG) application that serves as an AI-powered portfolio assistant.

Instead of relying solely on a language model's internal knowledge, the application retrieves relevant information from a personal knowledge base before generating responses. This enables accurate, context-aware answers about professional experience, technical skills, projects, education, and other portfolio information.

The project demonstrates a complete RAG pipeline using semantic search, vector embeddings, and Large Language Models.

---

## Features

- Retrieval-Augmented Generation (RAG)
- Semantic document search
- Personalized knowledge base
- OpenAI-powered response generation
- ChromaDB vector database
- Streamlit web interface
- Modular and extensible architecture
- Refreshable document indexing

---

## Architecture

```text
                    User Question
                          │
                          ▼
                 Generate Embedding
                          │
                          ▼
                ChromaDB Vector Search
                          │
                          ▼
              Retrieve Relevant Chunks
                          │
                          ▼
               Prompt Augmentation (RAG)
                          │
                          ▼
                  OpenAI Chat Model
                          │
                          ▼
                  Contextual Response
```

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
│   ├── resume.txt
│   ├── education.txt
│   ├── experience.txt
│   ├── projects.txt
│   └── skills.txt
│
├── src/
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── rag.py
│   ├── vectordb.py
│   └── __init__.py
│
├── tests/
│   ├── test_data_loading.py
│   └── test_setup.py
│
└── chroma_db/
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| LLM | OpenAI GPT |
| Embeddings | OpenAI Embeddings |
| Vector Database | ChromaDB |
| Frontend | Streamlit |
| Environment | python-dotenv |

---

## Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API Key

---

### Clone the Repository

```bash
git clone https://github.com/your-username/RAGfolio.git

cd RAGfolio
```

---

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

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key

CHAT_MODEL=gpt-4

EMBEDDING_MODEL=text-embedding-3-small

TEMPERATURE=0.2

MAX_TOKENS=500
```

---

## Knowledge Base

The chatbot retrieves information from the following documents.

```text
data/
├── resume.txt
├── education.txt
├── experience.txt
├── projects.txt
└── skills.txt
```

Simply edit these files and refresh the knowledge base from the application.

---

## Running the Application

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

Initialize the knowledge base before interacting with the chatbot.

---

## Example Queries

```text
What are your technical skills?

Tell me about your projects.

Describe your work experience.

What is your educational background?

Which technologies have you worked with?

Summarize your resume.

Have you worked on machine learning projects?

What programming languages do you know?
```

---

## RAG Pipeline

### Document Indexing

1. Load text documents
2. Split documents into chunks
3. Generate embeddings
4. Store embeddings in ChromaDB

### Query Processing

1. Convert user query into an embedding
2. Retrieve relevant document chunks
3. Build an augmented prompt
4. Generate a response using the language model

---

## Future Improvements

- PDF and DOCX support
- Local LLM integration
- Conversation memory
- Source citations
- Hybrid search
- Voice interface
- Authentication
- Docker support
- Cloud deployment

---

## License

This project is licensed under the MIT License.

---
