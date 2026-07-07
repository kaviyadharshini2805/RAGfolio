"""
RAG (Retrieval Augmented Generation) Module
Implements the RAG pipeline for question answering
"""
import os
from typing import List, Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.vectordb import VectorDBManager
from dotenv import load_dotenv

load_dotenv()


class RAGPipeline:
    """RAG pipeline for context-aware question answering"""
    
    def __init__(self, vectordb_manager: VectorDBManager, model: str = None, temperature: float = None):
        """
        Initialize the RAG pipeline
        
        Args:
            vectordb_manager: VectorDBManager instance
            model: Google Gemini model name
            temperature: Temperature for response generation
        """
        self.vectordb_manager = vectordb_manager
        self.model = model or os.getenv("CHAT_MODEL", "gemini-1.5-flash")
        self.temperature = temperature or float(os.getenv("TEMPERATURE", 0.7))
        
        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.temperature,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        # Create custom prompt template
        self.prompt_template = """You are a helpful AI assistant representing the person whose information is in the context below. 
Answer questions about their professional background, skills, experience, education, and projects in a natural and conversational way.

If you don't have enough information to answer a question, politely say so and suggest what information you do have that might be relevant.

Context: {context}

Question: {question}

Answer: """
        
        self.prompt = ChatPromptTemplate.from_template(self.prompt_template)
        
        # Initialize chain
        self.chain = None
        self._setup_chain()
    
    def _setup_chain(self):
        """Set up the RAG chain using LCEL (LangChain Expression Language)"""
        retriever = self.vectordb_manager.get_retriever(k=4)
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        # Create the chain using LCEL
        self.chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        
        self.retriever = retriever
    
    def query(self, question: str) -> Dict:
        """
        Query the RAG pipeline
        
        Args:
            question: User question
            
        Returns:
            Dictionary containing answer and source documents
        """
        if self.chain is None:
            raise ValueError("Chain not initialized")
        
        # Get answer
        answer = self.chain.invoke(question)
        
        # Get source documents separately
        source_docs = self.retriever.invoke(question)
        
        return {
            "answer": answer,
            "source_documents": source_docs
        }
    
    def get_relevant_context(self, question: str, k: int = 4) -> List[str]:
        """
        Get relevant context for a question without generating an answer
        
        Args:
            question: User question
            k: Number of context chunks to retrieve
            
        Returns:
            List of relevant context strings
        """
        docs = self.vectordb_manager.similarity_search(question, k=k)
        return [doc.page_content for doc in docs]
