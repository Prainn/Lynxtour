# P4-F Malaysia Landing Page Implementation

Date: 2026-06-30

Scope: Theme support for the future Shopify Page `Yunnan Private Tours from Malaysia`. This implementation creates the page template and section only. It does not publish the page in navigation or footer, create redirects, or change existing product, collection, booking, pricing, schema, robots, sitemap, CSS performance, JavaScript performance, analytics, header, footer, payment, or existing visible page content.

## Files Created

- `templates/page.yunnan-private-tours-from-malaysia.json`
- `sections/yunnan-malaysia-landing.liquid`
- `docs/geo-ai/p4-f-malaysia-landing-page.md`

## Manual Shopify Admin Steps

1. Create a page titled `Yunnan Private Tours from Malaysia`.
2. Set handle to `yunnan-private-tours-from-malaysia`.
3. Assign template `page.yunnan-private-tours-from-malaysia`.
4. Add SEO title: `Yunnan Private Tours from Malaysia | Lynxtour`.
5. Add meta description: `Plan a private Yunnan tour from Malaysia with Kunming, Dali, Lijiang, Shangri-La, flexible pacing, WhatsApp support, and human quote confirmation.`
6. Preview before publishing/indexing.

Expected future live URL:

- `/pages/yunnan-private-tours-from-malaysia`

## Implementation Notes

- The new JSON template includes the existing global navigation section, the new Malaysia landing section, and the existing footer section.
- The landing section reuses the Singapore landing page visual structure with Malaysia-specific copy, cautious Muslim-friendly planning language, and the same dark/gold Lynxtour visual direction.
- The hero supports an optional Shopify image setting. If no image is configured, the hero uses a dark/gold CSS gradient.
- No new external CSS, external JavaScript, inline script behavior, sliders, or third-party dependencies were introduced.
- Page-level JSON-LD is limited to `Service`, `BreadcrumbList`, and `FAQPage`. No `Product`, `Offer`, price, availability, rating, review, flight, visa, payment-method, Malaysia-office, or country-specific endorsement schema was added.
- The visible FAQ questions and answers match the FAQPage JSON-LD content in `sections/yunnan-malaysia-landing.liquid`.

## Validation Checklist

- Run `git diff --check`.
- Run `shopify theme check` if available; separate pre-existing baseline issues from new issues.
- Confirm only the new template, new section, and P4-F documentation were changed.
- Confirm no existing live page templates or sections were modified.
- Confirm no pricing, booking, schema, tracking, product, collection, robots, sitemap, CSS performance, JS performance, footer, payment, or navigation logic changed.
- Confirm no redirects or navigation/footer links were added.
- Confirm the page can render when assigned to a Shopify Page object with handle `yunnan-private-tours-from-malaysia`.
- Confirm visible FAQs match the FAQPage schema content.
- Confirm the hero image setting is optional and any configured image outputs width, height, loading, fetchpriority, decoding, and alt attributes.

## Operational Caution Notes

- Do not imply Lynxtour has a Malaysia office.
- Do not imply flights, visas, payment methods, airline partnerships, hotel names, final availability, or final prices are guaranteed online.
- Do not imply Lynxtour serves only Malaysia travelers.
- Do not assume all Malaysia travelers need Muslim-friendly planning.
- Use cautious wording such as `meal preferences can be reviewed where relevant`, `halal-friendly planning can be discussed where available`, `pork-free options where possible`, and `final route and quote require human confirmation`.
- Keep final route details, hotel level, vehicle arrangement, guide arrangement, meal planning where relevant, inclusions, exclusions, availability, and final price subject to Lynxtour human specialist review.

## Rollback Notes

Rollback risk is low because this change is isolated to one new page template, one new section, and this documentation note. To roll back before publishing, remove:

- `templates/page.yunnan-private-tours-from-malaysia.json`
- `sections/yunnan-malaysia-landing.liquid`
- `docs/geo-ai/p4-f-malaysia-landing-page.md`

If the Shopify Page has already been created manually, unassign the template or unpublish/delete the page in Shopify Admin as needed. No navigation, footer, redirect, product, collection, pricing, booking, analytics, robots, sitemap, CSS performance, JavaScript performance, payment, or existing live page cleanup should be required from this theme change.
