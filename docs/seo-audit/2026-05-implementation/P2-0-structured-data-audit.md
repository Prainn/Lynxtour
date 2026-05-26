# P2-0 Structured Data Audit

Date: 2026-05-26
Branch: `feat/seo-structured-data-audit-p2`
Scope: audit-only, documentation-only.

## Guardrails

- No Liquid behavior changed.
- No JSON templates changed.
- No CSS changed.
- No snippets changed.
- No product schema changed.
- No Product JSON-LD, price, variant, offer, availability, GA4/GTM, or redirect logic changed.
- Local repository files only. No MCP tools used.

## Exact Files Inspected

Requested files and areas inspected:

- `layout/theme.liquid`
- `snippets/seo-product-jsonld.liquid`
- `snippets/display-variant-price.liquid`
- `snippets/ga4-custom-events.liquid`
- `sections/luxury-private-tour-product.liquid`
- `sections/lijiang-product.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/one-day-trip-product.liquid`
- `sections/private-charter-service.liquid`
- `sections/main-article.liquid`
- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `templates/product.luxury-private-tour.json`
- `templates/product.jade-dragon-snow-mountain-private-tour.json`
- `templates/product.lijiang-to-shangri-la-private-tour.json`
- `templates/product.private-charter.json`
- `templates/product.one-day-trip.json`
- `templates/article.json`
- `templates/blog.json`
- `templates/page.destinations.json`
- `templates/page.dali.json`
- `templates/page.lijiang.json`
- `templates/page.lijiang-itinerary-3-days.json`
- `templates/page.dali-to-lijiang-private-tour.json`

Additional files inspected because repo search showed active or possible structured data:

- `sections/dali-product.liquid`
- `sections/shangri-la-product.liquid`
- `sections/xishuangbanna-product.liquid`
- `sections/product-route-support.liquid`
- `sections/page-route-support.liquid`
- `sections/seo-itinerary-page.liquid`
- `sections/destinations-page-overview.liquid`
- `sections/product-reviews.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/kunming-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`
- `sections/dali-collection.liquid`
- `sections/lijiang-collection.liquid`
- `sections/shangri-la-collection.liquid`
- `sections/xishuangbanna-collection.liquid`
- `sections/main-blog.liquid`
- `templates/collection.all-tuors-collection.json`
- `templates/collection.day-trips-collection.json`
- `templates/collection.luxury-private-tour.json`
- Product, collection, article/blog, and page templates listed by `rg --files`.

Repo search terms used:

- `application/ld+json`
- `schema.org`
- `Product`
- `Offer`
- `AggregateRating`
- `Review`
- `BreadcrumbList`
- `Organization`
- `WebSite`
- `Article`
- `BlogPosting`
- `FAQPage`
- `ItemList`
- `seo-product-jsonld`

## Current Structured Data Inventory

| Schema type | Source file | Page type affected | URL examples | Active? | Global or conditional |
|---|---|---|---|---|---|
| `WebSite` | `layout/theme.liquid` | Homepage only | `/` | Yes on index only | Conditional: `request.page_type == 'index'` |
| `Organization` | `layout/theme.liquid` | Homepage only | `/` | Yes on index only | Conditional: `request.page_type == 'index'` |
| `Product` | `snippets/seo-product-jsonld.liquid`, rendered by product sections | Product pages using listed product sections | `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`, `/products/jade-dragon-snow-mountain-private-tour`, `/products/lijiang-to-shangri-la-private-tour`, `/products/yunnan-private-car-charter-tour` | Yes where the product section renders | Conditional by template section usage |
| `Offer` | `snippets/seo-product-jsonld.liquid` | Same product pages | Same product examples | Yes when product has variants and currency | Conditional inside Product JSON-LD |
| `Brand` | `snippets/seo-product-jsonld.liquid` | Same product pages | Same product examples | Yes if `product.vendor` is present | Conditional field |
| Offer seller `Organization` | `snippets/seo-product-jsonld.liquid` | Same product pages | Same product examples | Yes inside each offer | Conditional with offers |
| `BreadcrumbList` | `snippets/seo-product-jsonld.liquid` | Product pages using shared snippet | Same product examples | Yes | Conditional by product section render; collection crumb only if collection context exists |
| `FAQPage` | `sections/product-route-support.liquid` | Product route-support add-on pages | `/products/jade-dragon-snow-mountain-private-tour`, `/products/lijiang-to-shangri-la-private-tour` | Yes when template includes route-support with FAQ blocks | Conditional: `faq_blocks.size > 0` |
| `FAQPage` | `sections/page-route-support.liquid` | Route support pages | `/pages/dali-to-lijiang-private-tour`, likely related route pages | Yes when FAQ blocks exist | Conditional: `faq_blocks.size > 0` |
| `BreadcrumbList` | `sections/page-route-support.liquid` | Route support pages | `/pages/dali-to-lijiang-private-tour` | Yes when `page` exists | Conditional by page context |
| `FAQPage` | `sections/seo-itinerary-page.liquid` | Itinerary pages | `/pages/lijiang-itinerary-3-days`, related itinerary pages | Yes when FAQ blocks exist | Conditional: `faq_blocks.size > 0` |
| `BreadcrumbList` | `sections/seo-itinerary-page.liquid` | Itinerary pages | `/pages/lijiang-itinerary-3-days` | Yes when page template renders | Conditional by template section |
| `FAQPage` | Destination page sections | Destination pages | `/pages/dali`, `/pages/lijiang`, `/pages/kunming`, `/pages/shangri-la`, `/pages/xishuangbanna` | Yes where FAQ blocks/settings exist | Conditional by section logic |
| `BreadcrumbList` | Destination page sections | Destination pages | Same destination examples | Yes where section includes block | Conditional by template section |
| `CollectionPage` | `sections/destinations-page-overview.liquid` | Destinations overview page | `/pages/destinations` | Yes | Conditional by page template |
| `Place` | `sections/destinations-page-overview.liquid` | Destinations overview page | `/pages/destinations` | Yes inside `about` list | Conditional by page template |
| `FAQPage` | `sections/destinations-page-overview.liquid` | Destinations overview page | `/pages/destinations` | Yes | Conditional by page template |
| `BreadcrumbList` | `sections/destinations-page-overview.liquid` | Destinations overview page | `/pages/destinations` | Yes | Conditional by page template |
| `FAQPage` | `sections/all-tours-collection.liquid` | All tours collection | `/collections/yunnan-private-tours` | Yes when FAQ content renders | Conditional inside collection section |
| `BreadcrumbList` | `sections/all-tours-collection.liquid` | All tours collection | `/collections/yunnan-private-tours` | Yes | Conditional inside collection section |
| `FAQPage` | `sections/day-trips-collection.liquid` | Day trips collection | `/collections/yunnan-private-day-trips` | Yes | Conditional inside collection section |
| `BreadcrumbList` | `sections/day-trips-collection.liquid` | Day trips collection | `/collections/yunnan-private-day-trips` | Yes | Conditional inside collection section |
| `FAQPage` / `BreadcrumbList` | Other collection sections found by search | Destination collection pages | `/collections/dali-private-tours`, `/collections/lijiang-private-tours`, `/collections/shangri-la-private-tours`, `/collections/xishuangbanna-private-tours` | Yes where mapped templates use these sections | Conditional by collection template |
| `Article` | `sections/main-article.liquid` | Article pages | `/blogs/travel-guides/jade-dragon-snow-mountain-guide`, `/blogs/travel-guides/lijiang-old-town-guide` | Yes through `templates/article.json` | Conditional by article template |
| Article author/publisher `Organization` | `sections/main-article.liquid` | Article pages | Same article examples | Yes inside Article JSON-LD | Conditional by article template |
| `Product` with `AggregateRating` / `Review` | `sections/product-reviews.liquid` | Product pages if the review section is enabled and has review blocks | Product template dependent | Potential only. Found disabled in `templates/product.lijiang.json`; not active in key product templates inspected | Conditional: `product and review_count > 0` |
| `BlogPosting` | Not found | Blog/article pages | N/A | Missing | N/A |
| `ItemList` | Not found | Collection pages | N/A | Missing | N/A |

## Product JSON-LD Audit

Shared implementation source: `snippets/seo-product-jsonld.liquid`.

Render points:

- `sections/luxury-private-tour-product.liquid`: line 1 renders `seo-product-jsonld`.
- `sections/lijiang-product.liquid`: line 1 renders `seo-product-jsonld`.
- `sections/one-day-trip-product.liquid`: line 1 renders `seo-product-jsonld`.
- `sections/private-charter-service.liquid`: line 1650 renders `seo-product-jsonld`.
- Additional product sections found with the same render pattern: `sections/dali-product.liquid`, `sections/shangri-la-product.liquid`, `sections/xishuangbanna-product.liquid`.

Key product templates:

| Product URL | Template inspected | Main product section | Product JSON-LD status | Additional schema on page |
|---|---|---|---|---|
| `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour` | `templates/product.luxury-private-tour.json` | `luxury-private-tour-product` | Active via snippet | No extra product-route FAQ in this template; `lijiang-product-text-images` has no JSON-LD |
| `/products/jade-dragon-snow-mountain-private-tour` | `templates/product.jade-dragon-snow-mountain-private-tour.json` | `one-day-trip-product` | Active via snippet | `product-route-support` FAQPage active if FAQ blocks present |
| `/products/lijiang-to-shangri-la-private-tour` | `templates/product.lijiang-to-shangri-la-private-tour.json` | `lijiang-product` | Active via snippet | `product-route-support` FAQPage active if FAQ blocks present |
| `/products/yunnan-private-car-charter-tour` | `templates/product.private-charter.json` | `private-charter-service` | Active via snippet | No additional JSON-LD found in inspected template |

Field source audit:

| Field | Current source | Notes |
|---|---|---|
| Product name | `seo_product.title | strip` | Uses Shopify product title. Reliable if product title is maintained. |
| Description | `seo_product.description | strip_html | strip_newlines | replace: '  ', ' ' | strip | truncate: 500` | Product description only. Does not use SEO meta description from `theme.liquid`. Long descriptions are safely truncated. Empty descriptions are omitted. |
| Image | Up to 8 `seo_product.images`, each rendered at width 1600 | Uses all product images, not only featured image. Omitted if no product images. |
| URL | `shop.url | append: seo_product.url` | Canonical-like product URL. Does not use `canonical_url`, but product handle URLs should be stable. |
| Brand | `seo_product.vendor` as `Brand.name` | Omitted if vendor blank. |
| Category | `seo_product.type` | Omitted if product type blank. |
| SKU | Single-variant product only, if selected/first variant SKU exists | Multi-variant product SKUs are attached to each offer when present. |
| Offer source | `seo_product.variants` | Single variant outputs one `Offer`; multiple variants output an array of `Offer` objects. |
| Price source | `variant.price | divided_by: 100.0 | round: 2` | Raw Shopify variant cents. No special quote/custom exclusion in JSON-LD. |
| Currency source | `cart.currency.iso_code | default: shop.currency` | May vary by cart currency if multi-currency is active; otherwise shop currency. |
| Availability source | `variant.available` | Maps to `https://schema.org/InStock` or `https://schema.org/OutOfStock`. |
| Variant handling | `seo_variant_count == 1` single offer, otherwise one offer per variant | All variants are included in multi-variant products. |
| Breadcrumb source | Home, optional current collection, product title | Collection crumb depends on collection context passed into section render. |

Zero-price custom/quote variant handling:

- `snippets/display-variant-price.liquid` has UI logic to label zero-price custom/request/quote/charter variants as quote-style text.
- `snippets/seo-product-jsonld.liquid` does not reuse that quote detection and does not exclude zero-price custom/quote variants.
- Result: any Shopify variant priced at `0` currently emits `"price": 0.0` in Product JSON-LD if the variant is included.
- This is the main Product JSON-LD risk found in this audit.
- Because the task forbids Product JSON-LD, price, variant, offer, and availability changes, this audit recommends validation and planning only for P2-A1.

Risk of misleading offer data:

- Low for normal paid variants whose Shopify prices match the visible booking UI.
- Medium to high for custom/quote variants if any key product contains zero-price variants that are intended as inquiry-only, because structured data may imply a free purchasable offer.
- Medium for private charter products if variant labels or booking UI communicate quote-based pricing while JSON-LD still emits raw variant prices.
- Low for availability if Shopify `variant.available` accurately reflects current sellability.
- Unknown for live product data because this audit used local theme files only and did not inspect Shopify Admin product records.

## Non-Product Schema Audit

| Schema | Current status | Implementation risk | P2 recommendation |
|---|---|---|---|
| `Organization` | Exists globally on homepage only in `layout/theme.liquid`; also nested as seller/publisher/author in Product and Article contexts | Low for audit, medium for broad implementation because Shopify may add app/theme defaults through `content_for_header` | P2-A2 audit first. Implement sitewide only after live duplicate checks. |
| `WebSite` | Exists on homepage only in `layout/theme.liquid`; `destinations-page-overview` also uses `isPartOf` WebSite inside `CollectionPage` | Low for current state | P2-A2 audit first. SearchAction can be considered later, but only if site search behavior is stable. |
| `BreadcrumbList` | Exists on Product pages via shared snippet, on several collection/page sections, and on destination/itinerary/route pages | Medium because multiple section-level implementations may vary in URL source and naming | P2-A3 recommended as audit-first, then unify only with handle-scoped, page-type-safe logic. |
| `Article` | Exists in `sections/main-article.liquid` and is active via `templates/article.json` | Low to medium. Uses full `article.content` as `articleBody`, which can be large. Does not use `BlogPosting` | P2-A4 audit/validation recommended before changing type or fields. |
| `BlogPosting` | Not found | Medium if converting from Article because output may conflict with current validation history | Defer unless validation suggests Article is insufficient. |
| `FAQPage` | Exists on several page, product route, destination, itinerary, and collection sections | Medium because Google FAQ rich result eligibility is limited and FAQ content must match visible content | P2-A5 feasibility check. Avoid broad new FAQPage expansion. |
| `ItemList` | Not found for collection product grids | Medium to high because collection pagination, sort order, hidden products, and variant price display can make list data unstable | P2-A6 feasibility only. Defer implementation unless there is a clear stable list source. |
| `CollectionPage` | Exists on `/pages/destinations` only | Low current risk | No immediate P2 change needed. |

## Duplicate / Conflict Risk

Duplicate Product schema risk:

- Current core Product JSON-LD is centralized in `snippets/seo-product-jsonld.liquid`.
- `sections/product-reviews.liquid` can emit a second `Product` object with `AggregateRating` and `Review` if enabled and review blocks exist.
- The reviewed `templates/product.lijiang.json` includes `product-reviews` but has `"disabled": true`.
- The key product templates inspected do not show an active `product-reviews` section.
- If `product-reviews` is enabled later, it may create duplicate Product entities rather than augmenting the existing Product graph.

Duplicate Article schema risk:

- `sections/main-article.liquid` emits one `Article` JSON-LD block.
- No `BlogPosting` JSON-LD was found.
- Duplicate risk is low in local files, but live Shopify apps or injected `content_for_header` output must be checked before changing article schema.

Duplicate Organization/WebSite risk:

- `layout/theme.liquid` emits homepage-only `WebSite` and `Organization`.
- Product offers include nested seller `Organization`.
- Article schema includes author/publisher `Organization`.
- `destinations-page-overview` includes an embedded `WebSite` in `isPartOf`.
- Live duplicate risk is unknown because Shopify apps can inject structured data through `content_for_header`.

Potential Shopify default conflicts:

- `{{ content_for_header }}` may include app-injected JSON-LD not visible in local Liquid files.
- Product schema fields could conflict with Shopify/app output if apps add Product, Offer, AggregateRating, or Review.
- Homepage Organization/WebSite may conflict with app-level Organization/WebSite.
- Collection BreadcrumbList and page BreadcrumbList are implemented section-by-section, so name or URL formatting can vary.

Fields that may be empty or unreliable:

- Product description can be omitted if `product.description` is blank.
- Product images can be omitted if no product images exist.
- Product brand is omitted if `product.vendor` is blank.
- Product category is omitted if `product.type` is blank.
- SKU is omitted when variant SKU is blank.
- Currency depends on `cart.currency.iso_code`, which may differ from visible display if currency handling changes.
- Offer price can be misleading for zero-price custom/quote variants.
- Product breadcrumb collection crumb can be absent if collection context is blank.
- Article image is omitted if `article.image` is absent.
- Article description is omitted if `article.excerpt` is blank.
- Article body uses stripped full content, which may be long.
- FAQPage content depends on section blocks/settings and should always match visible FAQ text.

## Recommended P2 Implementation Plan

### P2-A1: Product JSON-LD Validation Only

- Goal: Validate current Product JSON-LD output on key product URLs without changing schema code.
- Risk level: Low for audit, high for implementation because product offers touch price/variant logic.
- Likely files: `snippets/seo-product-jsonld.liquid`, product templates, product sections only for reference.
- Must not touch: Product JSON-LD, product schema, price, variant, offer, availability, booking UI, `display-variant-price`, checkout/cart behavior.
- Recommendation: Do now as validation-only. Do not implement changes in P2-A1.

### P2-A2: Organization/WebSite Audit or Implementation

- Goal: Confirm live homepage Organization/WebSite output and check app-injected duplicates.
- Risk level: Low to medium.
- Likely files: `layout/theme.liquid`.
- Must not touch: Product JSON-LD, GA4/GTM, page templates, redirects.
- Recommendation: Audit now. Implement later only if live validation shows no duplicate/conflict.

### P2-A3: BreadcrumbList Audit or Implementation

- Goal: Inventory existing section-level BreadcrumbList output and decide whether any normalization is needed.
- Risk level: Medium.
- Likely files: `snippets/seo-product-jsonld.liquid`, `sections/page-route-support.liquid`, `sections/seo-itinerary-page.liquid`, destination page sections, collection sections.
- Must not touch: Product offer logic, URLs, handles, template names, section names.
- Recommendation: Audit now. Implement only handle-scoped fixes where validation finds errors.

### P2-A4: Article/BlogPosting Audit or Implementation

- Goal: Validate current `Article` output and decide whether `BlogPosting` is beneficial.
- Risk level: Low for validation, medium for changing schema type.
- Likely files: `sections/main-article.liquid`, `templates/article.json`, `templates/blog.json`, `sections/main-blog.liquid`.
- Must not touch: Canonicals, duplicate article noindex logic, blog URLs, article handles.
- Recommendation: Validate now. Defer conversion to `BlogPosting` unless rich result validation or search requirements justify it.

### P2-A5: FAQPage Feasibility Check

- Goal: Confirm current FAQPage blocks match visible FAQ content and are not overused on thin/duplicative pages.
- Risk level: Medium.
- Likely files: collection sections, destination page sections, `sections/product-route-support.liquid`, `sections/page-route-support.liquid`, `sections/seo-itinerary-page.liquid`.
- Must not touch: Product JSON-LD, product pricing, product templates, GA4/GTM.
- Recommendation: Feasibility check now. Avoid broad expansion because FAQ rich result treatment is limited and content must remain visible.

### P2-A6: Collection ItemList Feasibility Check

- Goal: Decide whether collection grids have stable enough data for `ItemList`.
- Risk level: Medium to high.
- Likely files: `sections/all-tours-collection.liquid`, `sections/day-trips-collection.liquid`, `sections/luxury-private-tour-collection.liquid`, destination collection sections.
- Must not touch: Collection handles, pagination behavior, product card pricing, product card URLs, JSON templates.
- Recommendation: Feasibility only. Not recommended for immediate implementation until pagination, sorting, and product availability behavior are validated.

## Manual Validation Checklist

Use these tools:

- Google Rich Results Test
- Schema Markup Validator

Sample URLs to test:

- `/`
- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `/products/jade-dragon-snow-mountain-private-tour`
- `/products/lijiang-to-shangri-la-private-tour`
- `/products/yunnan-private-car-charter-tour`
- `/collections/yunnan-private-tours`
- `/collections/yunnan-private-day-trips`
- `/collections/yunnan-luxury-private-tours`
- `/pages/destinations`
- `/pages/dali`
- `/pages/lijiang`
- `/pages/lijiang-itinerary-3-days`
- `/pages/dali-to-lijiang-private-tour`
- `/blogs/travel-guides/jade-dragon-snow-mountain-guide`

Expected warnings that may be acceptable:

- Product missing `aggregateRating` or `review` when no verified reviews are intentionally included.
- Product missing `sku` when Shopify variants do not have SKUs.
- Product missing `brand` if product vendor is intentionally blank.
- Article missing image only if the article intentionally has no featured image.
- FAQPage may not be eligible for rich display even when valid.
- Organization logo missing if theme settings logo is blank.

Errors that must block implementation:

- Invalid JSON-LD syntax.
- Duplicate conflicting Product entities on the same product page.
- Product offers with visibly misleading `price`, especially `0` for custom/quote variants.
- Offer currency mismatch against visible booking currency.
- Availability mismatch against actual sellability.
- Breadcrumb URLs that do not match canonical URL patterns.
- FAQPage questions/answers that are not visible on the page.
- Article canonical or `mainEntityOfPage` mismatch, especially for known duplicate article variants.
- App-injected schema conflicts with theme schema.

## Exact Files Changed

- `docs/seo-audit/2026-05-implementation/P2-0-structured-data-audit.md`

No code files were changed.

## Rollback Risk

Rollback risk is low. This is a documentation-only addition. Removing this file reverts the audit with no theme behavior impact.
