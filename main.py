import os 
import sys 
from dotenv import load_dotenv 

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "./storage")

def main(): 
    # fresh index or load existing one 
    if not os.path.exists(CHROMA_PATH) or not os.listdir(CHROMA_PATH): 
        print("No existing index found. Building index from repo...")
        from indexer.index import build_index 
        index = build_index()
    else: 
        print("Loading existing index from storage...")
        from indexer.index import load_index
        index = load_index()

    # chat engine
    from agent.agent import build_chat_engine 
    chat_engine = build_chat_engine(index)

    print("\nRepo agent ready. Type your questions or 'quit' to exit.\n")

    # chat loop 
    while True: 
        try: 
            query = input("You: ").strip()
        except (KeyboardInterrupt, EOFError): 
            print("\nExiting.")
            break 

        if not query: 
            continue
        if query.lower() in ("quit", "exit"):
            print("Exiting.")
            break 

        response = chat_engine.chat(query)
        print(f"\nAgent: {response}\n")


if __name__ == "__main__": 
    main()
          
          



