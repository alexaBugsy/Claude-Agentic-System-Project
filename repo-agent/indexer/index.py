import os
import chromedb
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromeVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings 
from indexer.loader import load_repo
from dotenv import load_dotenv 

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "./storage")
REPO_PATH = os.getenv("REPO_PATH", "./my_repo")
MODEL_NAME = os.getenv("MODEL_NAME", "codellama")

def build_index(): 
    """
    loads repo, embeds all files, and saves the index to ChromaDB 
    must be ran once before using the agent
    """
    # use Ollama to generate embedding locally (no API cost)
    Settings.embed_model = OllamaEmbedding(model_name = MODEL_NAME)

    # load all code files from the repo
    documents = load_repo(REPO_PATH)

    # set up ChromeDB as the vector store
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection("repo_index")
    vector_store = ChromaVectorStore(chroma_collection = chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # to build and save the index 
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
    call this on subsequent runs instead of rebuild_index() 
    """
    Settings.embed_model = OllamaEmbedding(model_name = MODEL_NAME)

    chroma_client = chromadb.PersistentClient(path = CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection("repo_index")
    vector_store = ChromaVectorStore(chroma_collection = chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store= vector_store)

    index = VectorStoreIndex.from_vector_store(
        vector_store, 
        storage_context = storage_context
    )

    print("Index loaded from storage.")
    return index 
