# P2-9 GA4 Lead Click Events Implementation

## 1. What changed

Added normal GA4 lead-intent click event tracking inside the existing delegated click listener in `snippets/ga4-custom-events.liquid`.

The existing click events and form events were preserved. The existing Contact Us / form `generate_lead` behavior was not changed.

## 2. Why it is safe

- The change is limited to GA4 tracking logic.
- It uses the existing delegated document click listener.
- It tracks only user click actions.
- It does not track page-load lead events.
- It does not prevent default click behavior.
- It does not delay navigation.
- It checks for `window.gtag` before sending events.
- It dedupes each new event name with the existing click dedupe helper.
- It sends only one new lead-intent event per click, using a fixed priority order.

## 3. Event names added

- `lead_whatsapp_click`
- `lead_email_click`
- `lead_phone_click`
- `lead_contact_click`
- `lead_bespoke_request_click`
- `lead_quote_click`
- `product_inquiry_click`

## 4. Detection rules

Priority order:

1. `product_inquiry_click`
2. `lead_whatsapp_click`
3. `lead_email_click`
4. `lead_phone_click`
5. `lead_quote_click`
6. `lead_bespoke_request_click`
7. `lead_contact_click`

Rules:

- WhatsApp: link URL contains `wa.me`, `api.whatsapp.com`, or `whatsapp`.
- Email: link href starts with `mailto:`.
- Phone: link href starts with `tel:`.
- Contact page: link path contains `/pages/contact-us`.
- Bespoke / custom itinerary: link path contains `/pages/bespoke-custom-travel`, or visible link text contains `bespoke`, `custom`, `itinerary`, or `plan a custom`.
- Quote / inquiry: visible link text contains `quote`, `request`, `inquiry`, `contact us`, or `request a quote`.
- Product inquiry / booking intent: source page path starts with `/products/` and visible link text contains `book`, `booking`, `inquire`, `inquiry`, `quote`, `contact`, `whatsapp`, or `request`.

## 5. Parameters included

The new events include short, safe values where available:

- `page_location`
- `page_title`
- `source_path`
- `source_page_type`
- `source_handle`
- `link_url`
- `link_text`
- `cta_type`
- `lead_intent`
- `section_context`
- `product_handle`
- `collection_handle`
- `destination_handle`
- `article_handle`

`mailto:` and `tel:` URLs are sanitized to `mailto` and `tel`. WhatsApp URLs are sanitized to `whatsapp`.

## 6. Files changed

- `snippets/ga4-custom-events.liquid`
- `docs/seo-audit/2026-05-implementation/P2-9-ga4-lead-click-events-implementation.md`

## 7. What was not changed

- No GA4 Admin configuration was changed.
- No events were marked as key events in code.
- No Shopify sections were changed.
- No Shopify templates were changed.
- No CSS was changed.
- No product, collection, booking, cart, checkout, price, variant, inventory, JSON-LD, schema, canonical, robots, OG, Twitter, title, or meta logic was changed.
- No CTA text or URLs were changed.
- No Shopify forms were changed.
- No visual layout was changed.

## 8. Manual GA4 Realtime / DebugView validation checklist

Use GA4 Realtime or DebugView and click representative links:

- Click a WhatsApp CTA and confirm `lead_whatsapp_click`.
- Click an email link and confirm `lead_email_click`.
- Click a phone link and confirm `lead_phone_click`.
- Click a `/pages/contact-us` link and confirm `lead_contact_click` unless a higher-priority event applies.
- Click a bespoke / custom itinerary CTA and confirm `lead_bespoke_request_click` unless a higher-priority event applies.
- Click a quote / inquiry CTA and confirm `lead_quote_click` unless a higher-priority event applies.
- From a product page, click a booking / inquiry / quote / contact CTA and confirm `product_inquiry_click`.
- Confirm existing events such as `whatsapp_click`, `email_click`, `phone_click`, `contact_click`, `book_now_click`, `custom_trip_form_submit`, and `generate_lead` still appear where they appeared before.
- Confirm no page-load-only action sends the new lead click events.
- Confirm normal link navigation still works after clicking tracked links.

## 9. Rollback note

Rollback is low risk: remove the new lead-click helper functions and the single new-event send block from `trackClick` in `snippets/ga4-custom-events.liquid`. Existing pre-P2-9 click and form tracking can remain unchanged.
