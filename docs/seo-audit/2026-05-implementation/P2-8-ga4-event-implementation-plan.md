# P2-8 GA4 Event Implementation Plan

Date: 2026-05-27

Branch: `feat/seo-ga4-event-implementation-plan-p2`

Scope: documentation-only implementation plan for future GA4 event tracking improvements. This document does not implement tracking code.

## Safety Note

- This branch is documentation-only.
- No code behavior changed.
- No GA4/GTM implementation changed.
- No Liquid behavior, JSON templates, snippets, CSS, JavaScript behavior, tracking code, SEO title/meta/canonical/schema, links, CTAs, forms, booking, price, variant, cart, checkout, or layout logic was modified.
- No MCP tools were used.

## Exact Files Inspected

Tracking and layout:

- `layout/theme.liquid`
- `snippets/ga4-custom-events.liquid`

Product and product-support surfaces:

- `sections/private-charter-service.liquid`
- `sections/luxury-private-tour-product.liquid`
- `sections/one-day-trip-product.liquid`
- `sections/lijiang-product.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/product-route-support.liquid`

Commercial collection surfaces:

- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`

Bespoke and destination surfaces:

- `sections/bespoke-travel.liquid`
- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`

Template mappings and target SEO page templates:

- `templates/page.bespoke-travel.json`
- Product templates under `templates/product*.json`
- Collection templates under `templates/collection*.json`
- Target page templates under `templates/page*.json`

Existing P2-D docs:

- `docs/seo-audit/2026-05-implementation/P2-5-ga4-event-attribution-audit.md`
- `docs/seo-audit/2026-05-implementation/P2-6-ga4-live-click-validation.md`
- `docs/seo-audit/2026-05-implementation/P2-7-ga4-key-event-strategy.md`

## 1. Implementation Goal

Future GA4 tracking improvements should:

- Keep Contact Us WhatsApp as a confirmed key event.
- Add better visibility for qualified lead-intent actions on product, bespoke, car charter, collection, destination, and article pages.
- Avoid inflating conversions with generic navigation clicks.
- Keep normal engagement events separate from GA4 key events.
- Preserve all current storefront behavior, especially product booking, cart, checkout, WhatsApp outbound links, and contact forms.

This plan is intentionally narrow. It should guide a later implementation only after approval.

## 2. Current Tracking Baseline

Confirmed current behavior:

- P2-D1 confirmed that WhatsApp clicks on `/pages/contact-us` trigger GA4 key events.
- The exact GA4 event name and parameters for that live key event were not recorded.
- Other product, collection, destination, bespoke, article, quote, phone, email, or booking actions are not confirmed as GA4 key-event sources.
- Other pages not triggering key events is not currently confirmed as a bug.

Local code baseline:

- `layout/theme.liquid` globally renders `snippets/ga4-custom-events.liquid`.
- `snippets/ga4-custom-events.liquid` uses delegated listeners for clicks and form submits.
- Current local event names include `whatsapp_click`, `email_click`, `phone_click`, `contact_click`, `book_now_click`, `custom_trip_form_submit`, and `generate_lead`.
- Current click parameters include `page_location`, `page_path`, `event_source`, `cta_type`, `link_url`, and `link_text`.

Known limitation:

- Contact-page-only key-event attribution undercounts direct lead intent from product, car charter, bespoke, collection, destination, and article pages.
- Current broad events such as `contact_click` and `book_now_click` are useful but too vague for clean SEO lead attribution.

Why implementation must be narrow:

- The current Contact Us WhatsApp key event works and should not be disrupted.
- Product booking sections contain active JavaScript for date, quantity, cart, and checkout behavior.
- Broad selector changes could inflate conversion counts or double-count a single click.
- GA4 Admin key-event configuration must be validated after any tracking event changes.

## 3. Proposed Event Taxonomy

### Lead-Intent Events

| Proposed event | Purpose | Examples | GA4 key event candidate | Risk |
|---|---|---|---|---|
| `lead_whatsapp_click` | Track qualified WhatsApp lead clicks | Contact Us WhatsApp, product WhatsApp, car charter WhatsApp, destination WhatsApp | Yes | Medium, because WhatsApp can appear in multiple contexts |
| `lead_email_click` | Track qualified email lead clicks | Contact page `mailto:` link, future inquiry email links | Maybe | Medium, because some email links may be support or footer utility |
| `lead_phone_click` | Track qualified phone lead clicks | Product `Call hotline`, contact page phone link if present | Maybe | Medium, because phone intent must be confirmed as a real lead |
| `lead_quote_click` | Track quote-specific inquiry intent | `Request a custom route quote`, car charter quote CTA | Yes | Medium, because text matching must avoid generic request copy |
| `lead_bespoke_request_click` | Track bespoke custom itinerary request intent | Links to `/pages/bespoke-custom-travel`, bespoke request CTAs | Yes | Medium, because some links may be planning navigation rather than direct lead intent |
| `product_inquiry_click` | Track product-level inquiry intent | Product `Contact a travel advisor`, custom tour contact CTA | Yes | Medium, because product pages also have normal booking controls |

### Engagement and Navigation Events

| Proposed event | Purpose | Examples | GA4 key event candidate | Risk |
|---|---|---|---|---|
| `cta_navigation_click` | Track non-lead CTA navigation | Destination guide CTAs, collection browse CTAs, route-support links | No | Low |
| `article_internal_link_click` | Track guide/article internal movement | Article links to products, collections, bespoke page, destination guides | No | Low to medium, because article links can assist lead paths |
| `collection_product_click` | Track product-card navigation from collections | Product cards in all tours, day trips, luxury tours | No | Low |

Principle:

- Lead-intent events measure commercial actions.
- Engagement/navigation events measure pathing and assisted behavior.
- Only selected high-intent lead events should become GA4 key events after validation.

## 4. Proposed Event Parameters

### Standard Parameters

| Parameter | Required? | Purpose |
|---|---|---|
| `page_location` | Required | Full current URL for GA4 and debugging |
| `page_title` | Required | Human-readable page context |
| `source_page_type` | Required | Classifies source as homepage, product, collection, bespoke page, destination page, article/guide, itinerary page, route-support page, contact page, or unknown |
| `source_handle` | Required when available | Current page/product/collection/article handle |
| `link_url` | Required for link clicks | Destination URL clicked |
| `link_text` | Required when available | Visible CTA text for debugging |
| `cta_type` | Required | Stable CTA class such as `whatsapp`, `email`, `phone`, `quote`, `bespoke_request`, `product_inquiry`, `booking`, `navigation` |
| `lead_intent` | Required for lead-intent events | Stable lead intent such as `whatsapp`, `email`, `phone`, `quote`, `bespoke_request`, `product_inquiry`, `contact` |
| `product_handle` | Optional | Product handle when source or target product is known |
| `collection_handle` | Optional | Collection handle when source or target collection is known |
| `article_handle` | Optional | Article handle when source or target article is known |
| `destination_handle` | Optional | Destination page handle such as `kunming`, `dali`, `lijiang`, `shangri-la`, `xishuangbanna` |
| `section_context` | Optional | Context such as `booking_panel`, `custom_tour_panel`, `route_support`, `collection_support`, `destination_cta`, `article_body`, `footer`, `contact_page` |

Parameter rules:

- Lead-intent events should always include `page_location`, `page_title`, `source_page_type`, `link_url`, `link_text`, `cta_type`, and `lead_intent` where technically possible.
- Source handle parameters should be added when Liquid context can safely expose them without altering page behavior.
- Optional handle parameters should not block event dispatch when unavailable.
- UTM values do not need to be copied into custom params unless a later attribution audit requires it; GA4 should retain session source/medium/campaign separately.

## 5. Selector / Detection Plan

This section describes future detection only. Do not change code in this branch.

### WhatsApp Links

Future detection:

- `href` contains `wa.me`
- `href` contains `api.whatsapp.com`
- `href` contains `whatsapp`

Proposed event:

- `lead_whatsapp_click`

Classification:

- Key-event candidate when source context is Contact Us, product, car charter, bespoke, destination CTA, or other qualified lead surface.
- Normal lead-intent event only if the context is unclear.

### Email Links

Future detection:

- `href` starts with `mailto:`

Proposed event:

- `lead_email_click`

Classification:

- Key-event candidate only if Lynxtour confirms email clicks are real lead intent.
- Otherwise keep as normal lead-intent diagnostic event.

### Phone Links

Future detection:

- `href` starts with `tel:`

Proposed event:

- `lead_phone_click`

Classification:

- Key-event candidate only if phone calls are meaningful lead actions.
- Product `Call hotline` links are stronger candidates than generic footer text.

### Contact Page Links

Future detection:

- `href` contains `/pages/contact-us`

Proposed event:

- `product_inquiry_click` when clicked from product custom/inquiry panels.
- `lead_quote_click` when clicked from car charter quote context.
- `cta_navigation_click` when clicked as generic support navigation.

Classification:

- Do not treat every contact-page link as a key event.
- Use source page type, link text, and section context to distinguish inquiry from navigation.

### Quote / Inquiry / Bespoke CTAs

Future detection:

- Link text contains `quote`, `request`, `inquiry`, `bespoke`, `custom itinerary`, `contact`, or `plan`.
- URL contains `/pages/bespoke-custom-travel` or `/pages/contact-us`.
- Product pages and car charter pages should be treated with higher intent than generic navigation contexts.

Proposed events:

- `lead_quote_click`
- `lead_bespoke_request_click`
- `product_inquiry_click`
- `cta_navigation_click` when the action is not clearly lead intent

Classification:

- Product page custom tour CTAs and car charter quote CTAs are high-intent.
- Destination and article links to bespoke planning are lead-intent candidates but require stricter context labeling.
- Generic browse links should remain normal engagement events.

### Booking CTAs

Future detection:

- Buttons or links with `book`, `booking`, `add to cart`, `checkout`, or `request quote`.

Implementation caution:

- Do not interfere with booking behavior.
- Do not delay cart, checkout, date picker, variant, quantity, or booking actions.
- Do not mark generic `Book now` product-card navigation as a lead key event unless Lynxtour explicitly decides booking clicks are lead conversions.

Proposed treatment:

- Keep booking clicks separate from lead-intent inquiry events.
- If tracked, use either existing ecommerce/Shopify reporting or a normal diagnostic event until conversion meaning is confirmed.

## 6. Page-Type Classification Plan

Future tracking should classify source pages as:

- `homepage`
- `collection`
- `product`
- `bespoke_page`
- `destination_page`
- `article_guide`
- `itinerary_page`
- `route_support_page`
- `contact_page`
- `unknown`

Safe inference sources:

- `request.page_type` if made available from Liquid to the tracking snippet.
- URL path patterns such as `/products/`, `/collections/`, `/pages/`, and `/blogs/`.
- Template context if exposed safely through data variables.
- `product.handle`, `collection.handle`, `page.handle`, or `article.handle` where available.

Suggested path rules:

- `/` -> `homepage`
- `/collections/*` -> `collection`
- `/products/*` -> `product`
- `/pages/bespoke-custom-travel` -> `bespoke_page`
- `/pages/contact-us` -> `contact_page`
- `/pages/kunming`, `/pages/dali`, `/pages/lijiang`, `/pages/shangri-la`, `/pages/xishuangbanna` -> `destination_page`
- `/pages/*itinerary*` -> `itinerary_page`
- `/pages/dali-to-lijiang-private-tour` and `/pages/tiger-leaping-gorge-from-lijiang` -> `route_support_page`
- `/blogs/*` -> `article_guide`

Fallback:

- Use `unknown` when classification is uncertain.
- Unknown context events should not become key events until validated.

## 7. Key Event Candidate Rules

Recommended future key-event candidates:

- Contact Us WhatsApp click.
- Product page WhatsApp click.
- Product inquiry or quote click.
- Car charter quote or WhatsApp click.
- Bespoke custom itinerary request click.
- Email or phone clicks only if they represent real lead intent.

Not recommended as key events:

- Generic collection navigation.
- Article internal links.
- Destination page guide links.
- Footer social clicks.
- Normal product card clicks before inquiry intent.
- Generic route-support links without direct inquiry wording.
- Page-load events.
- Duplicate events for the same click.

Eligibility rules:

- The event must represent direct contact or inquiry intent.
- The event must be tied to a meaningful source page and source handle where possible.
- The event must not be generic navigation.
- The event must not fire automatically on page load.
- The event must not duplicate another key event for the same click.
- The event must be validated in GA4 Realtime and DebugView.

## 8. Implementation Phases

### P2-D4-A: Normal Event Coverage

Goal:

- Add or confirm normal events for WhatsApp, email, phone, and CTA clicks.

Rules:

- Do not mark all new events as key events yet.
- Preserve the current Contact Us WhatsApp key event.
- Keep product booking, cart, checkout, price, and variant behavior untouched.

Likely files:

- `snippets/ga4-custom-events.liquid` or a dedicated tracking snippet.

### P2-D4-B: Qualified Lead-Intent Tagging

Goal:

- Add `lead_intent` and `cta_type` parameters.
- Separate product, bespoke, car charter, contact, destination, collection, and article actions.

Rules:

- Use explicit context where possible.
- Avoid relying only on broad link text.
- Do not change link destinations or CTA copy.

Likely files:

- Tracking snippet only, unless a later approved plan adds safe data attributes to existing CTA elements.

### P2-D4-C: GA4 Key Event Configuration

Goal:

- Mark selected events as key events in GA4 Admin only after live validation.

Rules:

- Do not mark diagnostic navigation events as key events.
- Confirm duplicate firing behavior before enabling key-event status.
- Keep Contact Us WhatsApp as the known baseline until replacement or expansion is validated.

Likely files:

- No repo files if this is GA4 Admin configuration only.

### P2-D4-D: Validation and Rollback

Goal:

- Validate event dispatch, parameters, and key-event settings.

Checklist:

- GA4 Realtime test.
- GA4 DebugView test.
- Duplicate firing check.
- Event parameter check.
- Source page classification check.
- Link behavior check for outbound WhatsApp.
- Product booking/cart/checkout regression check.

Rollback plan:

- Revert the tracking snippet change only.
- Leave booking, price, variant, checkout, SEO, schema, and layout files untouched.
- If GA4 Admin key events were added, disable the new key events before reverting reports.

## 9. Risk Controls

Required safeguards:

- Avoid duplicate firing for the same click.
- Avoid tracking page-load events as leads.
- Avoid counting generic navigation as conversion.
- Do not break outbound WhatsApp behavior.
- Do not delay checkout, cart, or booking actions.
- Avoid vague event names.
- Avoid missing `link_url`, `link_text`, or page context.
- Avoid changing the current working Contact Us WhatsApp key event before replacement or expansion is validated.
- Keep booking, price, variant, cart, checkout, SEO, schema, and layout logic outside the implementation scope.

Specific technical controls for future implementation:

- Keep click handling delegated and lightweight.
- Use one primary lead-intent event per click.
- Use diagnostic engagement events only when they do not overlap key-event candidates.
- Use a short dedupe window for identical event/link/text combinations.
- Preserve normal link navigation and form submit behavior.
- Validate on live pages before changing GA4 key-event configuration.

## 10. Manual Validation Plan After Implementation

| Test | Page | Action | Expected event name | Expected parameters | Key event candidate | Pass/fail notes |
|---|---|---|---|---|---|---|
| Contact Us WhatsApp | `/pages/contact-us` | Click WhatsApp link | `lead_whatsapp_click` or current confirmed event if retained during transition | `page_location`, `page_title`, `source_page_type=contact_page`, `source_handle`, `link_url`, `link_text`, `cta_type=whatsapp`, `lead_intent=whatsapp`, `section_context=contact_page` | Yes | Must preserve current confirmed key-event behavior |
| Product page WhatsApp | Representative product page | Click product custom-panel WhatsApp | `lead_whatsapp_click` | `source_page_type=product`, `product_handle`, `link_url`, `link_text`, `cta_type=whatsapp`, `lead_intent=whatsapp`, `section_context=custom_tour_panel` | Yes | Confirm outbound WhatsApp still opens |
| Product inquiry | Representative product page | Click `Contact a travel advisor` or equivalent product inquiry CTA | `product_inquiry_click` | `source_page_type=product`, `product_handle`, `link_url`, `link_text`, `cta_type=product_inquiry`, `lead_intent=product_inquiry` | Yes | Do not interfere with product booking controls |
| Product book | Representative product page | Click `Book now` | Existing ecommerce event or normal diagnostic event if planned | `source_page_type=product`, `product_handle`, `link_text`, `cta_type=booking` | No by default | Confirm cart/checkout behavior unchanged |
| Product quote | Product page with quote/inquiry wording | Click quote/inquiry CTA | `lead_quote_click` or `product_inquiry_click` | `source_page_type=product`, `product_handle`, `link_url`, `link_text`, `cta_type=quote`, `lead_intent=quote` | Yes | Use only for clearly qualified quote actions |
| Car charter quote | `/products/yunnan-private-car-charter-tour` | Click `Request a custom route quote` | `lead_quote_click` | `source_page_type=product`, `product_handle=yunnan-private-car-charter-tour`, `link_url`, `link_text`, `cta_type=quote`, `lead_intent=quote`, `section_context=custom_charter_panel` | Yes | High-priority SEO lead event |
| Car charter WhatsApp | `/products/yunnan-private-car-charter-tour` | Click `Ask on WhatsApp` | `lead_whatsapp_click` | `source_page_type=product`, `product_handle`, `link_url`, `link_text`, `cta_type=whatsapp`, `lead_intent=whatsapp` | Yes | Check duplicate with quote/contact events |
| Bespoke request CTA | `/pages/bespoke-custom-travel` | Click or submit bespoke request CTA/form step | `lead_bespoke_request_click` for click; form event only if separately planned | `source_page_type=bespoke_page`, `source_handle=bespoke-custom-travel`, `link_text`, `cta_type=bespoke_request`, `lead_intent=bespoke_request` | Yes | Do not alter form behavior |
| Collection CTA to bespoke | `/collections/yunnan-private-tours` or related collection | Click bespoke/custom planning CTA | `lead_bespoke_request_click` or `cta_navigation_click` depending approved rule | `source_page_type=collection`, `collection_handle`, `link_url`, `link_text`, `cta_type=bespoke_request`, `lead_intent=bespoke_request` when qualified | Maybe | Decide whether collection support links are high-intent |
| Collection product card | Collection page | Click product card | `collection_product_click` | `source_page_type=collection`, `collection_handle`, `link_url`, `link_text`, `cta_type=product_navigation` | No | Normal engagement only |
| Destination CTA to bespoke | `/pages/kunming`, `/pages/dali`, `/pages/lijiang`, `/pages/shangri-la`, `/pages/xishuangbanna` | Click bespoke/custom CTA | `lead_bespoke_request_click` or `cta_navigation_click` depending approved rule | `source_page_type=destination_page`, `destination_handle`, `link_url`, `link_text`, `cta_type=bespoke_request` | Maybe | Validate source page classification |
| Article internal CTA to product | Guide article | Click product CTA or product card | `article_internal_link_click` | `source_page_type=article_guide`, `article_handle`, `link_url`, `link_text`, `cta_type=article_to_product` | No | Assisted attribution only |
| Article internal CTA to bespoke | Guide article | Click bespoke/custom planning link | `lead_bespoke_request_click` or `article_internal_link_click` depending approved rule | `source_page_type=article_guide`, `article_handle`, `link_url`, `link_text`, `cta_type=bespoke_request` | Maybe | Avoid overcounting informational guide clicks |
| Email click | Contact or qualified lead page | Click `mailto:` link | `lead_email_click` | `source_page_type`, `source_handle`, `link_url`, `link_text`, `cta_type=email`, `lead_intent=email` | Maybe | Key event only if email is accepted as lead intent |
| Phone click | Product/contact page | Click `tel:` link | `lead_phone_click` | `source_page_type`, `source_handle`, `link_url`, `link_text`, `cta_type=phone`, `lead_intent=phone` | Maybe | Key event only if phone is accepted as lead intent |

## 11. Recommendation

Do not implement code in this branch.

Next step:

- P2-D4-A should be a narrow tracking implementation only if this plan is approved.

Implementation guardrails:

- Keep the implementation small and reversible.
- Limit code changes to `snippets/ga4-custom-events.liquid` or a dedicated tracking snippet.
- Do not touch booking, price, variant, checkout, SEO, schema, layout, product template, collection template, or page template logic unless a later approved plan proves it is absolutely necessary.
- Validate normal events before configuring new GA4 key events.
- Preserve the current Contact Us WhatsApp key event until the expanded model is proven in GA4 Realtime and DebugView.

## Exact File Changed

- `docs/seo-audit/2026-05-implementation/P2-8-ga4-event-implementation-plan.md`
