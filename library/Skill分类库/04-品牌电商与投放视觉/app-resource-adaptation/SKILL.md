---
name: app-resource-adaptation
description: Generate, quality-check, and export finished App in-product marketing placements from any approved S01–S07 campaign. Use when a campaign needs home banners, feature-entry cards, popups, or feed cards; when adapting an approved material direction to App surfaces; or when building an offline resource-slot package without a publishing API.
---

# App Resource Adaptation

Treat App resource placements as a downstream adaptation layer, never as a new campaign direction. Read [references/placement-spec.md](references/placement-spec.md) before generating a placement.

## Required inputs

Require all of the following before an adaptation is final:

- Campaign Key Visual or approved source art.
- H0-approved copy; it is the only copy source.
- H1-locked Brand Kit and campaign identifier.
- H2 approval of the parent campaign.

If H2 is not complete, prepare a placement plan only. Do not present it as final or export-ready.

## Workflow

1. Lock the parent campaign context. Carry its Campaign Key Visual, H0 copy, Brand Kit, and quality constraints into every slot.
2. Mount this as a downstream Skill after the selected direction Skill (S01–S07). It does not create an eighth material direction. Support `home-banner`, `feature-entry`, and `new-feature-feed` unless the parent campaign requests a subset.
3. Re-enter the existing visual-generation path for each target ratio: H0 copy → H1 visual / Brand Kit → C5 typography prompt → image provider → C4 / OCR QA → H2. Never crop, stretch, frame, or post-compose the parent final.
4. Render the H0 strings verbatim as complete in-image typography. The C5 prompt must specify a page-specific type hierarchy, font roles, line breaks, contrast, text-to-image relationship, and safe frame for that ratio. Do not invent microcopy, UI labels, claims, logos, or a new CTA.
5. When an approved Brand Kit includes an official logo asset, pass it to the image-generation provider as a locked reference and reject altered, redrawn, missing, or unsafe logo treatment. Do not recreate the logo in text or vector.
6. Run the existing OCR, brand-consistency, legibility, safety-margin, and policy checks. If a placement fails, revise or regenerate that placement only; retain approved slots.
7. Package approved images with a machine-readable manifest containing `campaign_id`, `slot_id`, `size`, `copy_source: H0`, `brand_kit: H1`, `qa: PASS`, and `review: H2`.

## Delivery boundary

Expose only `生成资源位适配` and `导出资源位包` unless a real publishing integration is configured. Never label an export as uploaded, submitted, published, or successful. When a publishing integration is later available, add `提交至资源位` after the H2 gate.

## Quality gate

Reject a candidate if any approved glyph is cropped, unreadable, warped, incorrectly rendered, too close to an edge, or placed on a busy visual field. Reject a candidate that uses a parent image as a simple crop. Reject a candidate whose supplied official logo is redrawn, altered, missing, or placed without clear space. Keep one visual focal point and one primary CTA. Verify both full-size and card-scale readability.
