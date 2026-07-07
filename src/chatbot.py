"""
Chatbot Module
Main chatbot interface combining all components
"""
from typing import Dict, List
from src.vectordb import VectorDBManager
from src.embeddings import EmbeddingManager
from src.rag import RAGPipeline


class PersonalChatbot:
    """Personal AI Chatbot with RAG capabilities"""
    
    def __init__(self, vectordb_manager: VectorDBManager, embedding_manager: EmbeddingManager):
        """
        Initialize the chatbot
        
        Args:
            vectordb_manager: VectorDBManager instance
            embedding_manager: EmbeddingManager instance
        """
        self.vectordb_manager = vectordb_manager
        self.embedding_manager = embedding_manager
        self.rag_pipeline = RAGPipeline(vectordb_manager)
        self.conversation_history = []
    
    def get_response(self, user_input: str) -> str:
        """
        Get chatbot response to user input
        
        Args:
            user_input: User's question or message
            
        Returns:
            Chatbot's response
        """
        # Store user input in history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Get response from RAG pipeline
        result = self.rag_pipeline.query(user_input)
        response = result["answer"]
        
        # Store response in history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def get_response_with_sources(self, user_input: str) -> Dict:
        """
        Get chatbot response along with source documents
        
        Args:
            user_input: User's question or message
            
        Returns:
            Dictionary with response and sources
        """
        result = self.rag_pipeline.query(user_input)
        
        # Store in history
        self.conversation_history.append({"role": "user", "content": user_input})
        self.conversation_history.append({"role": "assistant", "content": result["answer"]})
        
        return {
            "response": result["answer"],
            "sources": [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]
        }
    
    def get_conversation_history(self) -> List[Dict]:
        """Get the conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
    
    def get_relevant_context(self, query: str, k: int = 4) -> List[str]:
        """
        Get relevant context chunks for a query
        
        Args:
            query: User query
            k: Number of chunks to retrieve
            
        Returns:
            List of relevant context strings
        """
        return self.rag_pipeline.get_relevant_context(query, k=k)
