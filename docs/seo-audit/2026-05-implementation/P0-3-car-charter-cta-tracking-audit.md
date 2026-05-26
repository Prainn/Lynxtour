# P0-3 Car Charter CTA and Tracking Audit

Date: 2026-05-26

## Scope

This audit used local theme files only. No booking logic, product price logic, variants, redirects, structured data, or GA4/GTM code were changed.

## Files Inspected

- `layout/theme.liquid`
- `templates/product.private-charter.json`
- `sections/private-charter-service.liquid`
- `snippets/display-variant-price.liquid`
- `snippets/ga4-custom-events.liquid`
- `docs/seo-audit/2026-05-ga4/01-organic-landing-pages.csv`
- `docs/seo-audit/2026-05-ga4/03-organic-by-device.csv`

## Page Control

The `/products/yunnan-private-car-charter-tour` product uses `templates/product.private-charter.json`, which renders:

- `global-navigation`
- `private-charter-service`
- `footer`

The main page behavior and visible booking/custom-charter UI are controlled by `sections/private-charter-service.liquid`.

## Existing CTA Labels and Destinations

Main booking UI:

- `Add to booking list`: button with `class="ota-btn-cart js-submit"` and `data-type="cart"`.
- `Book now`: button with `class="ota-btn-buy js-submit"` and `data-type="buy"`.

Custom charter panel:

- Before patch: `Contact a travel advisor` -> `/pages/contact-us`.
- Before patch: `Call hotline 0871-63218099` -> `tel:0871-63218099`.
- Before patch: `Message on WhatsApp` -> `https://wa.me/8613211685553`.

Lower route-planning links:

- `/collections/yunnan-private-tours`
- `/pages/kunming`
- `/pages/dali`
- `/pages/lijiang`
- `/pages/shangri-la`
- `/collections/yunnan-private-day-trips`
- `/pages/bespoke-custom-travel`

## Tracking Hook Review

`snippets/ga4-custom-events.liquid` uses delegated click tracking rather than per-link data attributes.

Recognizable hooks:

- WhatsApp URLs containing `wa.me`, `api.whatsapp.com`, or `whatsapp.com/send` trigger `whatsapp_click`.
- `tel:` links trigger `phone_click`.
- `/pages/contact-us` and contact-like link text trigger `contact_click`.
- Text such as `book now`, `booking`, and `add to booking list` triggers `book_now_click`.

The car charter page's contact, phone, WhatsApp, add-to-booking, and Book now controls are all recognizable by the existing delegated tracking logic. No small tracking-code bug was confirmed.

## Safe Patch Applied

In `sections/private-charter-service.liquid`, the existing custom charter panel copy was clarified:

- Heading changed to `Request a custom car charter quote`.
- Body now explicitly says `private car with driver`, `flexible route`, and `custom Yunnan car charter quote`.
- Contact link label changed to `Request a custom route quote`.
- WhatsApp label changed to `Ask on WhatsApp`.

No destinations, form behavior, booking buttons, variants, or prices were changed.

## Interpretation

The weak or unclear landing-level key event signal appears more likely to be a mix of small sample size and CTA clarity than a confirmed tracking failure. The tracking hooks are broad enough to capture the existing contact, WhatsApp, phone, and booking-intent actions.

## Recommended Follow-Up

After deployment, compare GA4 landing-page key events and pages/screens events for `/products/yunnan-private-car-charter-tour`. If events still appear in pages/screens but not landing reports, review attribution/reporting configuration before changing theme tracking.
