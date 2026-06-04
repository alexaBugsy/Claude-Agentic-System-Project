import os 
from llama_index.core.tools import FunctionTool 

def read_file(file_path: str) -> str: 
    """ reads and returns full contents of a file in the repo. """
    if not os.path.exists(file_path): 
        return f"File not found: {file_path}"
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f: 
        return f.read()
    

def list_files(directory: str = ".") -> str: 
    """ lists all files in directory recursively """
    result = []
    for root, dirs, files in os.walk(directory): 
        # to skip hidden folders like .git
        dirs[:] = [d for d in dirs if not d.startswitch(".") and d != "node_modules"]
        for file in files: 
            result.append(os.path.join(root, file))
    return "\n".join(result) if result else "No files found."


def search_code(keyword: str, directory: str = ".") -> str: 
    """ searches all code files for a keyword and returns matching lines """
    matches = []
    for root, dirs, files in os.walk(directory): 
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules"]
        for file in files: 
            if file.endswith((".py", ".js", ".ts", ".java", ".go", ".rs")): 
                path = os.path.join(root, file)
                try: 
                    with open(path, "r", encoding="utf-8", errors="ignore") as f: 
                        for i, line in enumerate(f, 1): 
                            if keyword.lower() in line.lower(): 
                                matches.append(f"{path}:{i} {line.rstrip()}")

                except Exception: 
                    continue 
    return "\n".join(matches) if matches else f"No matches found for '{keyword}'."


def get_tools(): 
    return [
        FunctionTool.from_defaults(fn=read_file), 
        FunctionTool.from_defaults(fn=list_files), 
        FunctionTool.from_defaults(fn=search_code), 
    ]