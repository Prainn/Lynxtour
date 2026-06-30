# P4-G Family-Friendly Yunnan Landing Page Implementation

Date: 2026-06-30

Scope: Theme support for the future Shopify Page `Family-Friendly Yunnan Private Tours`. This task created the page template, landing section, and implementation note only. It did not publish the page in navigation, add footer links, create redirects, or change existing product, collection, booking, pricing, analytics, robots, sitemap, header, footer, payment, CSS performance, JS performance, or existing visible page content.

## Files Created

- `templates/page.family-friendly-yunnan-private-tours.json`
- `sections/family-friendly-yunnan-landing.liquid`
- `docs/geo-ai/p4-g-family-friendly-landing-page.md`

## Manual Shopify Admin Steps

1. Create a page titled `Family-Friendly Yunnan Private Tours`.
2. Set handle to `family-friendly-yunnan-private-tours`.
3. Assign template `page.family-friendly-yunnan-private-tours`.
4. Add SEO title: `Family-Friendly Yunnan Private Tours | Lynxtour`.
5. Add meta description: `Plan a family-friendly Yunnan private tour with flexible pacing, walking-level review, hotel room planning, vehicle comfort, and human quote confirmation.`
6. Preview before publishing/indexing.

## Validation Checklist

- Confirm the Shopify Page object uses handle `family-friendly-yunnan-private-tours`.
- Confirm the assigned template is `page.family-friendly-yunnan-private-tours`.
- Confirm the rendered page shows the H1 `Family-Friendly Yunnan Private Tours`.
- Confirm the primary CTA points to `/pages/bespoke-custom-travel`.
- Confirm the WhatsApp CTA points to `https://api.whatsapp.com/send/?phone=8613211685553&type=phone_number&app_absent=0`.
- Confirm the visible FAQ questions match the FAQPage JSON-LD questions and answers.
- Confirm JSON-LD uses Service, BreadcrumbList, and FAQPage only.
- Confirm no Product, Offer, price, availability, rating, review, medical, child-care, senior-care, stroller-accessibility, altitude-safety, or endorsement schema was added.
- Confirm no navigation, footer, redirect, robots, sitemap, tracking, booking, pricing, product, collection, global CSS, or global JS logic changed.
- Run `git diff --check`.
- Run `shopify theme check` if available, separating pre-existing baseline issues from new issues.

## Operational Caution Notes

- Family pacing can be reviewed, but route suitability is not guaranteed for every family.
- Walking level and rest time can be adjusted where practical, subject to route, season, road time, attraction conditions, and group needs.
- Final route feasibility depends on age, walking ability, altitude comfort, season, road time, hotel availability, route scope, and group preferences.
- Shangri-La and other highland routes are altitude-sensitive and should be reviewed before confirmation.
- Travelers with medical concerns should consult a qualified medical professional before choosing high-altitude routes.
- Lynxtour does not claim child-care service, medical support, child-specialist guides, senior-care expertise, guaranteed stroller accessibility, or guaranteed accessibility for all attractions.
- Hotel room arrangement, breakfast expectations, nearby dining, hotel level, and vehicle comfort can be discussed before final quote, subject to availability and final confirmation.
- Final route details, hotel level, room arrangement, vehicle arrangement, guide arrangement, inclusions, exclusions, availability, and final price require Lynxtour human specialist confirmation.

## Rollback Notes

Rollback risk is low because this is a branch-local landing page support addition. To remove it, delete the new template, new section, and this implementation note. No existing live page template, section, navigation item, footer link, redirect, product, collection, booking, pricing, tracking, robots, sitemap, payment, or global asset logic needs to be reverted.
