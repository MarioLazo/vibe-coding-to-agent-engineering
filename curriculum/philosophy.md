# Operating Philosophy

The mental models behind the curriculum. These aren't abstractions — they're how
I actually work engagements, stated plainly. Each one maps to a point in the
course where it applies.

---

## Be a painkiller, not a vitamin

Zero in on one, two, three things that are genuinely painful. Not the full
capability map, not everything the technology *could* do — the specific pain
that has someone's attention right now.

A vitamin is nice to have. It gets deprioritized the moment budgets tighten. A
painkiller gets funded because not funding it costs more.

**Where it applies:** use case selection (Session 1). If you can't name whose pain
this is and what it costs them today, you've picked a vitamin.

---

## Invert, invert, invert

Ninety percent of how I look at things is inversion. Don't start with "how do we
make this work." Start with **"what's the biggest issue, and how does this fail?"**

Most of what I know came from post-mortems, not launches. Working backward from
failure surfaces the constraints that actually bind, and it does it before you've
spent the budget.

**Where it applies:** the pre-mortem (Session 2). The pre-mortem *is* inversion,
applied with a deadline.

---

## Test drive the Ferrari

Build a working prototype and put it in front of them early. Not a slide, not an
architecture diagram — something they can drive.

Two things happen. Expectations get set against reality instead of imagination.
And people become invested, which is the part that matters. **Unless people get
involved and invested early, they don't apply themselves** — and then every gap
surfaces at the end, as a surprise, in a meeting where someone has to be blamed.

**Where it applies:** Sessions 2 and 4. It's also why demos are graded on honesty
here — a prototype that hides its limitations sets the wrong expectation, which is
worse than no prototype.

---

## Do a vertical slice

Most implementation processes are heavyweight. They take forever, and by the time
they deliver, the problem has moved.

The alternative: **take a snippet of a use case and go end to end.** One thin
vertical cut through every layer — data, logic, interface, evaluation — rather
than building each layer horizontally and integrating at the end.

You learn where the real problems are in a week instead of a quarter. And the
problems are almost never where the architecture diagram says they'll be.

**Where it applies:** every project. Explicitly in Session 10 — start with the
minimum viable orchestration, two agents and one handoff, working. Students who
try to build the whole system in one session finish with nothing running.

---

## Approximate the data to provoke the conversation

You rarely get the real data early. That's fine — **use open-source or synthetic
data that approximates it**, and build against that.

The point isn't the data. It's that a working thing built on approximate data
provokes a much deeper conversation than a requirements document ever will.
People stop being polite about it. They say *"no, that's not how our data looks,
and here's what I actually care about."*

You've now learned the real requirement, and you didn't have to ask for it from a
position of authority. By then you've usually won the room.

**Where it applies:** Sessions 2–3. It's also the honest answer to "we can't start
until we have the data."

---

## Bake in black swans and typical events

When you plan, cover both the ordinary path and the improbable one. Not because
you'll predict the black swan correctly — you won't — but because **asking the
question provokes the recall.**

That's the actual mechanism. You ask "have we considered all the cases?" and
someone says *"oh — we forgot about X."* X was always there. Nobody had a reason
to say it out loud.

Most surprises in delivery are integration surprises and edge cases. Both are
findable in advance if you make room for the conversation.

**Where it applies:** the pre-mortem (Session 2), and the adversarial input
exercise (Session 5).

---

## The three O's — Observation³

When you're accountable for something and need to know whether it's actually
working, look in three directions:

| Direction | The question |
|---|---|
| **Inward** | What does the data say? Where did instinct diverge from measurement? |
| **Upward** | Are we hitting the strategic objective? Would a leader fund this? |
| **Outward** | What edge cases did we miss? What would an adversarial user do? |

Most retrospectives only look inward, and shallowly. **Upward** is what separates
a technically interesting project from one that survives a budget conversation.
**Outward** is where the failures you haven't met yet are hiding.

**Where it applies:** Session 5 and the final retrospective. Full treatment in
[frameworks](../frameworks/README.md#2--observation).

---

## Clarity, focus, cadence, plan, execute, manage exceptions

How I run delivery, in order:

1. **Clarity** — what are we actually solving
2. **Focus** — the one or two things that matter, not the list of twelve
3. **Cadence** — a rhythm people can rely on
4. **Plan** — sequenced, with what's deliberately not in scope
5. **Execute**
6. **Manage exceptions** — because there will be exceptions, and the plan is what makes them visible as exceptions rather than as chaos

The order matters. Cadence before plan is deliberate — a reliable rhythm makes a
mediocre plan survivable, and no plan survives an unreliable one.

**Where it applies:** project delivery across all three projects, and the Solution
Set's implementation approach.

---

## Distill the problem so it's cohesive and understandable

Clients are inundated. Every vendor is telling them something urgent, and most of
it is framed to sound sophisticated rather than to be understood.

The differentiator is being able to state the problem in a way that a room full of
people with different backgrounds all recognize as correct. That's harder than it
sounds and worth more than the architecture.

**Where it applies:** the Solution Set's executive summary. If it needs a glossary,
it isn't distilled yet.

---

## Going live is the only metric that counts

You can sing and dance and do anything. **At the end of the day you need to go
live.** Everything upstream — the architecture, the demo, the pilot — is
instrumental. The number one job is unblocking whatever stands between the work
and production.

Corollary: a system that works beautifully and hasn't shipped is a system that has
delivered nothing, no matter how good the evaluation numbers are.

**Where it applies:** the Tuesday-at-3pm question, which is this idea in
interrogative form.

---

## Crisis is an opportunity

When something blows up, that's usually when I get called in. The instinct is to
treat it as damage control. It isn't — it's the moment when people are finally
willing to look honestly at what's wrong.

The method: understand the expectation from the leadership side first, then the
tech stack, then what's already been tried. Then build a roadmap that fixes the
core issue rather than the symptom that got someone's attention.

You get one shot at that, and getting it right builds more trust than a project
that never broke.

**Where it applies:** Session 11 chaos testing, and the case studies — every one
of them is somebody's crisis.

---

## Agents need a hive mind, a semantic layer, and a harness

The architectural view underneath the course:

- **A hive mind knowledge structure** — shared knowledge the agents draw on, rather than each one reasoning from scratch
- **A consistent semantic context layer** — so "customer" means the same thing to every agent in the system
- **A harness** — the scaffolding that runs, constrains, observes, and evaluates them

Most agent projects build the agent and skip all three. Then they discover that
five agents with five private interpretations of the domain don't compose.

**Where it applies:** Session 9 orchestration design, and
[Module 7](../docs/07-microagents-and-project-knowledge.md).

---

## Stage deliberately, and prove it with numbers

The way to build trust with a skeptical organization is to stage the work in a
deliberate, foundational sequence — with a human in the loop — and to generate the
metrics that show it's working as you go.

The numbers that matter, every time: **latency, scale, cost, and compliance.**
Those are the gates. A system that's accurate and fails any of the four doesn't
ship.

**Where it applies:** the [Evaluation Framework](../frameworks/README.md#4--evaluation-framework)
and the Production Readiness Checklist.

---

## No BS

Say what's actually true, including when it's inconvenient. Be direct about what
you don't know. Don't dress up a limitation as a feature.

This is why demos in this course are graded on honesty rather than polish, and why
a well-documented failure is worth more than a demo that hides its edges. It's
also the standard the course material holds itself to — see the
[sourcing note](../REFERENCES.md#a-note-on-citation-quality).

---

*Part of [From Vibe Coding to Agent Engineering](../README.md).*
