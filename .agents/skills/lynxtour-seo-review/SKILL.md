---
name: lynxtour-seo-review
description: Use after Shopify Liquid SEO changes to review diffs for regressions, schema issues, duplicate metadata, Liquid mistakes, and indexation risks.
---

Review only the current diff unless asked to inspect more.

Check:
- Liquid syntax risk
- broken section schema
- duplicate title/meta/H1 logic
- canonical placement
- robots noindex/nofollow mistakes
- OG/Twitter fallback logic
- JSON-LD validity and duplicate schema risk
- product price/availability/schema consistency
- mobile layout regressions from SEO blocks
- accidental URL, handle, or template changes

Classify findings:
- Blocker: must fix before merge
- Suggestion: should fix soon
- Nit: optional cleanup

Rules:
- Do not rewrite the implementation unless asked.
- Be specific: cite file names and exact logic.
- If no serious issue exists, say it is safe to preview/test.
