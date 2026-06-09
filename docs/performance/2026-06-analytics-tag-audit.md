# Analytics And Tag Loading Audit

Date: 2026-06-09

Scope: audit only. No Liquid, CSS, JavaScript behavior, schema, URLs, handles, checkout, tracking, pixels, Shopify settings, Tailwind, or Google Fonts were changed.

Primary performance context: Shopify Lynxtour homepage.

## 1. Current Lighthouse Mobile Metrics

Current stable Lighthouse mobile baseline supplied for this audit:

| Metric | Current stable result |
| --- | ---: |
| Performance | 76 |
| FCP | 4.1s |
| LCP | 4.2s |
| TBT | 70ms |
| Speed Index | 4.1s |
| CLS | 0.008 |

## 2. PageSpeed Google Tag / GTM Payload Summary

PageSpeed diagnostics report a large unused JavaScript opportunity from Google Tag Manager / Google Tag scripts, totaling about 708 KiB.

Observed PageSpeed tag URLs include multiple Google tag loads, including:

- `GT-MR86M4HM`
- `G-XWLT4N9G7X`
- `AW-181...`
- repeated `gtag/js` style URLs with `cx=` and `gtm=` query parameters
- Shopify Web Pixels Manager also appears in the rendered storefront stack

Interpretation: the performance cost is real in the rendered page, but the searched theme source does not hard-code those Google loader URLs or measurement IDs. The most likely control surfaces are Shopify `content_for_header`, Shopify customer events / Web Pixels, Shopify analytics, Google & YouTube / Google sales channel settings, Google Tag Manager configuration, or another app/admin-managed pixel installation.

## 3. Exact Theme-Source Matches

Search scope used for this audit:

- `layout/theme.liquid`
- `snippets/**/*.liquid`
- `sections/**/*.liquid`
- `templates/**/*.json`
- `config/**/*.json`

Patterns searched:

- `gtag`
- `gtm`
- `googletagmanager`
- `google-analytics`
- `G-XWLT4N9G7X`
- `GT-MR86M4HM`
- `AW-`
- `Google Ads`
- `dataLayer`
- `snippets/ga4-custom-events`
- `customer events`
- `web pixel`
- `pixels`
- `analytics`
- `contact click`
- `whatsapp`
- `lead event`

### GA4 / gtag

| Source | Match | Audit note |
| --- | --- | --- |
| `layout/theme.liquid:774` | `{% render 'ga4-custom-events' %}` | Theme renders the custom event snippet globally near the end of `<body>`. |
| `snippets/ga4-custom-events.liquid:10-11` | `function hasGtag() { return typeof window.gtag === 'function'; }` | Snippet depends on an existing global `window.gtag`. It does not load GA4 itself. |
| `snippets/ga4-custom-events.liquid:37-39` | `if (!hasGtag()) return;` and `window.gtag('event', name, params || {});` | All custom events are sent through `gtag('event', ...)` only if `window.gtag` exists. |
| `snippets/ga4-custom-events.liquid:181` | `if (!hasGtag()) return;` | Click tracking exits if the base Google tag is absent. |
| `snippets/ga4-custom-events.liquid:298` | `if (!hasGtag()) return;` | Form-submit tracking exits if the base Google tag is absent. |

No local theme match was found for a hard-coded `G-XWLT4N9G7X` measurement ID.

### GTM / Google Tag Manager

No local theme match was found in the requested source areas for:

- `GT-MR86M4HM`
- `googletagmanager`
- `gtm`
- a standard GTM container snippet
- `dataLayer`

This suggests the GTM container seen by PageSpeed is not controlled directly by theme files in the searched source tree.

### Google Ads

No local theme match was found in the requested source areas for:

- `AW-`
- `Google Ads`
- a hard-coded Google Ads conversion loader

This suggests the `AW-181...` tag observed in PageSpeed is likely injected by Google tag configuration, Shopify customer events / Web Pixels, Shopify Google integration, Google Tag Manager, or another app/admin-managed integration.

### dataLayer

No local theme match was found for `dataLayer`.

### Custom Lead Events

The custom event implementation is theme-controlled through `snippets/ga4-custom-events.liquid`. Exact event matches:

| Source | Event / behavior |
| --- | --- |
| `snippets/ga4-custom-events.liquid:131-157` | Builds lead-click parameters including `source_path`, `source_page_type`, `cta_type`, `lead_intent`, `link_url`, `link_text`, and section/page handles. |
| `snippets/ga4-custom-events.liquid:159-177` | Classifies lead clicks into `product_inquiry_click`, `lead_whatsapp_click`, `lead_email_click`, `lead_phone_click`, `lead_quote_click`, `lead_bespoke_request_click`, and `lead_contact_click`. |
| `snippets/ga4-custom-events.liquid:194-197` | Sends the classified lead event as a normal GA4 event. |
| `snippets/ga4-custom-events.liquid:199-200` | Sends `whatsapp_click`. |
| `snippets/ga4-custom-events.liquid:203-204` | Sends `email_click`. |
| `snippets/ga4-custom-events.liquid:207-208` | Sends `phone_click`. |
| `snippets/ga4-custom-events.liquid:211-218` | Sends `contact_click`. |
| `snippets/ga4-custom-events.liquid:221-226` | Sends `book_now_click`. |
| `snippets/ga4-custom-events.liquid:229-232` | Sends queued click events through `sendEvent(...)`. |
| `snippets/ga4-custom-events.liquid:255-265` | Detects lead forms by contact/custom/bespoke/inquiry context and form fields. |
| `snippets/ga4-custom-events.liquid:297-308` | Sends `custom_trip_form_submit` and `generate_lead` on qualifying lead-form submits. |
| `snippets/ga4-custom-events.liquid:311-312` | Registers global click and submit listeners. |

### Lead And Contact Surfaces In Theme

Representative theme matches for links/forms that the custom snippet may classify:

| Source | Surface |
| --- | --- |
| `sections/contact-us.liquid:72-75` | Contact page WhatsApp link from section setting. |
| `sections/contact-us.liquid:419` | Contact page email-copy JavaScript selector; not a GA4 event sender by itself. |
| `sections/bespoke-travel.liquid:204-247` | Shopify contact form `DualContactForm` with name, email, WhatsApp, and hidden itinerary fields. |
| `sections/ai-contact-split.liquid:93-104` | Shopify contact form `DualContactForm` with WhatsApp / phone field. |
| `sections/contact-cta.liquid:13-40` | Shopify contact form `ContactCTA`. |
| `sections/all-tours-collection.liquid:1076-1077` | Contact page CTA plus WhatsApp CTA. |
| `sections/all-tours-collection.liquid:1330` | WhatsApp CTA. |
| `sections/dali-product.liquid:898-900` | Contact, phone, and WhatsApp product CTAs. |
| `sections/lijiang-product.liquid:1578-1580` | Contact, phone, and WhatsApp product CTAs. |
| `sections/one-day-trip-product.liquid:1245-1247` | Contact, phone, and WhatsApp product CTAs. |
| `sections/luxury-private-tour-product.liquid:1277-1279` | Contact, phone, and WhatsApp product CTAs. |
| `sections/private-charter-service.liquid:1277-1279` | Custom quote, phone, and WhatsApp product CTAs. |
| `sections/shangri-la-product.liquid:1516-1518` | Contact, phone, and WhatsApp product CTAs. |
| `sections/xishuangbanna-product.liquid:898-900` | Contact, phone, and WhatsApp product CTAs. |
| `sections/dali-page.liquid:965-966` | Destination-page WhatsApp CTA from section setting. |
| `sections/lijiang-page.liquid:983-984` | Destination-page WhatsApp CTA from section setting. |
| `sections/shangri-la-page.liquid:911-912` | Destination-page WhatsApp CTA from section setting. |
| `sections/xishuangbanna-page.liquid:595-596` and `808-809` | Destination-page WhatsApp CTAs from section setting. |

Template JSON also contains WhatsApp/contact copy and settings, for example:

- `templates/page.contact-us.json:37` stores the contact page WhatsApp number.
- `templates/page.dali.json:228-229` stores Dali page WhatsApp label and URL.
- many `templates/*.json` files contain `contact_title`, `contact_tel`, `contact_email`, and `contact_addr` settings for the footer/contact support block.

## 4. Which Tags Appear Theme-Controlled

Theme-controlled:

- The global render of `snippets/ga4-custom-events.liquid` from `layout/theme.liquid:774`.
- Custom GA4 event dispatch via `window.gtag('event', ...)` inside `snippets/ga4-custom-events.liquid`.
- Lead-click and form-submit event naming, parameters, dedupe timing, and event listener registration.
- The storefront contact/WhatsApp/phone/email links and Shopify contact forms that the snippet observes.

Not theme-controlled from the searched source:

- The base GA4 loader for `G-XWLT4N9G7X`.
- The GTM container loader for `GT-MR86M4HM`.
- The Google Ads tag beginning `AW-181...`.
- Shopify Web Pixels Manager.
- Shopify analytics / Monorail / customer-events runtime.

## 5. Which Tags Are Likely Shopify-Injected Or App/Admin-Configured

Likely Shopify-injected or app/admin-configured based on absence from local theme source and normal Shopify behavior:

- Shopify Web Pixels Manager.
- Shopify analytics and Monorail.
- Any Shopify Customer Events custom pixel or app pixel.
- Google tag URLs containing `G-XWLT4N9G7X`.
- Google Ads `AW-181...` tag.
- GTM container `GT-MR86M4HM`.
- Repeated `gtag/js` URLs with `cx=` and `gtm=` query parameters.

The likely control paths to inspect outside theme code are:

- Shopify Admin > Customer events.
- Shopify Admin > Settings > Customer privacy / pixels.
- Shopify Google & YouTube channel or related Google app configuration.
- Google Tag Manager container `GT-MR86M4HM`.
- Google tag settings for `G-XWLT4N9G7X`.
- Google Ads conversion configuration for the `AW-181...` account.

## 6. Whether Duplicate Google Tags Appear Likely

Duplicate Google tag loading appears likely in the rendered page because PageSpeed reports multiple `gtag/js` URLs, including GA4, GTM, Google Ads, and repeated variants with `cx=` / `gtm=` query parameters.

However, duplicate source ownership is not proven from the theme source:

- The local theme does not hard-code `G-XWLT4N9G7X`, `GT-MR86M4HM`, `AW-`, `googletagmanager`, or `dataLayer`.
- The theme custom-event snippet does not load any Google library. It only sends events if `window.gtag` already exists.
- The duplicates are therefore more likely caused by overlapping admin/app/GTM/Google tag configurations than by duplicated Liquid code.

Practical hypothesis to verify: GA4 and Google Ads may both be installed through one or more of Shopify Customer Events / Web Pixels, Google & YouTube channel, and GTM. If GTM also loads GA4 or Ads tags, and Shopify/Google integration loads them separately, PageSpeed will show repeated Google tag payloads.

## 7. Scripts Required For Current Conversion Tracking

Required or likely required until live validation proves otherwise:

- A single base Google tag or GTM path that creates `window.gtag`, because `snippets/ga4-custom-events.liquid` exits when `window.gtag` is unavailable.
- `snippets/ga4-custom-events.liquid`, because it sends the current custom lead events:
  - `product_inquiry_click`
  - `lead_whatsapp_click`
  - `lead_email_click`
  - `lead_phone_click`
  - `lead_quote_click`
  - `lead_bespoke_request_click`
  - `lead_contact_click`
  - `whatsapp_click`
  - `email_click`
  - `phone_click`
  - `contact_click`
  - `book_now_click`
  - `custom_trip_form_submit`
  - `generate_lead`
- Shopify Web Pixels Manager / Shopify analytics, if Shopify analytics, app pixels, customer events, consent handling, or ecommerce tracking currently depend on it.
- Google Ads conversion tag or GTM-hosted Google Ads conversion tag, if Ads lead/conversion reporting depends on `AW-181...`.
- Any GTM container logic that forwards custom GA4 events or Ads conversions, if such forwarding exists in `GT-MR86M4HM`.

## 8. Scripts That May Be Removable Or Consolidatable After Verification

Potential consolidation candidates only after verification:

- Remove duplicate GA4 loading if both Shopify/admin and GTM load the same GA4 measurement ID.
- Consolidate Google Ads loading into one approved path if both GTM and Shopify/Google integration load Ads tags.
- Prefer one owner for Google tag loading:
  - GTM-owned GA4 and Ads tags, or
  - Shopify/Google integration-owned tags, or
  - Google tag direct install,
  but not overlapping installs for the same IDs.
- Remove redundant Google tag destinations from GTM or Google tag settings if the same destination is already loaded elsewhere.
- Disable app/admin pixels that duplicate GTM-managed events, only after confirming they are not used for Shopify analytics, consent mode, enhanced conversions, Ads attribution, or checkout-related reporting.

Do not remove or consolidate from theme code based only on PageSpeed diagnostics. The source audit indicates the heavy tag loaders are probably outside the Liquid source tree.

## 9. Safe Implementation Plan

1. Capture live rendered evidence before any change:
   - Chrome DevTools Network filtered by `gtag`, `gtm`, `googletagmanager`, `collect`, `conversion`, `web-pixels`, and `monorail`.
   - Google Tag Assistant for `GT-MR86M4HM`, `G-XWLT4N9G7X`, and `AW-181...`.
   - GA4 DebugView / Realtime events for key lead actions.
   - Google Ads conversion diagnostics for active website conversion actions.

2. Map ownership:
   - Identify whether `G-XWLT4N9G7X` is loaded by Shopify Customer Events, Google & YouTube channel, GTM, or Google tag direct install.
   - Identify whether `AW-181...` is loaded by Google Ads direct integration, GTM, Google & YouTube channel, or a Shopify pixel.
   - Inspect GTM container `GT-MR86M4HM` for GA4 Configuration / Google Tag, GA4 Event, Google Ads Conversion, Conversion Linker, and consent tags.
   - Inspect Shopify Admin Customer Events for custom pixels and app pixels.

3. Decide one tag owner:
   - Keep one authoritative path for GA4 pageview/session loading.
   - Keep one authoritative path for Google Ads conversions and conversion linker behavior.
   - Keep Shopify Web Pixels Manager if Shopify analytics/app pixels/customer events need it.

4. Validate in staging or a cloned theme where possible:
   - Do not edit `snippets/ga4-custom-events.liquid` during tag-loader consolidation.
   - Change only one admin/GTM/app setting at a time.
   - Compare Network, Tag Assistant, GA4 Realtime, and Ads diagnostics after each change.

5. Roll out conservatively:
   - Keep a rollback note for every disabled tag, pixel, or GTM trigger.
   - Re-run Lighthouse mobile after validation, but treat conversion validation as the gate, not the Lighthouse score alone.

## 10. Risky Changes To Avoid

Avoid these changes unless a separate implementation task explicitly approves them:

- Do not remove `snippets/ga4-custom-events.liquid`.
- Do not edit `snippets/ga4-custom-events.liquid`.
- Do not remove `{% render 'ga4-custom-events' %}` from `layout/theme.liquid`.
- Do not remove `{{ content_for_header }}`.
- Do not disable Shopify Web Pixels Manager blindly.
- Do not remove Shopify analytics / Monorail scripts from theme output.
- Do not delete GTM container `GT-MR86M4HM` without proving GA4, Ads, and lead events still work.
- Do not remove `G-XWLT4N9G7X` or `AW-181...` from admin/GTM/app settings without confirming which path remains authoritative.
- Do not change consent or customer privacy settings for performance alone.
- Do not alter contact links, WhatsApp URLs, forms, booking UI, variant logic, checkout, URLs, handles, schema, Tailwind, or Google Fonts as part of this audit.

## 11. Validation Checklist

Run this checklist before and after any future tag-loader consolidation.

### GA4 Realtime / DebugView

- Confirm a page view appears for `https://lynxtour.cn/`.
- Confirm `window.gtag` exists on the live storefront before custom events are tested.
- Click a WhatsApp CTA and confirm both expected custom-event behavior and parameters:
  - `lead_whatsapp_click`
  - `whatsapp_click`
  - `event_source=lynxtour_theme`
  - `cta_type=whatsapp`
  - `source_page_type` and `source_path`
- Click a contact-page CTA and confirm:
  - `lead_contact_click` where applicable
  - `contact_click`
- Click email and phone CTAs and confirm:
  - `lead_email_click` / `email_click`
  - `lead_phone_click` / `phone_click`
- Click a product inquiry / booking-adjacent CTA and confirm:
  - `product_inquiry_click` where text/source qualifies
  - `book_now_click` where text/link qualifies

### Google Ads Conversions

- Confirm Google Ads Tag Assistant sees the intended Ads account/tag only once unless multiple destinations are intentionally configured.
- Confirm active lead/conversion actions still receive test events.
- Confirm conversion linker or equivalent Ads attribution support remains active if Ads reporting depends on it.
- Confirm no duplicate conversion actions fire for one user action unless intentionally configured.

### Shopify Analytics / Web Pixels

- Confirm Shopify analytics still receives storefront activity.
- Confirm Shopify Web Pixels Manager still initializes if app pixels/customer events remain in use.
- Confirm consent/customer privacy behavior is unchanged.
- Confirm checkout, cart, dynamic checkout, and lead forms still work normally.

### WhatsApp Click Events

- Test a homepage or collection WhatsApp CTA.
- Test a product-page WhatsApp CTA.
- Test a destination-page WhatsApp CTA.
- Confirm the link opens correctly and GA4 receives the expected click event(s).

### Form Submits

- Submit a safe test lead through the contact page or approved test form flow.
- Confirm `custom_trip_form_submit` fires once.
- Confirm `generate_lead` fires once.
- Confirm form dedupe prevents accidental duplicate events within the configured short window.
- Confirm Shopify contact form delivery still works.

### Contact Clicks

- Test `/pages/contact-us` links.
- Test `mailto:` links.
- Test `tel:` links.
- Test bespoke/custom-trip CTAs.
- Confirm GA4 Realtime shows the expected click event names and parameters.

## Summary

The theme-controlled analytics layer is the custom GA4 event snippet rendered from `layout/theme.liquid`. It does not load GA4, GTM, or Google Ads scripts; it depends on an existing `window.gtag`. The heavy Google Tag / GTM payload reported by PageSpeed is therefore likely coming from Shopify/admin/app/GTM configuration rather than duplicated hard-coded theme source. Duplicate Google tag loading appears likely in the rendered page, but the safe next step is ownership mapping and live conversion validation before removing or consolidating any tag path.
