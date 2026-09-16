---
name: image-generation-production
description: Turn a commercial visual brief into a controlled AI image-generation plan, reusable prompt, reference-image protocol, and delivery checklist. Use for product visuals, campaign key visuals, social content, editorial imagery, and image editing.
---

# Image Generation Production

Use this skill to produce a repeatable visual-generation plan, not a one-off style-word dump.

## Required inputs

- Purpose and delivery format: channel, aspect ratio, copy-safe area, and whether it is concept or final production.
- Hero subject: product, person, object, or spatial scene; list non-negotiable details.
- Brand direction: audience, palette, tone, and approved assets.
- References: label each one as `product`, `identity`, `style`, `composition`, `pose`, or `mood`.
- Constraints: rights, prohibited content, required text, and delivery deadline.

## Workflow

1. Write one visual proposition. Do not begin with multiple competing concepts.
2. Select the control route: natural-language generation/editing, style exploration, structured prompting, or ComfyUI workflow.
3. Give each reference image one primary role. Resolve conflicting references before generating.
4. Build the first prompt with: output, hero subject, subject relationship, composition, setting/materials, art direction, and constraints.
5. Generate a direction board first. Lock the selected composition before pursuing detail.
6. Use image-to-image, masks, or control images to preserve product geometry, identity, pose, or layout.
7. Put final brand typography, prices, legal copy, and dense information back into design software.
8. Save prompt, model/workflow, seed where available, references, and final QA result.

## Delivery

Return:

- A concise generation brief.
- The reusable prompt in English, with variables in `[brackets]`.
- Reference-image role mapping.
- Recommended iteration path and a QA checklist.

Read [prompt framework](references/prompt-framework.md) before writing a commercial prompt. Use [creative brief](templates/creative-brief.md) when the input is ambiguous.
