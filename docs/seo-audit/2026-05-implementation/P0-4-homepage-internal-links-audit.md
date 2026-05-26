# P0-4 Homepage Internal Links Audit

Date: 2026-05-26

## Scope

This audit used local theme files only. No homepage layout, hero rewrite, new section, global CSS, redirects, structured data, or tracking code changes were made.

## Files Inspected

- `templates/index.json`
- `sections/luxury-hero-header.liquid`
- `sections/brand-features.liquid`
- `layout/theme.liquid`

## Existing Homepage Links Found

Homepage hero and mega-menu settings in `templates/index.json` already linked to:

- `/pages/bespoke-custom-travel` through the secondary hero button.
- `/collections/yunnan-private-tours` through the Tours mega-menu side link.
- `/pages/bespoke-custom-travel` through the Travel Services mega-menu side link before this patch.

Homepage `brand-features` commercial link chips already linked to:

- `/collections/yunnan-private-tours`
- `/collections/yunnan-private-day-trips`
- `/pages/shangri-la`
- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`

## Target URL Coverage Before Patch

- `/collections/yunnan-private-tours`: present.
- `/collections/yunnan-private-day-trips`: present.
- `/collections/yunnan-luxury-private-tours`: not found on homepage.
- `/pages/bespoke-custom-travel`: present.
- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`: present.
- `/products/yunnan-private-car-charter-tour`: not found on homepage.

## Safe Patch Applied

Two existing homepage links were adjusted in `templates/index.json`:

1. Travel Services mega-menu side link now points to `/products/yunnan-private-car-charter-tour`.
   - Old target: `shopify://pages/bespoke-custom-travel`
   - New target: `shopify://products/yunnan-private-car-charter-tour`
   - Why safe: the same block already describes private transfers, custom planning, and support services. The hero secondary button still links to bespoke custom travel, so bespoke coverage remains.

2. The third `brand-features` commercial chip now points to `/collections/yunnan-luxury-private-tours`.
   - Old label/target: `Continue to the Shangri-La travel guide` -> `shopify://pages/shangri-la`
   - New label/target: `Browse Yunnan luxury private tours` -> `shopify://collections/yunnan-luxury-private-tours`
   - Why safe: the chip list is already a commercial planning-link block below copy about popular private routes and why private tours are useful. Replacing one informational destination guide link with a commercial luxury collection improves target coverage without adding layout or changing section structure.

## Target URL Coverage After Patch

- `/collections/yunnan-private-tours`: present.
- `/collections/yunnan-private-day-trips`: present.
- `/collections/yunnan-luxury-private-tours`: present.
- `/pages/bespoke-custom-travel`: present.
- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`: present.
- `/products/yunnan-private-car-charter-tour`: present.

## Recommended Follow-Up

After deployment, verify the homepage rendered links in Shopify preview because `templates/index.json` uses Shopify resource URLs. No admin-only SEO field change is required for this P0-C patch.
