# Context Engineering — Context Engineering

> Every agent you build will eventually run out of room. What happens then is a design decision, and most people never make it — they just find out.

**Supports Sessions 9–10** — orchestration, where context multiplies across agents

**Time:** 25 minutes · **Prerequisites:** Microagents & Project Knowledge

---

## The failure nobody plans for

Your agent works. Then a session runs long, the context window fills, and one of
three things happens:

1. **It truncates.** The model silently loses the earliest part of the
   conversation — often the instructions that defined the task.
2. **It errors.** Better, because at least it's visible.
3. **It degrades.** Cost and latency climb with every turn while quality quietly
   drops, and nobody connects the two.

The third is the dangerous one. There's no error, no alert, and no moment where
anyone says "the agent got worse." It just costs more and works less well, and by
the time someone investigates, the assumption is that the model changed.

**This is a Tuesday-at-3pm problem.** It doesn't show up in a demo, because demos
are short.

---

## Context is a budget with three claimants

At any moment your window is being spent on:

| Claimant | What it is | Grows with |
|---|---|---|
| **Instructions** | System prompt, project knowledge, skills | Your setup — fixed per session |
| **History** | The conversation so far, including tool calls and their output | Session length |
| **Working set** | The files, data, and results currently in play | Task complexity |

Instructions are the part you control directly ([Microagents & Project Knowledge](microagents.md)).
History is the part that grows without anyone deciding it should. **Tool output is
usually the largest and least examined component** — a single directory listing or
test run can consume more than the entire system prompt.

**Measure it before you optimize it.** Most people guess wrong about which claimant
dominates.

---

## Compaction: three tiers, cheapest first

The pattern that works is a cascade — try the cheap thing, escalate only when it
isn't enough.

### Tier 1 — Mechanical compaction (no model call)

Strip the *bodies* of old tool outputs while keeping the fact that the call
happened and what it returned in summary. Zero cost, zero latency, no risk of a
summarizer misrepresenting anything.

Surprisingly effective, because tool output dominates history in most real
sessions and the details stop mattering once you've acted on them.

### Tier 2 — Summarizing compaction (model call)

Replace older history with a generated summary, keeping a verbatim tail of recent
turns. Costs a call, and introduces real risk: **a summary that drops the wrong
detail is worse than truncation, because it looks complete.**

Two things make this safe enough to use:

- **Persist the compaction**, don't just hold it in memory. Write a checkpoint —
  the summary plus the kept tail — so a resumed or replayed session reconstructs
  the same state rather than a different one.
- **Keep a real tail.** Summary-only loses the specificity the model needs to
  continue coherently. The recent turns are the ones still being reasoned about.

### Tier 3 — Memory compression (on exit)

Long-lived memory — the facts an agent carries between sessions — needs its own
treatment. The naive approach drops the oldest lines when a cap is hit, which
loses old facts precisely because they're old, not because they stopped
mattering.

Compressing instead of dropping keeps the durable facts and discards the
redundant ones.

---

## Trigger on a fraction of the window, not a fixed number

The instinct is to compact at a threshold: "when history exceeds 50,000 tokens."
That breaks the moment you change models, because a number tuned for a 200k
window is wrong for a 1M window and catastrophic for a 32k one.

**Trigger relative to the window:**

```
compact when input_tokens >= context_window * (1 - reserve)
```

The reserve is headroom for the response and the next turn's tool output. Now the
same configuration behaves sensibly across models — which matters, because being
model-agnostic is one of the reasons to build this way at all.

---

## Make it visible

If compaction happens silently, two things follow: users don't understand why the
agent "forgot," and you can't tell whether your thresholds are sane.

Minimum viable visibility:

- **A context gauge** — how full is the window right now
- **A log line when compaction fires** — which tier, what triggered it, what it cost
- **A manual trigger** — let a user compact deliberately before starting something big

The manual trigger matters more than it sounds. It converts compaction from
something that happens *to* the user into something they can use.

---

## Where this lands in the frameworks

**Production Readiness** gains a row:

| Tier 1 (Doing) | Tier 2 (Deciding) | Tier 3 (Delegating) |
|---|---|---|
| Know your token usage per task; know your window | Compaction strategy defined and triggered on window fraction | Compaction persisted and replay-safe; per-agent context budgets |

**Evaluation** — compaction affects all four dimensions, which is why it's easy to
misdiagnose:

- **Accuracy** drops if the summary loses something load-bearing
- **Latency** improves after compaction, spikes during it
- **Cost** is the whole point — but a summarizing call isn't free
- **Failure rate** should fall, since window-overflow failures disappear

**Test it explicitly:** run your evaluation suite on a session long enough to
trigger compaction, and compare against the same tasks in a fresh session. If
accuracy drops, your summary is losing something. That's a real experiment, and
almost nobody runs it.

---

## Exercise 11.1 — Find your ceiling

**Time:** 25 minutes

1. **Instrument first.** Log input tokens per turn. You can't manage what you
   aren't measuring.
2. **Run a session until something breaks** — truncation, an error, or visible
   degradation. Note the turn count and token count.
3. **Categorize the spend** at the breaking point: what fraction was instructions,
   history, tool output? Most people are wrong about this before they measure.
4. **Implement Tier 1 only** — blank old tool-output bodies. Re-run. How much
   further did you get?
5. **Decide whether you need Tier 2.** For many single-purpose agents, mechanical
   compaction plus a shorter task is enough. Reach for a summarizer because you
   measured a need, not because it sounds sophisticated.

---

## What to take away

1. **Running out of context is a design decision you make by default if you don't make it deliberately.**
2. **Silent degradation is the real failure mode** — no error, rising cost, falling quality.
3. **Tool output usually dominates history.** Measure before optimizing.
4. **Cheapest tier first.** Mechanical compaction costs nothing and often suffices.
5. **Trigger on a fraction of the window**, so the design survives a model change.
6. **Persist compaction** or your replays diverge from your original runs.
7. **A summary that drops the wrong detail is worse than truncation**, because it looks complete.

---

**Next:** [Decision Records — Decision Records](decision-records.md)

*Part of [From Vibe Coding to Agent Engineering](../README.md).*
