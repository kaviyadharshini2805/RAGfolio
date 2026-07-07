"""
Personal AI Chatbot Application
Main entry point for the chatbot with Streamlit interface
"""
import streamlit as st
from src.chatbot import PersonalChatbot
from src.loader import DataLoader
from src.embeddings import EmbeddingManager
from src.vectordb import VectorDBManager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = None
    st.session_state.chat_history = []
    st.session_state.vectordb_initialized = False

# Sidebar
with st.sidebar:
    st.title("🤖 Personal AI Assistant")
    st.markdown("---")
    
    if st.button("Initialize/Refresh Knowledge Base"):
        with st.spinner("Loading and processing documents..."):
            try:
                # Initialize components
                loader = DataLoader()
                embedding_manager = EmbeddingManager()
                vectordb_manager = VectorDBManager()
                
                # Load documents
                documents = loader.load_all_documents()
                st.success(f"Loaded {len(documents)} documents")
                
                # Create embeddings and store in vector database
                vectordb_manager.create_or_update_vectordb(documents, embedding_manager)
                st.session_state.vectordb_initialized = True
                
                # Initialize chatbot
                st.session_state.chatbot = PersonalChatbot(vectordb_manager, embedding_manager)
                st.success("Knowledge base initialized!")
                
            except Exception as e:
                st.error(f"Error initializing knowledge base: {str(e)}")
    
    st.markdown("---")
    st.markdown("### About")
    st.info("This chatbot uses RAG (Retrieval Augmented Generation) to answer questions about your professional background.")
    
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# Main chat interface
st.title("💬 Chat with Your AI Assistant")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about my background..."):
    if not st.session_state.vectordb_initialized:
        st.warning("Please initialize the knowledge base first using the sidebar button.")
    else:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get chatbot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.chatbot.get_response(prompt)
                    st.markdown(response)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"Error generating response: {str(e)}"
                    st.error(error_msg)
                    st.session_state.chat_history.append({"role": "assistant", "content": error_msg})

# Display status in sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### Status")
    if st.session_state.vectordb_initialized:
        st.success("✅ Knowledge Base Ready")
    else:
        st.warning("⚠️ Knowledge Base Not Initialized")
