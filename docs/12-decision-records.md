# Module 12 — Decision Records

> The pre-mortem predicts what will go wrong. The decision record captures what you chose and why — including the choices you later reverse. Together they close the loop.

**Time:** 20 minutes · **Prerequisites:** Sessions 2 and 4

---

## The gap this fills

Your architecture doc says what the system *is*. Your pre-mortem says what might
break. Neither captures the thing you'll actually need in six months: **why you
chose this over the alternative you seriously considered.**

That knowledge decays fastest and hurts most when it's gone. Six months on, a
choice that was carefully reasoned looks arbitrary — so someone "fixes" it,
rediscovers the original constraint the hard way, and reverts. You have paid for
the same lesson twice.

Agent systems make this worse, because so many decisions are non-obvious:
which model, what autonomy level, where the human sits, how much context to
retain, what the agent is allowed to touch. Every one of those has a defensible
alternative. None of them explain themselves from the code.

---

## The format

Short. One decision per record. Numbered, dated, never deleted.

```markdown
# 0007. Read-only database role for the reporting agent

**Status:** Accepted
**Date:** 2026-03-14

## Context
What forced a decision. The constraint, the pressure, what we knew at the time.

## Decision
What we chose. Stated plainly.

## Alternatives considered
What else was real, and why it lost. Not a strawman.

## Consequences
What this makes easy. What it makes hard. What we accept as a cost.
```

**"Alternatives considered" is the section that earns the document.** A record
that only states what you did is a changelog. One that states what you rejected
and why is a decision record, and it's the part that stops someone re-litigating
the choice from scratch.

---

## Status is not decoration

The status field is what makes a record set honest over time:

| Status | Means |
|---|---|
| **Proposed** | Under discussion, not yet acted on |
| **Accepted** | In force |
| **Superseded by NNNN** | Replaced — the record stays, the pointer is added |
| **Amended by NNNN** | Still largely in force, one part revised |

**Never delete a record. Never edit a decision after it's accepted.** Supersede
it. The trail of what you believed and when is the entire value; a tidy set of
only-current-decisions is a set that has erased its own reasoning.

---

## The reversal is the most valuable record you'll write

Here's a real one, worth studying because of how it ends.

A team building a coding agent designed a **credential proxy**: the sandboxed
worker process would hold no secrets at all. Requests routed through a proxy that
attached credentials *after* leaving the token-free worker. Genuinely elegant —
the process running model-chosen commands never holds a secret.

Months later they killed it. Their own reasons:

- **It only worked in one of three sandbox modes.** In the remote backend — the
  one where isolation matters most — credentials were injected directly, because
  there was no network to hang the proxy off. The invariant was already false, and
  the codebase carried a documented exception saying so.
- **One knob, two mechanisms.** The same setting behaved differently depending on
  a backend nobody chose for security reasons.
- **The machinery kept growing:** a per-run network, a CA folded into the worker's
  trust store synchronously before first use (a race that needed its own
  regression test), a teardown ordering constraint, and a decoy token planted in
  the worker's environment purely because a CLI refuses to run with no token at
  all. Every one of those is a thing that breaks.
- **And the finding that settles it: it was never an exfiltration barrier.**
  Egress was *cooperative* — the worker was **pointed** at the proxy by
  convention, via environment variables that well-behaved libraries honour. A
  model that ignored them was never constrained by it at all.

> **Read that last point again, because it generalizes.** The control worked
> exactly as designed. It just didn't do the thing everyone believed it did.
>
> That's [the Meaning Gap](../frameworks/README.md) inside a security control:
> high confidence in a system that was solving a different problem than the one
> people thought. And the only reason it's legible now is that someone wrote down
> what they believed when they built it.

Without the original record, killing it looks like regression. With it, the
reversal is visible as progress — and the reasoning survives for whoever
considers building one again.

---

## Cooperative vs. enforced — the idea to steal

The sharpest transferable concept from that reversal, stated generally:

> **A boundary the agent has to cooperate with is not a boundary.**

Ask it of every guardrail you build:

| Cooperative (a convention) | Enforced (a property) |
|---|---|
| Environment variables the agent is expected to honour | Network egress denied at the container level |
| "Do not modify files outside `src/`" in the prompt | Filesystem mount that only contains `src/` |
| A rate limit the agent is asked to respect | A rate limit in the calling layer |
| "Ask before deleting" in the instructions | No credential with delete permission |

Cooperative controls aren't worthless — they shape default behavior and catch
honest mistakes. But **do not count them as safety**, and never describe them to a
stakeholder as though they were. Ask of each one: *what happens if the agent
simply doesn't cooperate?* If the answer is "nothing stops it," you have a
convention.

This is [Module 10](10-security-sandboxing-guardrails.md)'s least-privilege
principle arriving from the other direction: the permission you never granted is
the only one that can't be ignored.

---

## What to record in an agent project

Decisions worth a record, from experience:

- **Model choice** — and what you'd switch to, under what trigger
- **Autonomy level** — which of the [4 Modes](../frameworks/README.md#1--the-4-modes), and why not the next one up
- **Where the human sits** — which actions need approval, and the risk reasoning
- **Context strategy** — retention, compaction, what you accept losing
- **What the agent may touch** — and what you deliberately withheld
- **Anything you tried and abandoned** — the highest-value records in the set

That last one is the discipline. The instinct is to document what shipped. The
value is in documenting what didn't, and why.

---

## Exercise 12.1 — Write the reversal you already have

**Time:** 20 minutes

1. **Find a decision you already changed** in your project. Everyone has one by
   Session 5 — a prompt approach abandoned, a scope cut, a tool swapped.
2. **Write the original as an ADR**, honestly — as you understood it *then*, not
   with hindsight smuggled in.
3. **Write the superseding record.** What did you learn? Was the original wrong,
   or right-then-and-wrong-now? Those are different, and the distinction is worth
   stating.
4. **Check for the pattern in the reversal above:** did the original control work
   as designed but not do what you assumed? If so, name that explicitly. It'll
   happen again in a different disguise.

---

## What to take away

1. **Architecture docs say what. Pre-mortems say what might break. Decision records say why** — and why decays fastest.
2. **"Alternatives considered" is what separates a decision record from a changelog.**
3. **Never delete, never edit — supersede.** The trail is the value.
4. **Reversals are the most valuable records you'll write.**
5. **A boundary the agent has to cooperate with is not a boundary.**
6. **A control can work exactly as designed and still not do what you believe it does.** Writing down the belief is how that becomes discoverable.

---

*Part of [From Vibe Coding to Agent Engineering](../README.md). The credential
proxy example is drawn from the publicly documented ADR set in
[Building a Coding Agent From Scratch](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course)
(Decoding AI, Apache-2.0) — see [REFERENCES](../REFERENCES.md).*
