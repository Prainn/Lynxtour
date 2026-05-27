# P2-6 GA4 Live Click Validation

Date: 2026-05-27

Branch: `feat/seo-ga4-live-validation-p2`

Scope: documentation-only GA4 live validation report based only on the user-provided manual GA4 Realtime result.

## Safety Note

- This branch is validation-only.
- No code behavior changed.
- No GA4/GTM implementation changed.
- No Liquid, JSON templates, snippets, CSS, tracking code, SEO title/meta/canonical/schema, links, CTAs, forms, booking, price, variant, cart, or checkout logic was modified.

## Validation Scope

Validation method:

- GA4 Realtime was used by the user for manual validation.

Confirmed page:

- `https://lynxtour.cn/pages/contact-us`

Confirmed action:

- WhatsApp click on the Contact Us page triggers a GA4 key event.

Event detail note:

- Exact GA4 event name: not recorded.
- Exact GA4 parameters: not recorded.
- If the exact event name or parameters are provided later, this report can be updated without changing site behavior.

## Test Result Summary

| Page | Action | Observed key event behavior | Expected based on current setup | Status | Notes |
|---|---|---|---|---|---|
| `https://lynxtour.cn/pages/contact-us` | WhatsApp click on Contact Us page | Triggers GA4 key event | Expected, because the known historical setup was configured for this contact page | Pass | Exact event name and parameters were not recorded |
| Other commercial/product pages | Direct WhatsApp, inquiry, booking, or product CTA actions | Not validated as key events from the user-provided result | May not be configured as key events under the current historical setup | Watch | Not currently confirmed as a bug |
| Car charter/product quote surfaces | Quote or inquiry CTA actions | Not validated as key events from the user-provided result | May not be configured as key events unless separately configured | Watch | Attribution-limited if quote intent is a reporting goal |
| Bespoke page and bespoke CTAs | Bespoke custom itinerary actions | Not validated as key events from the user-provided result | May not be configured as key events unless separately configured | Watch | Exact event names and parameters were not recorded |
| Collection pages | Collection-to-inquiry or collection-to-bespoke CTA actions | Not validated as key events from the user-provided result | May not be configured as key events unless separately configured | Watch | Not currently confirmed as a bug |
| Destination pages | Destination CTA, WhatsApp, contact, or bespoke actions | Not validated as key events from the user-provided result | May not be configured as key events unless separately configured | Watch | Not currently confirmed as a bug |
| Article/guide pages | Article-to-product or article-to-bespoke assisted inquiry actions | Not validated as key events from the user-provided result | May not be configured as key events unless separately configured | Watch | Not currently confirmed as a bug |

## Interpretation

The current live behavior matches the known historical setup: tracking/key-event configuration was previously only set up for WhatsApp clicks on the Contact Us page.

No confirmed GA4 tracking bug was found from the user-provided validation result.

The current setup is intentionally narrow or historically narrow. It is suitable if Lynxtour only wants Contact Us WhatsApp clicks counted as GA4 key events.

The setup is attribution-limited if Lynxtour wants to measure SEO-driven WhatsApp or inquiry clicks from product, collection, bespoke, destination, or article pages. Other pages not triggering key events is not currently confirmed as a bug under the current setup.

## Attribution Limitation

The current key-event setup may undercount:

- Product page WhatsApp or inquiry intent.
- Car charter quote intent.
- Bespoke custom itinerary intent.
- Collection-to-inquiry intent.
- Destination-page assisted inquiry intent.
- Article-to-commercial assisted inquiry intent.

This limitation affects SEO conversion attribution because organic visitors may take commercial actions before reaching the Contact Us page, but those actions may not be counted as GA4 key events unless separately configured.

## Recommended Next Step

Do not modify code yet.

Proceed to P2-D2 measurement strategy decision. Decide whether key events should remain contact-page-only or expand to all qualified lead actions.

If expansion is approved, create a narrow implementation plan before touching GA4/GTM code.

## Suggested P2-D2 Decision Options

### Option A: Keep Current Setup

- Only Contact Us WhatsApp click is a key event.
- Lowest risk.
- Cleanest signal.
- Under-counts direct product/page leads.

Recommendation status: valid if Lynxtour wants only high-confidence Contact Us WhatsApp leads in key-event reporting.

### Option B: Track All WhatsApp Clicks as a Normal Event, but Only Contact Us WhatsApp Remains Key Event

- Better diagnostic data.
- Key event remains conservative.
- Requires tracking coverage check.

Recommendation status: useful middle path if Lynxtour wants visibility without expanding conversion/key-event counting yet.

### Option C: Count All Qualified WhatsApp / Quote / Inquiry Clicks as Key Events

- Best for SEO conversion attribution.
- Higher risk of inflated leads if low-intent clicks are included.
- Requires consistent event names and parameters.

Recommendation status: only recommended after a measurement strategy is approved and a narrow implementation plan is documented.

## Exact File Changed

- `docs/seo-audit/2026-05-implementation/P2-6-ga4-live-click-validation.md`
