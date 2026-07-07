"""
Vector Database Module
Handles ChromaDB operations for storing and retrieving embeddings
"""
import os
from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from src.embeddings import EmbeddingManager
from dotenv import load_dotenv

load_dotenv()


class VectorDBManager:
    """Manage ChromaDB vector database operations"""
    
    def __init__(self, persist_directory: str = None):
        """
        Initialize the vector database manager
        
        Args:
            persist_directory: Directory to persist the database
        """
        self.persist_directory = persist_directory or os.getenv(
            "CHROMA_PERSIST_DIRECTORY", 
            "./chroma_db"
        )
        self.vectorstore = None
    
    def create_or_update_vectordb(self, documents: List[Document], embedding_manager: EmbeddingManager):
        """
        Create or update the vector database with documents
        
        Args:
            documents: List of Document objects to store
            embedding_manager: EmbeddingManager instance
        """
        embeddings = embedding_manager.get_embeddings_object()
        
        # Create vector store
        self.vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=self.persist_directory
        )
    
    def load_vectordb(self, embedding_manager: EmbeddingManager):
        """
        Load existing vector database
        
        Args:
            embedding_manager: EmbeddingManager instance
        """
        embeddings = embedding_manager.get_embeddings_object()
        
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=embeddings
        )
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """
        Perform similarity search on the vector database
        
        Args:
            query: Query string
            k: Number of results to return
            
        Returns:
            List of most similar documents
        """
        if self.vectorstore is None:
            raise ValueError("Vector store not initialized. Please load or create the database first.")
        
        return self.vectorstore.similarity_search(query, k=k)
    
    def get_retriever(self, k: int = 4):
        """
        Get a retriever object for the vector store
        
        Args:
            k: Number of documents to retrieve
            
        Returns:
            Retriever object
        """
        if self.vectorstore is None:
            raise ValueError("Vector store not initialized. Please load or create the database first.")
        
        return self.vectorstore.as_retriever(search_kwargs={"k": k})
