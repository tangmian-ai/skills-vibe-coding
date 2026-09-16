---
name: content-pipeline
description: Convert a content opportunity into a traceable AI production workflow with topic evaluation, creative plan, reference binding, generation steps, review gates, and reusable records. Use for social-video or image-led content pipelines.
---

# Content Pipeline

This skill organizes AI content production as a sequence of decisions and records. It does not claim that content has been published, submitted, or approved unless a real integration returns that result.

## Inputs

- Content goal, audience, channel, and format.
- Topic, source material, or trend signal.
- Available brand/product assets and reference media.
- Production constraints: model/tool, duration or ratio, budget, and approval owner.

## Workflow

1. Evaluate the topic: relevance, novelty, brand fit, production feasibility, and rights risk.
2. Define one production hypothesis and its success signal.
3. Produce a brief with hook, visual direction, story/shot structure, assets, and channel format.
4. Bind every reference to a specific role: product, character, setting, opening frame, ending frame, or style.
5. Generate by stage: direction test, selected route, controlled variants, then local fixes only where needed.
6. Review for factual claims, identity/product consistency, typography, safety, and channel fit.
7. Save the approved plan, prompt/workflow, inputs, output, review decision, and reasons for rejection.

## Output

Return a production packet: evaluation, creative brief, run plan, reference map, QA checklist, and archive paths.

Use [production brief](templates/production-brief.md). Supporting visual workflow examples are in the repository's `library/Skill分类库/03-内容生产与自动化工作流/`.
