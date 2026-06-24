# P3-B Performance Asset Audit

Date: 2026-06-24

Scope: conservative asset-loading audit and safe loading hints only. P3-A image delivery work was not changed. No analytics, Google Ads, GA4, Shopify platform scripts, URLs, handles, schema, product booking logic, cart logic, datepicker logic, price calculation, forms, copy, or visual design were changed.

## Files Inspected

- `layout/theme.liquid`
- `snippets/*.liquid`
- `sections/*.liquid`
- `templates/*.json`
- `docs/performance/*.md`
- `assets/*.js` and `assets/*.css` were requested, but this workspace currently has no `assets/` directory.

## Globally Loaded CSS

Theme-controlled global CSS:

| Source | Resource | Notes |
| --- | --- | --- |
| `layout/theme.liquid` | Global inline `<style>` block | Critical global tokens, CTA/card utility classes, focus states, body font, and prose styling. Left untouched because splitting or deferring could change rendering. |
| `layout/theme.liquid` | `https://fonts.googleapis.com/css2?family=Noto+Serif+SC...&family=Inter...&display=swap` | Global Google Fonts stylesheet. Left untouched because font loading is visual and brand-sensitive. Existing Google Fonts preconnects remain. |

Section-scoped CSS loaded only when the section renders:

| Source | Resource | Notes |
| --- | --- | --- |
| `sections/bespoke-travel.liquid` | `https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css` | Bespoke form datepicker styling. |
| `sections/bespoke-travel.liquid` | `https://cdn.jsdelivr.net/npm/flatpickr/dist/themes/dark.css` | Bespoke form datepicker theme. |
| Product sections | `https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/flatpickr.min.css` | Datepicker styling for product booking flows. Present in `lijiang-product`, `dali-product`, `one-day-trip-product`, `luxury-private-tour-product`, `private-charter-service`, `shangri-la-product`, and `xishuangbanna-product`. |
| `sections/about-us.liquid` | `https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css` | About page carousel styling. |
| Destination / route sections | `Cormorant Garamond` and `Montserrat` Google Fonts stylesheet | Present in destination and route-support sections such as `destinations`, `kunming-page`, `dali-page`, `lijiang-page`, `shangri-la-page`, `xishuangbanna-page`, `seo-itinerary-page`, and `page-route-support`. Not exact duplicates of the global Inter/Noto Serif SC font stylesheet. |

## Globally Loaded JS

Theme-controlled global JavaScript:

| Source | Resource | Notes |
| --- | --- | --- |
| `layout/theme.liquid` | `https://cdn.tailwindcss.com` | Global Tailwind CDN script. It is a major render-blocking candidate, but it supports broad utility-class styling across the theme. It was not deferred or removed. A preconnect hint was added. |
| `layout/theme.liquid` | `{% render 'ga4-custom-events' %}` | Global custom GA4 click/form tracking snippet rendered near the end of `<body>`. Left intact. |
| `snippets/ga4-custom-events.liquid` | Inline tracking script | Sends custom events only when `window.gtag` exists. Left intact. |

Section-scoped JavaScript:

| Source | Resource | Notes |
| --- | --- | --- |
| `sections/global-navigation.liquid` | Inline mobile navigation script | Required for header/menu interaction. Left untouched. |
| `sections/header.liquid` | Inline menu script | Candidate only if this older header section is confirmed rendered and redundant with `global-navigation`; not changed. |
| `sections/bespoke-travel.liquid` | `https://cdn.jsdelivr.net/npm/flatpickr` plus inline bespoke form/AI script | Required for bespoke date fields and form behavior. Left execution order unchanged. |
| Product sections | `https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/flatpickr.min.js` plus inline booking scripts | Required for product date/quantity/package/price/form behavior. Left execution order unchanged. |
| `sections/lijiang-product-text-images.liquid` | `https://cdn.jsdelivr.net/npm/page-flip@2.0.7/dist/js/page-flip.browser.min.js` plus inline page-flip script | Product-specific interactive book/media section. Left execution order unchanged. |
| `sections/about-us.liquid` | `https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js` plus inline init script | About page carousel. Left untouched because not part of target validation pages. |
| Collection sections | Inline filters/sorting/interaction scripts | Present in collection sections such as all tours, day trips, Dali, Lijiang, Shangri-La, Xishuangbanna, and luxury private tours. Left untouched because they are template-specific and already section-scoped. |
| `sections/main-blog.liquid`, `sections/help-center.liquid`, `sections/hc-category-page.liquid`, `sections/product-reviews.liquid`, `sections/contact-us.liquid`, `sections/testimonials.liquid`, `sections/anchor-nav.liquid`, `sections/ai-contact-split.liquid`, `sections/customization-form.liquid`, `sections/luxury-hero-header.liquid` | Inline scripts | Section-owned behavior. Left untouched. |

## Analytics / Tracking Snippets

| Source | Tracking surface | Status |
| --- | --- | --- |
| `layout/theme.liquid` | `{% render 'ga4-custom-events' %}` | Still present near the end of `<body>`. |
| `snippets/ga4-custom-events.liquid` | `lead_whatsapp_click`, `lead_email_click`, `lead_phone_click`, `product_inquiry_click`, `lead_quote_click`, `lead_bespoke_request_click`, `lead_contact_click`, `whatsapp_click`, `email_click`, `phone_click`, `contact_click`, `book_now_click`, `custom_trip_form_submit`, and `generate_lead` | Still present. |
| Shopify / admin / app layer | Base GA4, Google Ads, GTM, Shopify Web Pixels Manager, customer events, consent and Monorail scripts | Not hard-coded in the theme source audited here. Expected to be injected through `{{ content_for_header }}` or Shopify/admin/app configuration. Not touched. |

## Shopify Platform Or App Scripts Not To Touch

- `{{ content_for_header }}` in `layout/theme.liquid`.
- Shopify Web Pixels Manager / customer events output.
- Shopify analytics / Monorail output.
- Shopify app-injected scripts and styles.
- Google and YouTube channel or Customer Events pixel output.
- Any GTM / GA4 / Google Ads loaders configured outside theme files.

## Template-Specific Loading Candidates

Already section-scoped and not globally loaded:

- Product booking scripts and flatpickr assets in product sections.
- Bespoke travel form flatpickr and AI/contact scripts in `sections/bespoke-travel.liquid`.
- Collection filter/sorting scripts in collection sections.
- Blog, help center, review, contact, testimonial, carousel, and anchor scripts in their owning sections.

Possible future candidates only after manual verification:

- Compile or replace the global Tailwind CDN script with a production CSS build.
- Consolidate repeated section-level Google Fonts loading after visual QA.
- Move flatpickr to a shared snippet only if duplicate same-page loads are proven on rendered pages.
- Defer or module-load section scripts only after confirming their dependent third-party libraries and inline init order.

## Suspected Duplicates

- No duplicate exact theme-source include was found for GA4, GTM, Google Ads, or Google tag loader scripts.
- No duplicate exact script include was found in `layout/theme.liquid`.
- Repeated flatpickr includes exist across multiple product section files, but those sections are template-specific and are not necessarily same-page duplicates.
- Multiple Google Fonts stylesheets exist across global and section templates, but they request different font families and are not exact duplicates.
- Prior analytics audit suggested rendered-page duplicate Google tag payloads may exist, but the local theme source does not hard-code the duplicated Google IDs. That needs Shopify/admin/GTM verification, not a theme-file removal.

## Implemented Safe Improvements

| File | Old logic | New logic | Risk |
| --- | --- | --- | --- |
| `sections/bespoke-travel.liquid` | Flatpickr library loaded as a normal parser-blocking external script. | Added `defer` to the flatpickr library script. | Low. The inline bespoke script registers on `DOMContentLoaded` and checks `window.flatpickr` before initializing the date field. |
| Product sections | Flatpickr library loaded as a normal parser-blocking external script in `lijiang-product`, `dali-product`, `one-day-trip-product`, `luxury-private-tour-product`, `private-charter-service`, `shangri-la-product`, and `xishuangbanna-product`. | Added `defer` to the flatpickr library script in each product section. | Low. The booking scripts register on `DOMContentLoaded` and include a `window.flatpickr` availability check / short polling fallback before initializing calendars. |
| `sections/lijiang-product-text-images.liquid` | Page-flip library loaded as a normal parser-blocking external script. | Added `defer` to the page-flip library script. | Low. The section already polls for `window.St.PageFlip` before initializing the flipbook and falls back to the content toggle if the library is unavailable. |
| `sections/about-us.liquid` | Swiper library loaded as a normal parser-blocking external script. | Added `defer` to the Swiper library script. | Low. The inline init is registered on `DOMContentLoaded`, and deferred scripts execute before that event. |

## Deferred / Needs Manual Verification

- Do not defer `https://cdn.tailwindcss.com` until Tailwind utility coverage and visual regression are complete. It is render-blocking, but also globally style-critical.
- Do not move product or bespoke flatpickr assets into a shared/global loader until rendered same-page duplicate loads are proven and booking/form behavior is manually verified.
- Do not remove or consolidate Google tag, GA4, Google Ads, GTM, Shopify Web Pixels, or app pixel scripts from theme source. The heavy rendered Google payload appears outside the local Liquid source.
- Do not split the global inline CSS or Google Fonts in this pass. That requires visual QA and Lighthouse before/after measurement.
- Do not change P3-A image loading, lazy-loading, `srcset`, or image section logic.

## Validation Notes

Validation performed in this branch:

- `git diff --check`: passed. Git also printed a CRLF normalization notice for `sections/lijiang-product-text-images.liquid`; no whitespace errors were reported.
- `shopify theme check`: ran and reported 125 total offenses across 29 files: 3 errors and 122 warnings. Remaining errors are the unchanged global Tailwind parser-blocking script in `layout/theme.liquid` and pre-existing `ValidSchema` errors in collection sections. The parser-blocking errors for the jsDelivr libraries changed in this branch were cleared by the `defer` updates.
- Static source inspection confirmed every `cdn.jsdelivr.net` script include now has `defer`.
- Static source inspection confirmed the global GA4 custom events snippet still renders from `layout/theme.liquid`, and `lead_whatsapp_click`, `lead_email_click`, `lead_phone_click`, `custom_trip_form_submit`, and `generate_lead` remain in `snippets/ga4-custom-events.liquid`.
- Static source inspection confirmed the requested target templates still point to their existing sections. No section names, template names, handles, URLs, schema, copy, booking markup, form markup, or tracking snippet code were changed.

Target page types to inspect:

- Homepage: `templates/index.json` inspected statically; no script/CSS changes were made to homepage-owned sections.
- Yunnan private tours collection: `templates/collection.all-tuors-collection.json` inspected statically; no script/CSS changes were made to the collection section.
- 8-day product page: `templates/product.lijiang.json` / default `templates/product.json` using `sections/lijiang-product.liquid`; flatpickr and page-flip libraries now use `defer`, while the booking controls, CTAs, date input, quantity controls, and inline booking logic remain unchanged.
- Bespoke custom travel page: `templates/page.bespoke-travel.json`; flatpickr now uses `defer`, while `DualContactForm`, the AI preview logic, and contact form submit flow remain unchanged.
- Private car charter page: `templates/product.private-charter.json`; flatpickr now uses `defer`, while product booking controls and CTAs remain unchanged.
- Blog article page: `templates/article.json` inspected statically; no script/CSS changes were made to article-owned sections.

Live browser console verification was not performed in this local pass because the Shopify storefront/preview runtime was not available from the workspace. The implemented changes were limited to external script loading attributes where the existing inline code already waits for `DOMContentLoaded` or polls for the library before use.
