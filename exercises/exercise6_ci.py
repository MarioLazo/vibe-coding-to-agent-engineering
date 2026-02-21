#!/usr/bin/env python3
"""
Exercise 6: Add a GitHub Action
===============================

Use OpenHands to create CI/CD configuration for your project.

This demonstrates:
- Creating infrastructure-as-code
- Multi-step configuration
- Working with YAML files

Instructions:
1. Run: python exercise6_ci.py
2. Check: cat .github/workflows/python-ci.yml
3. Optionally push to GitHub to see it run!

Learning objectives:
- How agents can create configuration files
- Specifying multi-step workflows
- CI/CD automation with AI
"""

import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool


def main():
    llm = LLM(
        model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL", None),
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
Create a GitHub Actions CI workflow for a Python project.

## Task 1: Create the workflow file
Create `.github/workflows/python-ci.yml` with:

### Triggers:
- Push to `main` branch
- Pull requests targeting `main` branch

### Jobs:
Run on `ubuntu-latest` with these steps:

1. **Checkout**: Use actions/checkout@v4

2. **Setup Python**: Use actions/setup-python@v5 with Python 3.11

3. **Install dependencies**:
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   pip install pytest flake8
   ```

4. **Lint with flake8**:
   ```
   flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
   flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
   ```

5. **Run tests**:
   ```
   pytest -v --tb=short
   ```

## Task 2: Create requirements.txt
Create a `requirements.txt` with:
```
pytest>=7.0.0
flake8>=6.0.0
```

## Task 3: Create a sample test
Create `test_sample.py` with a simple passing test:
```python
def test_example():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"
```

## Task 4: Verify
1. Show me the contents of the workflow file
2. Run flake8 locally to verify no errors
3. Run pytest locally to verify tests pass
"""

    print("🤖 Starting agent...")
    print("📝 Task: Create GitHub Actions CI workflow")
    print("-" * 50)

    conversation.send_message(prompt)
    conversation.run()

    print("-" * 50)
    
    workflow_path = ".github/workflows/python-ci.yml"
    if os.path.exists(workflow_path):
        print("✅ Exercise 6 complete!")
        print()
        print("Files created:")
        print(f"  - {workflow_path}")
        print("  - requirements.txt")
        print("  - test_sample.py")
        print()
        print("To use this in a real repo:")
        print("  git add .github/ requirements.txt test_sample.py")
        print('  git commit -m "Add CI workflow"')
        print("  git push")
    else:
        print("❌ Workflow file was not created. Check the agent output above.")


if __name__ == "__main__":
    main()
