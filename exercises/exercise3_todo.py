#!/usr/bin/env python3
"""
Exercise 3: Build a TODO App
============================

Use OpenHands to build a complete feature from scratch ("greenfield" development).

This demonstrates iterative development:
1. First prompt: Build the basic app
2. Second prompt: Add new features

Instructions:
1. Set your API key: export LLM_API_KEY="your-key"
2. Run: python exercise3_todo.py
3. Test the TODO app with the commands shown

Learning objectives:
- How to build complete features from scratch
- Breaking down features into clear requirements
- Iterating on features with additional prompts
"""

import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool
from openhands.tools.task_tracker import TaskTrackerTool


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
            Tool(name=TaskTrackerTool.name),
        ],
    )

    conversation = Conversation(agent=agent, workspace=os.getcwd())

    # Clear, specific requirements for a greenfield project
    prompt = """
Create a command-line TODO app in Python called `todo.py` with the following features:

## Commands:
1. Add a task: `python todo.py add "Task description"`
2. List all tasks: `python todo.py list`
3. Mark task as done: `python todo.py done <task_id>`
4. Delete a task: `python todo.py delete <task_id>`

## Requirements:
- Store tasks in a JSON file called `tasks.json`
- Each task should have: id, description, completed (bool), created_at (timestamp)
- IDs should be auto-incrementing integers
- When listing, show:
  - [ ] for incomplete tasks
  - [x] for completed tasks
- Handle edge cases: empty list, invalid IDs, missing file

## Example usage:
```
$ python todo.py add "Learn OpenHands"
Added task #1: Learn OpenHands

$ python todo.py add "Build something cool"
Added task #2: Build something cool

$ python todo.py list
TODO List:
  1. [ ] Learn OpenHands
  2. [ ] Build something cool

$ python todo.py done 1
Completed task #1: Learn OpenHands

$ python todo.py list
TODO List:
  1. [x] Learn OpenHands
  2. [ ] Build something cool
```

After creating the app, test it with the example commands above.
"""

    print("🤖 Starting agent...")
    print("📝 Task: Build a command-line TODO app")
    print("-" * 50)

    conversation.send_message(prompt)
    conversation.run()

    print("-" * 50)
    if os.path.exists("todo.py"):
        print("✅ Exercise 3 complete!")
        print()
        print("Try these commands:")
        print('  python todo.py add "Learn OpenHands"')
        print('  python todo.py add "Build something cool"')
        print("  python todo.py list")
        print("  python todo.py done 1")
        print("  python todo.py list")
    else:
        print("❌ todo.py was not created. Check the agent output above.")


if __name__ == "__main__":
    main()
