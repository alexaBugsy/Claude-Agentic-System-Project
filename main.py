import os 
import sys 
import shutil
import tempfile
from dotenv import load_dotenv 

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "./storage")

def is_github_url(path: str) -> str: 
    return path.startswith("https://github.com") or path.startswith("http://github.com")

def clone_repo(github_url: str) -> str: 
    """ Clones a GitHub repo into a temp folder and returns the path. """
    import git 

    # to pull repo name from URL for display
    repo_name = github_url.rstrip("/").split("/")[-1].replace("git", "")
    temp_dir = tempfile.mktemp(prefix=f"repo-agent-{repo_name}-")

    print(f"Cloning {repo_name} from GitHub...")
    git.Repo.clone_from(github_url, temp_dir)
    print(f"Cloned to {temp_dir}")

    return temp_dir, repo_name 


def main(): 
    # to check if a GitHub URL or local path was passed as an argument 
    if len(sys.argv) < 2:
        print("Usage:")
        print("  py -3.11 main.py https://github.com/user/repo")
        print("  py -3.11 main.py C:\\path\\to\\local\\repo")
        sys.exit(1)

    input_path = sys.argv[1]
    temp_dir = None 

    # to handle GitHub URL 
    if is_github_url(input_path): 
        temp_dir, repo_name = clone_repo(input_path)
        repo_path = temp_dir
    else: 
        # local path
        if not os.path.exists(input_path): 
            print(f"Error: Path not found: {input_path}") 
            sys.exit(1)
        repo_path = input_path 
        repo_name = os.path.basename(input_path.rstrip("/\\"))

    print(f"\nAnalyzing repo: {repo_name}")

    # always have to rebuild index for a new repo 
    clear_storage()
    print("Building index from repo files...")
    from indexer.index import build_index
    index = build_chat_engine(index)

    print(f"\nRepo agent ready for '{repo_name}'. Type your question or 'quit' to exit.\n")

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

    # to clean up cloned repo from temp folder 
    if temp_dir and os.path.exists(temp_dir): 
        shutil.rmtree(temp_dir)
        print("Cleaned up cloned repo.")


if __name__ == "__main__": 
    main()

    