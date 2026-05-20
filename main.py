import anyio
import os
from dotenv import load_dotenv 
from claude_agent_sdk import query, ClaudeAgentOptions

load_dotenv() # to load the .env file before the main()

async def main(): 
    # to pull key set up in terminal 
    api_key = os.getenv("ANTHROPIC_API_KEY") # to get key from terminal -> best to keep secret key out of source code 
        #to not leak if when push to GitHub 

    if not api_key: 
        print("Error: ANTHROPIC_API_KEY not found.")
        print("Fix: Run 'export ANTHROPIC_API_KEY=your_key_here' in your terminal.")
        return 
    
    # the SDK  uses the key automatically --> behind scenes --> once in environment 
    ####
    # SDK options 
    options = ClaudeAgentOptions(
        setting_sources=["project", "user"],  # source targets 
        allowed_tools=["Bash", "Read", "Glob", "Skill"] 
    )
# ADD REST CODE HERE LATER 
if __name__ == "__main__": 
    anyio.run(main)

