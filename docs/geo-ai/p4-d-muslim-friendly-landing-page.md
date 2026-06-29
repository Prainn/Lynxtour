# P4-D Muslim-Friendly Yunnan Landing Page Implementation

Date: 2026-06-29

Scope: Theme support for a future Shopify Page at `/pages/muslim-friendly-yunnan-private-tours`. This implementation does not publish the page in navigation or footer, does not create redirects, and does not change existing product, collection, booking, pricing, analytics, robots, sitemap, header, footer, or live page content.

## Files Created

- `templates/page.muslim-friendly-yunnan-private-tours.json`
- `sections/muslim-friendly-yunnan-landing.liquid`
- `docs/geo-ai/p4-d-muslim-friendly-landing-page.md`

## Manual Shopify Admin Steps

1. Create a page titled `Muslim-Friendly Yunnan Private Tours`.
2. Set the handle to `muslim-friendly-yunnan-private-tours`.
3. Assign template `page.muslim-friendly-yunnan-private-tours`.
4. Add SEO title: `Muslim-Friendly Yunnan Private Tours | Lynxtour`.
5. Add meta description: `Plan a Muslim-friendly Yunnan private tour with cautious halal-friendly meal planning where available, pork-free options where possible, private pacing, and human confirmation.`
6. Preview before publishing or indexing.

## Validation Checklist

- Confirm the Shopify Page object uses handle `muslim-friendly-yunnan-private-tours`.
- Confirm the page renders with the new `muslim-friendly-yunnan-landing` section.
- Confirm the page is not added to header navigation, footer navigation, collections, products, redirects, robots, or sitemap by this theme change.
- Confirm hero CTA links to `/pages/bespoke-custom-travel`.
- Confirm WhatsApp CTA uses `https://api.whatsapp.com/send/?phone=8613211685553&type=phone_number&app_absent=0` unless a verified replacement is configured in the section settings.
- Confirm visible FAQ questions and answers match the FAQPage JSON-LD in `sections/muslim-friendly-yunnan-landing.liquid`.
- Confirm schema output is limited to Service, BreadcrumbList, and FAQPage.
- Confirm there is no Product, Offer, price, availability, review, rating, halal certification, mosque access, religious facility, or endorsement schema.
- Run `git diff --check`.
- Run `shopify theme check` if available and separate pre-existing baseline issues from new issues.

## Operational Caution Notes

- Use `halal-friendly meal planning where available`, not certified halal meals unless explicitly verified.
- Use `pork-free options where possible`, not guaranteed pork-free dining everywhere.
- Use `restaurant choices can be reviewed before confirmation`, not a verified halal restaurant network.
- Use `private pacing can support timing considerations where practical`, not guaranteed prayer-time services, mosque access, or religious-service expertise.
- Keep final route feasibility, meal planning, restaurant choices, hotel level, vehicle arrangement, guide arrangement, inclusions, exclusions, availability, and final price subject to Lynxtour human specialist review.

## Rollback Notes

Rollback risk is low. To remove this theme support before publishing the Shopify Page, delete:

- `templates/page.muslim-friendly-yunnan-private-tours.json`
- `sections/muslim-friendly-yunnan-landing.liquid`
- `docs/geo-ai/p4-d-muslim-friendly-landing-page.md`

No existing live template, section, navigation, footer, product, collection, pricing, booking, analytics, robots, sitemap, CSS performance, or JavaScript performance logic was intentionally changed.
