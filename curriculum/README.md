# Curriculum

**12 taught sessions · 2 open workshop weeks · Demo Day · 15 calendar weeks**

The spacing is deliberate: foundational skills are front-loaded, then teams get
dedicated time for research, iteration, and polish before the final presentation.

> **The core question, asked of every design decision in this course:**
> **Would you deploy this agent on a Tuesday at 3pm?**

The mental models behind the curriculum are set out in
**[philosophy.md](philosophy.md)** — painkiller not vitamin, invert, vertical
slice, test drive the Ferrari, the three O's. Worth reading before Session 1;
they explain why the course is sequenced the way it is.

---

## The 3-project arc

Each project maps to one of the [4 Modes](../frameworks/README.md#1--the-4-modes)
and builds on the last.

| Project | Sessions | Mode | What you build |
|---|---|---|---|
| **1 · Assisted Agent** | 2–4 | **Doing** | A single agent executing one well-defined task within tight guardrails. Agent basics, prompt engineering, failure-first design. |
| **2 · Copilot Agent** | 6–8 | **Deciding** | A human-in-the-loop agent that recommends actions for approval. Multi-step workflows, feedback loops, trust calibration. |
| **3 · Multi-Agent System** | 10–12 | **Delegating** | An orchestrated system of coordinating agents. Task decomposition, distributed observability, governance, cost at scale. |

Sessions 1, 5, and 9 are milestones rather than build sessions — kickoff,
mid-course retrospective, and orchestration concepts.

---

## Semester map

| Week | Session | Topic | Key deliverables |
|---|---|---|---|
| 1 | 1 | Kickoff & Foundations | Self-assessment, environment setup, use case proposal |
| 2 | 2 | P1: Design & Pre-Mortem | Architecture doc, pre-mortem, repo setup |
| 3 | 3 | P1: Build & Prompt Engineering | Working agent, versioned prompts, unit tests |
| 4 | 4 | P1: Evaluation & Demo | Evaluation report, 5-min demo, playbook contribution |
| 5 | 5 | Mid-Course Review | Observation³ self-assessment, Project 2 proposal |
| 6 | 6 | P2: Design & Approval Gates | Workflow architecture, approval gate design, pre-mortem |
| 7 | 7 | P2: Build & Feedback | Working copilot agent, feedback logging, state management |
| 8 | 8 | P2: Testing & Approval Analysis | Integration tests, evaluation report, case study |
| 9 | 9 | Orchestration Concepts | Orchestration design doc, observability plan, cost model |
| 10 | 10 | P3: Core Orchestration Build | Working multi-agent orchestration, distributed logging |
| 11 | 11 | P3: Testing & Hardening | Chaos tests, circuit breakers, adversarial testing |
| 12 | 12 | P3: Checkpoint & Research Planning | Draft evaluation, plan for final deliverables |
| 13 | — | Open workshop: mockups & feedback | Informal demos, peer review, iteration |
| 14 | — | Open workshop: polish & rehearsal | Dry-run presentations, artifact refinement |
| 15 | Demo Day | Final presentations & submission | Recorded demos, Solution Set, portfolio, playbook |

**Expected time outside class:** 4–6 hours/week. More during build weeks
(3, 7, 10–11), less during design and review weeks.

---

## Session notes

Detail worth knowing beyond the map. Full teaching guidance lives in the
instructor materials.

### Session 1 — Kickoff & Foundations

Companion material: **[OpenHands Primer](openhands-primer.md)** — what the
platform is, how the SDK is structured, and the good-vs-bad prompt contrast.
Assign as pre-reading or work through it live during setup.

Establishes the **dev shop mental model**: engineering manager, solution
architect, onshore/offshore developers, business analysts, QA, trainers, support,
project manager. Understanding where you sit matters, because the agents you build
will assist, augment, or automate parts of these roles.

Students complete a **self-assessment** across three dimensions — functional
expertise (which dev-shop roles do you actually understand?), technical expertise
(languages, frameworks, honest proficiency levels), and growth interest (where
are you hungry to learn?).

*Teaching note:* review these before Session 2 and consider sharing anonymized
aggregates — "4 of 6 have backend experience, only 1 has worked with CI/CD."
Builds team awareness early.

### Session 2 — Design & Pre-Mortem

The pre-mortem is **inversion with a deadline** — don't ask how it works, ask how
it fails, and do it before the budget is spent. Specificity is the whole game.

> ❌ "The agent might fail."
> ✅ "The agent will hallucinate function signatures when given files with no type
> hints, detectable by comparing output to AST parsing."

The first is useless. The second is testable, and it tells you what to instrument
before you write a line of code.

Architecture doc covers five questions: what task, what inputs and outputs, what
boundaries, what success criteria, how will you observe it.

**Start a decision record set in the same session.** The architecture doc says
what the system is; the ADR says why you chose it over the alternative you
actually considered. Model choice, autonomy level, and what the agent may touch
are all worth a record from day one — and by Session 5 most students have their
first *reversal* to write, which is the more valuable document. See
[Decision Records](../deep-dives/decision-records.md).

Cover **black swans and typical events** both. You won't predict the black swan
correctly — that isn't the point. Asking the question provokes the recall:
someone says *"oh, we forgot about X."* X was always there; nobody had a reason to
say it out loud.

*Reference:* [IAM Modernization](../case-studies/README.md#1--iam-modernization) —
what skipping the pre-mortem costs.

### Session 3 — Build & Prompt Engineering

Demo-quality vs. production-quality prompting. Chain-of-Thought to make reasoning
visible. Error handling with retry logic and validation loops.

**Commit prompts to Git with meaningful messages, before and after changes.** This
habit looks like bureaucracy in week 3 and pays off in Session 8, when you analyze
which prompt changes actually moved your approval rate.

*Reference:* [Document Knowledge Mining](../case-studies/README.md#4--document-knowledge-mining)
— why "analyze this and extract insights" fails where a structured spec succeeds.

### Session 4 — Evaluation & Demo

Comprehensive evaluation across 10+ test cases spanning easy, medium, and hard.
Then compare your pre-mortem predictions against what actually happened.

**Demos are graded on honesty, not perfection.** A student who shows a failure and
explains what they learned is demonstrating more engineering maturity than one who
hides limitations.

### Session 5 — Mid-Course Review

[Observation³](../frameworks/README.md#2--observation) across Inward, Upward, and
Outward. Run as a structured workshop, not a lecture — individual completion
first, then rotate through three peer-discussion stations.

The **adversarial input exercise** (write five inputs designed to break your own
agent) reliably produces the most learning of any single activity in the course.

### Sessions 6–8 — The Copilot Arc

Approval gate design, then build, then approval-rate analysis.

Map the workflow **on paper first**, identifying every decision point where human
judgment adds value, before writing code. Session 7 is the most technically dense
build session — get the approval gate working end-to-end on a trivial workflow
before adding complexity.

In Session 8, analyze *rejection reasons*. If most rejections share a cause,
that's a prompt engineering opportunity — iterate and re-run the evaluation to
measure the improvement.

*Reference:* [Healthcare Authorization](../case-studies/README.md#2--healthcare-authorization)
— the approval gate paradox.

### Session 9 — Orchestration Concepts

Design-heavy, no coding. Decomposition into agent responsibilities, coordination
mechanisms (sequential, parallel, hierarchical), distributed observability, and
cost modelling of orchestrated vs. monolithic approaches.

Every student should leave with a decomposition plan critiqued by a partner.

**Also covered here: context budgets across agents.** Orchestration multiplies
context consumption — every sub-agent carries its own instructions and history.
Plan compaction and per-agent budgets at design time, not after the first
window-overflow. See [Context Engineering](../deep-dives/context-engineering.md).

### Sessions 10–12 — The Orchestration Arc

**Start with minimum viable orchestration** — two agents, one handoff, working.
This is the [vertical slice](philosophy.md#do-a-vertical-slice): one thin cut
through every layer rather than building each layer horizontally and integrating
at the end. Students who attempt the full system in one session typically finish
with nothing running.

Session 11's chaos testing is the eye-opener: deliberately kill an agent
mid-workflow and observe. The goal is graceful degradation, not perfection.
Document what breaks and what survives.

*Teaching note:* the Project 3 pre-mortem should be noticeably more sophisticated
than the Project 1 one. If it isn't, that's a coaching conversation.

### Weeks 13–15

No formal lecture in 13–14. Iterate, demo informally, rehearse.
**Nothing in the Week 15 presentation should be shown for the first time.**

---

## Assessment

| Component | Weight | Evaluated on |
|---|---|---|
| **Working code & documentation** | 45% | Functional agents across all 3 projects, production readiness items addressed, evaluation metrics reported, pre-mortems completed, **honest documentation of limitations** |
| **Playbook contributions** | 30% | Quality of your assigned sections — prompt templates, design patterns, evaluation rubrics, failure taxonomies. Individually assessed on clarity and usefulness |
| **Final presentation & peer review** | 25% | 15% demo quality + 10% peer review. Honest assessment of successes *and* failures |

---

## Student roles

Each student holds a primary domain and owns specific playbook sections —
differentiated to prevent overlap while requiring collaboration.

| Focus area | Playbook ownership |
|---|---|
| DevOps & Platform | Deployment patterns, infrastructure templates |
| AI/ML Engineering | Evaluation rubrics, guardrails library |
| Data Quality & Workflow | Data quality checklists, reporting templates |
| Core Agent Development | Agent architecture patterns, orchestration templates |
| Playbook Curation | Playbook structure, style guide, demo templates |
| Observability & Research | Observability templates, use case repository |

---

## Final deliverable: the Solution Set

A polished, reusable artifact modelled on a real client proposal — not a class
project binder. It demonstrates not just what you built, but how to scope, sell,
and deliver it.

| Component | Contents |
|---|---|
| **Executive summary** | One page: the solution, the business problem, measurable outcomes |
| **Problem statement & scope** | The modernization challenge, target systems, boundaries of the agent-assisted approach |
| **Solution architecture** | Agent roles, workflows, integration points, human oversight mechanisms |
| **Implementation approach** | Phased plan with milestones and resourcing, mapped to Doing → Deciding → Delegating |
| **Evaluation & metrics** | Accuracy, latency, cost, failure rate — with baseline vs. agent-assisted comparison |
| **Risk & mitigation** | Failure modes from your pre-mortems, with specific mitigations |
| **Cost model** | TCO including compute, human oversight, coordination overhead, scaling projections |
| **Recorded demo** | Narrated walkthrough explaining architectural decisions |
| **GitHub repositories** | Three portfolio-ready repos, clean READMEs, versioned prompts, documented results |
| **Community playbook** | Consolidated templates, patterns, rubrics, failure taxonomies |

---

## Environment setup

Confirm before Session 1:

- GitHub account with SSH key configured
- OpenHands installed and verified — can run a basic agent
- Python 3.10+ with a virtual environment
- Git workflow basics: branch, commit, pull request
- API keys for Claude or GPT-4, configured via environment variables — **never in prompts**
- Logging framework operational
- Async communication channel joined

---

*Part of [From Vibe Coding to Agent Engineering](../README.md).*
