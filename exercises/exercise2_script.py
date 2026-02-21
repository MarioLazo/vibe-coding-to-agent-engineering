#!/usr/bin/env python3
"""
Exercise 2: Bash Script Generator
=================================

Practice writing good prompts to generate a useful bash script.

This exercise demonstrates the difference between:
- BAD prompts (vibe coding): "Write a script"
- GOOD prompts (agent engineering): Specific, detailed instructions

Instructions:
1. Set your API key: export LLM_API_KEY="your-key"
2. Run: python exercise2_script.py
3. Test: ./file_summary.sh

Learning objectives:
- The difference between vague and specific prompts
- How to include expected output in prompts
- Why context matters for AI agents
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

    # This is a GOOD prompt - specific, detailed, with examples
    # Compare this to a BAD prompt like "Write a script"
    prompt = """
Create a bash script called `file_summary.sh` that:

1. Takes a directory path as the first argument
2. Defaults to the current directory if no argument is given
3. Counts files by extension and prints a summary table
4. Handles files without extensions (group as "no extension")
5. Shows the total file count at the end

Example output format:
```
File Summary for /path/to/dir
=============================
Extension   Count
---------   -----
.py         15
.js         8
.md         3
(none)      2
---------   -----
Total       28
```

After creating the script:
1. Make it executable with chmod +x
2. Test it on the current directory
3. Show me the test output
"""

    print("🤖 Starting agent...")
    print("📝 Task: Create a file summary bash script")
    print("-" * 50)

    conversation.send_message(prompt)
    conversation.run()

    print("-" * 50)
    if os.path.exists("file_summary.sh"):
        print("✅ Exercise 2 complete!")
        print("Try running: ./file_summary.sh")
        print("Or: ./file_summary.sh /path/to/another/directory")
    else:
        print("❌ file_summary.sh was not created. Check the agent output above.")


if __name__ == "__main__":
    main()
