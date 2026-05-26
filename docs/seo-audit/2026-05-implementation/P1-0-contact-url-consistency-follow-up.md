# P1-0 Contact URL Consistency Follow-Up

Date: 2026-05-26

## Scope

This pass used local theme files only. It did not delete pages, create redirects, alter GA4/GTM tracking, redesign templates, refactor Liquid, or touch booking, price, product JSON-LD, schema markup, or global CSS.

## Local References Found

### Primary contact page

- `templates/page.contact-us.json`: local Shopify page template for the contact page. It renders `sections/contact-us.liquid`.
- `sections/contact-us.liquid`: contact form, WhatsApp link, email link, office details, and social links.

### Internal links to `/pages/contact-us`

- `sections/all-tours-collection.liquid`: custom trip/contact link.
- `sections/dali-product.liquid`: product contact CTA.
- `sections/lijiang-product.liquid`: product contact/customize CTA.
- `sections/luxury-private-tour-product.liquid`: product contact CTA.
- `sections/one-day-trip-product.liquid`: product contact CTA.
- `sections/private-charter-service.liquid`: custom route quote CTA.
- `sections/shangri-la-product.liquid`: product contact CTA.
- `sections/xishuangbanna-product.liquid`: product contact CTA.
- `sections/kunming-page.liquid`: section schema default for secondary CTA.
- `templates/page.dali.json`: live Dali page secondary CTA setting.
- `templates/page.kunming.json`: live Kunming page secondary CTA setting.
- `templates/page.shangri-la.json`: live Shangri-La page secondary CTA setting.
- `templates/page.xishuangbanna.json`: live Xishuangbanna page secondary CTA setting.
- `templates/page.help-center.json` and `templates/page.hc-category.json`: help/support text links.

### Stale internal defaults updated from `/pages/contact-information`

- `sections/dali-page.liquid`: `quick_secondary_url` default and `cta_secondary_url` default.
- `sections/lijiang-page.liquid`: `cta_secondary_url` default.
- `sections/shangri-la-page.liquid`: `cta_secondary_url` default.
- `sections/xishuangbanna-page.liquid`: `cta_secondary_url` default.

### Tracking compatibility reference left unchanged

- `snippets/ga4-custom-events.liquid` still recognizes `/pages/contact-information` as a contact-intent path for delegated `contact_click` tracking.

This was intentionally left untouched. It is not a navigational link, and keeping it preserves event attribution if users still arrive at or click legacy contact URLs.

### WhatsApp, email, and phone references

- WhatsApp links appear in contact, destination, product, and collection sections using `wa.me` or `api.whatsapp.com`.
- `mailto:` appears in `sections/contact-us.liquid`.
- `tel:` appears in product/contact CTA blocks such as Dali, Lijiang, luxury tour, one-day trip, private charter, Shangri-La, and Xishuangbanna product sections.

These are external action links, not contact page URL inconsistencies, and were not changed.

## Files Changed

- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`
- `docs/seo-audit/2026-05-implementation/P1-0-contact-url-consistency-follow-up.md`

## Does `/pages/contact-information` Still Exist Locally?

No local `templates/page.contact-information.json` file was found.

After this patch, `/pages/contact-information` remains only in:

- `snippets/ga4-custom-events.liquid` as a legacy tracking matcher.
- historical audit/analytics documents.

No local theme template or internal navigation/CTA default now points users to `/pages/contact-information`.

## Shopify Admin Follow-Up

1. In Shopify admin, confirm that the intended contact page is `/pages/contact-us`.
2. Search Online Store pages for a page handle named `contact-information`.
3. If `contact-information` exists and is not intended as a live page, do not delete it immediately. First inspect traffic/indexation in GSC URL Inspection.
4. Check theme customizer settings for Dali, Lijiang, Shangri-La, and Xishuangbanna pages. If any live page instance still stores `/pages/contact-information`, manually update the setting to `/pages/contact-us`.

## Recommendation

- Redirect: Recommended only after Shopify admin confirms `/pages/contact-information` exists as a stale page and should consolidate into `/pages/contact-us`. Do this in Shopify URL redirects, not theme code.
- Canonicalize: Do not add theme-level canonical logic for contact pages unless both pages must remain live and Shopify admin cannot resolve it.
- Noindex: Do not noindex from theme code in this pass. If the stale page exists, prefer redirect/consolidation after admin verification.
- Leave untouched: If `/pages/contact-information` no longer exists in Shopify admin and only remains in GSC/GA4 history, leave code untouched beyond this patch and let the historical data age out.
