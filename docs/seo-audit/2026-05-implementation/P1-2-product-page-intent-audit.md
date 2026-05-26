# P1-2 Product Page Intent Audit

Date: 2026-05-26
Branch: `feat/seo-product-intent-p1`

## Files inspected

- `layout/theme.liquid`
- `templates/product.luxury-private-tour.json`
- `templates/product.jade-dragon-snow-mountain-private-tour.json`
- `templates/product.lijiang-to-shangri-la-private-tour.json`
- `templates/product.private-charter.json`
- `templates/product.lijiang.json`
- `templates/product.json`
- `sections/luxury-private-tour-product.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/lijiang-product.liquid`
- `sections/one-day-trip-product.liquid`
- `sections/private-charter-service.liquid`
- `sections/product-route-support.liquid`
- `snippets/seo-product-jsonld.liquid`
- `snippets/display-variant-price.liquid`
- `snippets/ga4-custom-events.liquid`

## Shared implementation notes

- All four target products already have product handle-based SEO overrides in `layout/theme.liquid`.
- `snippets/seo-product-jsonld.liquid`, `snippets/display-variant-price.liquid`, and GA4/GTM code were inspected for risk only and were not modified.
- Product handles, URLs, template names, section names, availability, booking logic, price logic, variant logic, cart logic, checkout logic, JSON-LD, and redirects were not changed.

## /products/kunming-dali-lijiang-shangri-la-8-day-private-tour

- Current title/meta source: product handle override in `layout/theme.liquid`.
- Current visible heading: product-specific H1 in `sections/lijiang-product.liquid`: `8-Day Kunming, Dali, Lijiang & Shangri-La Private Tour`; `sections/luxury-private-tour-product.liquid` also renders `{{ product.title }}` if that template is active.
- Current primary CTA language: `Book now`, `Add to booking list`; custom tab CTA says `Customize this 8-day Yunnan itinerary`.
- Current support/internal links: existing route-planning blocks in `sections/luxury-private-tour-product.liquid` and `sections/lijiang-product-text-images.liquid` linked to Yunnan private tours, bespoke planning, Shangri-La, Dali/Lijiang itinerary pages, Tiger Leaping Gorge, and the Lijiang to Shangri-La product.
- Intent mismatch: title/meta were close but did not exactly emphasize `8-Day Yunnan Private Tour`; support links were broader than needed for a benchmark route page.
- Recommended patch: update title/meta to requested mapping; keep existing first-screen heading/booking copy; trim existing route-planning support links to Yunnan private tours, bespoke planning, and Shangri-La guide.
- Patch status: done in code.
- Rollback risk: low. Changes are limited to handle-scoped SEO strings and existing support-link lists.

## /products/jade-dragon-snow-mountain-private-tour

- Current title/meta source: product handle override in `layout/theme.liquid`.
- Current visible heading: `sections/one-day-trip-product.liquid` renders `{{ product.title }}`.
- Current primary CTA language: `Book now`, `Add to booking list`; custom tab CTA says `Contact a travel advisor`.
- Current support/internal links: `templates/product.jade-dragon-snow-mountain-private-tour.json` uses `sections/product-route-support.liquid` with Lijiang collection, Lijiang guide, 8-day route, bespoke planning, and 3-day Lijiang itinerary links.
- Intent mismatch: meta description did not exactly match the Jade Dragon Snow Mountain + Blue Moon Valley private Lijiang day-trip intent; related links were broader than the day-trip decision path.
- Recommended patch: update meta description; keep title; replace one existing link card with the Jade Dragon Snow Mountain guide; render only three relevant support links: guide, Lijiang guide, and bespoke planning.
- Patch status: done in code.
- Rollback risk: low. Changes are limited to existing template copy and section block order; product booking and JSON-LD remain untouched.

## /products/lijiang-to-shangri-la-private-tour

- Current title/meta source: product handle override in `layout/theme.liquid`.
- Current visible heading: `sections/lijiang-product.liquid` renders `{{ product.title }}` for this product template.
- Current primary CTA language: `Book now`, `Add to booking list`; custom tab CTA says `Contact a travel advisor`.
- Current support/internal links: `templates/product.lijiang-to-shangri-la-private-tour.json` uses `sections/product-route-support.liquid` with Lijiang collection, Lijiang guide, Shangri-La guide, 8-day route, bespoke planning, and Tiger Leaping Gorge route links.
- Intent mismatch: title/meta used a broader northwest Yunnan framing instead of explicitly pairing the route with Tiger Leaping Gorge; related links were broader than needed for transfer-route intent.
- Recommended patch: update title/meta; keep existing route-support intro because it already says this is not a simple point-to-point transfer; render only Shangri-La guide, bespoke planning, and Tiger Leaping Gorge support links.
- Patch status: done in code.
- Rollback risk: low. Changes are limited to title/meta strings and existing route-support block order.

## /products/yunnan-private-car-charter-tour

- Current title/meta source: product handle override in `layout/theme.liquid`.
- Current visible heading: `sections/private-charter-service.liquid`: `Choose charter options`.
- Current primary CTA language: `Book now`, `Add to booking list`; custom tab CTA says `Request a custom car charter quote` and `Request a custom route quote`.
- Current support/internal links: existing lower content block links to Yunnan private tours, Kunming, Dali, Lijiang, Shangri-La, day trips, and bespoke planning.
- Intent mismatch: title/meta did not explicitly say `car with driver`; related links were broader than necessary for flexible transport intent.
- Recommended patch: update title/meta; keep existing transport-first support copy; trim lower support links to private tours, private day trips, and bespoke planning.
- Patch status: done in code.
- Rollback risk: low. Changes are limited to product handle SEO strings and existing lower support links.

## Admin-only notes

- No title/meta admin changes are required because all four target products are already controlled by code-level product handle overrides.
- The visible product headings for Jade Dragon Snow Mountain and Lijiang to Shangri-La are still sourced from Shopify product titles through `{{ product.title }}`. If the live admin titles do not contain the intended keywords, update product titles in Shopify admin rather than adding forced H1 overrides in code.
