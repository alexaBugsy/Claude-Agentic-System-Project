# Index 
1. Goal of Project
1.1. Reminders 
1.2. Current Plan / Checklist 
2. Notes  
3. Terminology  


# 1. Goal of Project 
Make agentic system that: 
- examines historical changes & development of activities 
- code analysis that checks/ensures that the code follows best practices, has vulnerabilities, security flaws, exposed keys
## 1.1. Reminders: 
- Test on open source repos 
## 1.2. Current Plan / Checklist
- [] Installation and setup -> the SDK requires **Python 3.10 or higher** --> it is recommended to use a **virtual environment** to keep **dependencies** clean 
    - [x] check what version of Python I have --> have python **3.14.3**
    - [] figure out how to use said virtual environment 
# 2. Notes
### *Core Stages of the Agentic Loop*
Reason --> Act --> Observe 
- **Perceive / Assemble Context:** The agent reads the user prompt, system instructions, error messages, or environment state. 
- **Reason:** The LLM analyzes the data and plans the next best move 
- **Act:** The agent executes a tool (such as writing code, calling an API, querying a database, or searching the web)
- **Observe:** The agent checks the output or test result returned by the tool to see if it worked 
- **Iterate or Stop:** If the goal is not met, it loops back to reason and try again; if the goal or stop condition is met, the loop ends. 

### *Key Components and Safety Guardrails*
Since autonomous loops can get stuck in infinite loops, spin out of control, or waste financial resources on API/token costs, it is on us to make the agentic systems reliable, must be programed with the following guardrails: 
- **Stop Conditions:** Clear, measurable endpoints (ex, "stop when all unit tests pass" or "stop after 10 iterations"). 
- **Hard Caps on Iterations:** A strict code-level limit to prevent infinite loops. 
- **Token Budget Ceilings:** Spending limits to stop excessive API charges.
- **Independent Verification:** Separate validation steps or tests to ensure the agent doesn't "self-grade" bad work as successful.

### *Claude Agents and Skills*
**Benefits of Skills:** (NOTE: can make custom ones as well)
- **Specialize Claude:** Tailor capabilities for domain-specific tasks
- **Reduce Repetition:** Create once, use automatically
- **Compose Capabilities:** Combine Skills to build complex workflows

### *Pre-built Agent Skills*
They are available on Claude.ai, the Claude API, Claude Platform on AWS, and Microsoft Foundry. 
**Available Skills:**
- **PowerPoint (pptx):** Create presentations, edit slides, analyze presentation content 
- **Excel (xlsx):** Create spreadsheets, analyze data, generate reports with charts
- **Word (docx):** Create documents, edit content, format text
- **PDF (pdf):** Generate formatted PDF documents and reports
**Open-Source Skills:**
- Anthropic also publishes open-source skills in skills repository

# 3. Terminology 
### *Term* 
def here 
### *API*
Stands for Application Programming Interface --> it is a set of rules and protocols that allows different software applications to communicate and exchange data with eachother --> **basics of how works:** --> software component sends a request --> the API processes it --> API returns a response --> said response is **often formatted in JSON**
### *Dependencies*
These are the outside libraries that x project needs, like **Anthropic SDK** or GitPython. Different projects often need different versions of the same library, and installing everything globally on the computer makes them crash. 
### *Agentic Loop*
A repeating, autonomous execution cycle where an AI system reasons about a task, takes an action using tools, observes the result, and then repeats the process until it reaches a defined goal. Unlike a standard chatbot that answers in a single pass, an " " maintains state and acts indepently without waiting for constant human input.  
### *Agent Skills*
Modular capabilities that extend Claude's functionality --> each skill packages instructions, metadata, and optional resources (scripts, templates) --> Claude uses them automatically when it is relevant. 
### *Skills*
Reusable filesystem-based resources that provide Claude with domain specifc expertise: 
- workflows
- context 
- best-practices that transform general-purpose agents into specialists 
**Note:** unlike **prompts**, bc " " load on-demand and eliminate the need to repeatedly provide the same guidance across multiple conversations. 
### *SDK*
Stands for Software Development Kit, it is a collection of prebuilt tools, libraries, code samples, documentation, and APIs that help  
### *Virtual environment (venv):*
A private folder holding its own copy of Python and its own installed libraries, used only by this project --> 
