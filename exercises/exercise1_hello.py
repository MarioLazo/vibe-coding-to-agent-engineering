#!/usr/bin/env python3
"""
Exercise 1: Hello World Agent
=============================

Your first OpenHands agent that analyzes a project and writes facts to a file.

Instructions:
1. Set your API key: export LLM_API_KEY="your-key"
2. Run: python exercise1_hello.py
3. Check: cat FACTS.txt

Learning objectives:
- Configure an LLM
- Create an Agent with tools
- Start a Conversation and send messages
"""

import os
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.terminal import TerminalTool


def main():
    # Step 1: Configure the LLM
    # The model name follows LiteLLM convention: provider/model_name
    llm = LLM(
        model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL", None),
    )

    # Step 2: Create an agent with tools
    # Tools give the agent capabilities to interact with the system
    agent = Agent(
        llm=llm,
        tools=[
            Tool(name=TerminalTool.name),      # Run bash commands
            Tool(name=FileEditorTool.name),    # Edit files
        ],
    )

    # Step 3: Start a conversation with a workspace
    # The workspace is where the agent will operate
    cwd = os.getcwd()
    conversation = Conversation(agent=agent, workspace=cwd)

    # Step 4: Send a task to the agent
    print("🤖 Starting agent...")
    print("📝 Task: Write 3 interesting facts about Python into FACTS.txt")
    print("-" * 50)
    
    conversation.send_message("Write 3 interesting facts about Python into FACTS.txt")
    conversation.run()

    # Step 5: Verify the result
    print("-" * 50)
    if os.path.exists("FACTS.txt"):
        print("✅ Exercise 1 complete! Contents of FACTS.txt:")
        print()
        with open("FACTS.txt", "r") as f:
            print(f.read())
    else:
        print("❌ FACTS.txt was not created. Check the agent output above.")


if __name__ == "__main__":
    main()
