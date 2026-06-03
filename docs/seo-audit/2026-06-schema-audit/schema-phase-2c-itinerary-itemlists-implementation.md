# Schema Phase 2C: Itinerary ItemList Implementation

## Files Changed

- `snippets/seo-itinerary-itemlist-jsonld.liquid`
- `sections/seo-itinerary-page.liquid`
- `sections/page-route-support.liquid`

## Pages Covered

- `/pages/dali-itinerary-3-days`
- `/pages/lijiang-itinerary-3-days`
- `/pages/dali-itinerary-2-days`
- `/pages/lijiang-itinerary-2-days`

These pages use visible `day` blocks in `sections/seo-itinerary-page.liquid`, so each visible day card maps cleanly to one `ListItem`.

## Pages Intentionally Skipped

- `/pages/dali-to-lijiang-private-tour`
- `/pages/tiger-leaping-gorge-from-lijiang`

These pages render through `sections/page-route-support.liquid`, but their visible `feature` cards describe route rationale, audience, flexibility, and onward planning. They are not clear route stops or step-by-step route sections. To avoid inventing route steps or misclassifying narrative content as route items, the section renders the shared snippet with `route_step` blocks only. No such blocks exist in the section schema, so no ItemList is output on these pages.

## ItemList @id Patterns

- `https://lynxtour.cn/pages/dali-itinerary-3-days#itinerary`
- `https://lynxtour.cn/pages/lijiang-itinerary-3-days#itinerary`
- `https://lynxtour.cn/pages/dali-itinerary-2-days#itinerary`
- `https://lynxtour.cn/pages/lijiang-itinerary-2-days#itinerary`

Route `@id` patterns are reserved in the snippet for safe future route-step data:

- `https://lynxtour.cn/pages/dali-to-lijiang-private-tour#route`
- `https://lynxtour.cn/pages/tiger-leaping-gorge-from-lijiang#route`

They do not output in this phase because there is no extractable visible route-step data.

## Number of Items Per Page

- `/pages/dali-itinerary-3-days`: 3 items
- `/pages/lijiang-itinerary-3-days`: 3 items
- `/pages/dali-itinerary-2-days`: 2 items
- `/pages/lijiang-itinerary-2-days`: 2 items
- `/pages/dali-to-lijiang-private-tour`: 0 items, skipped
- `/pages/tiger-leaping-gorge-from-lijiang`: 0 items, skipped

## Source of Item Data

- Source section: `sections/seo-itinerary-page.liquid`
- Source blocks: visible `day` blocks
- Item name source: visible day `tag` plus visible day `heading`
- Item description source: visible day `copy`

The four itinerary templates provide this data in their `main` section block settings. No copy was invented.

## Fields Included

- `@context`
- `@type: ItemList`
- `@id`
- `name`
- `url`
- `itemListOrder`
- `numberOfItems`
- `mainEntityOfPage` as `WebPage`
- `itemListElement`
- `ListItem.position`
- `ListItem.name`
- `ListItem.description` when visible copy exists

All string values are escaped with Liquid `json` filters.

## Fields Omitted

- Product, Offer, TouristTrip, TouristDestination, Service, BlogPosting, CollectionPage, and collection ItemList schema were omitted as out of scope.
- Ratings, reviews, prices, geo coordinates, opening hours, and fake commercial attributes were omitted because they are not visible itinerary item data and were explicitly out of scope.
- Route ItemList output was omitted because the target route pages do not expose visible step-by-step stop data.

## Validation Checklist

- Preview each target page.
- View source and confirm exactly one ItemList block on each covered itinerary page.
- Confirm `/pages/dali-to-lijiang-private-tour` and `/pages/tiger-leaping-gorge-from-lijiang` do not output ItemList.
- Confirm existing FAQPage and BreadcrumbList still render.
- Confirm JSON-LD is valid.
- Confirm no Product, Offer, TouristTrip, TouristDestination, Service, BlogPosting, rating, review, price, geo, or openingHours schema was added.
- Confirm no visual/UI changes.

## Validation Notes

- `shopify theme check` was run for the full theme. It exited nonzero because of pre-existing unrelated theme offenses in other files, including image dimension, parser-blocking script, remote asset, hardcoded route, and schema-template warnings/errors.
- Direct source checks on the changed files confirmed no forbidden schema terms were added.
- No CSS, JavaScript, URLs, handles, templates, section names, Shopify schema names, booking UI, cart, checkout, Product schema, TouristTrip schema, TouristDestination schema, Article schema, or BlogPosting schema were changed.
