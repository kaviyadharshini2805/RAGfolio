"""
Setup Test Script
Run this to verify your installation and configuration
"""

import os
import sys


def test_imports():
    """Test if all required packages are installed"""
    print("Testing package imports...")
    
    packages = {
        'streamlit': 'streamlit',
        'langchain': 'langchain',
        'chromadb': 'chromadb',
        'sentence_transformers': 'sentence-transformers',
        'openai': 'openai',
        'dotenv': 'python-dotenv'
    }
    
    missing = []
    for module, package in packages.items():
        try:
            __import__(module)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package}")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✓ All packages installed!\n")
    return True


def test_env_file():
    """Test if .env file is configured"""
    print("Testing environment configuration...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("  ✗ OPENAI_API_KEY not found in .env file")
        return False
    
    if api_key == 'your_openai_api_key_here':
        print("  ✗ OPENAI_API_KEY not configured (using placeholder)")
        print("\n⚠️  Please add your actual OpenAI API key to .env file")
        print("Get one at: https://platform.openai.com/api-keys")
        return False
    
    print(f"  ✓ OPENAI_API_KEY configured (starts with: {api_key[:10]}...)")
    print("\n✓ Environment configured!\n")
    return True


def test_data_files():
    """Test if resume data files exist and have content"""
    print("Testing resume data files...")
    
    files = [
        'resume.txt',
        'data/skills.txt',
        'data/experience.txt',
        'data/projects.txt',
        'data/education.txt'
    ]
    
    missing = []
    empty = []
    
    for filepath in files:
        if not os.path.exists(filepath):
            print(f"  ✗ {filepath} - Not found")
            missing.append(filepath)
        else:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    print(f"  ⚠️  {filepath} - Empty")
                    empty.append(filepath)
                elif '[' in content and ']' in content:
                    print(f"  ⚠️  {filepath} - Contains placeholders")
                    empty.append(filepath)
                else:
                    print(f"  ✓ {filepath}")
    
    if missing:
        print(f"\n⚠️  Missing files: {', '.join(missing)}")
        return False
    
    if empty:
        print(f"\n⚠️  Please fill in these files with your information:")
        for f in empty:
            print(f"    - {f}")
    else:
        print("\n✓ All data files ready!\n")
    
    return True


def test_project_structure():
    """Test if project structure is correct"""
    print("Testing project structure...")
    
    required_dirs = ['src', 'data']
    required_files = ['app.py', 'requirements.txt', '.env', 'README.md']
    
    all_good = True
    
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"  ✓ {dir_name}/")
        else:
            print(f"  ✗ {dir_name}/ - Missing")
            all_good = False
    
    for file_name in required_files:
        if os.path.isfile(file_name):
            print(f"  ✓ {file_name}")
        else:
            print(f"  ✗ {file_name} - Missing")
            all_good = False
    
    if all_good:
        print("\n✓ Project structure correct!\n")
    else:
        print("\n⚠️  Some files or directories are missing\n")
    
    return all_good


def test_modules():
    """Test if custom modules can be imported"""
    print("Testing custom modules...")
    
    try:
        from src.loader import ResumeDataLoader
        print("  ✓ src.loader")
    except Exception as e:
        print(f"  ✗ src.loader - {str(e)}")
        return False
    
    try:
        from src.embeddings import EmbeddingGenerator
        print("  ✓ src.embeddings")
    except Exception as e:
        print(f"  ✗ src.embeddings - {str(e)}")
        return False
    
    try:
        from src.vectordb import VectorDatabase
        print("  ✓ src.vectordb")
    except Exception as e:
        print(f"  ✗ src.vectordb - {str(e)}")
        return False
    
    print("\n✓ All modules can be imported!\n")
    return True


def main():
    """Run all tests"""
    print("="*60)
    print("Personal AI Chatbot - Setup Test")
    print("="*60)
    print()
    
    results = []
    
    results.append(("Package Installation", test_imports()))
    results.append(("Project Structure", test_project_structure()))
    results.append(("Environment Config", test_env_file()))
    results.append(("Resume Data Files", test_data_files()))
    results.append(("Custom Modules", test_modules()))
    
    print("="*60)
    print("Test Summary")
    print("="*60)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status} - {name}")
    
    all_passed = all(result[1] for result in results)
    
    print()
    if all_passed:
        print("🎉 All tests passed! You're ready to run the application.")
        print("\nRun the application with:")
        print("  streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("\nFor help, check:")
        print("  - README.md for detailed documentation")
        print("  - QUICKSTART.md for step-by-step guide")
    print()


if __name__ == "__main__":
    main()
