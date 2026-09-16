---
name: project-charter-interviewer
description: Research, frame, and author a decision-ready Project Charter from a brief, link, notes, or ambiguous idea. Use when a user asks to initiate a project, assess a proposal, plan a campaign or product initiative, clarify goals and scope, identify stakeholders and risks, prepare a kickoff, or create a Project Charter / 立项书 / 项目章程. Research public context first, ask only irreducible decision questions, and deliver a completed charter rather than a blank form.
---

# Project Charter Interviewer

Produce a completed, evidence-backed charter that lets a sponsor decide whether to proceed, revise, or stop. Treat the charter as an initiation and alignment document, not a detailed project plan.

## Operating Standard

- Start from the supplied brief, files, meeting notes, and links. Extract facts before interpreting them.
- When the request concerns a named company, product, market, audience, regulation, platform, competitor, or current trend, research the public context before drafting. Prefer official sites, primary documentation, filings, app stores, and first-party product materials. Use reputable independent sources only when primary evidence is unavailable.
- Tag every material claim as **Confirmed**, **Researched**, or **Working assumption**. Give researched claims a direct URL. Do not invent customer data, budgets, deadlines, internal owners, performance baselines, approvals, or legal status.
- Do not hand the user an empty template. Synthesize a complete recommendation from available evidence. For information that cannot be truthfully inferred, state the uncertainty, select a conservative working assumption, explain its consequence, and assign a validation action.
- Ask questions only when an answer changes the recommendation materially and cannot be resolved through supplied material or public research. Ask a maximum of three together; while waiting, still deliver the strongest draft possible.
- Write in the user's language. Keep the main charter to roughly two to four screens unless the project is complex.

## 1. Build An Evidence Map

Before drafting, create a private working map with four columns: claim, source, confidence, and implication. Separate:

1. **Business facts:** existing product, audience, commercial model, strategy, prior results.
2. **Market facts:** category behavior, competitor positioning, platform requirements, regulation, timing.
3. **Project facts:** requested outcome, delivery constraints, materials, decision-makers, stated deadline.
4. **Unknowns:** missing information that changes value, scope, feasibility, cost, timing, or approval.

When browsing, capture only facts that affect a decision. Record the source URL beside the fact. Do not confuse an inference with a verified fact.

## 2. Choose The Right Charter Depth

Classify the request and tailor the charter. Do not force irrelevant sections into a small project.

| Project type | Emphasize |
| --- | --- |
| Brand or creative campaign | audience insight, message, channels, formats, production plan, rights, performance signals |
| Product or feature | user problem, current journey, opportunity, release boundary, instrumentation, rollout, adoption risk |
| Automation or operations | current process, trigger, inputs/outputs, exception path, human review, access control, time/quality gain |
| Research or strategy | decision to inform, hypotheses, evidence plan, sample/source quality, decision date |
| Event or launch | audience, run of show, partners, critical path, contingency, safety and communications |

## 3. Resolve Only The Irreducible Questions

Do not run a questionnaire by default. Use research and reasoning first. Ask only when one of these is unknown and materially changes the recommendation:

- sponsor or final decision owner;
- non-negotiable deadline, cost cap, or legal/brand constraint;
- primary outcome when two plausible outcomes conflict;
- scope boundary when inclusion choices create materially different delivery paths;
- baseline or measurement source when success cannot otherwise be assessed.

Phrase each question with a recommended default and the trade-off. Example: “I recommend treating the US English launch as the first release and deferring localization; should the first release include additional markets?”

## 4. Make The Recommendation

Choose a recommended path; do not merely list possibilities. Explicitly state:

- whether the initiative should **Proceed**, **Proceed with conditions**, **Run a short discovery**, or **Do not proceed yet**;
- the smallest viable scope that can validate the value hypothesis;
- what must be true for success;
- what should be removed first if time or capacity tightens;
- which decision or evidence is needed before the next stage gate.

Use ranges and confidence labels for early estimates. Never turn a guessed value into a hard commitment.

## 5. Deliver A Completed Charter

Use [assets/charter-delivery-spec.md](assets/charter-delivery-spec.md) as the required output contract. Deliver every section with actual prose, decisions, and tables. A section may be marked **Not applicable** only with a one-sentence reason; never leave blanks, `TBD`, or placeholder rows.

Include an evidence appendix only when research materially informed the recommendation. Keep confidential inputs anonymous and avoid exposing personal data or internal-only information.

## 6. Validate Before Delivery

Read [references/charter-standard.md](references/charter-standard.md) for the quality baseline and [references/research-protocol.md](references/research-protocol.md) before researching or citing public facts.

Verify that the final charter:

1. names the business problem and intended outcome, not just an activity;
2. distinguishes evidence, recommendation, and assumption;
3. makes scope exclusions and descoping order explicit;
4. gives success measures a source, baseline status, target logic, owner, and review moment;
5. includes material dependencies, risks, early warnings, mitigations, and owners;
6. identifies a decision owner, approval gate, and immediate next action;
7. uses links for external facts and makes no unsupported claim of certainty.
