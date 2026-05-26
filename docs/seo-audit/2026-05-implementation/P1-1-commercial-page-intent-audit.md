# P1-1 Commercial Page Intent Audit

Date: 2026-05-26
Branch: `feat/seo-commercial-intent-p1`

## Files inspected

- `layout/theme.liquid`
- `templates/collection.all-tuors-collection.json`
- `templates/collection.day-trips-collection.json`
- `templates/collection.luxury-private-tour.json`
- `templates/page.bespoke-travel.json`
- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `sections/bespoke-travel.liquid`

## Shared implementation notes

- Canonical output remains controlled by `layout/theme.liquid` and was not changed.
- Robots logic remains unchanged: search pages, tagged/sorted collection parameter pages, and selected duplicate article variants can receive `noindex,follow`.
- OG/Twitter fields inherit the resolved `seo_title` and `seo_description`; the field structure was not changed.
- JSON-LD and product structured data were inspected only for risk and were not modified.
- GA4/GTM snippets were not modified.

## /collections/yunnan-private-tours

- Current title/meta source: handle-scoped collection override in `layout/theme.liquid` for `collection.handle == 'yunnan-private-tours'`.
- Current visible H1/hero heading: handle-scoped H1 in `sections/all-tours-collection.liquid`: `Yunnan Private Tours`.
- Current hero subheading: `PRIVATE JOURNEYS ACROSS YUNNAN`.
- Current primary CTA: related CTA link: `Request a custom Yunnan itinerary`; product cards use `SEE TOUR DETAILS`.
- Current internal links: existing top and bottom SEO-link blocks include destination collection links, the 8-day route, day-trip collection, bespoke planning, and travel guide links.
- Intent mismatch: title/meta were close, but still framed as packages and comparison rather than custom private Yunnan itinerary planning. Top related links emphasized Dali/Lijiang/Shangri-La rather than the target commercial planning paths.
- Recommended patch: update title/meta to custom private itinerary intent; keep H1; adjust existing related links toward bespoke planning, day trips, luxury private tours, and the 8-day benchmark route.
- Patch status: done in code.

## /collections/yunnan-private-day-trips

- Current title/meta source: handle-scoped collection override in `layout/theme.liquid` for `collection.handle == 'yunnan-private-day-trips'`.
- Current visible H1/hero heading: handle-scoped H1 in `sections/day-trips-collection.liquid`: `Yunnan Private Day Trips`.
- Current hero subheading: `PRIVATE DAY TOURS ACROSS YUNNAN`.
- Current primary CTA: product cards use `SEE TOUR DETAILS`; related-link block follows the product list.
- Current internal links: existing related block linked to broad private tour collections and travel guides.
- Intent mismatch: SEO title was broad and did not mention flexible one-day tours. Related links did not point clearly enough to custom itinerary planning or car charter options.
- Recommended patch: update title/meta to flexible one-day private tour intent; keep H1; change existing related links to multi-day private tours, private car charter, and custom itinerary planning.
- Patch status: done in code.

## /collections/yunnan-luxury-private-tours

- Current title/meta source: handle-scoped collection override in `layout/theme.liquid` for `collection.handle == 'yunnan-luxury-private-tours'`.
- Current visible H1/hero heading: collection title rendered by `sections/luxury-private-tour-collection.liquid`; expected admin collection title is the H1 source.
- Current hero subheading: `CURATED LUXURY ACROSS YUNNAN`.
- Current primary CTA: product cards use `EXPLORE`; side planning link uses custom high-end planning language.
- Current internal links: existing side links include Yunnan private tours, bespoke custom travel, the 8-day route, destination guides, and premium luxury products.
- Intent mismatch: title/meta mentioned high-end custom itineraries, but not the preferred `Yunnan Luxury Private Tours | Boutique Custom Travel` framing. Fallback hero description was Shangri-La-specific if collection admin description is blank.
- Recommended patch: update title/meta; replace generic fallback hero description with Yunnan luxury custom travel language; clarify bespoke side-link text.
- Patch status: done in code.

## /pages/bespoke-custom-travel

- Current title/meta source: handle-scoped page override in `layout/theme.liquid` for `page.handle == 'bespoke-custom-travel'`.
- Current visible H1/hero heading: template setting in `templates/page.bespoke-travel.json`, rendered by `sections/bespoke-travel.liquid`; previous value was `Custom Yunnan Trips`.
- Current primary CTA: `Start Planning My Trip`, `SKIP AI & REQUEST EXPERT PLAN`, `REQUEST EXPERT REVIEW`, and section setting `CONFIRM PLAN`.
- Current internal links: routing support block links to Yunnan private tours, Yunnan luxury private tours, Yunnan private car charter, and destination guide pages.
- Intent mismatch: the page was relevant, but first-screen H1 and CTAs were less explicit than the primary `custom Yunnan itinerary / bespoke private travel planning` intent.
- Recommended patch: update title/meta; update template H1 setting to `Custom Yunnan Itinerary`; clarify existing CTA labels to request a custom itinerary. Keep the form, AI planner, and contact flow unchanged.
- Patch status: done in code.

## Admin-only notes

- No target title/meta appeared to require Shopify admin-only changes because the active theme already has explicit code-level handle overrides for all four target handles.
- The luxury collection H1 is still sourced from the Shopify collection title. If the live admin title differs from `Yunnan Luxury Private Tours`, update the collection title in Shopify admin rather than adding a forced H1 override in code.

## Rollback risk

- Low. Changes are limited to handle-scoped SEO strings, existing visible CTA/link copy, one bespoke template setting value, and existing related-link targets.
- No URLs, handles, section names, template names, redirects, booking logic, variant/price logic, tracking code, global CSS, or JSON-LD were changed.
