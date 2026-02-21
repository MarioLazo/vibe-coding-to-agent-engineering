#!/usr/bin/env python3
"""
Exercise 4: Debug with TDD
==========================

Practice debugging using Test-Driven Development with OpenHands.

The workflow:
1. Write a failing test that exposes the bug
2. Run tests to confirm they fail
3. Fix the bug
4. Run tests to confirm they pass

Instructions:
1. First, create the buggy file: python exercise4_setup.py
2. Then run: python exercise4_debug.py
3. Verify: pytest test_search.py -v

Learning objectives:
- Test-Driven Development with AI agents
- How to describe bugs clearly
- The power of having agents run and verify tests
"""

import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool


def setup_buggy_file():
    """Create the buggy file if it doesn't exist."""
    buggy_code = '''def search_items(items, query):
    """Search for items containing the query string.
    
    BUG: This is case-sensitive, but it should be case-insensitive!
    """
    results = []
    for item in items:
        if query in item:  # BUG: Case-sensitive comparison
            results.append(item)
    return results


# Test data
inventory = ["Apple", "Banana", "ORANGE", "apple pie", "Grape"]

if __name__ == "__main__":
    # This finds only "Apple" and "apple pie", but should also find them
    # when searching for "APPLE" or "apple"
    print("Searching for 'apple':", search_items(inventory, "apple"))
    print("Searching for 'Apple':", search_items(inventory, "Apple"))
'''
    
    with open("buggy_search.py", "w") as f:
        f.write(buggy_code)
    print("✅ Created buggy_search.py with a case-sensitivity bug")


def main():
    # Ensure the buggy file exists
    if not os.path.exists("buggy_search.py"):
        setup_buggy_file()
    
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
The `search_items` function in `buggy_search.py` has a bug:
it performs case-sensitive searches, but we need case-insensitive searches.

Please follow these TDD steps:

## Step 1: Write Tests
Create `test_search.py` using pytest with these test cases:
- Searching for "apple" should find "Apple" and "apple pie"
- Searching for "APPLE" should find "Apple" and "apple pie"  
- Searching for "orange" should find "ORANGE"
- Searching for "grape" should find "Grape"
- Searching for "BANANA" should find "Banana"

## Step 2: Run Tests (they should FAIL)
Run: pytest test_search.py -v
Show me the failing output - this proves the bug exists.

## Step 3: Fix the Bug
Modify the `search_items` function in `buggy_search.py` to make 
the search case-insensitive. The fix should:
- Convert both the item and query to lowercase for comparison
- Return the original items (not lowercased versions)

## Step 4: Run Tests Again (they should PASS)
Run: pytest test_search.py -v
Show me the passing output - this proves the bug is fixed.
"""

    print("🤖 Starting agent...")
    print("📝 Task: Debug the search function using TDD")
    print("-" * 50)

    conversation.send_message(prompt)
    conversation.run()

    print("-" * 50)
    print("✅ Exercise 4 complete!")
    print()
    print("Verify the fix manually:")
    print("  pytest test_search.py -v")


if __name__ == "__main__":
    main()
