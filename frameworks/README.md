# Frameworks

Four classification and measurement tools used throughout the course. Each one
answers a question you'll otherwise answer by instinct — and instinct is what
produces demos that die in production.

---

## 1 · The 4 Modes

**The question it answers:** what is my agent actually doing, and who remains accountable?

| Mode | What the agent does | Who is accountable | Example |
|---|---|---|---|
| **Doing** | Executes a single, well-defined task | The agent, within its defined scope | A unit test generator for pure functions |
| **Deciding** | Recommends actions; a human approves | The human who approves | A refactoring assistant that suggests changes and explains tradeoffs |
| **Delegating** | Coordinates multiple sub-agents | Humans, through oversight and guardrails | A feature generator orchestrating backend, frontend, test, and deploy agents |
| **Designing** | — this is always your role | You, the architect | You define constraints, scope, guardrails, and success criteria for all of the above |

> **The key insight: agents gain autonomy; humans gain responsibility.**
>
> That asymmetry is intentional. Even at the Delegating level, you remain
> accountable for what your agents do. Designing never transfers.

Use this to check design decisions, not to label systems after the fact. If you
can't say which mode you're building for, the scope isn't defined yet.

**The three projects map directly:** Project 1 is Doing, Project 2 is Deciding,
Project 3 is Delegating. You are Designing throughout.

---

## 2 · Observation³

**The question it answers:** what did I actually learn, as opposed to what I assumed?

Applied at the Session 5 mid-course review and again at the end of the course.

| Dimension | The question |
|---|---|
| **Inward** — data vs. assumptions | What did the actual data tell me? Where did instinct diverge from measured results? |
| **Upward** — stakeholder viability | Would a manager fund this? Does the value justify the cost and maintenance burden? |
| **Outward** — edge cases | What edge cases did I miss? What could an adversarial user do to break this? |

Most retrospectives only do Inward, and shallowly. Upward is what separates a
project that's technically interesting from one that survives a budget
conversation. Outward is where the adversarial-input exercise lives — write five
inputs designed to break your own agent, and run them.

---

## 3 · Production Readiness Checklist

**The question it answers:** would you deploy this on a Tuesday at 3pm?

Tiered by project. Items carry forward — Tier 3 includes everything before it.
Treat it as a minimum bar, not a ceiling.

| Category | Tier 1 (Doing) | Tier 2 (adds — Deciding) | Tier 3 (adds — Delegating) |
|---|---|---|---|
| **Logging** | Prompt/response logging with timestamps | Structured logs for multi-step workflows + feedback tracking | Distributed traces across agents + orchestration metrics |
| **Prompts** | Version control for all prompts in Git | Iteration tracking tied to approval rates | Versioned prompt chains with rollback |
| **Error handling** | Graceful failure messages + retry logic | Human escalation paths + error classification by severity | Circuit breakers between agents to stop cascades |
| **Cost tracking** | Token usage per task | + human review time per task | Full system cost: compute, oversight, coordination overhead |
| **Security** | Input sanitization; no secrets in prompts | Approval gate auth + audit trail | Agent-to-agent auth + least privilege + dependency scanning |
| **Testing** | Unit tests for core functions | Integration tests incl. simulated human approval | End-to-end orchestration tests + chaos testing |
| **Documentation** | README with scope **and limitations** | Decision log for approval/rejection rationale | Governance docs: escalation policy, kill switches, compliance |
| **Decision records** | ADRs for model choice, autonomy level, and what the agent may touch | + records for approval-gate design and rejection handling | + records for orchestration topology and inter-agent trust. **Reversals recorded, not deleted** |
| **Context** | Know token usage per task and your window size | Compaction strategy defined, triggered on window *fraction* not a fixed number | Compaction persisted and replay-safe; per-agent context budgets |
| **Durability** | Runs complete or fail visibly — no silent partial state | Interrupted workflows recover to a known state | Runs are resumable and replayable; replay reconstructs the same state |

Rows people skip and regret:

- **Cost tracking at Tier 2** — human review time is the cost that kills ROI, and nobody measures it.
- **"And limitations" in the Tier 1 README** — an agent whose boundaries aren't written down will be used outside them.
- **Context at Tier 1** — running out of window is a design decision you make by default if you don't make it deliberately. See [Context Engineering](../deep-dives/context-engineering.md).
- **Durability at Tier 2** — the first time a multi-step workflow is interrupted mid-run, you find out whether you designed for it. Usually you didn't.

**One test that applies to every Security row:** is this control *enforced*, or does it depend on the agent cooperating? A boundary the agent has to honour voluntarily is a convention, not a boundary — see [Decision Records](../deep-dives/decision-records.md#cooperative-vs-enforced--the-idea-to-steal).

---

## 4 · Evaluation Framework

**The question it answers:** is it actually working, or does it just look like it?

Four dimensions, tracked from your first agent run — not retroactively. The point
is building measurement into the workflow rather than bolting it on for the demo.

| Dimension | Measures | Project 1 | Project 2 | Project 3 |
|---|---|---|---|---|
| **Accuracy** | How correct is the output? | Manual review vs. ground truth | + human approval rate | End-to-end task completion rate |
| **Latency** | How fast does it run? | Response time (p50, p90, p99) | Multi-step workflow time | Orchestration overhead (total − sum of agent times) |
| **Cost** | What does it actually cost? | Token usage per task | + human review time | Full system cost incl. coordination |
| **Failure rate** | How often does it break? | % tasks needing manual fixes | % rejected at approval gates | % orchestration breakdowns |

**Why p90 and p99, not just average.** An agent that responds in 2 seconds on
average and 45 seconds at p99 is unusable for interactive work, and the average
hides that completely.

**Why orchestration overhead is its own metric.** Total time minus the sum of
individual agent times is the coordination tax. If it exceeds the work itself,
your decomposition is wrong.

---

## How these fit together

```
4 Modes            →  what am I building, and who's accountable?
Production Ready   →  what must be true before it ships?
Evaluation         →  is it working, measurably?
Observation³       →  what did I actually learn?
```

The first three run before and during a build. The fourth runs after, and it's
the one that makes the next project better than the last.

---

*Part of [From Vibe Coding to Agent Engineering](../README.md). The
organizational layer — operating model, risk tiers, governance structures — is
developed in [Agentic CoE](https://github.com/MarioLazo/agentic-coe).*
