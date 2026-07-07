"""
Test script to verify data loading and see what content is being read
"""
from src.loader import DataLoader
import os

print("=" * 80)
print("DATA LOADING TEST")
print("=" * 80)

# Initialize loader
loader = DataLoader(data_dir="data")

# Check what files exist
print("\n1. Checking file existence:")
print("-" * 80)

files_to_check = [
    "resume.txt",
    "data/projects.txt",
    "data/skills.txt",
    "data/experience.txt",
    "data/education.txt"
]

for file_path in files_to_check:
    exists = os.path.exists(file_path)
    print(f"  {file_path}: {'✓ EXISTS' if exists else '✗ NOT FOUND'}")

# Load all documents
print("\n2. Loading all documents:")
print("-" * 80)

documents = loader.load_all_documents()
print(f"  Total documents (chunks) loaded: {len(documents)}")

# Show sample from projects
print("\n3. Sample content from projects.txt:")
print("-" * 80)

project_docs = [doc for doc in documents if 'projects.txt' in doc.metadata['source']]
if project_docs:
    print(f"  Found {len(project_docs)} chunks from projects.txt")
    print(f"\n  First chunk preview (first 500 chars):")
    print(f"  {project_docs[0].page_content[:500]}")
    
    # Check for placeholders
    has_placeholder = any('[Project Name]' in doc.page_content or '[Brief description' in doc.page_content 
                          for doc in project_docs)
    
    if has_placeholder:
        print("\n  ⚠️  WARNING: Placeholder text detected in projects.txt!")
    else:
        print("\n  ✓ No placeholder text found - data looks good!")
else:
    print("  ✗ No project documents found!")

# Show sample from skills
print("\n4. Sample content from skills.txt:")
print("-" * 80)

skill_docs = [doc for doc in documents if 'skills.txt' in doc.metadata['source']]
if skill_docs:
    print(f"  Found {len(skill_docs)} chunks from skills.txt")
    
    # Check for Java
    java_mentioned = any('Java' in doc.page_content for doc in skill_docs)
    print(f"  Java mentioned: {'✓ YES' if java_mentioned else '✗ NO'}")
    
    # Check for Python
    python_mentioned = any('Python' in doc.page_content for doc in skill_docs)
    print(f"  Python mentioned: {'✓ YES' if python_mentioned else '✗ NO'}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
print("\nIf you see placeholder warnings, the data files need to be updated.")
print("After updating files, restart Streamlit and click 'Initialize/Refresh Knowledge Base'")
print("=" * 80)
