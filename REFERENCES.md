# References & Evidence Base

Sources behind the claims in this course, plus related material worth your time.

**Sourcing standard used here:** peer-reviewed research, longitudinal industry
data, and primary sources first. Vendor content is cited only where it's the
authoritative source for its own product. Forum discussion and secondary
commentary are excluded — they're useful for sensing where practitioners are
frustrated, but they are not evidence, and this course asks students to hold
their own claims to a standard it should meet itself.

Last reviewed **2026-08**.

---

## The evidence for the production gap

The central claim of this course — that AI-assisted development increases
velocity while degrading system-level reliability — rests on convergent findings
from independent sources measuring different things.

| Finding | Source |
|---|---|
| **+3.4% code quality, −7.2% delivery stability.** Each 25 percentage points of AI adoption correlated with a 7.2% decrease in delivery stability | [DORA — State of DevOps Report 2024](https://dora.dev/research/) |
| **211 million changed lines analyzed (2020–2024).** Code churn projected to double; cross-file function calls down 35%; refactoring line moves down 70% | [GitClear — AI Code Quality Research](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) |
| **1.7× more major issues, 75% more logic errors, 2.74× higher rate of security vulnerabilities** in AI co-authored code without rigorous discipline | CodeRabbit review analysis |
| **PRs 18% larger, incidents per PR up 24%, change failure rates up 30%** | [Osmani — Code Review in the Age of AI](https://addyo.substack.com/p/code-review-in-the-age-of-ai) |
| **32% of practitioners cite output quality as the single largest barrier** to deploying multi-agent systems in production | LangChain — State of Agent Engineering survey |

**Why these agree despite measuring different things.** DORA measures delivery
outcomes, GitClear measures code structure, CodeRabbit measures defect density,
and LangChain measures practitioner-reported blockers. Four different
methodologies converging on the same conclusion is stronger evidence than any one
of them alone.

**The pattern:** micro-quality improves — individual functions are cleaner, more
idiomatic, better commented. System-level dependability degrades — more churn,
fewer cross-file abstractions, less refactoring, higher change-failure rates. AI
is good at the unit and poor at the seams, which is exactly where the
[case studies](case-studies/README.md) show production failures occurring.

### Academic

- [The Productivity-Reliability Paradox: Specification-Driven Governance for AI-Augmented Software Development](https://arxiv.org/abs/2605.01160) — arXiv
- [Security Degradation in Iterative AI Code Generation: A Systematic Analysis of the Paradox](https://arxiv.org/abs/2506.11022) — arXiv
- [Agentic Problem Frames: A Systematic Approach to Engineering Reliable Domain Agents](https://arxiv.org/html/2602.19065v1) — arXiv
- [From Prompt–Response to Goal-Directed Systems: The Evolution of Agentic AI Software Architecture](https://arxiv.org/html/2602.10479) — arXiv
- [The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents](https://arxiv.org/abs/2511.03690) — arXiv

---

## Primary sources

- **Andrej Karpathy** coined "vibe coding" in February 2025. Read the original framing before reading anyone's interpretation of it.
- [Karpathy — 2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/)
- [Addy Osmani — Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/) — the most practical articulation of the workflow
- [Osmani — The 80% Problem in Agentic Coding](https://addyo.substack.com/p/the-80-problem-in-agentic-coding) — assumption propagation, abstraction bloat, sycophantic agreement

---

## OpenHands

- [Documentation](https://docs.openhands.dev) · [SDK Guide](https://docs.openhands.dev/sdk) · [Prompting Best Practices](https://docs.openhands.dev/openhands/usage/tips/prompting-best-practices)
- [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) — the SDK with 24+ examples
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — core platform
- [OpenHands Cloud](https://app.all-hands.dev) — free credit for getting started

**Current capabilities (mid-2026):** multi-agent delegation via `TaskToolSet`,
microagents that auto-load project knowledge, native sandboxed execution,
model-agnostic routing, built-in security analysis, inline critic/verification
results.

**SWE-bench Verified:** 68.4% with Claude Opus 4.6, ~52% with Qwen3-235B-A22B,
46.8% with Devstral 24B. See
[Module 9](docs/09-evaluating-agent-work.md) for how to read those numbers —
and how not to.

---

## Related courses

### Building a Coding Agent From Scratch — *Decoding AI*

[decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course)
· Apache-2.0 · 8 articles, 4 videos, one codebase

*"From agent user to agent builder: build a Claude Code-style coding agent from
scratch in Python."*

**This is the technical complement to this course, and the two are genuinely
different in audience and intent:**

| | This course | Building a Coding Agent From Scratch |
|---|---|---|
| **Audience** | Practitioners who need to use, evaluate, and govern agents — analysts, architects, engineering leads, developers who aren't AI specialists | Engineers who want to build the harness itself |
| **You end up able to** | Scope, build, evaluate, and defend an agent system in production terms | Build a coding agent from first principles |
| **Core skill** | Judgment — what to build, how to know it works, what to do when it doesn't | Implementation — agent loops, durable runtime, sandboxing, subagent fan-out |
| **Deliverable** | Three working agents plus a Solution Set you could put in front of a client | One codebase you understand completely |

If you finish this course and want to understand what's happening *inside* the
agent runtime — the loop, the permission model, context compaction, replay —
that's the right next step. It covers ground this course deliberately treats as
a given.

The reverse also holds: if you can build an agent harness but can't answer
"would you deploy this on a Tuesday at 3pm?", the material here is what's
missing.

*Cited with appreciation. No affiliation.*

---

## Reading by session

| Sessions | Reading |
|---|---|
| Before 1 | OpenHands docs — setup, configuration, agent patterns. Chain-of-Thought and ReAct primer |
| 2–4 | OpenHands prompt engineering best practices. Anthropic and OpenAI prompting guides |
| 5 | Observation³ framework — [frameworks/](frameworks/README.md#2--observation) |
| 6–8 | Human-in-the-loop design patterns. State management in multi-step workflows |
| 9–12 | Chaos engineering principles. Circuit breaker patterns. [OpenTelemetry](https://opentelemetry.io/docs/) for distributed tracing |
| 13–15 | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Presentation practices for technical demos |

---

## A note on citation quality

Students are asked in this course to document limitations honestly and to
distinguish measured results from assumptions. That standard applies to the
course material too.

Where a claim here rests on a single source, or on a vendor's own data, it says
so. Where sources disagree, that's noted rather than resolved silently. If you
find a claim in this repository that isn't supported by what it cites, open an
issue — that's a contribution, not a complaint.

---

*Part of [From Vibe Coding to Agent Engineering](README.md).*
