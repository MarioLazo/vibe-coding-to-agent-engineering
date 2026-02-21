# 🤖 From Vibe Coding to Agent Engineering

> A hands-on course introducing OpenHands and the transition from unstructured AI prompting to systematic AI-driven development.

[![OpenHands](https://img.shields.io/badge/Powered%20by-OpenHands-blue)](https://openhands.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Overview

This course teaches software engineers how to move from **"vibe coding"** (unstructured, trial-and-error AI prompting) to **"agent engineering"** (systematic, context-aware development with AI agents).

### What You'll Learn

- **What is OpenHands?** - An open-source platform for AI software development agents
- **Good vs Bad Prompts** - The difference between vague and effective AI prompts
- **The Three Principles** - Concrete, location-specific, appropriately scoped
- **Hands-on Skills** - Build, debug, refactor, and automate with AI agents

---

## 🎯 Course Materials

### 📊 Presentation Slides

Interactive HTML slides covering all concepts:

```
slides/index.html
```

**Topics covered:**
1. What is "Vibe Coding"?
2. What is "Agent Engineering"?
3. Introduction to OpenHands
4. SDK Architecture
5. Good vs Bad Prompts
6. Best Practices

**Navigation:** Use ← → arrow keys or swipe on mobile

### 🧪 Hands-on Exercises

Six progressive exercises (~1.5 hours total):

| Exercise | File | Time | Focus |
|----------|------|------|-------|
| 1. Hello World | `exercises/exercise1_hello.py` | 15 min | First agent, basic workflow |
| 2. Bash Script | `exercises/exercise2_script.py` | 15 min | Good vs bad prompts |
| 3. TODO App | `exercises/exercise3_todo.py` | 25 min | Greenfield development |
| 4. Debug with TDD | `exercises/exercise4_debug.py` | 20 min | Test-driven debugging |
| 5. Refactor Code | `exercises/exercise5_refactor.py` | 15 min | Code improvement |
| 6. GitHub Action | `exercises/exercise6_ci.py` | 15 min | CI/CD configuration |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- An LLM API key (Anthropic, OpenAI, or [OpenHands Cloud](https://app.all-hands.dev))

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/vibe-coding-to-agent-engineering.git
cd vibe-coding-to-agent-engineering

# Install OpenHands SDK
pip install openhands-sdk openhands-tools

# Set your API key
export LLM_API_KEY="your-api-key-here"
export LLM_MODEL="anthropic/claude-sonnet-4-5-20250929"

# Run your first exercise
cd exercises
python exercise1_hello.py
```

---

## 📚 Key Concepts

### ❌ Vibe Coding (Don't Do This)

```
"Make the code better"
"Fix the bug"
"There's a bug somewhere in auth"
```

**Problems:** Too vague, no location, not scoped, no context

### ✅ Agent Engineering (Do This)

```
"Add a function `calculate_average` in `utils/math_operations.py` 
that takes a list of numbers and returns their average."

"Fix the TypeError in `frontend/src/components/UserProfile.tsx` 
on line 42. The error says we're accessing a property of undefined."
```

**The Three Principles:**
1. **Concrete** – Describe specific functionality
2. **Location-specific** – Include file paths and line numbers
3. **Appropriately scoped** – ~100 lines, single feature

---

## 🏗️ OpenHands Architecture

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
│  Claude | GPT | Qwen | Devstral | ...    │
└─────────────────────────────────────────┘
```

---

## 🔗 Resources & Links

### Official OpenHands

| Resource | Link |
|----------|------|
| **Documentation** | https://docs.openhands.dev |
| **SDK Guide** | https://docs.openhands.dev/sdk |
| **Prompting Best Practices** | https://docs.openhands.dev/openhands/usage/tips/prompting-best-practices |
| **OpenHands Cloud** | https://app.all-hands.dev (Free $10 credit!) |
| **Community Slack** | https://openhands.dev/joinslack |

### GitHub Repositories

| Repository | Description |
|------------|-------------|
| [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) | The main SDK with 24+ examples |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | Core OpenHands platform |
| [All-Hands-AI/openhands-resolver](https://github.com/All-Hands-AI/openhands-resolver) | GitHub Issue automation |

### SDK Examples Location

The official SDK repository includes many examples:
```
examples/01_standalone_sdk/
├── 01_hello_world.py           # Basic agent setup
├── 02_custom_tools.py          # Creating custom tools
├── 03_activate_microagent.py   # Using skills/context
└── ...more examples
```

---

## 💡 Best Practices

1. **Start small** – Begin with simple tasks, iterate
2. **Be specific** – Include file paths, line numbers, context
3. **Break down tasks** – One feature per prompt (~100 lines)
4. **Commit frequently** – Version control after each success
5. **Include errors** – Share full error messages and logs

---

## 📋 For Instructors

### Suggested Class Schedule

| Time | Activity |
|------|----------|
| 30 min | Slides presentation |
| 10 min | Q&A |
| 60 min | Hands-on exercises |
| 20 min | Review & discussion |

### Discussion Questions

1. What's the difference between "vibe coding" and "agent engineering"?
2. Why is specificity important when working with AI agents?
3. What are the benefits of using an open-source, model-agnostic platform?
4. How does sandboxed execution (Docker) improve safety?
5. When should you break a task into smaller prompts?

---

## 📄 License

This course material is released under the MIT License.

---

## 🙏 Acknowledgments

- [OpenHands](https://openhands.dev) - The open-source AI coding agent platform
- [All Hands AI](https://all-hands.dev) - The team behind OpenHands

---

*Made with 🤖 by AI agents, for teaching about AI agents*
