# Microagents & Project Knowledge — Microagents and Project Knowledge

> The single highest-leverage change most teams can make: stop re-explaining your project in every prompt.

**Supports Sessions 3 and 7** — prompt engineering and multi-step workflows

**Time:** 25 minutes · **Prerequisites:** Modules 1–6

---

## The problem you've already hit

By the sixth exercise you've written prompts like:

> "Add a function to `utils/math_operations.py`. Use pytest, not unittest. Follow the existing error-handling pattern. Don't add dependencies without asking."

Everything after the first sentence is **project knowledge** — true of every task in this repo, and you retyped it because the agent had no way to know it.

Do that fifty times and two things happen. You waste effort, and worse, you're inconsistent: some prompts mention the error-handling convention, some don't, and the codebase drifts accordingly.

---

## Microagents

OpenHands' **microagent** system holds conventions and project knowledge that **load automatically when triggered**, so the agent knows your project the moment it lands in the repo.

The mental shift:

| Prompting | Project knowledge |
|---|---|
| Repeated every task | Written once |
| Inconsistent by nature | Applied uniformly |
| Costs you attention | Costs context budget |
| Task-specific | Repo-specific |

A microagent is markdown. That's the whole format — which is also why the concept ports to Claude Code skills, Cursor rules, and Copilot instructions with editing rather than rewriting.

---

## What belongs in project knowledge

**Good candidates — true across tasks, expensive when wrong:**

- **Conventions the code doesn't state.** "Errors are returned, not raised, below the API boundary."
- **Structure that isn't obvious.** Which directory owns what, what's generated, what's vendored.
- **Hard constraints.** "Never modify files under `migrations/`." "This package must stay Python 3.9 compatible."
- **Local tooling.** How tests run *here*, how to build, what the lint gate is.
- **Decisions with history.** "We use X not Y — we tried Y in 2025 and hit Z."

That last category is the most valuable and most often lost. It's the knowledge that walks out the door when someone leaves.

**Poor candidates:**

- Anything already obvious from the code. The agent can read.
- Task-specific detail — that's a prompt, not a convention.
- Aspirations. "We should have more tests" helps nobody. "New code requires tests" is a rule.
- Anything you won't maintain. Stale project knowledge is worse than none, because it's confidently wrong.

---

## The three-corrections rule

The practical trigger for what to write down:

> **If you've corrected the agent on the same thing three times, that's project knowledge. Before three, it's a preference.**

This keeps the file honest. Everyone's instinct is to write an exhaustive style guide up front; almost all of it goes unread and unmaintained. Letting real corrections drive it means every line exists because something actually went wrong.

---

## Context is a budget

Project knowledge loads into context before work begins. It is not free.

- A tight file of hard-won conventions pays for itself immediately.
- A 2,000-line style guide crowds out the actual task and degrades the work you asked for.
- Contradictions are worse than absence — the agent picks one silently and never tells you.

**Review on a schedule.** Nothing forces you to revisit these files, so they accumulate. When a convention changes and the file doesn't, the agent enforces a rule your team abandoned months ago.

---

## Exercise 7.1 — Write your first microagent

**Time:** 20 minutes

1. **Look back at your last ten prompts** in a real repo. Highlight every line that was true of the project rather than the task.
2. **Group them.** Conventions, structure, constraints, tooling.
3. **Write the file.** Markdown, under 100 lines. Rules, not aspirations.
4. **Test it properly:** run a task you've done before, without restating the conventions. Did the agent follow them unprompted?
5. **Test the negative case too:** ask for something that *violates* a stated constraint. Does it push back, or comply?

Step 5 is the one people skip, and it's the one that tells you whether the file is actually loaded and understood, or merely present.

---

## Portability

Because microagents are markdown, the same content adapts across tools:

| Tool | Equivalent |
|---|---|
| OpenHands | Microagents |
| Claude Code | Skills / `CLAUDE.md` |
| Cursor | Rules |
| GitHub Copilot | Custom instructions |
| Any Plugins 1.0 client | Skills, under `plugin.json` |

**Agent Plugins 1.0** (August 2026) standardizes Agent Skills and MCP servers under one manifest, with support from VS Code, Cursor, Copilot, ChatGPT & Codex, and Kiro. Formats are converging — but keep the substance in prose, not vendor scaffolding, and it travels.

---

## What to take away

1. **Repeated prompt content is project knowledge in disguise.** Write it once.
2. **Three corrections, then write it down.** Before that, you're guessing.
3. **Context is a budget** — a tight file beats an exhaustive one.
4. **Test the negative case.** Does the agent refuse what it should refuse?
5. **Stale knowledge is worse than none.** Schedule the review.

---

**Next:** [Multi-Agent Delegation — Multi-Agent Delegation](delegation.md)

*Part of [From Vibe Coding to Agent Engineering](../README.md). Cross-tool skill selection and evaluation is covered in the [Skills Catalog](https://github.com/MarioLazo/agentic-coe/blob/main/tools/skills-catalog.md).*
