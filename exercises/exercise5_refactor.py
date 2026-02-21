#!/usr/bin/env python3
"""
Exercise 5: Refactor Code
=========================

Practice using OpenHands to refactor code in focused chunks.

This exercise shows how to:
- Give focused refactoring instructions
- Preserve functionality while improving code
- Use verification steps in prompts

Instructions:
1. This script will create messy_code.py with poor variable names
2. Run: python exercise5_refactor.py
3. Compare before/after: cat messy_code.py

Learning objectives:
- How to give focused refactoring instructions
- The importance of preserving functionality
- Using verification steps in prompts
"""

import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool


def setup_messy_code():
    """Create the messy code file."""
    messy = '''def process_data(d, t, f):
    """Process data - but what do d, t, and f mean?"""
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


# Usage examples - these should still work after refactoring!
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Filter: keep only even numbers
    evens = process_data(data, "filter", lambda x: x % 2 == 0)
    print(f"Evens: {evens}")  # [2, 4, 6, 8, 10]
    
    # Map: square all numbers
    squares = process_data(data, "map", lambda x: x ** 2)
    print(f"Squares: {squares}")  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    # Both: filter evens, then double them
    doubled_evens = process_data(
        data, 
        "both", 
        (lambda x: x % 2 == 0, lambda x: x * 2)
    )
    print(f"Doubled evens: {doubled_evens}")  # [4, 8, 12, 16, 20]
'''
    
    with open("messy_code.py", "w") as f:
        f.write(messy)
    print("✅ Created messy_code.py with poor variable names")


def main():
    # Create the messy file first
    setup_messy_code()
    
    # Show the before state
    print("\n📄 BEFORE refactoring:")
    print("-" * 40)
    with open("messy_code.py", "r") as f:
        print(f.read()[:500] + "...")
    print("-" * 40)
    
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
Refactor the code in `messy_code.py` to improve readability:

## Task 1: Rename Variables
Change all single-letter variable names to meaningful names:
- `d` → `data_list` (the input data to process)
- `t` → `operation_type` (filter, map, or both)
- `f` → `transform_func` (the function(s) to apply)
- `r` → `results` (the output list)
- `i` → `item` (each item being processed)

## Task 2: Add Type Hints
Add type hints to the function signature. Use:
- `List[Any]` for the data list
- `str` for operation type  
- `Union[Callable, Tuple[Callable, Callable]]` for the transform function
- `List[Any]` for the return type

## Task 3: Improve the Docstring
Write a clear docstring that explains:
- What the function does
- What each parameter means
- What it returns
- Example usage

## Important Requirements:
1. DO NOT change the logic - only improve readability
2. The usage examples at the bottom MUST still work
3. After refactoring, run `python messy_code.py` to verify it still works
4. Show me the output to confirm functionality is preserved
"""

    print("\n🤖 Starting agent...")
    print("📝 Task: Refactor messy code to improve readability")
    print("-" * 50)

    conversation.send_message(prompt)
    conversation.run()

    print("-" * 50)
    
    # Show the after state
    print("\n📄 AFTER refactoring:")
    print("-" * 40)
    with open("messy_code.py", "r") as f:
        print(f.read())
    print("-" * 40)
    
    print("\n✅ Exercise 5 complete!")
    print("Compare the before/after code above.")


if __name__ == "__main__":
    main()
