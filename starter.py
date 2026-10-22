import asyncio 
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama 
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings 
from llama_index.core.workflow import Context


# set global defaults for embedding and LLM 
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm= Ollama(
    model = "llama3.1", 
    request_timeout=360.0, 
    context_window = 8000, 
)

# define a simple calculator tool 
def multiply(a: float, b: float) -> float: 
    """ useful for multiplying two numbers """
    return a * b 

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

async def search_documents(query: str) -> str: 
    """ useful for answering natural language questions about the documents """
    response = FunctionAgent(
        tools = [multiply, search_documents], 
        llm = Settings.llm, 
        system_prompt = "You are a helpful assistant that can perform calculations and search through documents to answer questions.",
    )

# create an agent with both ends
agent = FunctionAgent(
    tools = [multiply, search_documents], 
    llm = Settings.llm, 
    system_prompt = "You are a helpful assistamt that can perform calculations and search through documents to answer questions.", 
)

async def main(): 
    # create context for chat history 
    ctx = Context(agent)
    # example: store user info in context 
    await agent.run("My name is Logan", ctx=ctx)
    # ask a question using both RAG and calculator 
    response = await agent.run("What did the author do in college? Also, what's 7 * 8", ctx=ctx)
    print(response)

if __name__ == "__main__": 
    asyncio.run(main())

# ----

import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

# Set global defaults to local models
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0, context_window=8000)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Example tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

# Load documents and create RAG tool
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

async def search_documents(query: str) -> str:
    response = await query_engine.aquery(query)
    return str(response)

# Create agent with tools
agent = FunctionAgent(
    tools=[multiply, search_documents],
    llm=Settings.llm,
    system_prompt="You are a helpful assistant that can perform calculations and search through documents."
)

async def main():
    response = await agent.run("What did the author do in college? Also, what's 7 * 8?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
