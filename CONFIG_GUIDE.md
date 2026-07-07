# Configuration Guide

Complete guide to configuring your Personal AI Chatbot.

## Environment Variables (.env)

### Required Settings

```env
# Your OpenAI API Key (REQUIRED)
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

Get your API key from: https://platform.openai.com/api-keys

### Optional Settings

```env
# Embedding Model (Default: all-MiniLM-L6-v2)
EMBEDDING_MODEL=all-MiniLM-L6-v2

# ChromaDB Storage Location (Default: ./chroma_db)
CHROMA_PERSIST_DIRECTORY=./chroma_db

# Language Model (Default: gpt-3.5-turbo)
LLM_MODEL=gpt-3.5-turbo

# Response Creativity (0.0-1.0, Default: 0.7)
LLM_TEMPERATURE=0.7

# Maximum Response Length (Default: 500)
MAX_TOKENS=500
```

## Embedding Model Options

Choose based on your needs:

### Fast & Lightweight (Recommended for most users)
```env
EMBEDDING_MODEL=all-MiniLM-L6-v2
```
- Dimension: 384
- Speed: Very fast
- Quality: Good
- Best for: General use, quick responses

### High Quality
```env
EMBEDDING_MODEL=all-mpnet-base-v2
```
- Dimension: 768
- Speed: Moderate
- Quality: Excellent
- Best for: When accuracy is critical

### Multilingual
```env
EMBEDDING_MODEL=paraphrase-multilingual-MiniLM-L12-v2
```
- Dimension: 384
- Languages: 50+
- Best for: Non-English resumes

### Large & Powerful
```env
EMBEDDING_MODEL=all-roberta-large-v1
```
- Dimension: 1024
- Speed: Slower
- Quality: Best
- Best for: Maximum accuracy, powerful hardware

## Language Model Options

### GPT-3.5 Turbo (Default - Recommended)
```env
LLM_MODEL=gpt-3.5-turbo
```
- Cost: $0.001/1K tokens (input), $0.002/1K tokens (output)
- Speed: Fast
- Quality: Very good
- Best for: Most users, cost-effective

### GPT-4 Turbo
```env
LLM_MODEL=gpt-4-turbo-preview
```
- Cost: $0.01/1K tokens (input), $0.03/1K tokens (output)
- Speed: Fast
- Quality: Excellent
- Best for: Complex queries, highest quality

### GPT-4
```env
LLM_MODEL=gpt-4
```
- Cost: $0.03/1K tokens (input), $0.06/1K tokens (output)
- Speed: Moderate
- Quality: Best
- Best for: Maximum capability

## Temperature Settings

Controls response creativity and randomness:

### Deterministic (0.0-0.3)
```env
LLM_TEMPERATURE=0.2
```
- More focused and consistent
- Best for: Factual resume information
- Example: Technical skills, dates, facts

### Balanced (0.4-0.7) - Recommended
```env
LLM_TEMPERATURE=0.7
```
- Good mix of accuracy and natural conversation
- Best for: General chatbot use
- Example: Answering varied questions naturally

### Creative (0.8-1.0)
```env
LLM_TEMPERATURE=0.9
```
- More varied and creative responses
- Best for: Brainstorming, cover letters
- Example: Generating unique descriptions

## Token Limits

Maximum length of responses:

### Short & Concise
```env
MAX_TOKENS=300
```
- Quick, to-the-point answers
- Lower cost
- Best for: Simple Q&A

### Medium (Recommended)
```env
MAX_TOKENS=500
```
- Balanced length
- Good detail without rambling
- Best for: Most conversations

### Long & Detailed
```env
MAX_TOKENS=1000
```
- Comprehensive responses
- Higher cost
- Best for: Complex explanations

## Cost Optimization

### Budget-Friendly Setup
```env
LLM_MODEL=gpt-3.5-turbo
LLM_TEMPERATURE=0.5
MAX_TOKENS=400
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

**Estimated cost**: ~$0.10 per 100 conversations

### High-Quality Setup
```env
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.7
MAX_TOKENS=600
EMBEDDING_MODEL=all-mpnet-base-v2
```

**Estimated cost**: ~$1.50 per 100 conversations

### Balanced Setup (Recommended)
```env
LLM_MODEL=gpt-3.5-turbo
LLM_TEMPERATURE=0.7
MAX_TOKENS=500
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

**Estimated cost**: ~$0.15 per 100 conversations

## Advanced Configuration

### Changing Chunk Size

Edit `src/vectordb.py`, line ~30:

```python
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Increase for longer context
    chunk_overlap=50,    # Increase for more context continuity
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)
```

**Guidelines:**
- `chunk_size`: 300-1000 (smaller = more precise, larger = more context)
- `chunk_overlap`: 10-20% of chunk_size

### Changing Retrieval Count

Edit `src/rag.py`, line ~60:

```python
retriever=self.vectordb.get_retriever(k=4)  # Number of chunks to retrieve
```

**Guidelines:**
- `k=2`: Fast, minimal context
- `k=4`: Balanced (recommended)
- `k=6-8`: More context, slower

### Custom System Prompt

Edit `src/rag.py`, line ~50:

```python
template = """You are a helpful AI assistant representing the person whose resume...

[Customize this prompt to change chatbot personality and behavior]

Context: {context}
Question: {question}
Answer: """
```

## Testing Your Configuration

Run the test script:

```bash
python test_setup.py
```

This will verify:
- ✓ All packages installed
- ✓ Environment configured
- ✓ Data files present
- ✓ Modules working

## Troubleshooting

### API Key Issues

**Error**: `AuthenticationError: Invalid API key`
- Verify your key starts with `sk-`
- Check for extra spaces or quotes
- Ensure key is active on OpenAI platform

### Memory Issues

**Error**: `Out of memory` or slow performance
- Use smaller embedding model
- Reduce chunk_size
- Reduce retrieval count (k)

### Quality Issues

**Problem**: Responses not accurate
- Increase retrieval count (k)
- Use better embedding model
- Add more detail to resume files
- Lower temperature for more factual responses

**Problem**: Responses too generic
- Add more specific details to resume files
- Customize system prompt
- Increase chunk_size for more context

## Performance Benchmarks

### Response Time

| Model | Avg Time | Cost/Query |
|-------|----------|------------|
| GPT-3.5 | 1-2s | $0.001 |
| GPT-4 Turbo | 2-4s | $0.015 |
| GPT-4 | 3-5s | $0.045 |

### Embedding Models

| Model | Load Time | Embed Time | Size |
|-------|-----------|------------|------|
| MiniLM-L6 | 1-2s | <0.1s | 80MB |
| MPNet-base | 2-3s | ~0.2s | 420MB |
| RoBERTa-large | 3-5s | ~0.5s | 1.4GB |

## Recommended Configurations by Use Case

### Job Application / Portfolio
```env
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.6
MAX_TOKENS=600
```
Professional, detailed, high quality

### Quick Demo / Testing
```env
LLM_MODEL=gpt-3.5-turbo
LLM_TEMPERATURE=0.7
MAX_TOKENS=400
```
Fast, affordable, good enough

### Non-English Resume
```env
EMBEDDING_MODEL=paraphrase-multilingual-MiniLM-L12-v2
LLM_MODEL=gpt-3.5-turbo
```
Multilingual support

### Privacy-Conscious Setup
- Use local LLM (requires additional setup)
- Keep all data in local ChromaDB
- No API calls to external services
