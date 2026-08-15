# 🤖 From Vibe Coding to Agent Engineering

### A practitioner's curriculum for building production-grade AI agents

[![OpenHands](https://img.shields.io/badge/Built%20on-OpenHands-1F5F5B?style=flat-square)](https://openhands.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Sessions](https://img.shields.io/badge/12%20sessions-15%20weeks-0A66C2?style=flat-square)](curriculum/README.md)

> ### Would you deploy this agent on a Tuesday at 3pm?
>
> That question frames every design decision, every evaluation metric, and every
> architectural choice in this course.

---

## 📖 What this is

A 15-week curriculum that teaches agent engineering the way production systems
actually get built: **constraints first, not features.**

You will not just write agents that work in demos. You will build agents that
survive contact with real users, real data, and real failure modes — and you'll
be able to prove it with numbers rather than a convincing walkthrough.

The arc runs from **assisted automation** (agents that do one thing well),
through **human-in-the-loop collaboration** (agents that decide with oversight),
to **orchestrated multi-agent systems** (agents that delegate across workflows).
Production readiness is baked into the deliverables at every stage, not added at
the end.

### 👥 Who this is for

**Practitioners who need to use, evaluate, and govern agents** — developers,
analysts, architects, engineering leads. You need programming fundamentals
(Python preferred) and comfort with Git. **You do not need AI/ML background.**
The agent-specific skills are taught from the ground up.

If you want to build the agent *runtime itself* — the loop, the permission model,
context compaction — see [Building a Coding Agent From Scratch](REFERENCES.md#related-courses),
which is the technical complement to this course.

### 🎓 What you walk away with

- **Three portfolio-ready GitHub repositories** demonstrating progressive complexity
- **A community playbook** with real templates and failure taxonomies
- **Hands-on experience with OpenHands** for agentic development
- **A polished Solution Set** — a reusable proposal framework you could put in front of a client

---

## 🧭 Start here

| If you want to… | Go to |
|---|---|
| See the full 15-week plan | **[Curriculum](curriculum/README.md)** |
| Understand the frameworks | **[Frameworks](frameworks/README.md)** |
| Read what goes wrong in production | **[Case Studies](case-studies/README.md)** |
| Go deeper on advanced topics | **[Part II modules](#-part-ii--advanced-modules)** |
| Check a claim | **[References](REFERENCES.md)** |
| Just start building | **[Exercises](exercises/README.md)** |

---

## 🤔 Why this course exists

Vibe coding — prompting a model, accepting what it generates, moving fast without
systematic testing — works for prototypes. It fails in production. That isn't an
opinion; four independent bodies of evidence converge on it:

| Finding | Source |
|---|---|
| +3.4% code quality, **−7.2% delivery stability** | [DORA 2024](https://dora.dev/research/) |
| Cross-file function calls **down 35%**, refactoring moves **down 70%** (211M lines analyzed) | [GitClear](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) |
| **1.7×** major issues, **2.74×** security vulnerabilities | CodeRabbit |
| **32%** cite output quality as the top production blocker | LangChain survey |

**The pattern is consistent: micro-quality improves, system-level dependability
degrades.** Individual functions get cleaner. The seams between them get worse.
And the seams are where production failures live — as every one of the
[case studies](case-studies/README.md) demonstrates.

Full sourcing and methodology notes in **[REFERENCES.md](REFERENCES.md)**.

---

## 🎯 The 4 Modes

The classification tool used throughout. It answers one question: **what is my
agent actually doing, and who remains accountable?**

| Mode | The agent… | Accountable |
|---|---|---|
| **Doing** | Executes a single, well-defined task | The agent, within scope |
| **Deciding** | Recommends; a human approves | The human who approves |
| **Delegating** | Coordinates multiple sub-agents | Humans, via oversight and guardrails |
| **Designing** | — this is always your role | **You, the architect** |

> **Agents gain autonomy; humans gain responsibility.** That asymmetry is
> intentional. Even at the Delegating level, you remain accountable. Designing
> never transfers.

The three projects map directly: **Project 1 is Doing · Project 2 is Deciding ·
Project 3 is Delegating.** You are Designing throughout.

Full framework set — including Observation³, the Production Readiness Checklist,
and the Evaluation Framework — in **[frameworks/](frameworks/README.md)**.

---

## 🗺️ The 3-project arc

| Project | Sessions | Mode | What you build |
|---|---|---|---|
| **1 · Assisted Agent** | 2–4 | Doing | A single agent executing one task within tight guardrails |
| **2 · Copilot Agent** | 6–8 | Deciding | A human-in-the-loop agent recommending actions for approval |
| **3 · Multi-Agent System** | 10–12 | Delegating | An orchestrated system of coordinating agents |

15 weeks: 12 taught sessions, 2 open workshop weeks, and Demo Day.
Full week-by-week map in **[curriculum/](curriculum/README.md)**.

---

## ⚖️ Vibe coding vs. agent engineering

| Dimension | Vibe coding | Agent engineering |
|---|---|---|
| **Objective** | Rapid ideation, casual experimentation | Reliable execution of production workloads |
| **The model is…** | An oracle producing final solutions | A stochastic processor requiring strict instruction sets |
| **Input** | Unstructured conversational description | Typed interfaces, structured schemas, boundary conditions |
| **Posture** | Trusting delegation | **Adversarial verification** — assume subtle flaws until proven otherwise |
| **Constraints** | Frameless | Policy-as-code, validation gates, rate limits |

**The useful mental model:** stop treating the model as an omniscient oracle and
start treating it as the CPU of a Turing-complete machine. The prompt is the
instruction set — it manages state, coordinates retrieval, handles I/O, and
orchestrates control flow. That reframing makes standard software engineering
rigor obviously applicable, rather than optional.

### ❌ Vibe coding

```
"Make the code better"
"Fix the bug"
"There's a bug somewhere in auth"
```

Too vague, no location, unscoped, no context.

### ✅ Agent engineering

```
Add a function `calculate_average` in `utils/math_operations.py`
that takes a list of numbers and returns their average.

Fix the TypeError in `frontend/src/components/UserProfile.tsx`
line 42. The error says we're accessing a property of undefined.
```

**Three principles:** concrete · location-specific · appropriately scoped
(~100 lines, single feature).

---

## 🧪 Hands-on exercises

Six progressive exercises, ~1.5 hours total. Start here if you want to build
before you read.

| # | Exercise | Time | Focus |
|---|---|---|---|
| 1 | [Hello World](exercises/exercise1_hello.py) | 15 min | First agent, basic workflow |
| 2 | [Bash Script](exercises/exercise2_script.py) | 15 min | Good vs. bad prompts |
| 3 | [TODO App](exercises/exercise3_todo.py) | 25 min | Greenfield development |
| 4 | [Debug with TDD](exercises/exercise4_debug.py) | 20 min | Test-driven debugging |
| 5 | [Refactor](exercises/exercise5_refactor.py) | 15 min | Code improvement |
| 6 | [GitHub Action](exercises/exercise6_ci.py) | 15 min | CI/CD configuration |

Full instructions: **[exercises/README.md](exercises/README.md)** ·
Slides: **[slides/index.html](slides/index.html)**

---

## 📗 Part II — Advanced modules

Working *as an agent engineer* rather than *with* an agent. These separate a demo
from something you'd run on real work.

| Module | Covers | Time |
|---|---|---|
| **[7 · Microagents & Project Knowledge](docs/07-microagents-and-project-knowledge.md)** | Stop re-explaining your project every prompt. The three-corrections rule, context budget, cross-tool portability | 25 min |
| **[8 · Multi-Agent Delegation](docs/08-multi-agent-delegation.md)** | TaskToolSet and sub-agents. Cascading errors, and why decomposition is the decision that matters | 25 min |
| **[9 · Evaluating Agent Work](docs/09-evaluating-agent-work.md)** | **The module most courses skip.** Correctness vs. quality vs. meaning. Reading SWE-bench honestly. Build your own benchmark | 30 min |
| **[10 · Security, Sandboxing & Guardrails](docs/10-security-sandboxing-guardrails.md)** | Agents as privileged identities. Tool poisoning. Testing your kill switch | 25 min |

> **Why Module 9 matters most.** We teach people to prompt agents and almost never
> to judge the output. "It ran" is not evaluation — and neither is "the tests
> passed," when the agent wrote the tests.

---

## 🚀 Quick start

```bash
git clone https://github.com/MarioLazo/vibe-coding-to-agent-engineering.git
cd vibe-coding-to-agent-engineering

pip install openhands-sdk openhands-tools

export LLM_API_KEY="your-api-key-here"
export LLM_MODEL="anthropic/claude-sonnet-4-5-20250929"

cd exercises && python exercise1_hello.py
```

**Prerequisites:** Python 3.10+ · Git fundamentals · an LLM API key
([OpenHands Cloud](https://app.all-hands.dev) includes free credit).
Full setup checklist in [curriculum/](curriculum/README.md#environment-setup).

---

## 📅 How LLM coding got here

| Year | Capability | Representative tools |
|---|---|---|
| 2023 | Context-unaware snippets | Early Copilot, Codex |
| 2024 | Context-aware generation | Cursor, Copilot X |
| 2025 | Single agents for tasks | OpenHands, Devin, Claude Code |
| 2026 | Parallel multi-agent workflows | Replit Agent 3, Cursor Teams, OpenHands TaskToolSet |

**OpenHands, mid-2026:** multi-agent delegation via `TaskToolSet`, microagents
that auto-load project knowledge, native sandboxed execution, model-agnostic
routing, built-in security analysis, inline critic results. SWE-bench Verified:
**68.4%** with Claude Opus 4.6, **46.8%** with Devstral 24B — a gap that matters
less than it looks, since Devstral runs locally. [Module 9](docs/09-evaluating-agent-work.md)
covers how to read those numbers.

---

## 🏛️ Taking this into an organization

This course is about individual and team practice. Rolling agent engineering out
across an enterprise is a different problem — operating model, risk tiers,
quality gates, and who signs off on what.

That's **[Agentic CoE](https://github.com/MarioLazo/agentic-coe)**: the Agent Card
documentation standard, a ten-gate Pre-Flight Checklist, the BXT scorecard for
use-case selection, governance-organized catalogs for MCP servers and agent
skills, and an 11,000-word reference for regulated industries.

---

## 📋 For instructors

Session-by-session teaching notes, agendas, assessment weightings, student role
definitions, and the Solution Set specification are all in
**[curriculum/](curriculum/README.md)**.

Two things worth knowing before you teach it:

- **Grade demos on honesty, not perfection.** A student who shows a failure and
  explains what they learned is demonstrating more engineering maturity than one
  who hides limitations. This shapes the whole culture of the course.
- **The pre-mortem is the highest-leverage exercise.** Push relentlessly for
  specificity. "The agent might fail" is useless; "the agent will hallucinate
  function signatures on files with no type hints, detectable by comparing output
  to AST parsing" is actionable.

---

## 📄 License & attribution

Course material released under the [MIT License](LICENSE). Frameworks, curriculum
design, and case studies are original work by **[Mario Lazo](https://github.com/MarioLazo)**.

Built on [OpenHands](https://openhands.dev) by [All Hands AI](https://all-hands.dev).
Sources and related work credited in **[REFERENCES.md](REFERENCES.md)**.
