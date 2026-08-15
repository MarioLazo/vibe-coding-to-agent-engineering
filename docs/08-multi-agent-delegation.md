# Module 8 — Multi-Agent Delegation

> Where agent engineering starts to look like engineering management — and inherits the same failure modes.

**Time:** 25 minutes · **Prerequisites:** Module 7

---

## What delegation actually is

OpenHands supports delegating specialized tasks to sub-agents via **TaskToolSet**. One agent decomposes a goal, hands pieces to others, and integrates what comes back.

That's the mechanic. The interesting part is what it changes about your job.

With a single agent you review one output. With delegation you're reviewing a **process you didn't watch** — decomposition you didn't approve, handoffs you didn't see, and integration of results you never independently checked.

You have moved from reviewing code to managing a team whose internal communications you can't read. That's a materially harder problem, and it's why this module comes after evaluation rather than before.

---

## When delegation earns its complexity

**Good fits — genuinely separable work:**

- **Breadth over depth.** "Audit every module for this pattern." Parallel, independent, easy to merge.
- **Distinct expertise.** One sub-agent researching an API while another writes tests against a known interface.
- **Adversarial pairing.** One writes, another tries to break it. Independence is the whole value.

**Poor fits:**

- **Tightly coupled work.** If piece B needs decisions from piece A, you've built a sequence with extra failure points.
- **Anything small.** Delegation overhead exceeds the task.
- **Work you can't verify independently.** If you can't check a sub-agent's output on its own, you can't tell where a failure came from.

**The honest default:** most tasks do not need delegation. It's frequently reached for because it's impressive rather than because it's warranted. A single well-scoped agent with good project knowledge beats a poorly-decomposed swarm nearly every time.

---

## Where it fails

### Cascading errors

The defining risk. A wrong assumption in an early sub-agent propagates through everything downstream — and each hop makes it *more* confident, because subsequent agents treat upstream output as established fact.

Single-agent errors are usually visible in the output. Delegated errors are laundered through layers of plausible-looking work.

### Decomposition failures

The parent agent splits the task badly — overlapping scopes, a missing piece, or boundaries that don't match the real structure of the problem. Every sub-agent then succeeds at its assigned piece, and the assembled result is still wrong.

Nobody reports failure. Everyone did their job.

### Integration gaps

Each piece works. Together they don't. Interfaces don't line up, assumptions conflict, and the seams are exactly where nobody was looking.

### Attribution loss

Something's wrong three layers down. Which agent? Which handoff? Without per-agent logging you're debugging a conversation you can't read.

---

## Controls that actually help

**Approve the decomposition before execution.** Have the parent agent state its plan — sub-tasks, boundaries, integration approach — and read it before anything runs. Most delegation failures are visible in the plan and cheap to fix there.

**Log every handoff.** Which agent, what input, what output. Without it, debugging is guesswork.

**Verify sub-agent outputs independently.** If a sub-agent's work can only be judged as part of the whole, your decomposition is wrong.

**Cap the depth.** Sub-agents spawning sub-agents compounds every problem above. Two levels is plenty for most real work.

**Keep an override at every node**, not just at the end.

---

## The connection to autonomy levels

Delegation is a jump in autonomy, not just capability. Useful ladder:

| Level | What the agent does | Your job |
|---|---|---|
| 1 | Completes a bounded task | Review output |
| 2 | Acts, you approve before it lands | Approve each action |
| 3 | Acts autonomously inside a policy envelope | Define the envelope, handle exceptions |
| **4** | **Orchestrates other agents, adapts as it goes** | **Define goals and guardrails, audit the process** |
| 5 | Sets its own sub-goals over long horizons | Experimental — not recommended in production |

**Delegation is Level 4.** The most common failure in real deployments is running Level 4 workflows with Level 2 governance — approving individual outputs while a system makes structural decisions you never see.

If you're delegating, your controls need to be about the *process*, not the artifact.

---

## Exercise 8.1 — Delegate, then audit

**Time:** 25 minutes

1. Pick a genuinely parallel task — auditing several modules for one pattern works well.
2. **Before running it,** write down how *you* would split it. Keep that.
3. Run it with delegation, and capture the plan the parent agent produces.
4. **Compare the two decompositions.** Where do they differ, and who's right?
5. Review each sub-agent's output *independently*, before looking at the integrated result.
6. Then review the integration. Any seams?

**The question worth sitting with:** did delegation produce a better result, or just a faster one that was harder to check? Both are legitimate answers. Knowing which one you got is the skill.

---

## What to take away

1. **Delegation moves you from reviewing output to auditing a process you didn't watch.**
2. **Cascading errors are the defining risk** — early mistakes get laundered into confident downstream work.
3. **Approve the decomposition before execution.** Most failures are visible in the plan.
4. **If a sub-agent's output can't be verified alone, the decomposition is wrong.**
5. **Level 4 autonomy needs Level 4 governance.** Approving artifacts isn't enough when the system is making structural choices.

---

**Next:** [Module 9 — Evaluating Agent Work](09-evaluating-agent-work.md)

*Part of [From Vibe Coding to Agent Engineering](../README.md). Autonomy levels and their governance requirements are developed in [Agentic CoE](https://github.com/MarioLazo/agentic-coe).*
