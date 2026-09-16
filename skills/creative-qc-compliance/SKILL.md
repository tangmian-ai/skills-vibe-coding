---
name: creative-qc-compliance
description: Audit creative outputs for visual quality, reference fidelity, brand consistency, readability, image-generation defects, and commercial compliance before delivery.
---

# Creative QC & Compliance

Use this skill after generation or adaptation and before an asset is marked delivery-ready.

## Review dimensions

- Brief fit: one clear message, correct audience and channel.
- Product and identity fidelity: product shape, packaging, logo handling, person/character consistency.
- Visual craft: composition, hierarchy, lighting, anatomy, materials, edge quality, and scale.
- Typography: correct copy source, legibility, safe margins, and no generated long-text errors.
- Reference handling: references used for their intended role without accidental style or identity drift.
- Commercial risk: rights, trademarks, endorsements, platform screenshots, factual claims, and prohibited content.
- Delivery: correct ratio, export, naming, source assets, prompt/workflow, and review status.

## Output format

```yaml
status: pass | needs_revision | blocked
issues:
  - severity: critical | major | minor
    finding: ""
    fix: ""
evidence_checked: []
release_notes: []
```

Read `references/` for the detailed high-quality generation, reference-reconstruction, consistency, and compliance standards.
