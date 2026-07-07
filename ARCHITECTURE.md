# System Architecture

Visual guide to understanding how the Personal AI Chatbot works.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         USER                                 │
│                  (Web Browser / CLI)                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Question
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  STREAMLIT APP (app.py)                      │
│                   - UI Management                            │
│                   - Session State                            │
│                   - Display Logic                            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ ask(question)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 RAG CHATBOT (src/rag.py)                     │
│                   - Conversation Memory                      │
│                   - Query Processing                         │
│                   - Response Generation                      │
└────────┬───────────────────────────────────────────┬────────┘
         │                                           │
         │ similarity_search()                       │ generate()
         ▼                                           ▼
┌─────────────────────────┐             ┌───────────────────────┐
│   VECTOR DB             │             │   OPENAI GPT          │
│   (src/vectordb.py)     │             │   (Language Model)    │
│                         │             │                       │
│   - ChromaDB            │             │   - GPT-3.5/GPT-4     │
│   - Similarity Search   │             │   - Text Generation   │
│   - Document Retrieval  │             │   - Context Window    │
└────────┬────────────────┘             └───────────────────────┘
         │
         │ get_retriever()
         ▼
┌─────────────────────────┐
│   EMBEDDINGS            │
│   (src/embeddings.py)   │
│                         │
│   - Sentence Transform  │
│   - Vector Generation   │
│   - 384D Embeddings     │
└─────────────────────────┘
```

## Data Flow Diagram

### Initialization Phase

```
┌──────────────┐
│  Resume      │
│  Files       │
│  (.txt)      │
└──────┬───────┘
       │
       │ load_all_documents()
       ▼
┌──────────────────────────┐
│  Document Loader         │
│  (src/loader.py)         │
│                          │
│  - Read files            │
│  - Create Document objs  │
│  - Add metadata          │
└──────┬───────────────────┘
       │
       │ List[Document]
       ▼
┌──────────────────────────┐
│  Text Splitter           │
│  (in vectordb.py)        │
│                          │
│  - Chunk documents       │
│  - Overlap strategy      │
│  - 500 chars/chunk       │
└──────┬───────────────────┘
       │
       │ Split Documents
       ▼
┌──────────────────────────┐
│  Embedding Generator     │
│  (src/embeddings.py)     │
│                          │
│  - Sentence Transformer  │
│  - all-MiniLM-L6-v2      │
│  - 384D vectors          │
└──────┬───────────────────┘
       │
       │ Embeddings
       ▼
┌──────────────────────────┐
│  ChromaDB                │
│  (./chroma_db/)          │
│                          │
│  - Store vectors         │
│  - Persist to disk       │
│  - Index for search      │
└──────────────────────────┘
```

### Query Phase

```
┌──────────────┐
│   User       │
│   Question   │
└──────┬───────┘
       │
       │ "What are your skills?"
       ▼
┌───────────────────────────────────┐
│  RAG Chatbot                      │
│  (src/rag.py)                     │
│                                   │
│  Step 1: Embed Query              │
│  ├─ Query → Vector (384D)         │
│  │                                │
│  Step 2: Similarity Search        │
│  ├─ ChromaDB.search(vector)       │
│  ├─ Returns: Top 4 documents      │
│  │                                │
│  Step 3: Build Context            │
│  ├─ Combine: System Prompt        │
│  │          + Retrieved Docs      │
│  │          + User Question        │
│  │          + Chat History         │
│  │                                │
│  Step 4: Generate Response        │
│  ├─ Send to OpenAI GPT            │
│  ├─ Receive generated text        │
│  │                                │
│  Step 5: Update Memory            │
│  └─ Store Q&A in history          │
└──────┬────────────────────────────┘
       │
       │ {answer, sources, success}
       ▼
┌──────────────┐
│  Streamlit   │
│  Display     │
│              │
│  - Answer    │
│  - Sources   │
│  - History   │
└──────────────┘
```

## Component Interactions

```
app.py
  │
  ├─► Initialize
  │     │
  │     ├─► setup_vectorstore()
  │     │      │
  │     │      ├─► ResumeDataLoader.load_all_documents()
  │     │      │      └─► Read .txt files
  │     │      │
  │     │      ├─► EmbeddingGenerator()
  │     │      │      └─► Load sentence-transformer
  │     │      │
  │     │      └─► VectorDatabase.initialize()
  │     │             └─► Create ChromaDB collection
  │     │
  │     └─► RAGChatbot(vectordb)
  │            └─► Setup conversation chain
  │
  └─► Query Loop
        │
        ├─► Display chat history
        │
        ├─► Get user input
        │
        ├─► chatbot.ask(question)
        │      │
        │      ├─► Embed query
        │      ├─► Search vectors
        │      ├─► Retrieve documents
        │      ├─► Call OpenAI API
        │      └─► Update memory
        │
        └─► Display response + sources
```

## Module Dependencies

```
app.py
  └─► src/rag.py
        ├─► src/vectordb.py
        │     ├─► src/embeddings.py
        │     └─► src/loader.py
        └─► langchain
              ├─► ChatOpenAI
              ├─► ConversationalRetrievalChain
              └─► ConversationBufferMemory

src/chatbot.py
  └─► src/rag.py
        (same dependencies as above)
```

## Data Models

### Document Object

```python
Document {
    page_content: str,      # The actual text content
    metadata: {
        "source": str,      # Filename (e.g., "skills.txt")
        "type": str         # Document type (e.g., "skills")
    }
}
```

### Query Result

```python
{
    "answer": str,              # Generated response
    "source_documents": [       # Retrieved documents
        Document {...},
        Document {...},
        ...
    ],
    "success": bool,            # Operation status
    "error": str (optional)     # Error message if failed
}
```

### Embedding Vector

```python
# 384-dimensional float array
[0.123, -0.456, 0.789, ..., 0.321]  # 384 values
```

## Processing Pipeline

### Document Chunking Example

```
Original Resume (2000 chars)
        │
        ▼
Text Splitter (chunk_size=500, overlap=50)
        │
        ├─► Chunk 1: chars 0-500
        ├─► Chunk 2: chars 450-950    (50 char overlap)
        ├─► Chunk 3: chars 900-1400   (50 char overlap)
        └─► Chunk 4: chars 1350-1850  (50 char overlap)
```

### Similarity Search Process

```
User Query: "Python experience?"
        │
        ▼
Embedding: [0.12, -0.34, 0.56, ..., 0.78]
        │
        ▼
ChromaDB: Calculate cosine similarity with all vectors
        │
        ├─► Doc A: similarity = 0.92  ✓ High match
        ├─► Doc B: similarity = 0.87  ✓ High match
        ├─► Doc C: similarity = 0.81  ✓ High match
        ├─► Doc D: similarity = 0.79  ✓ High match
        ├─► Doc E: similarity = 0.45  ✗ Low match
        └─► Doc F: similarity = 0.32  ✗ Low match
        │
        ▼
Return: Top 4 documents (A, B, C, D)
```

### LLM Context Building

```
System Prompt
+──────────────────────────────────────────
| You are a helpful AI assistant representing
| the person whose resume you have access to.
| Answer professionally and conversationally.
+──────────────────────────────────────────

Retrieved Context
+──────────────────────────────────────────
| Doc 1: Python (Advanced) - 5 years
|        Django, FastAPI, Flask...
|
| Doc 2: Projects: Built AI chatbot using
|        Python and LangChain...
|
| Doc 3: Experience: Senior Developer at...
|        Python backend development...
+──────────────────────────────────────────

Conversation History
+──────────────────────────────────────────
| User: What languages do you know?
| AI: I'm proficient in Python, JavaScript...
+──────────────────────────────────────────

Current Question
+──────────────────────────────────────────
| User: Tell me about your Python experience
+──────────────────────────────────────────
        │
        ▼
    OpenAI GPT
        │
        ▼
Generated Response
```

## Performance Characteristics

### Latency Breakdown

```
Total Query Time: ~1.5 seconds
│
├─► Query Embedding:     ~0.1s  (6%)
├─► Vector Search:       ~0.05s (3%)
├─► LLM API Call:        ~1.2s  (80%)
└─► Post-processing:     ~0.15s (10%)
```

### Storage Requirements

```
Resume Data:        ~10 KB
Embeddings:         ~100 KB
ChromaDB Index:     ~500 KB
Sentence Model:     ~80 MB
Total:              ~81 MB
```

### API Call Costs

```
Per Query:
├─► Embedding:      $0 (local)
├─► Vector Search:  $0 (local)
└─► LLM Call:       ~$0.001 (GPT-3.5)

Per 100 Queries:    ~$0.10 (GPT-3.5)
Per 100 Queries:    ~$1.50 (GPT-4)
```

## Scaling Considerations

### Vertical Scaling (Single Machine)

```
Resume Size         ChromaDB     Response Time
─────────────────────────────────────────────
1-10 pages          < 1 MB       1-2 seconds
10-50 pages         < 5 MB       1-2 seconds
50-100 pages        < 10 MB      2-3 seconds
100-500 pages       < 50 MB      2-4 seconds
```

### Concurrent Users

```
Local Deployment:   1-5 users
Streamlit Cloud:    10-50 users
AWS/GCP:            50-1000+ users
```

## Error Handling Flow

```
User Query
    │
    ▼
┌─────────────────────────┐
│  Try: Process Query     │
└─────────┬───────────────┘
          │
          ├─► Success? → Return Response
          │
          └─► Error?
                │
                ├─► API Key Invalid
                │     └─► Show error message
                │
                ├─► Rate Limit Hit
                │     └─► Retry with backoff
                │
                ├─► Network Error
                │     └─► Show connection error
                │
                └─► Unknown Error
                      └─► Log & show generic error
```

## Security Architecture

```
┌──────────────────────────────────────────┐
│  Environment Variables (.env)             │
│  - OPENAI_API_KEY (sensitive)            │
│  - Config parameters (non-sensitive)     │
└──────────────┬───────────────────────────┘
               │
               ├─► .gitignore prevents commit
               └─► Load at runtime only

┌──────────────────────────────────────────┐
│  Resume Data (data/*.txt)                │
│  - Personal information                  │
│  - Professional details                  │
└──────────────┬───────────────────────────┘
               │
               ├─► Stored locally
               ├─► Not sent to OpenAI (only embeddings)
               └─► ChromaDB local persistence

┌──────────────────────────────────────────┐
│  API Communication                        │
│  - HTTPS only                            │
│  - API key in headers                    │
│  - Context + query sent to OpenAI       │
└──────────────────────────────────────────┘
```

---

This architecture provides:
- **Modularity**: Easy to modify components
- **Scalability**: Can handle growing data
- **Performance**: Fast response times
- **Reliability**: Error handling at each level
- **Security**: Protected credentials and data
