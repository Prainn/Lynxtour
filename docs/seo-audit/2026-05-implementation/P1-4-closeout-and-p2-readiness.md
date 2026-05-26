# P1-4 SEO Closeout and P2 Readiness

Date: 2026-05-26

Branch context: `feat/seo-p1-closeout-p2-readiness`

Scope: documentation-only closeout for completed P0/P1 SEO work and readiness plan for P2.

## Files Inspected

Implementation docs:
- `docs/seo-audit/2026-05-implementation/P0-0-contact-url-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P0-2-jade-dragon-bespoke-internal-links.md`
- `docs/seo-audit/2026-05-implementation/P0-3-car-charter-cta-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P0-4-homepage-internal-links-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-0-contact-url-consistency-follow-up.md`
- `docs/seo-audit/2026-05-implementation/P1-1-commercial-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-2-product-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-3-destination-page-intent-audit.md`

Current local theme files:
- `layout/theme.liquid`
- `sections/main-article.liquid`
- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `sections/bespoke-travel.liquid`
- `sections/private-charter-service.liquid`
- `sections/luxury-private-tour-product.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/xishuangbanna-page.liquid`
- `templates/index.json`
- `templates/page.bespoke-travel.json`
- `templates/page.contact-us.json`
- `templates/page.dali-itinerary-2-days.json`
- `templates/page.dali-itinerary-3-days.json`
- `templates/page.dali-to-lijiang-private-tour.json`
- `templates/page.kunming.json`
- `templates/page.dali.json`
- `templates/page.lijiang.json`
- `templates/page.lijiang-itinerary-2-days.json`
- `templates/page.lijiang-itinerary-3-days.json`
- `templates/page.shangri-la.json`
- `templates/page.tiger-leaping-gorge-from-lijiang.json`
- `templates/page.xishuangbanna.json`
- `templates/product.jade-dragon-snow-mountain-private-tour.json`
- `templates/product.lijiang-to-shangri-la-private-tour.json`
- `templates/product.luxury-private-tour.json`
- `templates/product.private-charter.json`
- `templates/product.lijiang.json`
- `templates/product.json`
- `templates/collection.all-tuors-collection.json`
- `templates/collection.day-trips-collection.json`
- `templates/collection.luxury-private-tour.json`
- `snippets/ga4-custom-events.liquid`
- `snippets/seo-product-jsonld.liquid`
- `snippets/display-variant-price.liquid`

## Completed Work Summary

### P0: GSC/GA4 Guided Immediate Fixes

- Audited contact URL fragmentation between `/pages/contact-us` and `/pages/contact-information`.
- Confirmed `/pages/contact-us` as the locally linked primary contact page and documented the legacy `/pages/contact-information` risk.
- Improved Jade Dragon Snow Mountain and bespoke planning internal links from relevant articles and Lijiang itinerary pages.
- Clarified the car charter custom quote CTA copy while preserving booking, cart, price, and variant behavior.
- Improved homepage commercial link coverage for private tours, private day trips, luxury tours, bespoke planning, the 8-day route, and car charter.

### P1-A: Contact URL Consistency

- Updated stale destination section schema defaults from `/pages/contact-information` to `/pages/contact-us`.
- Left `snippets/ga4-custom-events.liquid` compatibility for `/pages/contact-information` untouched so legacy traffic can still be tracked.
- Did not create redirects; the docs recommend Shopify admin and GSC confirmation before any redirect decision.

### P1-B1: Commercial Collection and Bespoke Intent Alignment

- Aligned handle-scoped SEO title/meta for `/collections/yunnan-private-tours`, `/collections/yunnan-private-day-trips`, `/collections/yunnan-luxury-private-tours`, and `/pages/bespoke-custom-travel`.
- Strengthened collection route links toward bespoke planning, day trips, luxury tours, car charter, and the 8-day benchmark product.
- Clarified bespoke page first-screen and CTA language around custom Yunnan itinerary planning.

### P1-B2: Product Intent Alignment

- Aligned product handle SEO title/meta for:
  - `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
  - `/products/jade-dragon-snow-mountain-private-tour`
  - `/products/lijiang-to-shangri-la-private-tour`
  - `/products/yunnan-private-car-charter-tour`
- Adjusted existing product support links toward fewer, more intent-matched next steps.
- Preserved product booking UI, variant display, price rendering, product JSON-LD, cart, and checkout logic.

### P1-C: Destination Page Intent Alignment

- Aligned destination page handle SEO title/meta for `/pages/kunming`, `/pages/dali`, `/pages/lijiang`, `/pages/shangri-la`, and `/pages/xishuangbanna`.
- Improved existing destination CTA settings toward private tours, day trips, bespoke planning, and car charter where relevant.
- Kept destination pages guide-first while making the commercial next step clearer.

## Final URL Coverage

### Homepage

- `/`
- Key covered routes: `/collections/yunnan-private-tours`, `/collections/yunnan-private-day-trips`, `/collections/yunnan-luxury-private-tours`, `/pages/bespoke-custom-travel`, `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`, and `/products/yunnan-private-car-charter-tour`.

### Commercial Collections

- `/collections/yunnan-private-tours`
- `/collections/yunnan-private-day-trips`
- `/collections/yunnan-luxury-private-tours`
- Supporting destination collections observed in local routing: `/collections/dali-private-tours`, `/collections/lijiang-private-tours`, `/collections/shangri-la-private-tours`, `/collections/xishuangbanna-private-tours`.

### Bespoke Page

- `/pages/bespoke-custom-travel`
- Internal routing support points to Yunnan private tours, luxury private tours, private car charter, and destination guide pages.

### Destination Pages

- `/pages/kunming`
- `/pages/dali`
- `/pages/lijiang`
- `/pages/shangri-la`
- `/pages/xishuangbanna`

### Product Pages

- `/products/jade-dragon-snow-mountain-private-tour`
- `/products/yunnan-private-car-charter-tour`
- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `/products/lijiang-to-shangri-la-private-tour`
- Related product routes observed in support blocks include Kunming day trips, Shangri-La day/luxury routes, and longer Yunnan private tours.

### Article and Itinerary Pages

- `/blogs/travel-guides/dianchi-lake-guide`
- `/blogs/travel-guides/jade-dragon-snow-mountain-guide`
- `/blogs/travel-guides/lijiang-travel-guide`
- `/blogs/travel-guides/stone-forest-shilin-guide`
- `/blogs/travel-guides/lijiang-old-town-guide`
- `/pages/dali-itinerary-2-days`
- `/pages/dali-itinerary-3-days`
- `/pages/lijiang-itinerary-2-days`
- `/pages/lijiang-itinerary-3-days`
- `/pages/dali-to-lijiang-private-tour`
- `/pages/tiger-leaping-gorge-from-lijiang`

## Files Changed Across P0/P1

### `layout/theme.liquid` SEO Overrides

- Homepage title/meta override.
- Collection handle overrides for private tours, private day trips, luxury private tours, Dali private tours, and Lijiang private tours.
- Page handle overrides for destination, itinerary, route-planning, and bespoke pages.
- Article slug overrides for key travel guides.
- Product handle overrides for the four high-priority product pages.

### Article and Internal Link Blocks

- `sections/main-article.liquid` gained or refined handle-scoped article routing and CTA links for Dianchi, Jade Dragon Snow Mountain, Lijiang, Stone Forest, and related guide contexts.
- Itinerary JSON templates for Dali/Lijiang gained targeted links toward relevant guide, product, bespoke, and route pages.

### Collection Sections

- `sections/all-tours-collection.liquid`: commercial routing and intent support for `/collections/yunnan-private-tours`.
- `sections/day-trips-collection.liquid`: private day trip positioning and support links to multi-day tours, car charter, and bespoke planning.
- `sections/luxury-private-tour-collection.liquid`: luxury private tour intent support, fallback copy, and bespoke route links.

### Product Support Blocks

- `sections/private-charter-service.liquid`: custom car charter quote CTA copy and lower support links.
- `sections/luxury-private-tour-product.liquid`: support links for the 8-day benchmark route where that template applies.
- `sections/lijiang-product-text-images.liquid`: product support links for multi-day route comparison contexts.
- Product JSON templates use `product-route-support` settings for Jade Dragon Snow Mountain and Lijiang to Shangri-La support routing.

### Destination Page JSON Settings

- `templates/page.kunming.json`
- `templates/page.dali.json`
- `templates/page.lijiang.json`
- `templates/page.shangri-la.json`
- `templates/page.xishuangbanna.json`

These were used for page-specific H1/intro/CTA/link settings without changing handles, template names, or section names.

### Documentation Files

- P0/P1 audit docs under `docs/seo-audit/2026-05-implementation/`
- This closeout and P2 readiness file.

## Safety Summary

- No booking logic was intended in P0/P1 SEO work.
- No price or variant logic was intended.
- No JSON-LD or structured data change was intended.
- No GA4/GTM tracking-code change was intended.
- No redirects were intended.
- No global CSS redesign was intended.
- No product handles, page handles, collection handles, template names, or section names were intended to change.
- P0/P1 changes were primarily handle-scoped SEO strings, page-specific settings, existing CTA copy, and existing internal-link destinations.

## Live QA Checklist

### SEO Title and Meta

- Open each target URL source or SEO browser extension and confirm the final `<title>` includes Lynxtour only once.
- Confirm meta descriptions render for all target URLs, especially `/pages/xishuangbanna`, which previously lacked a handle-specific meta description.
- Check paginated collection title/meta behavior on page 2+ for private tour collections.
- Confirm canonical URLs remain self-referential except documented duplicate article canonical rewrites.
- Confirm robots remains indexable for target pages and collections.

### CTA Links

- Click first-screen and lower-page CTAs on homepage, collections, bespoke, destinations, products, and priority guides.
- Confirm internal links resolve to live 200 pages, not theme editor placeholders.
- Confirm Shopify resource URLs in JSON templates render to expected storefront URLs.
- Confirm no CTA still points visibly to `/pages/contact-information`.

### Product Booking Cards

- On product pages, verify `Add to booking list` and `Book now` still appear and submit normally.
- Confirm variant rows, date picker, quantity/price totals, and checkout/cart flow behave as before.
- Confirm no SEO support link overlays or blocks interfere with booking card interaction on mobile.

### WhatsApp and Contact Events

- Click WhatsApp links and confirm they open `wa.me` or `api.whatsapp.com` targets.
- Click `/pages/contact-us` and `/pages/bespoke-custom-travel` CTAs and confirm GA4 debug/realtime captures contact-intent events where configured.
- Submit a test contact/custom trip form only in an appropriate staging or safe live testing process.
- Confirm legacy `/pages/contact-information` is not visibly linked, while GA4 compatibility remains if legacy traffic occurs.

### Mobile First-Screen Layout

- Check homepage, commercial collections, bespoke page, five destination pages, and four product pages on mobile.
- Confirm first-screen H1/subheading/CTA text is readable and not clipped.
- Confirm buttons wrap cleanly and do not overlap hero or booking UI.
- Confirm no new text creates layout shifts in existing card grids.

### Internal Link Rendering

- Spot-check article guide links from `sections/main-article.liquid`.
- Spot-check collection support links on private tours, day trips, and luxury tours.
- Spot-check destination route-planning cards for Kunming, Dali, Lijiang, Shangri-La, and Xishuangbanna.
- Spot-check product support links for Jade Dragon, car charter, 8-day Yunnan, and Lijiang to Shangri-La.

## Measurement Plan

Use the same target URL set for every checkpoint. Compare against the 28-day period before deployment and annotate deployment date in GA4/GSC notes if possible.

Target URLs:
- `/blogs/travel-guides/dianchi-lake-guide`
- `/collections/yunnan-private-tours`
- `/collections/yunnan-private-day-trips`
- `/collections/yunnan-luxury-private-tours`
- `/pages/bespoke-custom-travel`
- `/products/jade-dragon-snow-mountain-private-tour`
- `/products/yunnan-private-car-charter-tour`
- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `/pages/kunming`
- `/pages/dali`
- `/pages/lijiang`
- `/pages/shangri-la`
- `/pages/xishuangbanna`

| Checkpoint | GSC clicks | GSC impressions | GSC CTR | GSC average position | GA4 organic sessions | GA4 key events | WhatsApp/contact events |
|---|---|---|---|---|---|---|---|
| Day 7 | Check for indexing or tracking regressions only; do not judge SEO lift yet. | Watch for crawl pickup on changed snippets/titles. | Flag severe CTR drops. | Flag large position drops on branded/exact page queries. | Confirm organic traffic still lands on target URLs. | Confirm booking/contact events still fire. | Confirm WhatsApp/contact clicks are visible. |
| Day 14 | Compare early click trend against prior 14 days. | Check if impressions expand on private tour/day trip terms. | Identify title/meta CTR outliers. | Segment by page and query intent. | Compare organic sessions by URL group. | Check key events by landing page and page path. | Compare contact and WhatsApp event counts by landing page. |
| Day 28 | Primary short-term read. Compare 28 days after vs 28 days before. | Look for collection/destination impression growth. | Check whether changed title/meta improved or weakened CTR. | Review query-level winners/losers. | Compare organic sessions for target URL set. | Review event rate, not only event count. | Review WhatsApp/contact rate by URL. |
| Day 60 | Medium-term read after more stable crawling. | Evaluate durable click growth. | Confirm impressions are not only low-quality expansion. | Decide if P2 implementation is justified. | Compare organic contribution to leads. | Check assisted conversion paths if available. | Decide whether CTA/event naming needs a P2 implementation pass. |

## P2 Readiness Recommendations

### P2-A: Structured Data / JSON-LD Audit First

- Goal: inventory all JSON-LD output on homepage, articles, collections, destination pages, and product pages; identify duplicate, invalid, or thin schema.
- Risk level: high if implemented without audit, because schema changes can affect rich results and product eligibility.
- Files likely involved: `layout/theme.liquid`, `sections/main-article.liquid`, collection sections, destination sections, `snippets/seo-product-jsonld.liquid`.
- Must not be touched: booking logic, product price/variant logic, product availability logic, existing JSON-LD implementation during the audit phase.
- Recommendation: audit-only first. Implementation should be a separate scoped P2 ticket after validation.

### P2-B: Canonical, OG, Twitter Meta Audit

- Goal: verify canonical behavior, duplicate article rewrites, OG/Twitter title/description/image output, and collection pagination/parameter handling.
- Risk level: medium. The current logic is centralized, so a small mistake can affect many URLs.
- Files likely involved: `layout/theme.liquid`, theme settings for logo/share image, representative JSON templates for pages/products/collections.
- Must not be touched: redirects, handles, canonical rewrites, robots logic, or social tags during the audit phase.
- Recommendation: audit-only first, with implementation only for confirmed defects.

### P2-C: Internal Link Crawl and Broken-Link Check

- Goal: crawl target URL clusters and confirm internal links render, resolve, and do not point to stale handles or draft-only content.
- Risk level: low for audit, medium for implementation if many links are changed at once.
- Files likely involved: `sections/main-article.liquid`, collection sections, destination sections, product support sections, JSON templates touched in P0/P1.
- Must not be touched: page handles, collection handles, product handles, redirects, layout, or section structure.
- Recommendation: audit first; implementation can follow in small page-family batches.

### P2-D: GA4 Event Naming and Conversion Attribution Audit

- Goal: confirm `whatsapp_click`, `contact_click`, `book_now_click`, `custom_trip_form_submit`, and `generate_lead` are consistently captured and mapped to useful reporting/key events.
- Risk level: medium to high if code is changed before attribution and admin settings are understood.
- Files likely involved: `snippets/ga4-custom-events.liquid`, contact/bespoke form sections, product CTA sections, GA4 admin configuration outside repo.
- Must not be touched: GTM container, GA4 custom event JavaScript, booking buttons, forms, or checkout logic during the audit phase.
- Recommendation: audit-only first. Implementation should happen only after GA4 admin event/key-event configuration is documented.

### P2-E: Shopify Admin SEO Field Consistency Check

- Goal: compare code-level handle overrides with Shopify admin SEO fields, collection titles, product titles, page titles, and merchant-edited section settings.
- Risk level: low for audit; implementation risk depends on whether live admin content differs from repo templates.
- Files likely involved: primarily documentation; possible future admin changes rather than theme code. Local references include `layout/theme.liquid` and relevant JSON templates.
- Must not be touched: theme behavior, Liquid templates, JSON templates, handles, redirects, or product data without explicit admin-side approval.
- Recommendation: audit-only first. Implement via Shopify admin notes where admin-owned fields are the source of truth.

## Closeout Position

P0/P1 SEO work is ready for live QA and measurement. P2 should start with audits rather than code changes, especially for structured data, social/canonical metadata, and analytics attribution.
