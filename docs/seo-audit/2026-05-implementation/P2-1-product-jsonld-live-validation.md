# P2-A1 Product JSON-LD Live Validation

Date: 2026-05-26
Branch: `feat/seo-product-jsonld-validation-p2`
Scope: live validation documentation only.

## Guardrails

- No Liquid changed.
- No JSON templates changed.
- No snippets changed.
- No Product JSON-LD changed.
- No price, variant, offer, availability, booking, cart, or checkout logic changed.
- No GA4/GTM changed.
- No redirects created.
- No MCP tools used.

## Tools Used

- Google Rich Results Test
- Schema Markup Validator

## Validation Summary

All four URLs below were tested manually on 2026-05-26. No critical structured data errors, invalid JSON-LD syntax, duplicate/conflicting Product schema issue, obvious zero-price Product Offer issue, currency mismatch, or availability mismatch was reported during manual validation.

| URL | Product detected | Product count | Offer count | Price values found | Currency | Availability | Duplicate Product risk | Errors | Warnings | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `https://lynxtour.cn/products/kunming-dali-lijiang-shangri-la-8-day-private-tour` | Yes, based on manual validation | Not recorded | Not recorded | No obvious zero-price issue reported | No mismatch observed | No mismatch observed | None reported in manual validation | None reported | Missing review and aggregateRating only | Pass / monitor only |
| `https://lynxtour.cn/products/jade-dragon-snow-mountain-private-tour` | Yes, based on manual validation | Not recorded | Not recorded | No obvious zero-price issue reported | No mismatch observed | No mismatch observed | None reported in manual validation | None reported | Missing review and aggregateRating only | Pass / monitor only |
| `https://lynxtour.cn/products/lijiang-to-shangri-la-private-tour` | Yes, based on manual validation | Not recorded | Not recorded | No obvious zero-price issue reported | No mismatch observed | No mismatch observed | None reported in manual validation | None reported | Missing review and aggregateRating only | Pass / monitor only |
| `https://lynxtour.cn/products/yunnan-private-car-charter-tour` | Yes, based on manual validation | Not recorded | Not recorded | No obvious zero-price issue reported | No mismatch observed | No mismatch observed | None reported in manual validation | None reported | Missing review and aggregateRating only | Pass / monitor only |

## Zero-Price Offer Check

No obvious zero-price Product Offer issue was reported during manual validation.

Because exact offer output was not copied, this remains a monitor item, not an implementation blocker.

## Conflict Check

No duplicate/conflicting Product schema was reported.

No app-injected Product schema conflict was reported by manual validation.

No review schema conflict was reported.

## Review / AggregateRating Decision

Missing review and aggregateRating warnings are acceptable.

Do not add review or aggregateRating unless verified product-level review data exists and can be safely connected to the Product JSON-LD.

## Recommended Next Action

No code change needed now.

Monitor only.

Proceed to P2-B canonical / OG / Twitter audit-only.

## Safety Note

This branch is validation-only.

No code behavior changed.
