# Real-World Scenarios

Five anonymized case studies from actual enterprise implementations. Each teaches
one specific lesson about what goes wrong in production, and each is referenced
at a particular point in the curriculum where the lesson lands hardest.

These are used as teaching material, not illustrations. The point of each is that
the team involved was competent and the failure still happened.

---

## 1 · IAM Modernization

**Used in:** Session 2 — Design & Pre-Mortem

A financial services firm built an agent to modernize identity and access
management rules. It worked perfectly against sample datasets. In production it
hallucinated rules that did not exist in the source system. Three weeks of manual
remediation followed.

> **Lesson:** demo success does not guarantee production reliability. Validation
> mechanisms must be designed *before* building, not added after the first
> failure.

**Why it's taught at the pre-mortem:** this is what skipping the pre-mortem costs.
The failure mode was predictable — sample data was clean, production data wasn't —
and thirty minutes of structured prediction would have surfaced it.

---

## 2 · Healthcare Authorization

**Used in:** Session 6 — Approval Gates

A prior-authorization agent shipped with uniform approval gates: every action
required human review. Throughput dropped 70%. The fix was risk-stratified gates —
auto-approve low-risk, flag medium, full review for high — which restored speed
without giving up safety.

> **Lesson:** approval gates should align with risk level, not be applied
> uniformly.

**The approval gate paradox:** uniform gates feel safer and are usually less safe
in practice, because reviewers facing hundreds of identical low-risk approvals
stop reading them. Graduated gates keep attention where it matters. Uniform
controls get disabled within a week; graduated ones survive.

---

## 3 · Legacy Code Migration

**Used in:** Session 5 — Observation³, Outward dimension

An agent migrated a legacy codebase file by file. Each file migrated correctly.
The system broke on integration, because the agent had no visibility into
cross-file dependencies and silently assumed there were none.

> **Lesson:** agents make assumptions you did not know you were making. Those
> assumptions become visible only at failure.

**Why it's taught with Observation³:** this is the Outward dimension in its purest
form. Nothing about the per-file output looked wrong. The failure lived in the
space between the units the agent was reasoning over.

---

## 4 · Document Knowledge Mining

**Used in:** Sessions 3 and 4 — Prompt Engineering, Evaluation

A document-analysis agent seemed accurate under spot-checking. Systematic
evaluation found that **15% of responses contradicted the source documents.**

> **Lesson:** subjective review creates false confidence. Systematic measurement
> creates reliability.

**The mechanism:** spot-checking samples non-randomly. Reviewers check the outputs
they find interesting or suspicious, which are unrepresentative in both
directions. It also fails against a specific failure mode — plausible, fluent,
confidently wrong output is exactly what survives a skim.

This scenario is also why the prompt "analyze this and extract insights" fails
where a structured prompt specification succeeds. Vague instructions produce
output that's hard to evaluate, which makes the 15% invisible.

---

## 5 · Medical Device Support

**Used in:** Session 4 — Evaluation & Demo

A support agent generated confident, correct-sounding responses even when it
lacked sufficient information to answer. It never signalled uncertainty, because
nothing in its design asked it to.

> **Lesson:** design agents to recognize and communicate uncertainty rather than
> hallucinate plausible answers.

**Why this is the hardest one to fix:** fluency and confidence are what the model
is optimized for. An agent that says "I don't have enough information" looks
worse in a demo than one that guesses well. The design has to make the
uncertainty path explicit — a defined output for the "insufficient information"
case, and evaluation that rewards using it.

Related: the Production Gate Question. If the agent gives a confident answer to a
question it can't actually answer, how would you know?

---

## Reading these as a set

Four of the five share a shape: **the failure was invisible at the unit level and
only appeared in aggregate or at integration.** That is the defining
characteristic of agent failure modes and the reason this course front-loads
pre-mortems and systematic evaluation.

The fifth (Healthcare Authorization) is the exception, and it's the one about
governance design rather than technical failure — which is why it points toward
the organizational material rather than the engineering material.

| Scenario | Failure was invisible at | Caught by |
|---|---|---|
| IAM Modernization | Sample-data testing | Production |
| Legacy Code Migration | Per-file review | Integration |
| Document Knowledge Mining | Spot-checking | Systematic evaluation |
| Medical Device Support | Response quality review | Uncertainty testing |
| Healthcare Authorization | — (worked, but unusably) | Throughput measurement |

---

*Part of [From Vibe Coding to Agent Engineering](../README.md).*
