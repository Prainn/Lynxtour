# Schema Phase 3: Rendered Source Validation

## Purpose

This phase validates live rendered HTML and page source after deployment. It is not a theme-source-code audit. The goal is to confirm that Shopify, theme Liquid, app injections, and rendered JSON-LD output combine into a valid, consistent schema entity graph on real URLs.

## Tools To Use

- Google Rich Results Test
- Schema.org Validator
- Browser view-source
- Google Search Console URL Inspection for important URLs after validation

## URL Groups To Validate

### Homepage

- `https://lynxtour.cn/`

### Destination Pages

- `https://lynxtour.cn/pages/kunming`
- `https://lynxtour.cn/pages/dali`
- `https://lynxtour.cn/pages/lijiang`
- `https://lynxtour.cn/pages/shangri-la`
- `https://lynxtour.cn/pages/xishuangbanna`

### Product Pages

- `https://lynxtour.cn/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `https://lynxtour.cn/products/kunming-dali-lugu-lake-lijiang-shangri-la-10-day-private-tour`
- `https://lynxtour.cn/products/kunming-dali-lijiang-6-day-private-tour`
- `https://lynxtour.cn/products/jade-dragon-snow-mountain-private-tour`
- `https://lynxtour.cn/products/lijiang-to-shangri-la-private-tour`
- `https://lynxtour.cn/products/shangri-la-pudacuo-national-park-songzanlin-monastery-1-day-private-tour`
- `https://lynxtour.cn/products/yunnan-private-car-charter-tour`

### Itinerary Pages

- `https://lynxtour.cn/pages/dali-itinerary-3-days`
- `https://lynxtour.cn/pages/lijiang-itinerary-3-days`
- `https://lynxtour.cn/pages/dali-itinerary-2-days`
- `https://lynxtour.cn/pages/lijiang-itinerary-2-days`
- `https://lynxtour.cn/pages/dali-to-lijiang-private-tour`
- `https://lynxtour.cn/pages/tiger-leaping-gorge-from-lijiang`

### Service Page

- `https://lynxtour.cn/pages/bespoke-custom-travel`

### Article Pages

2E-A samples:

- `https://lynxtour.cn/blogs/travel-guides/dianchi-lake-guide`
- `https://lynxtour.cn/blogs/travel-guides/lijiang-old-town-guide`
- `https://lynxtour.cn/blogs/travel-guides/jade-dragon-snow-mountain-guide`

2E-B samples:

- `https://lynxtour.cn/blogs/travel-guides/xishuangbanna-travel-guide`
- `https://lynxtour.cn/blogs/travel-guides/shangri-la-travel-guide`
- `https://lynxtour.cn/blogs/travel-guides/songzanlin-monastery-guide`
- `https://lynxtour.cn/blogs/travel-guides/lijiang-naxi-culture-dongba-guide`

Unmapped article:

- `[choose one article not covered by 2E-A or 2E-B]`

## Expected Schema By Page Type

### Homepage Expected

- `Organization` / `TravelAgency`
- `WebSite`
- No `Product`
- No `TouristTrip`
- No `Service` unless intentionally added later

### Destination Page Expected

- `Organization` / `TravelAgency` from global layout
- `WebSite` from global layout
- `TouristDestination`
- `BreadcrumbList` if already present
- `FAQPage` if already present
- No `Product`
- No `TouristTrip`
- No `Service`

### Normal Tour Product Expected

- `Organization` / `TravelAgency`
- `WebSite`
- `Product`
- `BreadcrumbList`
- `TouristTrip` only for mapped target products
- No `Service` except car charter
- No `"price": 0` for quote/custom variants

### Car Charter Product Expected

- `Organization` / `TravelAgency`
- `WebSite`
- `Product`
- `Service`
- `BreadcrumbList`
- No `TouristTrip`
- No fake `Offer`, `priceRange`, `rating`, or `review`

### Itinerary Page Expected

- `Organization` / `TravelAgency`
- `WebSite`
- `ItemList` only on the four day-by-day itinerary pages
- No `ItemList` on the two route narrative pages unless `route_step` data exists in future
- `FAQPage` and `BreadcrumbList` remain if already present
- No `Product`
- No `TouristTrip`
- No `Service`

### Bespoke Page Expected

- `Organization` / `TravelAgency`
- `WebSite`
- `Service`
- `BreadcrumbList` if present
- No `Product`
- No `TouristTrip`
- No `ItemList`

### Article Page Expected

- `Organization` / `TravelAgency`
- `WebSite`
- Exactly one `Article` JSON-LD block
- `BreadcrumbList`
- Mapped articles include `articleSection`, `about`, `mentions`, and `keywords`
- Unmapped articles keep original `Article` schema without semantic context
- No `Product`
- No `TouristTrip`
- No `Service`
- No `ItemList`

## Manual View-Source Checks

Search rendered source for:

- `application/ld+json`
- `"@type": "Article"`
- `"@type": "Product"`
- `"@type": "TouristTrip"`
- `"@type": "TouristDestination"`
- `"@type": "ItemList"`
- `"@type": "Service"`
- `#organization`
- `#website`
- `#product`
- `#touristtrip`
- `#touristdestination`
- `#service`
- `#itinerary`
- `"price": 0`
- `"price": "0"`
- `aggregateRating`
- `review`

## Pass/Fail Table

| URL | Page type | Expected schema | Unexpected schema found | Validator result | Warnings | Action needed | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `https://lynxtour.cn/` | Homepage | `Organization` / `TravelAgency`, `WebSite` |  |  |  |  |  |
| `https://lynxtour.cn/pages/kunming` | Destination | `Organization` / `TravelAgency`, `WebSite`, `TouristDestination`, optional `BreadcrumbList` / `FAQPage` |  |  |  |  |  |
| `https://lynxtour.cn/products/kunming-dali-lijiang-shangri-la-8-day-private-tour` | Product | `Organization` / `TravelAgency`, `WebSite`, `Product`, `BreadcrumbList`, mapped `TouristTrip` if expected |  |  |  |  |  |
| `https://lynxtour.cn/products/yunnan-private-car-charter-tour` | Car charter product | `Organization` / `TravelAgency`, `WebSite`, `Product`, `Service`, `BreadcrumbList` |  |  |  |  |  |
| `https://lynxtour.cn/pages/dali-itinerary-3-days` | Itinerary | `Organization` / `TravelAgency`, `WebSite`, `ItemList`, optional `BreadcrumbList` / `FAQPage` |  |  |  |  |  |
| `https://lynxtour.cn/pages/dali-to-lijiang-private-tour` | Route narrative | `Organization` / `TravelAgency`, `WebSite`, optional `BreadcrumbList` / `FAQPage`; no `ItemList` unless route data exists |  |  |  |  |  |
| `https://lynxtour.cn/pages/bespoke-custom-travel` | Service | `Organization` / `TravelAgency`, `WebSite`, `Service`, optional `BreadcrumbList` |  |  |  |  |  |
| `https://lynxtour.cn/blogs/travel-guides/dianchi-lake-guide` | Article 2E-A | `Organization` / `TravelAgency`, `WebSite`, one `Article`, `BreadcrumbList`, semantic context |  |  |  |  |  |
| `https://lynxtour.cn/blogs/travel-guides/xishuangbanna-travel-guide` | Article 2E-B | `Organization` / `TravelAgency`, `WebSite`, one `Article`, `BreadcrumbList`, semantic context |  |  |  |  |  |
| `[choose one article not covered by 2E-A or 2E-B]` | Unmapped article | `Organization` / `TravelAgency`, `WebSite`, one original `Article`, `BreadcrumbList`; no semantic context |  |  |  |  |  |

## Known Acceptable Warnings

- Google Rich Results Test may not show rich results for every schema type.
- Some non-critical `LocalBusiness` / `TravelAgency` warnings may appear depending on optional properties.
- Schema.org types like `TouristTrip`, `TouristDestination`, and `Service` may validate structurally but not trigger Google rich result eligibility.
- The goal is a valid, consistent entity graph, not forcing every page into a rich result.

## Failure Patterns To Watch

- Duplicate `Article` JSON-LD
- Duplicate `Product` schema
- Product page outputting `"price": 0` or `"price": "0"` for quote/custom variants
- `Service` appearing on normal tour products
- `TouristTrip` appearing on car charter product
- `ItemList` appearing on narrative route pages without `route_step` data
- Article semantic context appearing on unmapped articles
- Invalid JSON caused by comma placement
- Old app-injected schema conflicting with theme schema

## Post-Validation Actions

If all pass:

- Commit the validation report.
- Submit or request indexing for priority URLs in Google Search Console.
- Monitor Enhancements, Merchant listings, Products, and Breadcrumbs where applicable.
- Wait for recrawl before judging ranking impact.

If issues are found:

- Create a fix branch specific to the issue.
- Do not batch unrelated schema fixes into one branch.

## Final Summary

- Date validated:
- Validator used:
- URLs passed:
- URLs needing fixes:
- Notes:
- Next recommended action:
