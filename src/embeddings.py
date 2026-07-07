"""
Embeddings Module
Handles text embedding generation using HuggingFace (free and local)
"""
import os
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


class EmbeddingManager:
    """Manage embeddings for text documents"""
    
    def __init__(self, model: str = None):
        """
        Initialize the embedding manager
        
        Args:
            model: HuggingFace embedding model name
        """
        self.model = model or os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple documents
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        return self.embeddings.embed_documents(texts)
    
    def embed_query(self, text: str) -> List[float]:
        """
        Generate embedding for a single query
        
        Args:
            text: Query text to embed
            
        Returns:
            Embedding vector
        """
        return self.embeddings.embed_query(text)
    
    def get_embeddings_object(self):
        """Return the underlying embeddings object for LangChain integration"""
        return self.embeddings
