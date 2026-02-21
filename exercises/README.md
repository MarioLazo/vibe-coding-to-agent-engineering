# 🧪 OpenHands Hands-on Exercises

Welcome to the hands-on exercises for "From Vibe Coding to Agent Engineering"!

These exercises will take you from your first agent to building real features, debugging, and refactoring code.

---

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.9+ installed
- [ ] An LLM API key (Anthropic, OpenAI, or OpenHands Cloud)
- [ ] The OpenHands SDK installed

### Quick Setup

```bash
# Install uv package manager (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install OpenHands SDK
pip install openhands-sdk openhands-tools

# Set your API key
export LLM_API_KEY="your-api-key-here"
export LLM_MODEL="anthropic/claude-sonnet-4-5-20250929"  # or your preferred model
```

---

## 🎯 Exercise 1: Hello World Agent (15 minutes)

### Objective
Create your first OpenHands agent that analyzes a project and writes facts to a file.

### Instructions

1. Create a new file called `exercise1_hello.py`:

```python
import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool

# Configure the LLM
llm = LLM(
    model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    api_key=os.getenv("LLM_API_KEY"),
)

# Create an agent with tools
agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
    ],
)

# Start a conversation
cwd = os.getcwd()
conversation = Conversation(agent=agent, workspace=cwd)

# Send a task to the agent
conversation.send_message("Write 3 interesting facts about Python into FACTS.txt")
conversation.run()

print("✅ Exercise 1 complete! Check FACTS.txt")
```

2. Run the agent:
```bash
python exercise1_hello.py
```

3. Check the output:
```bash
cat FACTS.txt
```

### Success Criteria
- [ ] The agent creates `FACTS.txt`
- [ ] The file contains 3 facts about Python
- [ ] No errors during execution

### 🎓 What You Learned
- How to configure an LLM
- How to create an Agent with tools
- How to start a Conversation and send messages
- The basic workflow: configure → create → run

---

## 🎯 Exercise 2: Bash Script Generator (15 minutes)

### Objective
Practice writing good prompts to generate a useful bash script.

### Part A: Bad Prompt (Vibe Coding)

Try this vague prompt and observe the results:

```python
conversation.send_message("Write a script")
```

**Observation questions:**
- What did the agent create?
- Was it useful?
- What could go wrong?

### Part B: Good Prompt (Agent Engineering)

Now try a specific, well-engineered prompt:

```python
prompt = """
Create a bash script called `file_summary.sh` that:
1. Takes a directory path as the first argument
2. Defaults to the current directory if no argument is given
3. Counts files by extension and prints a summary
4. Example output:
   File Summary for /path/to/dir:
   .py: 15 files
   .js: 8 files
   .md: 3 files
   Total: 26 files
5. Make the script executable
6. Test it on the current directory
"""
conversation.send_message(prompt)
```

### Create `exercise2_script.py`:

```python
import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool

llm = LLM(
    model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    api_key=os.getenv("LLM_API_KEY"),
)

agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
    ],
)

conversation = Conversation(agent=agent, workspace=os.getcwd())

prompt = """
Create a bash script called `file_summary.sh` that:
1. Takes a directory path as the first argument
2. Defaults to the current directory if no argument is given
3. Counts files by extension and prints a summary table
4. Make the script executable
5. Test it on the current directory
"""

conversation.send_message(prompt)
conversation.run()

print("✅ Exercise 2 complete! Try running: ./file_summary.sh")
```

### Success Criteria
- [ ] `file_summary.sh` is created and executable
- [ ] The script works with the current directory
- [ ] The output shows file counts by extension

### 🎓 What You Learned
- The difference between vague and specific prompts
- How to include expected output in prompts
- Why context matters for AI agents

---

## 🎯 Exercise 3: Build a TODO App (25 minutes)

### Objective
Use OpenHands to build a complete feature from scratch ("greenfield" development).

### Instructions

1. Create `exercise3_todo.py`:

```python
import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool
from openhands.tools.task_tracker import TaskTrackerTool

llm = LLM(
    model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    api_key=os.getenv("LLM_API_KEY"),
)

agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
        Tool(name=TaskTrackerTool.name),
    ],
)

conversation = Conversation(agent=agent, workspace=os.getcwd())

# Step 1: Create the basic app
prompt1 = """
Create a command-line TODO app in Python called `todo.py` with:
1. Add a task: python todo.py add "Buy groceries"
2. List tasks: python todo.py list
3. Complete a task: python todo.py done 1
4. Delete a task: python todo.py delete 1

Store tasks in a JSON file called `tasks.json`.
Include task IDs, descriptions, and completion status.
"""

conversation.send_message(prompt1)
conversation.run()

print("✅ Part 1 complete! TODO app created.")
```

2. Run it:
```bash
python exercise3_todo.py
```

3. Test the TODO app:
```bash
python todo.py add "Learn OpenHands"
python todo.py add "Build something cool"
python todo.py list
python todo.py done 1
python todo.py list
```

### Bonus Challenge: Add a Feature

Create a new conversation to add a feature:

```python
prompt2 = """
Modify the todo.py app to add a new feature:
- Add a due date option: python todo.py add "Task" --due 2024-12-25
- When listing, show overdue tasks in a special way
- Add a command to show only overdue tasks: python todo.py overdue
"""
```

### Success Criteria
- [ ] `todo.py` is created and functional
- [ ] Can add, list, complete, and delete tasks
- [ ] Tasks persist in `tasks.json`
- [ ] (Bonus) Due dates work correctly

### 🎓 What You Learned
- How to build complete features from scratch
- Breaking down features into clear requirements
- Iterating on features with additional prompts

---

## 🎯 Exercise 4: Debug with TDD (20 minutes)

### Objective
Practice debugging using Test-Driven Development with OpenHands.

### Setup: Create a Buggy Function

First, create a file with a known bug:

```bash
cat > buggy_search.py << 'EOF'
def search_items(items, query):
    """Search for items containing the query string."""
    results = []
    for item in items:
        if query in item:  # BUG: This is case-sensitive!
            results.append(item)
    return results

# Test data
inventory = ["Apple", "Banana", "ORANGE", "apple pie", "Grape"]
EOF
```

### Part A: Write a Failing Test

Create `exercise4_debug.py`:

```python
import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool

llm = LLM(
    model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    api_key=os.getenv("LLM_API_KEY"),
)

agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
    ],
)

conversation = Conversation(agent=agent, workspace=os.getcwd())

prompt = """
The `search_items` function in `buggy_search.py` has a bug:
it does case-sensitive searches, but we want case-insensitive searches.

Please:
1. Write a test file `test_search.py` using pytest that:
   - Tests that searching for "apple" finds "Apple" and "apple pie"
   - Tests that searching for "ORANGE" finds "ORANGE"
   - Tests that searching for "grape" finds "Grape"

2. Run the tests (they should fail initially)

3. Fix the `search_items` function in `buggy_search.py` to make all tests pass

4. Run the tests again to confirm they pass
"""

conversation.send_message(prompt)
conversation.run()

print("✅ Exercise 4 complete! Bug fixed with TDD.")
```

### Part B: Verify the Fix

```bash
# Run tests manually to verify
python -m pytest test_search.py -v
```

### Success Criteria
- [ ] `test_search.py` is created with proper test cases
- [ ] Tests initially fail (demonstrating the bug)
- [ ] `buggy_search.py` is fixed
- [ ] All tests pass after the fix

### 🎓 What You Learned
- Test-Driven Development with AI agents
- How to describe bugs clearly
- The power of having agents run and verify tests

---

## 🎯 Exercise 5: Refactor Code (15 minutes)

### Objective
Practice using OpenHands to refactor code in focused chunks.

### Setup: Create a Messy Function

```bash
cat > messy_code.py << 'EOF'
def process_data(d, t, f):
    """Process data - but what do these variables mean?"""
    r = []
    for i in d:
        if t == "filter":
            if f(i):
                r.append(i)
        elif t == "map":
            r.append(f(i))
        elif t == "both":
            if f[0](i):
                r.append(f[1](i))
    return r

# Usage examples
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = process_data(data, "filter", lambda x: x % 2 == 0)
squares = process_data(data, "map", lambda x: x ** 2)
EOF
```

### Create `exercise5_refactor.py`:

```python
import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool

llm = LLM(
    model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    api_key=os.getenv("LLM_API_KEY"),
)

agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
    ],
)

conversation = Conversation(agent=agent, workspace=os.getcwd())

prompt = """
Refactor the code in `messy_code.py`:

1. Rename all single-letter variables to meaningful names:
   - d → data_list
   - t → operation_type
   - f → transform_func
   - r → results
   - i → item

2. Add type hints to the function signature

3. Improve the docstring to explain parameters and return value

4. Keep the same functionality - the usage examples at the bottom
   should still work exactly the same

5. Run Python to verify the code still works after refactoring
"""

conversation.send_message(prompt)
conversation.run()

print("✅ Exercise 5 complete! Code refactored.")
```

### Verify:
```bash
python messy_code.py  # Should run without errors
cat messy_code.py     # Check the improvements
```

### Success Criteria
- [ ] All variables have meaningful names
- [ ] Type hints are added
- [ ] Docstring is improved
- [ ] Code still runs correctly

### 🎓 What You Learned
- How to give focused refactoring instructions
- The importance of preserving functionality
- Using verification steps in prompts

---

## 🎯 Exercise 6: Add a GitHub Action (15 minutes)

### Objective
Use OpenHands to create CI/CD configuration.

### Create `exercise6_ci.py`:

```python
import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool

llm = LLM(
    model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    api_key=os.getenv("LLM_API_KEY"),
)

agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
    ],
)

conversation = Conversation(agent=agent, workspace=os.getcwd())

prompt = """
Create a GitHub Actions workflow file at `.github/workflows/python-ci.yml` that:

1. Triggers on:
   - Push to main branch
   - Pull requests to main branch

2. Runs on ubuntu-latest with Python 3.11

3. Steps:
   - Checkout code
   - Set up Python
   - Install dependencies from requirements.txt (if it exists)
   - Run pytest with verbose output
   - Run flake8 for linting

4. Also create a simple `requirements.txt` with:
   - pytest
   - flake8

5. Show me the workflow file after creating it
"""

conversation.send_message(prompt)
conversation.run()

print("✅ Exercise 6 complete! GitHub Action created.")
```

### Verify:
```bash
cat .github/workflows/python-ci.yml
```

### Success Criteria
- [ ] `.github/workflows/python-ci.yml` exists
- [ ] Workflow has correct triggers
- [ ] All steps are present
- [ ] `requirements.txt` is created

---

## 📊 Progress Tracker

| Exercise | Status | Time | Notes |
|----------|--------|------|-------|
| 1. Hello World | ⬜ | 15 min | |
| 2. Bash Script | ⬜ | 15 min | |
| 3. TODO App | ⬜ | 25 min | |
| 4. Debug with TDD | ⬜ | 20 min | |
| 5. Refactor Code | ⬜ | 15 min | |
| 6. GitHub Action | ⬜ | 15 min | |

**Total Time:** ~1.5 hours

---

## 🏆 Challenge Exercises (Optional)

### Challenge 1: Multi-step Feature
Build a REST API endpoint that:
- Accepts POST requests with JSON data
- Validates the input
- Stores data in SQLite
- Returns appropriate responses

### Challenge 2: Code Review
Have OpenHands review your code:
```
Review the code in [file]. Look for:
- Security issues
- Performance problems
- Code style improvements
Suggest specific fixes with line numbers.
```

### Challenge 3: Documentation Generator
```
Generate comprehensive documentation for all Python files in this project.
Create a docs/ folder with markdown files for each module.
Include function signatures, descriptions, and usage examples.
```

---

## 💡 Tips for Success

1. **Start small** - Don't try to do everything in one prompt
2. **Be specific** - Include file paths, expected behavior, and examples
3. **Iterate** - Build on what works, fix what doesn't
4. **Verify** - Always test the output
5. **Commit often** - Save your progress frequently

---

## 🆘 Troubleshooting

### "API key not found"
```bash
export LLM_API_KEY="your-key-here"
```

### "Module not found"
```bash
pip install openhands-sdk openhands-tools
```

### Agent seems stuck
- Try breaking the task into smaller pieces
- Add more context to your prompt
- Check if previous files exist that might conflict

### Unexpected output
- Review what the agent actually did
- Provide more specific instructions
- Include example expected output in your prompt

---

## 📚 Additional Resources

- **OpenHands Docs**: https://docs.openhands.dev
- **SDK Guide**: https://docs.openhands.dev/sdk
- **Prompting Best Practices**: https://docs.openhands.dev/openhands/usage/tips/prompting-best-practices
- **Example Code**: https://github.com/OpenHands/software-agent-sdk/tree/main/examples

---

*Good luck with the exercises! Remember: Agent Engineering > Vibe Coding* 🚀
