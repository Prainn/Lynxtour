# P4-C Singapore Landing Page Implementation Note

Date: 2026-06-29

Scope: Theme support for the future Shopify Page `Yunnan Private Tours from Singapore`. This implementation creates the page template and section only. It does not publish the page in navigation, create redirects, or change existing product, collection, booking, pricing, robots, sitemap, CSS performance, JavaScript performance, or analytics logic.

## Files Created

- `templates/page.yunnan-private-tours-from-singapore.json`
- `sections/yunnan-singapore-landing.liquid`
- `docs/geo-ai/p4-c-singapore-landing-page.md`

## Manual Shopify Admin Steps

1. Create a page titled `Yunnan Private Tours from Singapore`.
2. Set handle to `yunnan-private-tours-from-singapore`.
3. Assign template `page.yunnan-private-tours-from-singapore`.
4. Add SEO title: `Yunnan Private Tours from Singapore | Lynxtour`.
5. Add meta description: `Plan a private Yunnan tour from Singapore with Kunming, Dali, Lijiang, Shangri-La, custom pacing, hotel-level flexibility, and human quote confirmation.`
6. Preview before publishing/indexing.

Expected future live URL:

- `/pages/yunnan-private-tours-from-singapore`

## Implementation Notes

- The new JSON template includes the existing global navigation section, the new Singapore landing section, and the existing footer section.
- The landing section uses inline section CSS only, matching the current dark/gold Lynxtour visual direction without introducing external CSS, JavaScript, sliders, or dependencies.
- The hero supports an optional Shopify image setting. If no image is configured, the hero uses a graceful dark/gold CSS gradient.
- The WhatsApp CTA uses a section setting with the existing theme-style default: `https://api.whatsapp.com/send/?phone=8613211685553&text&type=phone_number&app_absent=0`.
- Copy follows the P4-B planning guardrails: inquiry-led, useful for travelers, Singapore-specific without making Lynxtour sound Singapore-only, and clear that final route details, hotel level, vehicle, guide, inclusions, exclusions, availability, and final price require human specialist confirmation.
- Page-level JSON-LD is limited to `Service`, `BreadcrumbList`, and `FAQPage`. The `Service` block reuses the existing `snippets/seo-service-jsonld.liquid` pattern. No `Product`, `Offer`, price, rating, review, or availability schema was added.

## Validation Checklist

- Run `git diff --check`.
- Run `shopify theme check` if available; separate pre-existing baseline issues from new issues.
- Confirm only the new template, new section, and P4-C documentation changed.
- Confirm no existing live page templates or sections were modified.
- Confirm no pricing, booking, tracking, product, collection, robots, sitemap, CSS performance, or JS performance logic changed.
- Confirm no redirects or navigation links were added.
- Confirm the page can render when assigned to a Shopify Page object with handle `yunnan-private-tours-from-singapore`.
- Confirm visible FAQs match the FAQPage schema content.
- Confirm the hero image setting is optional and any configured image outputs width, height, loading, fetchpriority, decoding, and alt attributes.

## Rollback Notes

Rollback risk is low because this change is isolated to one new page template, one new section, and this documentation note. To roll back before publishing, remove:

- `templates/page.yunnan-private-tours-from-singapore.json`
- `sections/yunnan-singapore-landing.liquid`
- `docs/geo-ai/p4-c-singapore-landing-page.md`

If the Shopify Page has already been created manually, unassign the template or unpublish/delete the page in Shopify Admin as needed. No navigation or redirect cleanup should be required from this theme change.
