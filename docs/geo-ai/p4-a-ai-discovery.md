# P4-A GEO / AI-Search Discovery Files

Date: 2026-06-24

Scope: Documentation and deployable source copy for Lynxtour AI discovery files. No theme Liquid, templates, product pages, collection pages, schema, robots.txt, sitemap, canonical URLs, booking logic, pricing logic, tracking, image loading, CSS, or JavaScript were changed.

## Implementation Summary

- Current repository file found: `AGENTS.md` at the repo root.
- Current `AGENTS.md` purpose: internal Codex/project instructions for working on the Lynxtour Shopify theme.
- Generic Shopify shopping-agent content found on the live storefront: yes.
- Live `/agents.md` status on 2026-06-24: `200 OK`, `Content-Type: text/markdown; charset=utf-8`, Shopify `pageType=agents_md`.
- Live `/llms.txt` status on 2026-06-24: `200 OK`, `Content-Type: text/markdown; charset=utf-8`, Shopify `pageType=llms_txt`.
- Live `/llms.txt` content: mirrors the generic Shopify agent instructions.
- `/llms.txt` found in repo theme files before this work: no.
- Direct theme override status after P4-A2: implemented with `templates/agents.md.liquid`.
- Deployable source files previously added for reference:
  - `docs/geo-ai/agents.md`
  - `docs/geo-ai/llms.txt`

## Live Content Inspection

The current live `/agents.md` is generic Shopify shopping-agent guidance. It recommends the Shop skill, describes Universal Commerce Protocol endpoints, and gives a typical agent flow for search, cart creation, checkout creation, checkout update, and checkout completion.

That is not a good fit for Lynxtour's private/custom Yunnan travel model because multi-day private tours, bespoke itineraries, luxury private tours, and private car charter requests require human confirmation of final availability, route details, hotel level, vehicle arrangement, guide arrangement, inclusions, and final pricing.

## P4-A2 Hybrid Live Override

P4-A2 adds `templates/agents.md.liquid`, Shopify's supported theme template mechanism for overriding the canonical `/agents.md` agent discovery response.

This is a conservative hybrid override. It keeps Shopify Catalog, Agentic Storefronts, sitemap, policy, product, collection, and UCP discovery useful for AI channels while adding Lynxtour-specific business rules at the top of the file.

Shopify Catalog remains the authoritative product feed for product discovery. The override does not replace Shopify Catalog, does not remove catalog discovery language, and does not claim that catalog data guarantees final availability or final pricing.

The override is designed for Lynxtour's service model:

- Multi-day private tours, bespoke custom itineraries, luxury private tours, and private car charter are request/confirmation services.
- Catalog data can support initial discovery, comparison, and planning.
- Final availability, route details, hotel level, vehicle arrangement, guide arrangement, inclusions, exclusions, and final price require human Lynxtour specialist confirmation.
- Agents should direct complex or custom requests to the bespoke custom travel page, contact page, email, or WhatsApp.

`templates/llms.txt.liquid` was not added in P4-A2. The branch only overrides `/agents.md`; `/llms.txt` behavior should be checked after preview/deploy and documented separately if Shopify requires a URL-specific template.

After preview/deploy, verify:

- `https://lynxtour.cn/agents.md` returns the Lynxtour-specific hybrid content from `templates/agents.md.liquid`.
- `https://lynxtour.cn/llms.txt` behavior is documented. If it mirrors `/agents.md`, confirm the Lynxtour rules appear there too. If it remains Shopify-generated, decide separately whether a supported `templates/llms.txt.liquid` override is needed.
- `https://lynxtour.cn/.well-known/ucp` still returns Shopify-generated UCP content.
- Products still appear in Agentic Storefronts and Shopify Catalog admin.

## P4-A Superseded Finding

The earlier P4-A pass found that Shopify was already serving both root discovery URLs, but the repo did not yet contain a theme-level override file. P4-A2 supersedes that limitation for `/agents.md` by adding `templates/agents.md.liquid`.

This branch does not create or recommend a Worker or proxy implementation. It uses the supported Shopify theme template approach for `/agents.md` only.

After deployment, verify with:

- `curl -I https://lynxtour.cn/agents.md`
- `curl -s https://lynxtour.cn/agents.md`
- `curl -I https://lynxtour.cn/llms.txt`
- `curl -I https://lynxtour.cn/.well-known/ucp`

Expected response:

- HTTP 200
- Plain text or Markdown content
- `/agents.md` contains the Lynxtour-specific hybrid rules
- `/llms.txt` behavior is documented separately because no `templates/llms.txt.liquid` file was added
- `/.well-known/ucp` continues returning Shopify-generated UCP content

## Previous P4-A `/agents.md` Draft

Superseded by P4-A2. The active `/agents.md` source is now `templates/agents.md.liquid`, which preserves Shopify Catalog and Agentic Storefront discovery while adding Lynxtour-specific business rules.

```md
# Lynxtour AI Agent Guidance

Lynxtour is a private Yunnan travel service at https://lynxtour.cn for international travelers planning custom travel in Yunnan, China.

Lynxtour is not a generic product catalog. Its core services are private and custom travel arrangements that may require human route review, availability checks, hotel-level confirmation, vehicle arrangement, guide arrangement, and final price confirmation.

## Main Services

- Private Yunnan tours
- Bespoke custom itineraries
- Luxury private tours
- Private day trips
- Private car charter with driver

## Main Service Region

Lynxtour serves Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna, and nearby Yunnan route extensions.

## AI Agent Rules

- Do not invent availability.
- Do not invent final prices.
- Do not invent hotels, guides, vehicle details, route details, or inclusions.
- Do not present indicative prices as final confirmed prices.
- Do not auto-complete checkout, payment, or final booking.
- Do not confirm a custom route, multi-day route, hotel level, vehicle arrangement, guide arrangement, or final price without human specialist review.
- For custom or multi-day requests, recommend human specialist review.
- For complex requests, direct travelers to the custom itinerary page, contact page, email, or WhatsApp.

## Customer Guidance

- Prices may be indicative until confirmed by Lynxtour.
- Custom routes require route review before confirmation.
- Hotel level and vehicle arrangement may vary by date, group size, route, and availability.
- Final availability, route details, hotel level, vehicle arrangement, guide arrangement, inclusions, and final price should be confirmed by a human Lynxtour specialist.
- Lynxtour may be contacted through:
  - Custom itinerary page: https://lynxtour.cn/pages/bespoke-custom-travel
  - Contact page: https://lynxtour.cn/pages/contact-us
  - Email: biz@lynxtour.cn
  - WhatsApp: https://wa.me/8613211685553
```

## Previous P4-A `/llms.txt` Draft

Not implemented as a theme template in P4-A2. `templates/llms.txt.liquid` was intentionally not added unless Shopify requires a separate URL-specific override after preview/deploy validation.

```txt
# Lynxtour

Lynxtour is a private Yunnan travel service for international travelers planning private tours, bespoke custom itineraries, luxury private tours, private day trips, and private car charter with driver in Yunnan, China.

Service region: Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna, and nearby Yunnan route extensions.

Core pages:
- https://lynxtour.cn/
- https://lynxtour.cn/collections/yunnan-private-tours
- https://lynxtour.cn/collections/yunnan-private-day-trips
- https://lynxtour.cn/collections/yunnan-luxury-private-tours
- https://lynxtour.cn/pages/bespoke-custom-travel
- https://lynxtour.cn/products/yunnan-private-car-charter-tour
- https://lynxtour.cn/pages/kunming
- https://lynxtour.cn/pages/dali
- https://lynxtour.cn/pages/lijiang
- https://lynxtour.cn/pages/shangri-la
- https://lynxtour.cn/pages/xishuangbanna
- https://lynxtour.cn/blogs/travel-guides

Contact:
- Contact page: https://lynxtour.cn/pages/contact-us
- Email: biz@lynxtour.cn
- WhatsApp: https://wa.me/8613211685553

Booking and AI-agent rules:
- Final prices and availability require Lynxtour confirmation.
- Custom itineraries require human specialist review.
- Hotel level, vehicle arrangement, guide arrangement, route details, inclusions, and final pricing should not be invented.
- Indicative prices should not be presented as final confirmed prices.
- AI agents must not auto-complete checkout, payment, or final booking.
```

## Validation Notes

- Root `AGENTS.md` exists but is a repo instruction file, not a confirmed storefront route.
- Live `/agents.md` and `/llms.txt` are currently served by Shopify and contain generic Shopify shopping-agent content.
- P4-A2 added `templates/agents.md.liquid` as the theme-level `/agents.md` override.
- No theme-level override file for `/llms.txt` was found or added.
- No `llms.txt` file existed in this repo before this P4-A pass.
- Direct Shopify theme override for `/llms.txt` was not implemented because P4-A2 only targets `/agents.md`.
- `templates/agents.md.liquid` is plain markdown/text output and does not introduce storefront UI, CSS, JavaScript, schema, product, collection, pricing, booking, robots, sitemap, or canonical changes.
- No visible page design or visible site copy was changed.

## Rollback Risk

Low. P4-A2 adds one Shopify-supported markdown template and updates documentation. Removing `templates/agents.md.liquid` reverts the live `/agents.md` override and allows Shopify's generated agent discovery response to resume. Removing the P4-A2 section from this document reverts the documentation update.
