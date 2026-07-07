"""
Document Loader Module
Handles loading and preprocessing of text documents
"""
import os
from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DataLoader:
    """Load and process documents from various sources"""
    
    def __init__(self, data_dir: str = "data", chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the data loader
        
        Args:
            data_dir: Directory containing data files
            chunk_size: Size of text chunks for splitting
            chunk_overlap: Overlap between chunks
        """
        self.data_dir = data_dir
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    def load_text_file(self, file_path: str) -> List[Document]:
        """
        Load a single text file
        
        Args:
            file_path: Path to the text file
            
        Returns:
            List of Document objects
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create document with metadata
            doc = Document(
                page_content=content,
                metadata={"source": file_path, "filename": os.path.basename(file_path)}
            )
            
            # Split into chunks
            chunks = self.text_splitter.split_documents([doc])
            return chunks
            
        except Exception as e:
            print(f"Error loading {file_path}: {str(e)}")
            return []
    
    def load_all_documents(self) -> List[Document]:
        """
        Load all documents from data directory and root
        
        Returns:
            List of all Document objects
        """
        all_documents = []
        
        # Load resume.txt from root
        resume_path = "resume.txt"
        if os.path.exists(resume_path):
            all_documents.extend(self.load_text_file(resume_path))
        
        # Load all files from data directory
        if os.path.exists(self.data_dir):
            for filename in os.listdir(self.data_dir):
                if filename.endswith('.txt'):
                    file_path = os.path.join(self.data_dir, filename)
                    all_documents.extend(self.load_text_file(file_path))
        
        return all_documents
    
    def get_document_count(self) -> int:
        """Get total number of documents loaded"""
        return len(self.load_all_documents())
