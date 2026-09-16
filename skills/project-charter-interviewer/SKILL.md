---
name: project-charter-interviewer
description: Conduct structured project-discovery interviews and turn ambiguous briefs, meeting notes, or stakeholder inputs into an actionable Project Charter. Use when a user needs to clarify a new project, define goals and scope, surface risks and dependencies, align stakeholders, prepare a kickoff, or write a project charter / 立项访谈纪要 / 项目章程.
---

# Project Charter Interviewer

Turn an ambiguous request into a decision-ready charter. Adapt the depth to the project's scale. Do not invent facts, owners, dates, budgets, baselines, or approvals.

## Start With Available Context

1. Read supplied briefs, research, meeting notes, product documents, links, or prior decisions.
2. Extract confirmed facts into: background, desired outcome, audience, scope, constraints, stakeholders, timing, dependencies, and unknowns.
3. State the current understanding in 3-6 bullets before questioning. Mark unverified statements as assumptions.
4. Use the confirmed facts to avoid asking the user to repeat information already provided.

## Run The Interview In Rounds

Ask no more than five high-value questions per round. Use direct, answerable questions. Offer options only where they reduce ambiguity; leave room for the user's own answer.

### Round 1: Outcome And Value

Clarify the business problem, target users, expected change, and why the work matters now.

- What decision, behavior, or metric should this project change?
- Who is the primary user or customer segment?
- What is the minimum observable result that would make this initiative worthwhile?
- What happens if the project does not proceed?

### Round 2: Scope And Deliverables

Separate the essential deliverable from desirable follow-on work.

- What must be delivered for the first usable release or milestone?
- What is explicitly out of scope?
- Which channels, regions, platforms, formats, or languages are included?
- What existing assets, systems, or work can be reused?

### Round 3: Execution Conditions

Identify decision rights and constraints early.

- Who sponsors the project, owns delivery, approves key decisions, and supplies inputs?
- What fixed dates, budget limits, legal requirements, brand rules, technical limits, or vendor commitments apply?
- Which external teams, tools, data sources, or approvals can block progress?
- What is the preferred review cadence and final sign-off path?

### Round 4: Measurement And Risk

Turn vague success language into observable evidence.

- Which leading and lagging indicators will be tracked? What is the baseline, target, and measurement window?
- What could most likely delay, weaken, or invalidate the work?
- What assumptions must be tested first?
- What decision is needed now to unblock the next step?

## Synthesize Before Continuing

After each round, summarize answers, list changed assumptions, and identify remaining decision gaps. Do not proceed to detailed planning when the project goal, primary audience, or scope boundary is still unclear.

If the requester cannot answer a question, record an explicit assumption with an owner and a validation date instead of filling the gap yourself.

## Produce The Project Charter

Use [assets/project-charter-template.md](assets/project-charter-template.md) as the output structure. Create a concise charter in the user's language and include:

- a one-sentence project statement;
- measurable success criteria, clearly marked as confirmed or proposed;
- in-scope and out-of-scope boundaries;
- deliverables and milestone-level timeline;
- stakeholder roles and decision rights;
- dependencies, assumptions, and open decisions;
- a risk register with an owner and mitigation for every material risk;
- immediate next actions with owner and due date when known.

Keep the main charter scannable. Place unresolved detail in the decision log rather than hiding it in prose.

## Handle Common Situations

Read [references/interview-patterns.md](references/interview-patterns.md) when choosing questions for a creative campaign, product feature, operational workflow, or research initiative. Read [references/risk-and-metrics.md](references/risk-and-metrics.md) when defining risks, dependencies, baselines, and success measures.

- **Only a vague idea is provided:** run Round 1 first; do not draft a delivery plan.
- **A solution is prescribed but the goal is unclear:** ask what outcome the solution is intended to achieve, then validate alternatives.
- **Stakeholders disagree:** represent each position neutrally, identify the decision owner, and record the decision required.
- **A deadline is fixed:** work backward from the deadline, expose trade-offs, and label the minimum viable scope.
- **A creative project is requested:** define the audience insight, message hierarchy, channels, deliverable formats, approval route, and usage rights.

## Quality Check

Before delivering, verify that the charter:

1. Distinguishes confirmed facts, assumptions, and open decisions.
2. Names a measurable outcome rather than only activities or outputs.
3. Includes explicit exclusions to prevent scope drift.
4. Assigns every material risk, dependency, and next action to an owner when one is known.
5. Does not expose private, confidential, or personally identifying information unnecessarily.
