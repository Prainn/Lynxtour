# Schema Phase 2B: TouristTrip Implementation

## Files Changed

- `snippets/seo-tourist-trip-jsonld.liquid`
- `snippets/seo-product-jsonld.liquid`
- `docs/seo-audit/2026-06-schema-audit/schema-phase-2b-tourist-trips-implementation.md`

## Product Handles Covered

- `kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `kunming-dali-lugu-lake-lijiang-shangri-la-10-day-private-tour`
- `kunming-dali-lijiang-6-day-private-tour`
- `jade-dragon-snow-mountain-private-tour`
- `lijiang-to-shangri-la-private-tour`
- `shangri-la-pudacuo-national-park-songzanlin-monastery-1-day-private-tour`

## Product Handles Intentionally Omitted

- `yunnan-private-car-charter-tour`

The car charter page is intentionally omitted because it is not a route-level tour itinerary. It is better handled later as Service schema and should not be described as a TouristTrip.

## TouristTrip @id Patterns

- `https://lynxtour.cn/products/kunming-dali-lijiang-shangri-la-8-day-private-tour#touristtrip`
- `https://lynxtour.cn/products/kunming-dali-lugu-lake-lijiang-shangri-la-10-day-private-tour#touristtrip`
- `https://lynxtour.cn/products/kunming-dali-lijiang-6-day-private-tour#touristtrip`
- `https://lynxtour.cn/products/jade-dragon-snow-mountain-private-tour#touristtrip`
- `https://lynxtour.cn/products/lijiang-to-shangri-la-private-tour#touristtrip`
- `https://lynxtour.cn/products/shangri-la-pudacuo-national-park-songzanlin-monastery-1-day-private-tour#touristtrip`

The Product `@id` remains `https://lynxtour.cn/products/{handle}#product`. The TouristTrip `@id` is stable and distinct.

## Itinerary Route Lists Used

### 8-Day Kunming, Dali, Lijiang & Shangri-La Private Tour

- Kunming: `TouristDestination`, `https://lynxtour.cn/pages/kunming#touristdestination`
- Dali: `TouristDestination`, `https://lynxtour.cn/pages/dali#touristdestination`
- Lijiang: `TouristDestination`, `https://lynxtour.cn/pages/lijiang#touristdestination`
- Shangri-La: `TouristDestination`, `https://lynxtour.cn/pages/shangri-la#touristdestination`

### 10-Day Kunming, Dali, Lugu Lake, Lijiang & Shangri-La Private Tour

- Kunming: `TouristDestination`, `https://lynxtour.cn/pages/kunming#touristdestination`
- Dali: `TouristDestination`, `https://lynxtour.cn/pages/dali#touristdestination`
- Lugu Lake: `Place`, name only
- Lijiang: `TouristDestination`, `https://lynxtour.cn/pages/lijiang#touristdestination`
- Shangri-La: `TouristDestination`, `https://lynxtour.cn/pages/shangri-la#touristdestination`

### 6-Day Kunming, Dali & Lijiang Private Tour

- Kunming: `TouristDestination`, `https://lynxtour.cn/pages/kunming#touristdestination`
- Dali: `TouristDestination`, `https://lynxtour.cn/pages/dali#touristdestination`
- Lijiang: `TouristDestination`, `https://lynxtour.cn/pages/lijiang#touristdestination`

### Jade Dragon Snow Mountain Private Tour

- Lijiang: `TouristDestination`, `https://lynxtour.cn/pages/lijiang#touristdestination`
- Jade Dragon Snow Mountain: `TouristAttraction`, name only
- Blue Moon Valley: `TouristAttraction`, name only

### Lijiang to Shangri-La Private Tour

- Lijiang: `TouristDestination`, `https://lynxtour.cn/pages/lijiang#touristdestination`
- Tiger Leaping Gorge: `TouristAttraction`, name only
- Shangri-La: `TouristDestination`, `https://lynxtour.cn/pages/shangri-la#touristdestination`

### Shangri-La Pudacuo National Park & Songzanlin Monastery 1-Day Private Tour

- Shangri-La: `TouristDestination`, `https://lynxtour.cn/pages/shangri-la#touristdestination`
- Songzanlin Monastery: `TouristAttraction`, name only
- Pudacuo National Park: `TouristAttraction`, name only

## Fields Included

- `@context`
- `@type: TouristTrip`
- `@id`
- `name`
- `url`
- `description`
- `provider` referencing `https://lynxtour.cn/#organization`
- `touristType`
- `duration` where a safe duration is available
- `itinerary` as a route-level `ItemList`
- `mainEntityOfPage` using `https://lynxtour.cn/products/{handle}#webpage`

Descriptions use the visible Shopify product description when available. If the product description is blank, the handle-scoped fallback description from the implementation brief is used.

## Fields Omitted and Why

- `offers` omitted to avoid duplicating or conflicting with the existing Product Offer schema.
- `duration` omitted for `lijiang-to-shangri-la-private-tour` because no safe visible duration was found in the template content.
- Product relationship via `subjectOf` or `isRelatedTo` omitted because a Product reference is not a conservative fit for those TouristTrip properties. The Product and TouristTrip nodes remain connected by stable same-page URLs and distinct `@id` patterns.
- Attraction URLs and `@id` values omitted for Lugu Lake, Blue Moon Valley, Tiger Leaping Gorge, Songzanlin Monastery, Pudacuo National Park, and Jade Dragon Snow Mountain because no stable Lynxtour destination page IDs exist for them in the current schema graph.
- `aggregateRating`, `review`, fake price, `priceRange`, geo coordinates, `openingHours`, Service schema, BlogPosting schema, TouristDestination changes, CollectionPage schema, and collection ItemList schema omitted as out of scope.

## Validation Checklist

- Preview each target product page.
- View source and confirm exactly one TouristTrip block on each target product page.
- Confirm non-target products do not output TouristTrip.
- Confirm existing Product schema still renders.
- Confirm Product `@id` and TouristTrip `@id` are stable and distinct.
- Confirm Product seller still points to `https://lynxtour.cn/#organization`.
- Confirm no quote/custom product emits fake price 0.
- Confirm JSON-LD is valid.
- Confirm no visual/UI changes.
