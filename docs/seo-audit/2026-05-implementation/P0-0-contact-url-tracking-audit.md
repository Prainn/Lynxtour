# P0-0 Contact URL and Tracking Audit

Date: 2026-05-26

## Scope

This audit used local theme files only. No contact URLs, redirects, canonical logic, or GA4/GTM tracking code were changed.

## `/pages/contact-us` appearances

Theme/template references:

- `templates/page.contact-us.json`: the live contact page template uses the `contact-us` section and sets the visible page content, WhatsApp number, email, office address, and footer contact settings.
- `sections/contact-us.liquid`: renders the contact form, WhatsApp link, and email link used by the `page.contact-us` template.
- `snippets/ga4-custom-events.liquid`: treats `/pages/contact-us` as a contact-intent URL for delegated `contact_click` tracking.
- Product templates link directly to `/pages/contact-us` from booking/contact fallback CTAs: `sections/dali-product.liquid`, `sections/lijiang-product.liquid`, `sections/luxury-private-tour-product.liquid`, `sections/one-day-trip-product.liquid`, `sections/private-charter-service.liquid`, `sections/shangri-la-product.liquid`, and `sections/xishuangbanna-product.liquid`.
- Destination/page templates or JSON settings also point to `/pages/contact-us`: `sections/all-tours-collection.liquid`, `sections/kunming-page.liquid`, `templates/page.dali.json`, `templates/page.kunming.json`, `templates/page.shangri-la.json`, `templates/page.xishuangbanna.json`, `templates/page.help-center.json`, and `templates/page.hc-category.json`.

Analytics/audit references:

- GA4 audit exports list `/pages/contact-us` as an Organic Search landing page and page/screen path.

## `/pages/contact-information` appearances

Theme/template references:

- `snippets/ga4-custom-events.liquid`: treats `/pages/contact-information` as a contact-intent URL for delegated `contact_click` tracking.
- Destination section schema defaults still contain `/pages/contact-information` as secondary CTA defaults: `sections/dali-page.liquid`, `sections/lijiang-page.liquid`, `sections/shangri-la-page.liquid`, and `sections/xishuangbanna-page.liquid`.

Analytics/audit references:

- GSC audit exports list `https://lynxtour.cn/pages/contact-information` with clicks.
- GA4 audit exports also list `/pages/contact-information` as a small Organic Search landing page and page/screen path.

I did not find a `templates/page.contact-information.json` file in the local theme.

## Primary Linked Contact Page

`/pages/contact-us` appears to be the primary linked contact page in the current theme. It has a dedicated JSON template, a matching `sections/contact-us.liquid` implementation, product-page contact links, destination JSON settings, help-center links, and GA4 contact-intent tracking coverage.

`/pages/contact-information` appears to be an older or alternate contact URL that remains in GSC/GA4 data and in several section schema defaults. Existing page instances may still store `/pages/contact-information` in Shopify admin settings if they were created before newer JSON settings changed to `/pages/contact-us`.

## Canonical, Title, and Meta Treatment

`layout/theme.liquid` uses Shopify `canonical_url` by default and only applies special canonical rewrites for duplicate article variants:

- `jade-dragon-snow-mountain-travel-guide`
- `lijiang-old-town-travel-guide`
- `dali-old-town-travel-guide`

There is no handle-specific canonical override for either `contact-us` or `contact-information`.

`layout/theme.liquid` has handle-scoped SEO title/meta overrides for several pages, collections, articles, and products. There is no special title/meta override for either contact URL. Contact pages therefore rely on Shopify page SEO fields, page title, page content fallback, or the generic page fallback logic.

Robots logic does not treat either contact URL specially. The only relevant noindex cases found are search pages, collection parameter/tag/sort pages, and duplicate article variants.

## Contact Tracking Hooks

`snippets/ga4-custom-events.liquid` implements delegated click and form tracking through JavaScript, not through per-link `data-*` attributes.

Identifiable event hooks:

- WhatsApp links containing `wa.me`, `api.whatsapp.com`, or `whatsapp.com/send` fire `whatsapp_click`.
- `mailto:` links fire `email_click`.
- `tel:` links fire `phone_click`.
- Links to `/pages/contact`, `/pages/contact-us`, `/pages/contact-information`, `/pages/bespoke-custom-travel`, or CTA text containing contact/enquiry/custom wording fire `contact_click`.
- Booking/cart/checkout text and URLs fire `book_now_click`.
- Lead-like contact forms fire `custom_trip_form_submit` and `generate_lead`.

Contact form locations found:

- `sections/contact-us.liquid`: Shopify `{% form 'contact' %}` on the contact page.
- `sections/ai-contact-split.liquid`: `{% form 'contact', id: 'DualContactForm' %}`.
- `sections/bespoke-travel.liquid`: `{% form 'contact', id: 'DualContactForm' %}`.
- `sections/contact-cta.liquid`: `{% form 'contact', id: 'ContactCTA' %}`.

No small existing-event code bug was confirmed in this pass. The GA4 mismatch may be caused by URL fragmentation, Shopify/admin page state, attribution scope differences between landing-page and pages/screens reports, or key-event configuration rather than a theme event-listener failure.

## Recommended Next Patch

Do not create redirects until the canonical live page is confirmed in Shopify admin and GSC URL Inspection.

Exact next patch recommendation:

1. Confirm in Shopify admin which page is intended to be canonical: likely `contact-us`.
2. If `contact-us` is confirmed primary, update stale section settings/defaults that still point to `/pages/contact-information` to `/pages/contact-us`, starting with visible page instances before schema defaults.
3. Update Shopify admin SEO fields for the primary contact page if they are blank or inconsistent.
4. After confirming both URLs in GSC URL Inspection, decide whether a Shopify URL redirect from `/pages/contact-information` to `/pages/contact-us` is appropriate.
5. Re-check GA4 key-event configuration for `contact_click`, `whatsapp_click`, `email_click`, `phone_click`, `custom_trip_form_submit`, and `generate_lead`; no theme tracking-code change is recommended before that check.
