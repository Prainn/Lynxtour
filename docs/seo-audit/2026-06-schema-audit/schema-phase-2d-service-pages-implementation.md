# Schema Phase 2D: Service Pages Implementation

## Files Changed

- `snippets/seo-service-jsonld.liquid`
- `sections/bespoke-travel.liquid`
- `sections/private-charter-service.liquid`

## Pages Covered

- `/pages/bespoke-custom-travel`
- `/products/yunnan-private-car-charter-tour`

Each page gets one conservative `Service` JSON-LD block from visible page or product copy.

## Service @id Patterns

- `https://lynxtour.cn/pages/bespoke-custom-travel#service`
- `https://lynxtour.cn/products/yunnan-private-car-charter-tour#service`

## Fields Included

- `@context`
- `@type: Service`
- `@id`
- `name`
- `serviceType`
- `url`
- `description`
- `provider` as `https://lynxtour.cn/#organization`
- `areaServed`
- `audience`
- `mainEntityOfPage` as `WebPage`

All string fields are escaped with Liquid `json` filters. Descriptions are stripped of HTML before output.

## Source of Service Data

### Bespoke Custom Travel

The description uses visible hero copy from `sections/bespoke-travel.liquid`: the page asks travelers to share dates, pace, destinations, budget style, hotel preferences, and interests, then has a local Yunnan specialist review the request before sending a tailored itinerary and quotation. It also references visible copy about private Yunnan routes across Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna, and custom combinations.

### Yunnan Private Car Charter

The description uses visible lower-page copy from `sections/private-charter-service.liquid`: the car charter is described as a transport-first private service for travelers who want a private vehicle, driver-guide support, flexible pickup city, route timing control, one-day transfers, multi-day intercity routes, airport pickup with onward travel, or custom Yunnan routing.

## Fields Intentionally Omitted

- `Offer`, prices, `priceRange`, fake rates, and commercial quote data were omitted because the Service schema should not duplicate Product/Offer data or imply fixed service pricing.
- `aggregateRating`, `rating`, and `review` were omitted because no review/rating data was added for this phase.
- `geo`, coordinates, and `openingHours` were omitted because they are not needed for these conversion/service pages and were out of scope.
- Product, TouristTrip, TouristDestination, ItemList, Article, BlogPosting, and CollectionPage schema were not added or changed.

## Car Charter Scope Control

The car charter Service render is inside:

```liquid
{% if product.handle == 'yunnan-private-car-charter-tour' %}
```

This keeps Service schema limited to `/products/yunnan-private-car-charter-tour` and prevents normal tour products from outputting Service schema. The existing Product JSON-LD render remains unchanged and still runs after the Service block.

## Validation Checklist

- Preview `/pages/bespoke-custom-travel`.
- Preview `/products/yunnan-private-car-charter-tour`.
- View source and confirm exactly one Service block on each page.
- Confirm normal tour products do not output Service.
- Confirm existing Product schema still renders on the car charter product.
- Confirm existing FAQPage and BreadcrumbList still render where present.
- Confirm JSON-LD is valid.
- Confirm no Product, Offer, TouristTrip, TouristDestination, ItemList, Article, BlogPosting, CollectionPage, rating, review, price, priceRange, geo, or openingHours schema was added or changed.
- Confirm no visual/UI changes.

## Validation Notes

- `git diff --check` passed.
- `shopify theme check` was run. It exited nonzero with 105 files inspected and 178 total offenses across 36 files, matching unrelated pre-existing theme baseline issues such as parser-blocking scripts, remote assets, image dimensions, hardcoded routes, and schema warnings.
- Direct source checks confirmed the new `seo-service-jsonld` snippet does not contain Product, Offer, TouristTrip, TouristDestination, ItemList, Article, BlogPosting, CollectionPage, rating, review, price, priceRange, geo, or openingHours fields.
- No CSS, JavaScript behavior, URLs, handles, templates, section names, Shopify schema names, booking UI, cart, checkout, Product schema, TouristTrip schema, TouristDestination schema, ItemList schema, Article schema, BlogPosting schema, pricing display, or visible content was changed.
