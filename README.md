# Personal AI Chatbot with RAG

A personal AI chatbot powered by Retrieval Augmented Generation (RAG) that answers questions about your professional background, skills, experience, and projects.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI's GPT models for natural language understanding
- 📚 **RAG Architecture**: Retrieves relevant context from your documents before generating responses
- 💾 **Vector Database**: ChromaDB for efficient similarity search
- 🎨 **Modern UI**: Clean Streamlit interface for easy interaction
- 📝 **Document Management**: Easily update your information by editing text files

## Architecture

The chatbot uses a RAG (Retrieval Augmented Generation) pipeline:

1. **Document Loading**: Text files are loaded and split into chunks
2. **Embeddings**: Text chunks are converted to vector embeddings using OpenAI
3. **Vector Storage**: Embeddings are stored in ChromaDB for fast retrieval
4. **Query Processing**: User questions are embedded and similar chunks are retrieved
5. **Response Generation**: Retrieved context is passed to GPT to generate accurate answers

## Project Structure

```
personal-ai-chatbot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── resume.txt             # Your resume information
├── data/                  # Additional data files
│   ├── projects.txt       # Your projects
│   ├── skills.txt         # Your skills
│   ├── experience.txt     # Work experience
│   └── education.txt      # Educational background
├── chroma_db/             # Vector database (created automatically)
└── src/                   # Source code modules
    ├── loader.py          # Document loading and preprocessing
    ├── embeddings.py      # Embedding generation
    ├── vectordb.py        # Vector database operations
    ├── rag.py             # RAG pipeline implementation
    └── chatbot.py         # Main chatbot logic
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- OpenAI API key

### 2. Installation

```bash
# Clone or download this repository
cd personal-ai-chatbot

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

1. Open the `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

2. Customize your information by editing the text files:
   - `resume.txt` - Your resume and personal information
   - `data/projects.txt` - Your projects
   - `data/skills.txt` - Your technical and soft skills
   - `data/experience.txt` - Your work experience
   - `data/education.txt` - Your educational background

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

1. **Initialize Knowledge Base**: Click the "Initialize/Refresh Knowledge Base" button in the sidebar to load and process your documents

2. **Start Chatting**: Type questions in the chat input at the bottom of the page, such as:
   - "What are your main technical skills?"
   - "Tell me about your work experience"
   - "What projects have you worked on?"
   - "What is your educational background?"

3. **Refresh Data**: After updating any text files, click "Initialize/Refresh Knowledge Base" again to reload the data

4. **Clear History**: Use the "Clear Chat History" button to start a fresh conversation

## Customization

### Modify Data Files

Simply edit the `.txt` files in the root directory and `data/` folder with your information. Use markdown formatting for better structure.

### Adjust Model Parameters

Edit the `.env` file to change:
- `CHAT_MODEL`: GPT model to use (e.g., "gpt-4", "gpt-3.5-turbo")
- `EMBEDDING_MODEL`: Embedding model (default: "text-embedding-ada-002")
- `TEMPERATURE`: Response creativity (0.0 = focused, 1.0 = creative)
- `MAX_TOKENS`: Maximum response length

### Customize Prompts

Edit `src/rag.py` to modify the system prompt and change how the chatbot responds.

## How It Works

### Document Processing

1. Documents are loaded from text files
2. Text is split into overlapping chunks (1000 characters with 200 overlap)
3. Each chunk is converted to a vector embedding
4. Embeddings are stored in ChromaDB with metadata

### Question Answering

1. User question is converted to an embedding
2. Most similar document chunks are retrieved from ChromaDB
3. Retrieved context is combined with the question
4. GPT generates a response based on the context
5. Response is displayed in the chat interface

## Technologies Used

- **LangChain**: Framework for building LLM applications
- **OpenAI**: GPT models and embeddings
- **ChromaDB**: Vector database for embeddings
- **Streamlit**: Web interface
- **Python**: Core programming language

## Troubleshooting

### "OpenAI API key not found"
Make sure you've set your API key in the `.env` file

### "Knowledge base not initialized"
Click the "Initialize/Refresh Knowledge Base" button in the sidebar

### Empty or irrelevant responses
- Check that your text files contain sufficient information
- Try rephrasing your question
- Refresh the knowledge base after updating files

## Future Enhancements

- [ ] Support for PDF and DOCX files
- [ ] Multi-modal support (images, code)
- [ ] Conversation memory and context
- [ ] Export chat history
- [ ] Advanced analytics dashboard
- [ ] Multiple language support

## License

This project is open source and available for personal use.

## Contributing

Feel free to fork this project and customize it for your needs. Contributions and improvements are welcome!

## Contact

For questions or suggestions, please refer to the contact information in your `resume.txt` file.
