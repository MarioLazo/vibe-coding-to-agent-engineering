# 🤖 From Vibe Coding to Agent Engineering

> A hands-on course introducing OpenHands and the transition from unstructured AI prompting to systematic AI-driven development.

[![OpenHands](https://img.shields.io/badge/Powered%20by-OpenHands-blue)](https://openhands.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Overview

This course teaches software engineers how to move from **"vibe coding"** (unstructured, trial-and-error AI prompting) to **"agent engineering"** (systematic, context-aware development with AI agents).

### What You'll Learn

- **The WHY** - Four compelling reasons for agent engineering
- **History** - Evolution of LLM coding from 2023-2026
- **What is OpenHands?** - An open-source platform for AI software development agents
- **Good vs Bad Prompts** - The difference between vague and effective AI prompts
- **Hands-on Skills** - Build, debug, refactor, and automate with AI agents

---

## 🤔 Begin with the WHY

### 1. 💸 The Reliability Why: Mitigating "The Hidden Tax"

Vibe coding comes with a heavy performance cost. Data from CodeRabbit shows that AI co-authored code without rigorous discipline results in:

| Metric | Impact |
|--------|--------|
| Major Issues | **1.7x** more |
| Logic Errors | **75%** more (flawed control flow) |
| Security Vulnerabilities | **2.74x** higher rate |

> **Goal:** Turn unreliable agents into reliable systems through testing and oversight.

### 2. 🎼 The Professional Why: Orchestration vs. Consumption

The industry is shifting from using AI as simple "autocomplete" to complex task orchestration.

| Vibe Coding | Agent Engineering |
|-------------|-------------------|
| "Forget the code exists, embrace the vibes" | Act as oversight for agents that write code |
| Prompt consumer | Agent engineer leading digital workers |

> **Goal:** Move from "prompt consumers" to "agent engineers" who can lead a team of digital workers.

### 3. ⚠️ The Risk Why: Avoiding the "Plausible but Wrong" Trap

In enterprise environments, agents can take on many roles—each with specific risks:

- **Business Analysts:** May generate requirements that are "plausible but wrong"
- **Solution Architects:** May "hallucinate" design patterns
- **Developers:** May write code with subtle bugs or security holes
- **QA Engineers:** May create tests that pass but don't validate requirements

> **Goal:** Use engineering discipline (Plan, Review, Test, Own) to ensure we don't deploy code we can't explain or verify.

### 4. 📈 The Scale Why: Moving Toward Autonomy

The "4 Modes Framework" shows increasing agent autonomy:

```
Mode 4: Designing    ← Agent architects solutions (highest risk)
Mode 3: Delegating   ← Agent handles features
Mode 2: Directing    ← Agent completes tasks
Mode 1: Doing        ← Agent assists with snippets (lowest risk)
```

⚠️ Without guardrails, asking an agent to "add docstrings" might accidentally refactor your entire codebase.

> **Goal:** Establish guardrails and "kill switches" so humans remain in control of ethics and constraints.

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

## 📖 References & Further Reading

### 🔑 Essential Reading (Start Here)

| Resource | Description |
|----------|-------------|
| [**Karpathy: Agentic Engineering**](https://x.com/karpathy/status/2019137879310836075) | The primary source. Read the full thread — his retrospective on the past year. (Feb 2026) |
| [**Osmani: Agentic Engineering**](https://addyosmani.com/blog/agentic-engineering/) | **ESSENTIAL.** The most practical articulation of the agentic engineering workflow. |
| [**Karpathy: 2025 LLM Year in Review**](https://karpathy.bearblog.dev/year-in-review-2025/) | Broader context on how AI crossed the capability threshold for programming. |

### 📊 Data & Research

| Resource | Key Data |
|----------|----------|
| [**Wikipedia: Vibe Coding**](https://en.wikipedia.org/wiki/Vibe_coding) | Comprehensive history, criticism, and the CodeRabbit study data. |
| [**Osmani: The 80% Problem in Agentic Coding**](https://addyo.substack.com/p/the-80-problem-in-agentic-coding) | Failure modes: assumption propagation, abstraction bloat, sycophantic agreement. |
| [**Osmani: Code Review in the Age of AI**](https://addyo.substack.com/p/code-review-in-the-age-of-ai) | PRs 18% larger with AI, incidents per PR up 24%, change failure rates up 30%. (Jan 2026) |
| [**The New Stack: Vibe Coding Is Passé**](https://thenewstack.io/vibe-coding-is-passe/) | Good secondary summary for quick reference. (Feb 2026) |

### 🛠️ OpenHands Resources

| Resource | Link |
|----------|------|
| OpenHands Index | https://openhands.dev/blog/openhands-index |
| OpenHands Documentation | https://docs.openhands.dev |
| OpenHands SDK | https://docs.openhands.dev/sdk |


### ⚠️ Warning: Canonical GitHub References (Use these sources)

The transition from "vibe coding" to "agent engineering" moves AI development from ad-hoc, prompt-driven prototyping to structured, production-grade systems with persistent memory, tool-use, and strict governance. Use the canonical repositories below when referencing this evolution.

#### Andrej Karpathy & Vibe Coding Origins
- [karpathy/LLM_Council](https://github.com/karpathy/LLM_Council) — "99% vibe-coded" project example.
- [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) — foundational LLM training mechanics.
- [karpathy/llama2.c](https://github.com/karpathy/llama2.c) — compact LLM inference reference.
- [karpathy (org)](https://github.com/karpathy/) — canonical profile for Karpathy projects.

#### Claude Code & Anthropic
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) — tool use and evaluation patterns.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — MCP reference implementations.
- [fiftynotai/igris-ai](https://github.com/fiftynotai/igris-ai) — multi-agent engineering team example.

#### Cursor & Systemized Guardrails
- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) — curated Cursor rules.
- [JhonMA82/awesome-clinerules](https://github.com/JhonMA82/awesome-clinerules) — Cline system prompts.

#### GitHub Copilot Agent Ecosystem
- [github/awesome-copilot](https://github.com/github/awesome-copilot) — Copilot instruction collections.
- [Code-and-Sorts/awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents) — curated prompts and skills.

#### Enterprise Agent Frameworks & SRE Example
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — open-source autonomous agent platform.
- [rajshah4/openhands-sre](https://github.com/rajshah4/openhands-sre) — example SRE agent implementation.
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — stateful multi-actor workflows.

### 🔔 Reminder: Keep Content Accurate & Up to Date

- Re-verify all external links at the start of each cohort.
- Update model names, SDK package names, and minimum Python versions as they evolve.
- Prefer canonical repositories over forks unless you intentionally teach a forked workflow.
- Keep OpenHands references pointed at https://github.com/All-Hands-AI/OpenHands.

## 🧪 CI/CD Evaluation for Agent Outputs

Use CI/CD to turn agent output into production-grade artifacts with automated checks.

**Suggested exercises:**
- Add a workflow that runs tests, linting, and dependency audits on every PR.
- Create a "model output verification" test suite that asserts required files/sections exist.
- Add an allowlist of trusted bots (Dependabot) that can auto-merge only when checks pass.

**Key references:**
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — end-to-end automation of agent workflows.
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) — evaluation and tool-use patterns.
- [rajshah4/openhands-sre](https://github.com/rajshah4/openhands-sre) — SRE agent example for operational checks.

## 🧭 Architectural Governance & System Prompts

Governance turns agent behavior into consistent, reviewable engineering decisions.

**Suggested exercises:**
- Draft `.cursorrules` or equivalent system rules that enforce architecture boundaries.
- Add `.github/copilot-instructions.md` to standardize Copilot agent behavior.
- Define an MCP policy document that describes allowed tools and data boundaries.

**Key references:**
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — standardized MCP integrations.
- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) — curated Cursor rules.
- [JhonMA82/awesome-clinerules](https://github.com/JhonMA82/awesome-clinerules) — Cline system prompts.
- [github/awesome-copilot](https://github.com/github/awesome-copilot) — Copilot instruction patterns.

## 📚 Reference Guide (Canonical Repos & Why They Matter)

| Area | Repository | Relevant content summary |
|------|------------|--------------------------|
| Vibe Coding Origins | [karpathy/LLM_Council](https://github.com/karpathy/LLM_Council) | "99% vibe-coded" example of delegating large builds to AI. |
| LLM Foundations | [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | LLM training mechanics used by modern coding agents. |
| LLM Foundations | [karpathy/llama2.c](https://github.com/karpathy/llama2.c) | Minimal inference implementation for understanding model internals. |
| Claude Tooling | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Tool integration, routing, evaluations. |
| MCP Architecture | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Standardized servers to connect agents to enterprise data. |
| Multi-Agent Teams | [fiftynotai/igris-ai](https://github.com/fiftynotai/igris-ai) | Persistent memory + multi-agent execution patterns. |
| Cursor Guardrails | [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | Enforce coding standards and architectural constraints. |
| Cline Guardrails | [JhonMA82/awesome-clinerules](https://github.com/JhonMA82/awesome-clinerules) | System rules to reduce refactor churn. |
| Copilot Governance | [github/awesome-copilot](https://github.com/github/awesome-copilot) | Instruction files to standardize Copilot behavior. |
| Copilot Governance | [Code-and-Sorts/awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents) | Prompts and skills to constrain autonomy. |
| Agent Platform | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | Open-source, sandboxed autonomous agent platform. |
| Stateful Workflows | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Graph-based, multi-actor orchestration. |
| SRE Agent Example | [rajshah4/openhands-sre](https://github.com/rajshah4/openhands-sre) | Practical SRE agent for incident response workflows. |
| Karpathy Canon | [karpathy (org)](https://github.com/karpathy/) | Official profile for Karpathy repos. |


### 📅 History of LLM Coding

| Year | Capability | Example Tools |
|------|------------|---------------|
| 2023 | Context-unaware snippets | Early Copilot, Codex |
| 2024 | Context-aware generation | Cursor, Copilot X |
| 2025 | Single agents for tasks | OpenHands, Devin, Claude Code |
| 2026 | Parallel multi-agent workflows | Replit Agent 3, Cursor Teams |

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
