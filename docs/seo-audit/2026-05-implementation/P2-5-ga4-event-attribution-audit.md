# P2-5 GA4 Event Naming and Conversion Attribution Audit

Date: 2026-05-27

Branch: `feat/seo-ga4-attribution-audit-p2`

Scope: documentation-only local theme audit for GA4/GTM event naming, CTA tracking coverage, and conversion attribution readiness.

## Safety Note

- This branch is audit-only.
- No code behavior changed.
- No GA4/GTM implementation changed.
- No Liquid, JSON template, snippet, CSS, canonical/meta/schema, link, CTA, form, booking, price, variant, cart, or checkout logic was modified.
- No MCP tools were used.

## Exact Files Inspected

Primary tracking and layout files:

- `layout/theme.liquid`
- `snippets/ga4-custom-events.liquid`

Navigation, footer, contact, and bespoke surfaces:

- `sections/global-navigation.liquid`
- `sections/footer.liquid`
- `sections/contact-us.liquid`
- `sections/bespoke-travel.liquid`
- `sections/customization-form.liquid`

Product and product-support surfaces:

- `sections/private-charter-service.liquid`
- `sections/luxury-private-tour-product.liquid`
- `sections/one-day-trip-product.liquid`
- `sections/lijiang-product.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/product-route-support.liquid`
- Related product template mappings in `templates/product.*.json`

Collection surfaces:

- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- Related collection template mappings in `templates/collection.*.json`

Destination and guide surfaces:

- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`
- `sections/main-article.liquid`
- `templates/page.bespoke-travel.json`
- Target page templates under `templates/page.*.json`
- `templates/article.json`

Existing audit docs:

- `docs/seo-audit/2026-05-implementation/P0-0-contact-url-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P0-3-car-charter-cta-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-4-closeout-and-p2-readiness.md`
- `docs/seo-audit/2026-05-implementation/P2-0-structured-data-audit.md`
- `docs/seo-audit/2026-05-implementation/P2-1-product-jsonld-live-validation.md`
- `docs/seo-audit/2026-05-implementation/P2-2-canonical-og-twitter-audit.md`
- `docs/seo-audit/2026-05-implementation/P2-3-live-meta-validation.md`
- `docs/seo-audit/2026-05-implementation/P2-4-internal-link-broken-link-audit.md`

## Current Tracking Inventory

### GA4/GTM Inclusion

Local theme files show one custom GA4 event snippet render:

- `layout/theme.liquid`: renders `{% render 'ga4-custom-events' %}` near the end of the body.

No local `dataLayer.push(...)` implementation was found in the inspected theme files. No GTM container snippet was identifiable from local file search. The custom snippet depends on an existing global `window.gtag` function and exits when `window.gtag` is not available.

### Custom Event Listener Location

Custom event listeners are defined in:

- `snippets/ga4-custom-events.liquid`

The snippet registers delegated listeners:

- `document.addEventListener('click', trackClick, true)`
- `document.addEventListener('submit', trackSubmit, true)`

This means the observed custom tracking is global, not page-specific. It should run on all storefront pages where `layout/theme.liquid` renders and where `window.gtag` is available.

### Event Names Found in Local Tracking Code

Detected custom or GA4-relevant event names:

| Event name | Source | Intended trigger from local code |
|---|---|---|
| `whatsapp_click` | `snippets/ga4-custom-events.liquid` | Clicks on links containing `wa.me`, `api.whatsapp.com`, or `whatsapp.com/send` |
| `email_click` | `snippets/ga4-custom-events.liquid` | Clicks on `mailto:` links |
| `phone_click` | `snippets/ga4-custom-events.liquid` | Clicks on `tel:` links |
| `contact_click` | `snippets/ga4-custom-events.liquid` | Clicks to contact/bespoke paths or contact-like text |
| `book_now_click` | `snippets/ga4-custom-events.liquid` | Clicks to cart/checkout paths or booking-like text |
| `custom_trip_form_submit` | `snippets/ga4-custom-events.liquid` | Lead-like form submit |
| `generate_lead` | `snippets/ga4-custom-events.liquid` | Same lead-like form submit, using a GA4 recommended-style event name |

### Selectors and Link Patterns Tracked

Click tracking is delegated to:

- `a`
- `button`
- `[role="button"]`

Tracked link patterns and text patterns:

- WhatsApp: `wa.me`, `api.whatsapp.com`, `whatsapp.com/send`
- Email: `mailto:`
- Phone: `tel:`
- Contact paths: `/pages/contact`, `/pages/contact-us`, `/pages/contact-information`, `/pages/bespoke-custom-travel`
- Contact-like text: `contact us`, `contact`, `enquire`, `inquiry`, `customize`, `custom trip`
- Booking-like URLs: `/cart`, `/checkout`
- Booking-like text: `book now`, `booking`, `add to booking list`, `reserve`, `start planning`, `plan my trip`

Form tracking is delegated to any form that meets at least one of these local-code conditions:

- Current path contains `/pages/bespoke-custom-travel`
- Form `action` contains `/contact`
- Form id/name/class/aria-label contains `contact`, `custom`, `bespoke`, `inquiry`, or `enquire`
- Any field name/id/aria-label/placeholder contains `contact`, `inquiry`, `message`, `email`, or `phone`

### Parameters Found in Local Tracking Code

Click events include:

- `page_location`
- `page_path`
- `event_source`
- `cta_type`
- `link_url`
- `link_text`

Form events include:

- `page_location`
- `page_path`
- `event_source`
- `cta_type`
- `form_id`
- `form_action`
- `form_name`

`generate_lead` additionally includes:

- `currency`
- `value`
- `lead_type`

Parameters not found in local custom event code:

- `page_url`
- `page_type`
- `item_handle`
- `product_handle`
- `collection_handle`
- `article_handle`
- `destination`
- `cta_location`
- `section_id`
- `utm_source`
- `utm_medium`
- `utm_campaign`

## CTA and Conversion Action Coverage

| Action | Likely source file(s) | Expected event name if detectable | Coverage from local code | Risk | Recommended validation |
|---|---|---|---|---|---|
| WhatsApp clicks | `sections/contact-us.liquid`, product sections, collection sections, destination sections | `whatsapp_click`; often also `contact_click` if link text contains contact-like terms | Appears covered globally for WhatsApp URL patterns | Low | GA4 Realtime/DebugView click test on home/contact/product/destination pages |
| Email clicks | `sections/contact-us.liquid`; footer email appears as text in footer settings rather than a confirmed `mailto:` footer link | `email_click` | Covered for `mailto:` links; copy-email buttons and text-only emails are unknown/not covered as email clicks | Medium | Test contact page email link and copy-email behavior separately |
| Phone clicks | Product custom panels; `tel:` links in product sections | `phone_click`; may also be `contact_click` if text contains contact-like terms | Covered for `tel:` links | Low | Test product `Call hotline` link in DebugView |
| Contact page clicks | Product panels, destination CTA defaults, collection CTAs, nav/menu links if configured to `/pages/contact-us` | `contact_click` | Appears covered for `/pages/contact-us`, `/pages/contact`, `/pages/contact-information` and contact-like text | Low | Test product, destination, and collection contact CTAs |
| Book now / booking CTA clicks | Product booking sections; article product cards | `book_now_click` | Covered by text matching for `Book now`, `booking`, `Add to booking list`, and cart/checkout URLs | Medium | Test product buttons and article card `Book Now`; confirm buttons that submit AJAX cart still fire before route change |
| Request quote clicks | `sections/private-charter-service.liquid`; possible quote labels in `snippets/display-variant-price.liquid` | Usually `contact_click` for contact path/text; no dedicated quote event | Broadly covered as contact intent when linked to `/pages/contact-us`; no quote-specific event | Medium | Test car-charter quote CTA; confirm whether GA4 needs a separate quote dimension/event later |
| Bespoke custom itinerary CTA clicks | `sections/bespoke-travel.liquid`, collections, product support, articles, destination pages | `contact_click` for `/pages/bespoke-custom-travel`; `book_now_click` may fire for text like `Plan My Trip` | Covered as contact-intent link to bespoke path; naming does not distinguish bespoke from contact | Medium | Test `/pages/bespoke-custom-travel` entry links from collection, product, destination, article |
| Product inquiry CTAs | Product custom tour panels in `sections/lijiang-product.liquid`, `one-day-trip-product.liquid`, `luxury-private-tour-product.liquid`, private-charter and related product sections | `contact_click`, `phone_click`, `whatsapp_click` | Appears covered for contact, phone, and WhatsApp links | Low | Test each product template family, especially custom package tab/view |
| Car charter quote CTAs | `sections/private-charter-service.liquid` | `contact_click`, `phone_click`, `whatsapp_click`; `book_now_click` for booking buttons | Covered in broad contact/phone/WhatsApp/booking buckets; no charter-specific event | Medium | Test `Request a custom route quote`, `Ask on WhatsApp`, `Book now`, and `Add to booking list` |
| Destination page bespoke CTAs | `sections/kunming-page.liquid`, `dali-page.liquid`, `lijiang-page.liquid`, `shangri-la-page.liquid`, `xishuangbanna-page.liquid` | `contact_click`; WhatsApp buttons as `whatsapp_click` | Appears covered for bespoke/contact links and WhatsApp links | Low | Test each destination CTA block, with special attention to stored section settings |
| Collection page CTA clicks | `sections/all-tours-collection.liquid`, `day-trips-collection.liquid`, `luxury-private-tour-collection.liquid` | `contact_click`, `whatsapp_click`, possibly `book_now_click` for product cards if label says Book Now | Appears covered for contact/bespoke/WhatsApp; product-card clicks without booking text are not conversion events | Medium | Test collection CTA blocks and product-card click paths separately |
| Article guide internal CTA clicks | `sections/main-article.liquid` | `contact_click` for bespoke links; `book_now_click` for `Book Now` product-card CTAs | Appears covered for explicit bespoke and Book Now links; ordinary guide-to-product links are not conversion events | Medium | Test article end CTA, inline bespoke links, and article product cards |

## Event Naming Consistency Audit

### Duplicate Event Names Used for Different Intent

- `contact_click` is intentionally broad. It can represent:
  - Direct contact page clicks.
  - Bespoke custom itinerary clicks.
  - Product inquiry links.
  - Car charter quote links.
  - Destination page custom-trip links.
  - Text-based contact/enquiry/custom clicks even if destination URL varies.
- `book_now_click` can represent:
  - Product `Book now`.
  - `Add to booking list`.
  - Article product card `Book Now`.
  - Generic text such as `Start planning` or `Plan my trip`.

This is not confirmed broken, but it reduces reporting clarity because different commercial intents collapse into the same event.

### Different Event Names Used for the Same Intent

Some clicks can reasonably emit more than one event:

- A WhatsApp link with text such as `Message on WhatsApp` should emit `whatsapp_click`. If its text also contains contact-like language, it may also emit `contact_click`.
- A bespoke link to `/pages/bespoke-custom-travel` emits `contact_click`, while the final bespoke form submit emits both `custom_trip_form_submit` and `generate_lead`.
- A booking-related text link to a product URL may emit `book_now_click`, while the eventual add-to-cart/checkout action may be handled by Shopify or GA4 ecommerce outside this local snippet.

This may be acceptable if GA4 reporting intentionally treats multiple intent layers separately, but it needs live validation to avoid double-counting key events.

### Vague Event Names

- `contact_click` is too broad to distinguish contact, bespoke planning, product inquiry, and car charter quote demand.
- `book_now_click` is broad enough to include `Add to booking list` and `Plan My Trip`, which are not identical to checkout intent.
- `custom_trip_form_submit` is clearer than `contact_click`, but it may fire for lead-like forms beyond the bespoke final contact form depending on page/form fields.
- `generate_lead` is useful for GA4 standard reporting, but its local `lead_type` is always `custom_trip_or_contact_form`, which does not distinguish contact page, bespoke page, or other lead forms.

### Parameter Consistency

Current parameter names are internally consistent for the custom snippet:

- Clicks consistently use `page_location`, `page_path`, `event_source`, `cta_type`, `link_url`, and `link_text`.
- Forms consistently use `page_location`, `page_path`, `event_source`, `cta_type`, `form_id`, `form_action`, and `form_name`.

Watch items:

- Local code uses `page_location`, not `page_url`. That is normal for GA4, but any downstream reporting expecting `page_url` will not receive it from this custom snippet.
- No explicit `page_type`, `item_handle`, `product_handle`, `collection_handle`, `article_handle`, `cta_location`, or `section_id` parameter is sent.
- Without a product/collection/article handle parameter, SEO lead quality must be inferred from landing page, page path, link URL, and link text rather than from normalized content identifiers.
- No UTM parameters are copied into event params. GA4 should still attribute sessions/campaigns natively, but event-level custom dimensions for UTMs are not present in local code.

### SEO Lead Quality Limits

The current local event model can likely count broad lead intent, but it may struggle to answer fine-grained SEO questions such as:

- Was this lead a car charter quote or a general contact?
- Was this bespoke click from a destination page, collection page, product page, or article page?
- Did the visitor click a product card for reading/comparison or a product booking CTA?
- Which product handle or article handle produced the highest-intent lead?

Those questions may still be answerable through GA4 landing page, page path, event path, and exploration reports, but not through normalized custom parameters from this snippet alone.

## SEO Conversion Attribution Readiness

| Question | Likely answerable? | Local-code basis | Attribution watch item |
|---|---|---|---|
| Which organic landing pages drive WhatsApp clicks? | Likely yes | `whatsapp_click` includes `page_location` and `page_path`; GA4 should provide session default channel group/landing page | Requires GA4 key event setup and landing-page exploration validation |
| Which product pages drive quote/contact actions? | Partly | `contact_click`, `whatsapp_click`, `phone_click`, `custom_trip_form_submit`, `generate_lead` include current page path | Product handle not sent; quote/contact intent is broad |
| Which collection pages drive bespoke planning actions? | Partly | Bespoke links to `/pages/bespoke-custom-travel` should emit `contact_click` with link URL/text and page path | No dedicated `bespoke_click` or collection handle |
| Whether destination pages assist conversions | Partly | Destination page clicks to contact/bespoke/WhatsApp can be counted on page path | Assisted conversion paths require GA4 exploration, not local code alone |
| Whether blog/guide pages lead to product or bespoke pages | Partly | Bespoke links and `Book Now` article cards are tracked; ordinary guide-to-product links are not custom conversion events | Requires path exploration or enhanced link-click tracking if later justified |
| Whether TikTok/Facebook/Instagram UTMs can be separated from organic search | Likely yes at GA4 session/campaign level | Local code does not overwrite UTMs | Requires live GA4 source/medium/campaign validation; UTMs are not custom event params |

Overall readiness: good for broad lead attribution, weaker for intent segmentation. The local implementation appears intentionally conservative and global. The main limitation is reporting specificity, not a clearly broken tracking path.

## High-Risk Gaps and Watch Items

### Confirmed Local Blockers

No confirmed tracking-code blocker was found from local files alone.

### Watch Items

- Requires GA4 Realtime validation that `window.gtag` exists on live pages before this snippet runs.
- Requires Tag Assistant validation that the base GA4/GTM installation is present outside this snippet or in Shopify settings/app configuration.
- Requires DebugView validation that delegated click events fire before AJAX product booking code changes page state.
- Requires GA4 Admin check that intended events are marked as key events/conversions.
- Requires confirmation that duplicate event firing, such as `whatsapp_click` plus `contact_click`, is intentional before either event is used as a key event.
- Requires live browser click testing for stored Shopify section settings, because JSON defaults may differ from production admin-edited settings.
- Requires GA4 exploration validation that landing page/session attribution is being used, not only event page path.
- Requires UTM consistency validation for TikTok/Facebook/Instagram campaign links outside the local theme.

## Manual Validation Checklist

| Test | Page to test | Action to click/submit | Expected event name | Expected parameters | Pass/fail notes |
|---|---|---|---|---|---|
| Homepage WhatsApp click | Homepage, if a WhatsApp CTA is present through navigation, footer, or hero settings | Click WhatsApp CTA | `whatsapp_click` | `page_location`, `page_path`, `event_source=lynxtour_theme`, `cta_type=whatsapp`, `link_url`, `link_text` | Confirm if homepage has live WhatsApp CTA in Shopify settings |
| Collection CTA click | `/collections/yunnan-private-tours` or all-tours template page | Click `Plan a Custom Yunnan Trip`, `Request a custom Yunnan itinerary`, or WhatsApp CTA | `contact_click` or `whatsapp_click` | For contact: `cta_type=contact`, `link_url`, `link_text`; for WhatsApp: `cta_type=whatsapp` | Confirm collection handle and template used live |
| Bespoke CTA click | Any product, collection, destination, or article page with `/pages/bespoke-custom-travel` link | Click bespoke/custom itinerary CTA | `contact_click` | `cta_type=contact`, `link_url` containing `/pages/bespoke-custom-travel`, `link_text` | Good candidate for GA4 path and landing-page testing |
| Bespoke form start or submit | `/pages/bespoke-custom-travel` | Submit final expert review/contact form | `custom_trip_form_submit` and `generate_lead` | `cta_type=form_submit`, `form_id`, `form_action`, `form_name`; `generate_lead` also `currency=CNY`, `value=0`, `lead_type=custom_trip_or_contact_form` | No custom `form_start` event found locally; submit only |
| Product Book now click | Product using `lijiang-product`, `one-day-trip-product`, `luxury-private-tour-product`, or `private-charter-service` | Click `Book now` | `book_now_click` | `cta_type=book_now`, `page_path`, `link_text=Book now`; `link_url` may be blank for button-only click | Confirm event fires before AJAX cart/checkout handling |
| Product WhatsApp/contact click | Product custom tour panel | Click `Contact a travel advisor`, `Call hotline`, `Message on WhatsApp` | `contact_click`, `phone_click`, `whatsapp_click` | Contact/phone/WhatsApp `cta_type`, `page_path`, `link_url`, `link_text` | Check whether WhatsApp also emits contact event |
| Car charter quote click | `/products/yunnan-private-car-charter-tour` | Click `Request a custom route quote` | `contact_click` | `cta_type=contact`, `link_url=/pages/contact-us`, `link_text` | No dedicated `quote_click` event expected |
| Destination bespoke CTA click | `/pages/kunming`, `/pages/dali`, `/pages/lijiang`, `/pages/shangri-la`, `/pages/xishuangbanna` | Click custom/bespoke planning CTA | `contact_click` | `cta_type=contact`, `link_url`, `link_text`, `page_path` | Validate each destination because section settings may differ |
| Article guide to product click | Blog/guide article | Click article product card `Book Now` | `book_now_click` | `cta_type=book_now`, `link_url` to product, `link_text=Book Now` | Ordinary inline product links may not emit custom conversion events |
| Footer social/contact click | Any page footer | Click Instagram/Facebook/YouTube/TikTok or footer menu/contact links | Usually no custom event unless URL/text matches contact rules | If matched: contact params; otherwise none from custom snippet | Social outbound tracking is not explicitly covered by current local custom events |

## Recommended P2-D Follow-Up Plan

### P2-D1: GA4 Live Click Validation Only

- Goal: confirm live Realtime/DebugView events for the current global snippet.
- Risk level: Low.
- Likely files: none; validation only.
- Must not be touched: Liquid, JSON templates, snippets, CSS, GA4/GTM code, links, CTAs, forms, booking, price, variant, cart, checkout.
- Recommendation: do now, before any implementation planning.

### P2-D2: Event Naming Cleanup Plan Only

- Goal: decide whether broad events such as `contact_click` and `book_now_click` need a future naming or parameter plan.
- Risk level: Low if documentation-only.
- Likely files: future plan may reference `snippets/ga4-custom-events.liquid`, product sections, collection sections, destination sections, and article section.
- Must not be touched: implementation code during the planning task.
- Recommendation: later, after P2-D1 live evidence confirms actual event volume and duplicate firing behavior.

### P2-D3: Key Event / Conversion Configuration Check

- Goal: document which GA4 events are marked as key events and whether duplicate/broad events are being counted correctly.
- Risk level: Low if admin review only.
- Likely files: none in repo; GA4 Admin configuration outside local theme.
- Must not be touched: theme code, GTM container code, booking/checkout logic.
- Recommendation: do after P2-D1, before any event-name changes.

### P2-D4: UTM Attribution Consistency Audit

- Goal: confirm TikTok, Facebook, Instagram, and other campaign URLs use consistent `utm_source`, `utm_medium`, and `utm_campaign`, and verify GA4 can separate them from organic search.
- Risk level: Low if audit-only.
- Likely files: possibly docs only; campaign links may live outside repo.
- Must not be touched: current theme links unless a separate confirmed implementation ticket is approved.
- Recommendation: later, after key-event setup is confirmed.

### P2-D5: Implementation Only If a Confirmed Tracking Defect Exists

- Goal: fix only a confirmed defect from live validation, such as a missing event on an important CTA or a broken parameter needed for reporting.
- Risk level: Medium because it would touch tracking behavior.
- Likely files: `snippets/ga4-custom-events.liquid` and only the smallest necessary CTA source file if selector-specific markup is required.
- Must not be touched: canonical/meta/schema, URL handles, template names, section names, product price, variant, booking, cart, checkout, unrelated CSS.
- Recommendation: not recommended now. Implementation should wait until P2-D1 to P2-D3 confirm a real tracking gap.

## Summary

The current local theme uses a conservative, global delegated GA4 custom-event snippet. It appears to cover the core Lynxtour lead actions at a broad level: WhatsApp, email, phone, contact/bespoke links, booking-intent buttons, and lead-like form submits.

The main audit finding is not a confirmed missing tracking path. It is a reporting-specificity risk: broad events such as `contact_click` and `book_now_click` may be too coarse to distinguish bespoke planning, product inquiry, car charter quote, collection CTA, article CTA, and true checkout intent without GA4 exploration work or future parameter/event cleanup.

Exact file changed:

- `docs/seo-audit/2026-05-implementation/P2-5-ga4-event-attribution-audit.md`
