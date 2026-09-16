# Placement recipes

Use these target recipes for the S01–S07 downstream adaptation layer. They are delivery recipes, not new material directions.

| Slot ID | Placement | Canvas | Composition and type rule |
| --- | --- | --- | --- |
| `home-banner` | 首页焦点 Banner | 1920 × 1080, 16:9 | Keep the primary message and focal subject in the central safe zone. Use one clear headline, one support line, and one CTA. Preserve at least 10% left/right, 15% top, and 20% bottom clearance for potentially overlaid chrome. |
| `feature-entry` | 功能入口卡 | 1080 × 1440, 3:4 | Compose as a fresh card, not a vertical crop. Give the headline at least two readable lines and keep CTA separate from the artwork edge. |
| `new-feature-feed` | 新功能弹窗 / 信息流大卡 | 1080 × 1350, 4:5 | Make the feature benefit visible at card scale. Keep only one message hierarchy and one CTA; avoid fake controls or dense interface chrome. |

## Prompt contract

State the slot ratio, exact H0 strings, Brand Kit, parent campaign signature, safe margins, and explicit prohibition on extra readable text. Prefix the visual prompt with its C5 typography contract: named type roles, hierarchy, line breaks, text-image relationship, contrast, and no distorted glyphs. When a Brand Kit contains an official logo file, pass that file as a locked provider reference and state its clear-space rule. Ask the image generator for a finished in-image-text raster deliverable, not a mockup, crop, background plate, or post-production layout.

## Sources informing the guardrails

- Google Play's current promotional-image guidance: keep critical elements in a safe zone because placements can be cropped across surfaces; it documents a 16:9 1920 × 1080 primary image and warns against borders. <https://support.google.com/googleplay/android-developer/answer/12929944>
- GitHub Marketplace's feature-card guide: treat the background image and readable text color as separate branded decisions; its example feature-card artwork is 965 × 482. <https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/writing-a-listing-description-for-your-app>
- `google-labs-code/design.md`: retain brand personality and design tokens as a shared, machine-readable source of truth between tools and agents. <https://github.com/google-labs-code/design.md/blob/main/docs/spec.md>
