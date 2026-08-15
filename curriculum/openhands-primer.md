# OpenHands Introduction Demo - From Vibe Coding to Agent Engineering

## 📖 Course Overview

This document outlines an introductory demo for teaching software engineering students about OpenHands and the transition from "vibe coding" (unstructured AI prompting) to "agent engineering" (systematic AI-driven development).

---

## 1️⃣ What is OpenHands?

### Definition
**OpenHands** is an open-source platform for building AI software development agents that interact with the world like a human developer:
- Writing code
- Executing commands in a terminal
- Browsing the web
- Editing files
- Managing version control

### Key Differentiators

| Feature | OpenHands | Traditional AI Assistants |
|---------|-----------|---------------------------|
| **Execution** | Actually runs code and commands | Just suggests code |
| **Model Agnostic** | Works with Claude, GPT, Qwen, etc. | Often locked to one model |
| **Open Source** | MIT Licensed | Often proprietary |
| **Sandboxed** | Runs in Docker containers safely | Varies |
| **Benchmarked** | Top performer on SWE-bench | Varies |

### Ways to Use OpenHands

1. **OpenHands CLI** - Command-line interface (like Claude Code or Codex)
2. **OpenHands Local GUI** - Web interface for laptop use
3. **OpenHands Cloud** - Hosted solution at app.all-hands.dev
4. **OpenHands SDK** - Python library for building custom agents

---

## 2️⃣ Types of Prompts (Vibe Coding vs Agent Engineering)

### ❌ Bad Prompts (Vibe Coding)

These are vague, unfocused prompts that lead to poor results:

```
"Make the code better"
"Fix the bug"
"Rewrite the entire backend to use a different framework"
"There's a bug somewhere in the user authentication"
```

**Why they fail:**
- Too vague, not concrete
- No location information
- Not appropriately scoped
- Lacks specificity

### ✅ Good Prompts (Agent Engineering)

Characteristics of effective prompts:
- **Concrete**: Clearly describe functionality or the error
- **Location-specific**: Specify files and line numbers
- **Appropriately scoped**: Focus on single features (~100 lines)

**Examples:**

```
"Add a function `calculate_average` in `utils/math_operations.py` 
that takes a list of numbers as input and returns their average."

"Fix the TypeError in `frontend/src/components/UserProfile.tsx` 
occurring on line 42. The error suggests we're trying to access 
a property of undefined."

"Implement input validation for the email field in the registration 
form. Update `frontend/src/components/RegistrationForm.tsx` to check 
if the email is in a valid format before submission."
```

### Prompt Engineering Tips

1. **Be specific** about the desired outcome
2. **Provide context** including relevant file paths and line numbers
3. **Break large tasks** into smaller, manageable prompts
4. **Include error messages** or logs when debugging
5. **Specify the tech stack** if not obvious

---

## 3️⃣ Prerequisites

### For OpenHands CLI/GUI

- **Docker** (for sandboxed execution)
- **LLM API Key** from one of:
  - Anthropic (Claude)
  - OpenAI (GPT-4, etc.)
  - Any LiteLLM-supported provider
  - OR OpenHands Cloud account (free $10 credit)

### For OpenHands SDK

- **Python 3.9+**
- **uv package manager** (version 0.8.13+)
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **SDK Installation:**
  ```bash
  pip install openhands-sdk        # Core SDK
  pip install openhands-tools      # Built-in tools
  pip install openhands-workspace  # Optional: Docker sandboxing
  ```

### Environment Variables

```bash
export LLM_API_KEY="your-api-key-here"
export LLM_MODEL="anthropic/claude-sonnet-4-5-20250929"  # or your preferred model
```

---

## 4️⃣ GitHub Repos for Learning

### Official OpenHands Repositories

| Repository | Description | Link |
|------------|-------------|------|
| **software-agent-sdk** | The main SDK for building agents | [github.com/OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) |
| **OpenHands** | Main OpenHands platform repo | [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) |
| **openhands-resolver** | GitHub Issue resolver using OpenHands | [github.com/All-Hands-AI/openhands-resolver](https://github.com/All-Hands-AI/openhands-resolver) |

### Example Code Locations

The SDK repository includes 24+ examples:
```
examples/01_standalone_sdk/
├── 01_hello_world.py           # Basic agent setup
├── 02_custom_tools.py          # Creating custom tools
├── 03_activate_microagent.py   # Using skills/context
└── ...more examples
```

---

## 5️⃣ Demo Outline

### Demo 1: Hello World Agent (5 min)

```python
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool

# Configure LLM
llm = LLM(
    model="anthropic/claude-sonnet-4-5-20250929",
    api_key=os.getenv("LLM_API_KEY"),
)

# Create agent with tools
agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
    ],
)

# Start conversation
conversation = Conversation(agent=agent, workspace=os.getcwd())
conversation.send_message("Write 3 facts about the current project into FACTS.txt.")
conversation.run()
```

### Demo 2: CLI Quick Start (5 min)

```bash
# Install
pip install openhands-cli

# Run (interactive)
openhands
```

### Demo 3: Good vs Bad Prompts (10 min)

**Bad prompt demo:**
> "Fix the code"

**Good prompt demo:**
> "Add a GitHub action to lint the code. Create `.github/workflows/lint.yml` 
> that runs on push and PR events, using ESLint for JS files."

### Demo 4: First Projects Progression (15 min)

1. **Hello World**: Simple script generation
2. **Greenfield**: Build a TODO app from scratch
3. **Expand Existing Code**: Add a new API endpoint
4. **Refactor**: Split a large function
5. **Debug**: Fix a specific bug with TDD

---

## 6️⃣ Core Concepts to Cover

### SDK Architecture

```
┌─────────────────────────────────────────┐
│                  Agent                   │
│  (Reasoning + Planning + Tool Execution) │
├─────────────────────────────────────────┤
│                  Tools                   │
│  Terminal | FileEditor | Browser | ...   │
├─────────────────────────────────────────┤
│               Workspace                  │
│  Local | Docker | Remote                 │
├─────────────────────────────────────────┤
│           LLM (via LiteLLM)              │
│  Claude | GPT | Qwen | Devstral | ...   │
└─────────────────────────────────────────┘
```

### Key Terms

- **Agent**: AI entity that reasons, plans, and executes actions
- **Tools**: Capabilities (bash, file editing, web browsing, etc.)
- **Workspace**: Execution environment (local, Docker, remote)
- **Conversation**: Manages the interaction lifecycle
- **Skills/Microagents**: Repository-specific context and instructions

---

## 7️⃣ Live Demo Tasks

### Task 1: Build a Simple Script
```
"Write a bash script that takes a directory as an argument and 
prints a summary of file types and their counts."
```

### Task 2: Create a React Component
```
"Build a frontend-only TODO app in React. All state should be 
stored in localStorage. Include add, delete, and toggle complete 
functionality."
```

### Task 3: Add a Feature to Existing Code
```
"Modify ./backend/api/routes.js to add a new route `/api/stats` 
that returns JSON with the count of users and tasks."
```

### Task 4: Debugging with TDD
```
"The `search_widgets` function in ./app.py is doing a case-sensitive 
search. Write a test that fails for case-insensitive search, then 
fix the code so it passes."
```

---

## 8️⃣ Resources

### Documentation
- **OpenHands Docs**: https://docs.openhands.dev
- **SDK Guide**: https://docs.openhands.dev/sdk
- **Prompting Best Practices**: https://docs.openhands.dev/openhands/usage/tips/prompting-best-practices

### Community
- **Slack**: https://openhands.dev/joinslack
- **GitHub**: https://github.com/OpenHands

### Cloud (Free Trial)
- **OpenHands Cloud**: https://app.all-hands.dev (free $10 credit)

---

## 9️⃣ Discussion Questions for Students

1. What's the difference between "vibe coding" and "agent engineering"?
2. Why is specificity important when working with AI agents?
3. What are the benefits of using an open-source, model-agnostic platform?
4. How does sandboxed execution (Docker) improve safety?
5. When should you break a task into smaller prompts vs. giving one large prompt?

---

## 🎯 Takeaways

1. **OpenHands** is an open-source AI coding agent platform
2. **Good prompts** are concrete, location-specific, and appropriately scoped
3. **Agent Engineering** = systematic, iterative, context-aware prompting
4. **Start small**, iterate, and commit frequently
5. **Model-agnostic** means you're not locked into one vendor

---

*Created for Software Engineering class - From Vibe Coding to Agent Engineering*
