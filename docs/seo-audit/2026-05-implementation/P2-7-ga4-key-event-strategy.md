# P2-7 GA4 Key Event Strategy

Date: 2026-05-27

Branch: `feat/seo-ga4-key-event-strategy-p2`

Scope: documentation-only GA4 measurement strategy decision for Lynxtour. This document defines which actions should remain normal engagement events, which should become lead-intent events, and which should be considered GA4 key events in a future implementation.

## Safety Note

- This branch is documentation-only.
- No code behavior changed.
- No GA4/GTM implementation changed.
- No Liquid, JSON templates, snippets, CSS, tracking code, SEO title/meta/canonical/schema, links, CTAs, forms, booking, price, variant, cart, or checkout logic was modified.
- No MCP tools were used.

## Exact Files Inspected

Current tracking and layout:

- `layout/theme.liquid`
- `snippets/ga4-custom-events.liquid`

Commercial and lead-intent source surfaces:

- `sections/bespoke-travel.liquid`
- `sections/private-charter-service.liquid`
- `sections/luxury-private-tour-product.liquid`
- `sections/one-day-trip-product.liquid`
- `sections/lijiang-product.liquid`
- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`

Merged P2-D/P2-D1 docs:

- `docs/seo-audit/2026-05-implementation/P2-5-ga4-event-attribution-audit.md`
- `docs/seo-audit/2026-05-implementation/P2-6-ga4-live-click-validation.md`

Related P0/P1 docs:

- `docs/seo-audit/2026-05-implementation/P0-0-contact-url-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P0-3-car-charter-cta-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-1-commercial-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-2-product-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-4-closeout-and-p2-readiness.md`

## Current Confirmed Setup

The current confirmed GA4 key-event setup is narrow:

- Contact Us WhatsApp click is confirmed as a GA4 key event.
- The confirmed page is `/pages/contact-us`.
- Other product, collection, destination, bespoke, guide, quote, booking, phone, or email actions are not confirmed as GA4 key-event sources.
- Other pages not triggering key events is not currently confirmed as a tracking bug.
- The setup is clean and conservative, but it undercounts direct product/page lead intent if Lynxtour wants SEO conversion attribution beyond the Contact Us page.

Local theme context:

- `layout/theme.liquid` renders `snippets/ga4-custom-events.liquid` globally.
- `snippets/ga4-custom-events.liquid` currently sends broad custom events such as `whatsapp_click`, `email_click`, `phone_click`, `contact_click`, `book_now_click`, `custom_trip_form_submit`, and `generate_lead` when `window.gtag` is available.
- P2-D1 live validation confirmed only the Contact Us WhatsApp click as a key event. Exact event name and parameters were not recorded in P2-D1.

## Measurement Goals

Lynxtour needs GA4 to answer these business and SEO questions:

- Which organic landing pages create lead intent?
- Which product pages create WhatsApp, contact, or quote intent?
- Which collection pages assist bespoke planning?
- Whether destination and guide pages assist commercial actions.
- Whether paid social UTMs from TikTok, Facebook, Instagram, or other campaigns can be separated from organic search.

The current contact-page-only key-event setup answers a narrower question:

- Which users reach the Contact Us page and click WhatsApp?

That may be enough for a very conservative lead signal, but it is not enough for full SEO landing-page attribution across product, collection, destination, bespoke, and article journeys.

## Event Hierarchy Recommendation

Use a three-level measurement model. The goal is to separate ordinary navigation from lead intent, and then separate lead intent from official GA4 key events.

### Level 1: Normal Engagement Events

Purpose: measure useful site movement without treating it as lead intent.

Examples:

- Guide internal links.
- Collection navigation.
- Destination page navigation.
- Product detail navigation.
- Non-lead CTA clicks.
- Article-to-guide or guide-to-destination links.
- Generic product-card clicks where the user is still browsing.

Recommended treatment:

- Keep these as normal events.
- Do not mark them as GA4 key events.
- Use them for funnel/path analysis only.

### Level 2: Lead-Intent Events

Purpose: measure actions that suggest direct commercial interest, even if they are not all counted as official conversions/key events.

Examples:

- WhatsApp click.
- Email click.
- Phone click.
- Contact page click.
- Quote request click.
- Bespoke itinerary CTA.
- Product inquiry CTA.
- Car charter quote CTA.
- Lead-like form submit.

Recommended treatment:

- Track with clearer event names and parameters in a future implementation plan.
- Keep as normal events unless they meet key-event eligibility rules.
- Use these events to understand SEO landing-page and assisted-conversion value.

### Level 3: GA4 Key Events

Purpose: count high-intent lead actions that Lynxtour is comfortable treating as conversions.

Recommended key-event candidates:

- Contact Us WhatsApp click.
- Product page WhatsApp or inquiry click.
- Car charter quote or WhatsApp click.
- Bespoke custom itinerary request click.
- Possibly email or phone clicks if Lynxtour confirms they represent real lead intent.

Recommended treatment:

- Mark only selected high-intent lead actions as key events.
- Avoid marking broad navigation, product-card browsing, or low-intent informational clicks as key events.
- Validate each key-event candidate in GA4 Realtime and DebugView before relying on reports.

## Key Event Decision Options

### Option A: Keep Current Setup

- Only Contact Us WhatsApp remains a key event.
- Lowest risk.
- Cleanest signal.
- Under-counts direct product/page leads.

Best fit:

- Lynxtour wants a very conservative conversion count.
- Contact Us WhatsApp is the only action that should count as a formal lead.
- SEO reporting can tolerate missing direct lead intent from product, collection, destination, bespoke, and article pages.

Risk:

- Product-page WhatsApp or quote demand may be invisible in key-event reports.
- Destination or guide pages may look weaker than they are because assisted lead actions are not counted as key events.

### Option B: Track All Lead-Intent Clicks as Normal Events; Keep Only Contact Us WhatsApp as Key Event

- Good diagnostic visibility.
- Conservative conversion count.
- Better than the current setup if tracking coverage is expanded and validated.
- Still undercounts SEO conversions as key events.

Best fit:

- Lynxtour wants to learn where lead intent happens before changing conversion/key-event definitions.
- GA4 key-event reporting should remain conservative for now.
- The immediate need is diagnostic attribution rather than official conversion expansion.

Risk:

- Requires tracking coverage check.
- SEO key-event reports will still show only the narrow Contact Us WhatsApp signal.
- Normal event reports may need custom exploration work to be useful.

### Option C: Track All Qualified Lead-Intent Clicks and Mark Selected High-Intent Ones as Key Events

- Best for SEO conversion attribution.
- Higher risk of inflated conversion count if selectors are too broad.
- Requires consistent event names and parameters.

Best fit:

- Lynxtour wants landing-page and source/medium reports to reflect real lead actions across product, collection, bespoke, destination, and guide journeys.
- Product inquiries, car charter quotes, and bespoke requests are considered conversion-worthy.
- GA4 reporting needs to compare organic search with paid social and other campaigns.

Risk:

- Broad text matching can overcount if generic navigation is included.
- Duplicate firing can inflate leads if one click sends both channel-specific and generic contact events as key events.
- Key events may become less clean if all contact-like clicks are included without strict rules.

Recommended direction:

- Recommend Option C eventually, but only after a narrow implementation plan and live validation.
- For now, proceed with an implementation plan, not code changes.

## Suggested Event Naming Model

This is a strategy proposal only. Do not implement these names until P2-D3 defines exact selectors, event dispatch rules, and GA4 key-event candidates.

| Proposed event | Intended meaning | Suggested key-event eligibility |
|---|---|---|
| `lead_whatsapp_click` | A WhatsApp click from a qualified lead surface | Eligible when from Contact Us, product, quote, bespoke, or high-intent CTA areas |
| `lead_email_click` | A `mailto:` click that indicates direct lead intent | Eligible only if email is a primary inquiry route |
| `lead_phone_click` | A `tel:` click that indicates direct lead intent | Eligible only if phone calls are meaningful leads |
| `lead_quote_click` | A quote-specific CTA click, especially car charter or custom route quote | Eligible when CTA is clearly quote/inquiry oriented |
| `lead_bespoke_request_click` | A bespoke custom itinerary request CTA click | Eligible when the CTA points to bespoke planning or starts a bespoke request |
| `product_inquiry_click` | A product-level inquiry/contact CTA click | Eligible when the source product and CTA intent are clear |
| `cta_navigation_click` | Non-lead navigation CTA click | Not eligible as a key event |

Suggested parameters:

- `page_location`
- `page_title`
- `source_page_type`
- `source_handle`
- `link_url`
- `link_text`
- `cta_type`
- `lead_intent`
- `product_handle` where relevant
- `collection_handle` where relevant
- `article_handle` where relevant

Parameter guidance:

- `source_page_type` should distinguish product, collection, page, article, blog, index, cart, and other page families where possible.
- `source_handle` should hold the current page/product/collection/article handle when available.
- `lead_intent` should use stable values such as `whatsapp`, `email`, `phone`, `quote`, `bespoke_request`, `product_inquiry`, or `contact`.
- `cta_type` should describe the UI action, not only the destination URL.
- `link_text` should remain useful for debugging, but reporting should not depend on text alone.

## Key Event Eligibility Rules

An event should become a GA4 key event only when all of these are true:

- It represents direct contact or inquiry intent.
- It can be tied to a meaningful source page.
- It is not just generic navigation.
- It does not fire automatically on page load.
- It does not duplicate another key event for the same click.
- It can be validated in GA4 Realtime and DebugView.
- It has enough parameters to distinguish source page, CTA type, and lead intent.
- It has a stable naming pattern that will remain understandable in GA4 reports.

Events should not become key events when:

- They only represent browsing or route exploration.
- They are generic internal links without clear inquiry intent.
- They may fire more than once for the same user action.
- They cannot be attributed to a useful source page.
- They depend only on broad text matching that could capture unrelated clicks.

## Risks and Safeguards

| Risk | Why it matters | Safeguard |
|---|---|---|
| Duplicate firing | A single click can inflate lead counts if both generic and specific events are marked as key events | Choose one key-event layer per click; keep secondary events as diagnostics only |
| Inflated lead counts | Broad contact/book/custom text matching can include lower-intent actions | Define exact qualified lead selectors and destination rules before implementation |
| Vague event names | `contact_click` and `book_now_click` are too broad for lead-quality reporting | Use lead-specific names and stable `lead_intent` parameters |
| Missing parameters | Without handles/page type, SEO reports rely on page path and link text only | Add `source_page_type`, `source_handle`, and relevant handle parameters in the plan |
| Page navigation interrupting event dispatch | Clicks that navigate immediately may not always dispatch reliably | Validate in Realtime/DebugView; consider GA4 transport behavior during implementation planning |
| Contact-page-only attribution blind spot | Product, collection, bespoke, destination, and article lead intent may be undercounted | Expand measurement only after P2-D3 plan approval |
| Paid social and organic source separation | UTMs need to remain distinguishable from organic search | Validate GA4 session source/medium/campaign reporting; do not overwrite UTMs in event code |
| Key-event configuration drift | GA4 Admin settings may not match theme event behavior | Document GA4 Admin key-event settings alongside any implementation plan |

## Recommended Next Step

Proceed to P2-D3: narrow GA4 event implementation plan only.

Do not change tracking code yet.

The P2-D3 plan should define:

- Exact lead-intent actions to track.
- Exact selectors or link/destination rules.
- Final event names.
- Final parameters.
- Which events are normal events only.
- Which events are key-event candidates.
- How duplicate firing will be prevented.
- How each event will be validated in GA4 Realtime and DebugView.
- Which GA4 Admin key-event settings must be reviewed.

Implementation should only happen after the plan is approved.

## Decision Summary

The current Contact Us WhatsApp key-event setup is valid and conservative. It should remain the confirmed baseline until Lynxtour approves a broader measurement model.

For SEO conversion attribution, the recommended strategic direction is Option C eventually: track qualified lead-intent clicks and mark only selected high-intent actions as key events. The next task should be an implementation plan, not code changes.

## Exact File Changed

- `docs/seo-audit/2026-05-implementation/P2-7-ga4-key-event-strategy.md`
