import os
import chromadb
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings 
from indexer.loader import load_repo
from dotenv import load_dotenv 

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "./storage")
MODEL_NAME = os.getenv("MODEL_NAME", "codellama")

def build_index(repo_path: str): 
    """
    Loads repo, embeds all files, & saves the index to ChromaDB 
    """
    Settings.embed_model = OllamaEmbedding(model_name = MODEL_NAME)

    documents = load_repo(repo_path)

    chroma_client = chromadb.PersistentClient(path = CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection("repo_index")
    vector_store = ChromaVectorStore(chroma_collection = chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store = vector_store)

    index = VectorStoreIndex.from_documents(
        documents, 
        storage_context = storage_context, 
        show_progress = True
    )

    print(f"Index built and saved to {CHROMA_PATH}")
    return index 

def load_index(): 
    """
    loads an existing index from ChromaDB 
    """
    Settings.embed_model = OllamaEmbedding(model_name = MODEL_NAME)

    chroma_client = chromadb.PersistentClient(path = CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection("repo_index")
    vector_store = ChromaVectorStore(chroma_collection = chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store = vector_store)

    index = VectorStoreIndex.from_vector_store(
        vector_store, 
        storage_context = storage_context
    )

    print("Index loaded from storage.")
    return index
