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
- Direct theme override: not implemented because this repo does not contain a Shopify-supported theme file that controls the generated `/agents.md` or `/llms.txt` root routes.
- Deployable source files added for an edge/static-route implementation:
  - `docs/geo-ai/agents.md`
  - `docs/geo-ai/llms.txt`

## Live Content Inspection

The current live `/agents.md` is generic Shopify shopping-agent guidance. It recommends the Shop skill, describes Universal Commerce Protocol endpoints, and gives a typical agent flow for search, cart creation, checkout creation, checkout update, and checkout completion.

That is not a good fit for Lynxtour's private/custom Yunnan travel model because multi-day private tours, bespoke itineraries, luxury private tours, and private car charter requests require human confirmation of final availability, route details, hotel level, vehicle arrangement, guide arrangement, inclusions, and final pricing.

## Shopify Route / Override Limitation

Shopify is already serving both root discovery URLs, but the controlling implementation is not present in this theme repo. This repo contains no `templates/agents.md.liquid`, `templates/llms.txt.liquid`, setting file, or route-specific Liquid file that can safely override those generated responses.

Shopify theme architecture supports the standard theme directories: `assets`, `blocks`, `config`, `layout`, `locales`, `sections`, `snippets`, and `templates`. Assets are referenced through Shopify asset URLs, not arbitrary root routes. Shopify documents a special `templates/robots.txt.liquid` route for `/robots.txt`, but this repo does not contain an equivalent supported theme template for `/agents.md` or `/llms.txt`.

Safest implementation path:

1. First check whether Shopify admin has an official setting or app-controlled method to customize AI agent discovery content for `/agents.md` and `/llms.txt`.
2. If no native customization is available, use Cloudflare Worker or another edge/static-route layer in front of `lynxtour.cn` to override:
   - `https://lynxtour.cn/agents.md`
   - `https://lynxtour.cn/llms.txt`
3. Alternative: use a Shopify app proxy only if it can serve or override the exact root-level discovery paths without redirect or HTML wrapping.
4. Avoid publishing these as normal Shopify pages if the intended target is the exact root path, because `/pages/llms-txt` or `/pages/agents-md` is not equivalent to `/llms.txt` or `/agents.md`.
5. After deployment, verify with:
   - `curl -I https://lynxtour.cn/agents.md`
   - `curl -I https://lynxtour.cn/llms.txt`
   - `curl -s https://lynxtour.cn/agents.md`
   - `curl -s https://lynxtour.cn/llms.txt`

Expected response:

- HTTP 200
- Plain text or Markdown content
- No storefront theme HTML wrapper
- No redirect to a Shopify page

## Recommended `/agents.md`

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

## Recommended `/llms.txt`

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
- No theme-level override file for `/agents.md` or `/llms.txt` was found in this repo.
- No `llms.txt` file existed in this repo before this P4-A pass.
- Direct Shopify theme override for `/agents.md` and `/llms.txt` was not implemented because the controlling route is not represented by a supported editable theme file in this repo.
- No Liquid files were changed, so no new Liquid syntax surface was introduced.
- No visible page design or visible site copy was changed.

## Rollback Risk

Low. This change is documentation-only. Removing `docs/geo-ai/p4-a-ai-discovery.md` fully reverts the current repo change. Live storefront behavior is unchanged until the recommended edge/static-route deployment is implemented outside the theme.
