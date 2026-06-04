import os 
from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama 
from llama_index.core import Settings 
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import CondensePlusContextEngine 
from agent.prompts import SYSTEM_PROMPT
from dotenv import load_dotnev 

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "codellama")

def build_chat_engine(index: VectorStoreIndex): 
    """
    chat engine that remembers conversation history 
    queries repo index on each message 
    """
    llm = Ollama(model=MODEL_NAME, request_timeout=120.0)
    Settings.llm = llm

    memory = ChatMemoryBuffer.from_defaults(token_limit=4000)

    chat_engine = index.as_chat_engine(
        chat_mode="condense_plus_context", 
        memory=memory, 
        system_prompt=SYSTEM_PROMPT, 
        verbose=True
    )

    return chat_engine 

def run_query(query: str, index: VectorStoreIndex) -> str:
    """
    one-shot query against the index - no conversation history 
    good for single questions 
    """
    llm = Ollama(model=MODEL_NAME, request_timeout=120.0)
    Settings.llm = llm

    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return str(response)