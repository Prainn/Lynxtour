# P2-10 GA4 Lead Events Live Validation

## 1. Validation scope

- Validation target: P2-D4-A GA4 lead-intent normal event tracking.
- GA4 tool: Realtime.
- Test environment: live site.
- Status: manual live validation passed for expected event appearance.
- Parameter validation status: not fully recorded.

## 2. Implementation baseline

P2-D4-A added new normal GA4 lead-intent click events for WhatsApp, email, phone, contact, bespoke / custom itinerary, quote / inquiry, and product inquiry intent.

No GA4 key-event configuration was changed. The existing Contact Us WhatsApp key-event behavior should remain unchanged. Existing legacy events such as `whatsapp_click`, `email_click`, `phone_click`, `contact_click`, and `book_now_click` may continue to fire.

No booking, checkout, price, variant, schema, SEO head, CTA, or URL behavior was changed.

## 3. Live validation result table

| Page | Action | Expected new event | Expected legacy event if applicable | Should be key event now? | Observed result | Parameter validation | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| https://lynxtour.cn/pages/contact-us | Click WhatsApp | `lead_whatsapp_click` | `whatsapp_click` may also fire; existing key event should still fire | Existing Contact Us WhatsApp key-event behavior only; do not newly mark P2-D4-A event as key event | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Existing Contact Us WhatsApp key-event behavior should remain unchanged. |
| https://lynxtour.cn/products/jade-dragon-snow-mountain-private-tour | Click WhatsApp / inquiry / contact / request | `product_inquiry_click` | `whatsapp_click` may also fire if WhatsApp link | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Product inquiry has higher priority than generic WhatsApp for the new lead-intent event. |
| https://lynxtour.cn/products/yunnan-private-car-charter-tour | Click quote / WhatsApp / contact | `product_inquiry_click` or `lead_quote_click` depending on clicked element text and source context | `whatsapp_click` may also fire if WhatsApp link | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | A WhatsApp legacy event alongside one new lead-intent event is expected when applicable. |
| https://lynxtour.cn/pages/bespoke-custom-travel | Click custom itinerary / request / contact CTA | `lead_bespoke_request_click` or `lead_quote_click` depending on clicked element text | None specifically expected | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Priority rules determine which single new lead-intent event fires. |
| https://lynxtour.cn/pages/kunming | Click PLAN A CUSTOM YUNNAN ROUTE | `lead_bespoke_request_click` | None specifically expected | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Destination page source context should be reviewed in later parameter validation. |
| https://lynxtour.cn/collections/yunnan-private-tours | Click bespoke / custom / contact CTA | `lead_bespoke_request_click` or `lead_contact_click` depending on clicked element | None specifically expected | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Collection source context should be reviewed in later parameter validation. |
| Sitewide where visible | Click mailto link if visible | `lead_email_click` | `email_click` may also fire | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Full email-link parameter details were not recorded. |
| Sitewide where visible | Click tel link if visible | `lead_phone_click` | `phone_click` may also fire | No | Expected event appeared according to user manual GA4 Realtime validation | Not fully recorded | Pass for event appearance | Full phone-link parameter details were not recorded. |

## 4. Parameter checklist

Parameters that should be checked in a later parameter-level validation:

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
- `product_handle` where relevant
- `collection_handle` where relevant
- `destination_handle` where relevant
- `article_handle` where relevant

Event appearance was validated. Parameter-level completeness was not fully recorded and remains a watch item.

## 5. Pass / watch / block assessment

Pass:

- Expected new events appeared in GA4 Realtime during user manual testing.
- No confirmed blocker was reported.
- No key-event configuration change was made.

Watch:

- Parameter-level validation was not fully recorded.
- DebugView validation was not separately recorded.
- Future key-event configuration should wait until candidate events are reviewed.

Block:

- None reported.

## 6. Recommendation

Do not change tracking code further now. Do not mark all new events as key events automatically.

Proceed to P2-D4-C GA4 key-event candidate review. Candidate review should decide which of the newly visible events should become GA4 key events. Keep parameter-level validation as a watch item.

## 7. Safety note

- This branch is documentation-only.
- No code behavior changed.
- No GA4/GTM implementation changed.
- No key-event configuration changed.
