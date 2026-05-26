# P0-2 Jade Dragon and Bespoke Internal Links

Date: 2026-05-26

## Scope

This P0-B pass used local theme files only. No booking logic, product price logic, redirects, structured data, or GA4/GTM tracking code were changed.

## Files Inspected

- `layout/theme.liquid`
- `sections/main-article.liquid`
- `sections/lijiang-page.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/product-route-support.liquid`
- `sections/seo-itinerary-page.liquid`
- `templates/page.lijiang.json`
- `templates/page.lijiang-itinerary-2-days.json`
- `templates/page.lijiang-itinerary-3-days.json`
- `templates/product.jade-dragon-snow-mountain-private-tour.json`

## Files Changed

- `sections/main-article.liquid`
- `templates/page.lijiang-itinerary-2-days.json`
- `templates/page.lijiang-itinerary-3-days.json`
- `docs/seo-audit/2026-05-implementation/P0-2-jade-dragon-bespoke-internal-links.md`

## New or Updated Links

### `/blogs/travel-guides/lijiang-travel-guide`

Updated existing Jade Dragon product link text in the Lijiang guide intro block:

- URL: `/products/jade-dragon-snow-mountain-private-tour`
- Anchor: `explore the Jade Dragon Snow Mountain private tour`

Added a small custom itinerary link in the existing Lijiang route-planning block:

- URL: `/pages/bespoke-custom-travel`
- Anchor: `request a custom Yunnan itinerary`

Why safe: both changes are inside existing `is_lijiang_travel_guide` handle-scoped article blocks. The page already discusses Lijiang route planning, Jade Dragon Snow Mountain, Tiger Leaping Gorge, and northbound extensions, so both links are contextually relevant.

### `/blogs/travel-guides/jade-dragon-snow-mountain-guide`

Updated existing product link text in the Jade Dragon guide brief:

- URL: `/products/jade-dragon-snow-mountain-private-tour`
- Anchor: `private Jade Dragon Snow Mountain tour`

Why safe: the link already pointed to the same product and remains inside the existing `is_jade_dragon_snow_mountain_guide` block. The change only makes the anchor clearer for the exact product intent.

### `/pages/lijiang-itinerary-2-days`

Added a contextual product link in the Day 2 itinerary copy:

- URL: `/products/jade-dragon-snow-mountain-private-tour`
- Anchor: `Jade Dragon Snow Mountain private tour`

Why safe: the Day 2 card already centers on Jade Dragon Snow Mountain as the main scenic day. This adds one relevant link within the existing page content, without adding new sections or changing layout logic.

### `/pages/lijiang-itinerary-3-days`

Added a contextual product link in the Day 2 itinerary copy:

- URL: `/products/jade-dragon-snow-mountain-private-tour`
- Anchor: `Jade Dragon Snow Mountain private tour`

Why safe: the Day 2 card already discusses Jade Dragon Snow Mountain, Blue Moon Valley, transport, ticketing, and pacing. The link is a natural next step for the exact high-intent mountain-day context.

## Existing Bespoke CTA Coverage Confirmed

No duplicate bespoke CTA was added to pages that already had clear existing links:

- `/pages/lijiang` already links to `/pages/bespoke-custom-travel` in its CTA settings.
- `/pages/lijiang-itinerary-2-days` already links to `/pages/bespoke-custom-travel` in a link card and CTA.
- `/pages/lijiang-itinerary-3-days` already links to `/pages/bespoke-custom-travel` in a link card and CTA.
- `/products/jade-dragon-snow-mountain-private-tour` already links to `/pages/bespoke-custom-travel` in product route support JSON.

## Recommended Shopify Admin Follow-Up

Because the two itinerary edits are in JSON template content, confirm in Shopify admin that the rendered section text still matches the theme file after deployment. If the live admin theme editor has newer unpublished content for these pages, apply the same two Day 2 link updates there instead of overwriting merchant edits.
