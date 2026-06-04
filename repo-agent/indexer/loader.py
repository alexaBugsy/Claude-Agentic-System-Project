import os 
from llama_index.core import SimpleDirectoryReader

SUPPORTED_EXTENSIONS = [
    ".py", ".js", ".ts", ".jsx", ".tsx", 
    ".java", ".go", ".rs", ".cpp", ".c", 
    ".md", ".txt", ".yaml", ".yml", ".json"
]

def load_repo(repo_path: str): 
    """
    loads all supported code files 
    returns a list of Document objects from LlamaIndex to index 
    """
    if not os.path.exists(repo_path): 
        raise FileNotFoundError(f"Repo path not found: {repo_path}")
    
    reader = SimpleDirectoryReader(
        input_dir = repo_path, 
        recursive = True, 
        required_exts =SUPPORTED_EXTENSIONS, 
        exclude = ["*.pyc", "__pycache__", ".git", "node_modules"]
    )

    documents = reader.load_data()
    print(f"Loaded {len(documents)} files from {repo_path}")
    return documents 