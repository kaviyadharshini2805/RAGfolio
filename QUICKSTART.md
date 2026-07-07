# Quick Start Guide

## Step-by-Step Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit (web interface)
- LangChain (RAG framework)
- ChromaDB (vector database)
- OpenAI (language model)
- Sentence Transformers (embeddings)

### 2. Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy your API key

### 3. Configure Environment

Edit the `.env` file:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx  # Replace with your actual key
```

### 4. Add Your Resume Information

Update these files with your information:

**resume.txt**
```
Add your name, contact info, and professional summary
```

**data/skills.txt**
```
List your technical and soft skills
```

**data/experience.txt**
```
Add your work experience with details
```

**data/projects.txt**
```
Describe projects you've worked on
```

**data/education.txt**
```
Add your educational background
```

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### 6. Test the Chatbot

Try asking questions like:
- "What are your main skills?"
- "Tell me about your experience"
- "What projects have you worked on?"

## Troubleshooting

**Problem**: API key error
**Solution**: Make sure your OpenAI API key is correctly set in `.env`

**Problem**: No documents loaded
**Solution**: Add content to the resume files before running

**Problem**: Module not found
**Solution**: Run `pip install -r requirements.txt`

## Next Steps

1. Customize the resume data with your information
2. Adjust the LLM settings in `.env` (temperature, model, etc.)
3. Test different types of questions
4. Deploy to Streamlit Cloud or other hosting services

## Cost Estimate

Using GPT-3.5-turbo:
- Embedding generation: Free (local model)
- Chat queries: ~$0.001-0.002 per conversation
- 100 questions ≈ $0.10-0.20

## Support

For issues or questions, refer to:
- README.md for detailed documentation
- LangChain docs: https://python.langchain.com/
- Streamlit docs: https://docs.streamlit.io/
