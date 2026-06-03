# Schema Phase 2E-A: Article Semantic Context Implementation

## Files Changed

- `sections/main-article.liquid`
- `snippets/seo-article-semantic-context.liquid`
- `docs/seo-audit/2026-06-schema-audit/schema-phase-2e-article-semantic-context-implementation.md`

## Article Handles Covered

- `dianchi-lake-guide`
- `stone-forest-shilin-guide`
- `kunming-city-walk-guide`
- `cuihu-park-green-lake-guide`
- `dali-city-walk-guide`
- `xizhou-ancient-town-guide`
- `erhai-lake-guide`
- `cangshan-mountain-guide`
- `lijiang-travel-guide`
- `lijiang-old-town-guide`
- `jade-dragon-snow-mountain-guide`

## Article Handles Intentionally Left Unchanged

All article handles not listed above are intentionally left unchanged. The semantic context snippet outputs nothing unless the current `article.handle` slug matches the Phase 2E-A mapping.

## Fields Added

Mapped articles receive these fields inside the existing `Article` JSON-LD object:

- `articleSection`
- `about`
- `mentions`
- `keywords`

The Article block still owns the existing `articleBody`, `mainEntityOfPage`, `headline`, optional `description`, optional `image`, `datePublished`, `dateModified`, `author`, and `publisher` fields.

## Entity References Used

Existing stable `TouristDestination` entity references are used where available:

- `https://lynxtour.cn/pages/kunming#touristdestination`
- `https://lynxtour.cn/pages/dali#touristdestination`
- `https://lynxtour.cn/pages/lijiang#touristdestination`

The existing custom travel Service entity is referenced only in mapped Kunming attraction guide mentions where requested:

- `https://lynxtour.cn/pages/bespoke-custom-travel#service`

Attractions and themes without stable Lynxtour entity IDs use conservative name-only entities such as `TouristAttraction`, `Place`, or `Thing`.

## Fields Omitted And Why

- A second `Article` or `BlogPosting` block was omitted to avoid duplicate article schema.
- Ratings, reviews, prices, offers, geo coordinates, opening hours, and fake commercial data were omitted because they are out of scope and not supported by the provided article mapping.
- Product, TouristTrip, TouristDestination, ItemList, Service, CollectionPage, Offer, rating, review, price, geo, and openingHours schema were not added or changed.
- Visible page text, article content, blog content, CSS, JavaScript behavior, Shopify schema, URLs, handles, templates, section names, cart, checkout, booking UI, variant logic, and price display were not changed.

## Validation Checklist

- Preview several mapped article URLs.
- View source and confirm there is still exactly one Article JSON-LD block per article page.
- Confirm mapped articles include `about`, `mentions`, `articleSection`, and `keywords`.
- Confirm unmapped articles still render the original Article schema without added semantic context.
- Confirm existing `BreadcrumbList` still renders.
- Confirm JSON-LD is valid.
- Confirm no Product, Offer, TouristTrip, TouristDestination, ItemList, Service, CollectionPage, rating, review, price, geo, or openingHours schema was added or changed.
- Confirm no visual/UI changes.

## Validation Notes

- The implementation adds one render line inside the existing Article JSON-LD object in `sections/main-article.liquid`.
- `snippets/seo-article-semantic-context.liquid` emits only extra Article properties for mapped handles and emits no JSON-LD script tag.
- All mapped string values are escaped with Liquid `json` filters.
- Source checks confirmed `sections/main-article.liquid` still contains the existing Article JSON-LD script and the existing BreadcrumbList JSON-LD script only.
- `git diff --check -- sections/main-article.liquid snippets/seo-article-semantic-context.liquid docs/seo-audit/2026-06-schema-audit/schema-phase-2e-article-semantic-context-implementation.md` passed.
- `shopify theme check` was run. It exited nonzero with 106 files inspected and 178 total offenses across 36 files, matching the unrelated pre-existing theme baseline pattern such as parser-blocking scripts, remote assets, image dimensions, hardcoded routes, and schema warnings.
- No CSS, JavaScript behavior, URLs, handles, templates, section names, Shopify schema names, Product schema, TouristTrip schema, TouristDestination schema, ItemList schema, Service schema, booking UI, cart, checkout, article content, blog content, product content, or price display was changed.
