# Index 
1. Goal of Project
1.1. Reminders 
2. Notes  
3. Terminology  


# 1. Goal of Project 
Make agentic system that: 
- examines historical changes & development of activities 
- code analysis that checks/ensures that the code follows best practices, has vulnerabilities, security flaws, exposed keys
## 1.1. Reminders: 
- Test on open source repos 

# 2. Notes
### *Core Stages of the Agentic Loop*
Reason --> Act --> Observe 
- **Perceive / Assemble Context:** The agent reads the user prompt, system instructions, error messages, or environment state. 
- **Reason:** The LLM analyzes the data and plans the next best move 
- **Act:** The agent executes a tool (such as writing code, calling an API, querying a database, or searching the web)
- **Observe:** The agent checks the output or test result returned by the tool to see if it worked 
- **Iterate or Stop:** If the goal is not met, it loops back to reason and try again; if the goal or stop condition is met, the loop ends. 

### *Key Components and Safety Guardrails*
Since 
# 3. Terminology 
### *Term* 
def here 
### *Agentic Loop*
a repeating, autonomous execution cycle where an AI system reasons about a task, takes an action using tools, observes the result, and then repeats the process until it reaches a defined goal. Unlike a standard chatbot that answers in a single pass, an " " maintains state and acts indepently without waiting for constant human input.  
