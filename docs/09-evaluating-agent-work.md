# Module 9 — Evaluating Agent Work

> **The module most agent courses skip.** We spend enormous effort teaching people to prompt agents and almost none teaching them to tell whether the output was any good. That gap is where production failures come from.

**Time:** 30 minutes · **Prerequisites:** Modules 1–6

---

## The problem

You gave the agent a task. It produced code. The code runs. Tests pass.

**Was it good work?**

Most engineers answer this by reading the diff and forming an impression. That works at ten lines and fails completely at scale — which is the entire point of agent engineering. If your quality signal is "I read it and it seemed fine," you have not moved past vibe coding. You have automated the writing and kept the vibes.

The uncomfortable data from Module 1: AI co-authored code without rigorous discipline shows **1.7× more major issues, 75% more logic errors, and a 2.74× higher rate of security vulnerabilities.** Those defects were all reviewed by someone who thought the code seemed fine.

---

## Three questions, in order

Evaluation gets muddled because people ask one vague question. Split it into three, because they fail independently and need different checks.

### 1. Did it do what I asked? — Correctness

The narrowest question and the easiest to automate.

- Do the tests pass? Did the agent write the tests, or did you?
- Does it handle the edge cases you named, and the ones you didn't?
- Does it run outside the agent's sandbox, on your machine, from a clean state?

⚠️ **Agent-written tests that validate agent-written code are a closed loop.** Both can encode the same misunderstanding and agree with each other perfectly. If the agent wrote both the implementation and its tests, you have consistency evidence, not correctness evidence.

### 2. Did it do it well? — Quality

- Does it match the surrounding code, or import a new pattern for no reason?
- Did it add dependencies? Were they necessary?
- Is it the smallest change that solves the problem, or did scope creep in?
- Could you explain every line to a colleague?

**The last one is the real bar.** If you can't explain it, you can't maintain it, and you've taken on debt the agent won't service.

### 3. Did I ask for the right thing? — Meaning

The question nobody asks, and where the expensive failures live.

The agent did exactly what you said. The tests pass. The code is clean. **And it solves the wrong problem** — because the task you wrote was a proxy for what you actually needed, and the agent optimized the proxy faithfully.

This is the **Meaning Gap**: the distance between what a system optimizes and what you actually needed. A system can be precise and wrong at the same time, and precision makes the wrongness harder to see.

The diagnostic:

> **"If this gives the right answer to the wrong question, how would you know?"**

If your only answer is "the tests pass," you have no detection mechanism for the most expensive category of failure.

---

## Practical evaluation, at three levels of effort

### Level 1 — Per task, 2 minutes

Run before accepting any agent output:

- [ ] Ran it myself, from a clean state, outside the agent's environment
- [ ] Read the full diff — not just the summary the agent gave me
- [ ] Checked for scope creep: files touched that I didn't expect
- [ ] Checked new dependencies
- [ ] Can explain every changed line

The scope-creep check catches the most common real failure: you asked for docstrings and got a refactor.

### Level 2 — Per workflow, 20 minutes

When you're deciding whether a *prompt pattern*, skill, or model is worth adopting:

1. **Name what should improve, before you change anything.** Fewer review comments? Fewer failed builds? Less rework? If you can't name it, you can't detect it — and you'll keep the change on vibes.
2. **Collect 5–10 representative tasks** from real work, not synthetic examples.
3. **Run them on the current setup. Save the outputs.**
4. **Make the change. Run the same tasks. Compare.**
5. **Check the cost side too:** tokens, wall-clock time, and how often you had to intervene.

This is more evaluation than most published prompt patterns and skills have ever received.

### Level 3 — Per system, ongoing

For agents running as part of a real workflow:

- **Track intervention rate.** What fraction of tasks needed you to step in? Trending the wrong way is your earliest signal.
- **Sample and review blind.** Take a random 10%, review without knowing what the agent said about its own work.
- **Watch downstream, not just output.** Did agent-written code correlate with more incidents? That's the metric that matters, and the slowest to arrive.

> Industry data worth knowing: PRs are running **18% larger** with AI assistance, incidents per PR **up 24%**, and change-failure rates **up 30%**. Velocity went up. So did the cost of being wrong.

---

## Benchmarks: useful, and commonly misread

**SWE-bench Verified** — 500 real GitHub issues — is the standard reference for coding agents. Recent OpenHands results:

| Model backend | SWE-bench Verified |
|---|---|
| Claude Opus 4.6 | **68.4%** |
| Qwen3-235B-A22B (MoE) | ~52% (estimated) |
| Devstral 24B | 46.8% |

**How to read these.** The gap between a frontier model and a small open model is roughly 20 points — real, but smaller than most people assume, and Devstral runs locally. If your work is well-scoped and reviewable, a 46.8% model that runs on your hardware for free may beat a 68.4% model you pay per token for.

**How not to read them.** A 68.4% score does not mean 68.4% of *your* tasks will succeed. SWE-bench tasks are self-contained issues with existing test suites in open-source repos. Your codebase has undocumented conventions, missing tests, and tribal knowledge. Benchmarks measure relative capability. Only your tasks measure your outcomes.

**The most useful benchmark you have is the one you build:** ten real tasks from your own repo, run against each candidate setup. It takes an afternoon and tells you more than every public leaderboard combined.

---

## Verification built into the loop

OpenHands ships a **critic** — a verification pass whose results render inline in the conversation, so quality assessment sits where the work is rather than in a separate step.

The principle generalizes beyond any one tool:

> **The agent that did the work is the worst judge of whether it succeeded.** It has already committed to an interpretation of the task. Verification needs to come from somewhere else — a separate pass, a different model, a test it didn't write, or a human.

This is why "write tests first, then implement" works so well with agents. The tests become an independent judge the agent has to satisfy rather than a rationalization it produces afterward.

---

## Exercise 9.1 — Build your own benchmark

**Time:** 30 minutes. The most valuable half hour in this course.

1. Pick **five real tasks** from your actual work over the last month. Real ones — including one that went badly.
2. For each, write down: the task, and what a *good* result looks like specifically enough that someone else could judge it.
3. Run all five through your current agent setup. Save the outputs.
4. Score each on the three questions: correct, quality, right thing.
5. **Keep this.** Rerun it when you change models, adopt a skill, or change your prompting approach.

You now have something almost nobody has: a repeatable measure of whether your agent workflow is getting better or just different.

---

## What to take away

1. **"It ran" is not evaluation.** Neither is "the tests passed," when the agent wrote the tests.
2. **Correctness, quality, and meaning fail independently.** Check them separately.
3. **The expensive failures are meaning failures** — precisely executed answers to the wrong question.
4. **Public benchmarks rank models. Only your tasks measure your outcomes.**
5. **The agent can't grade its own work.** Verification comes from outside the loop.

---

**Next:** [Module 10 — Security, Sandboxing, and Guardrails](10-security-sandboxing-guardrails.md)

*Part of [From Vibe Coding to Agent Engineering](../README.md). The governance side of this material is developed further in [Agentic CoE](https://github.com/MarioLazo/agentic-coe).*
