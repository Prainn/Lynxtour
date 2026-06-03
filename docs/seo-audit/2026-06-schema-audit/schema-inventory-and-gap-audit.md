# LynxTour Schema Inventory and Gap Audit

Audit date: 2026-06-03

Scope: local Shopify theme files under `layout/`, `templates/`, `sections/`, `snippets/`, `config/`, `locales/`, and `docs/` where relevant. The workspace does not contain an `assets/` directory, so no asset-level schema code was available to audit. This was an audit-only pass; no Liquid, JSON template, CSS, JavaScript, config, locale, or production theme files were changed.

## 1. Executive Summary

Current structured data is mostly JSON-LD. No microdata (`itemscope`, `itemtype`, `itemprop`) was found in the audited theme paths.

The theme currently has:

- Homepage-only `WebSite` and `Organization` JSON-LD in `layout/theme.liquid`.
- Product `Product`, `Offer`, nested seller `Organization`, optional `Brand`, and product `BreadcrumbList` JSON-LD in `snippets/seo-product-jsonld.liquid`, rendered by product sections.
- Article `Article` JSON-LD in `sections/main-article.liquid`.
- FAQPage and BreadcrumbList JSON-LD in many collection, destination, route-support, and itinerary sections.
- A destinations overview `CollectionPage` with embedded `Place` entries, plus FAQPage and BreadcrumbList, in `sections/destinations-page-overview.liquid`.
- A possible second Product schema with `AggregateRating` and `Review` in `sections/product-reviews.liquid` if that section is enabled and has review blocks.

Schema that appears basically correct:

- Product JSON-LD is centralized and uses safe Liquid `json` output for product name, description, images, URLs, SKU, and variant offers.
- Product prices and availability use Shopify variant data, which is appropriate for normal bookable variants.
- Visible FAQ blocks generally match emitted FAQPage JSON-LD because the same section settings or hardcoded visible FAQ content are used.
- Article JSON-LD uses live article fields for headline, content, dates, image, author, and publisher.
- BreadcrumbList is present on product pages and many important collection/page templates.

Risky or incomplete areas:

- `Organization` and `WebSite` schema only appear on the homepage and do not use stable `@id` values. Nested seller/publisher organizations are not connected to one canonical organization entity.
- Product `Offer` schema can emit `"price": 0.0` for zero-price custom, quote, request, or charter variants because the Product JSON-LD does not reuse the quote-style display logic in `snippets/display-variant-price.liquid`.
- `sections/product-reviews.liquid` can create a duplicate Product entity with reviews/aggregate rating if enabled, instead of attaching reviews to the existing Product `@id`.
- Destination pages do not currently use `TouristDestination` schema.
- Tour product pages do not currently use `TouristTrip` or itinerary `ItemList` schema.
- Collection pages do not currently use stable `ItemList` schema for visible product lists.
- Article schema uses `Article`, not `BlogPosting`, and publisher/author do not reference a stable organization `@id`.
- Live Shopify/app-injected schema remains unknown because `{{ content_for_header }}` can add structured data that is not visible in local theme files.

Biggest missing GEO + SEO opportunities:

- Define one global LynxTour entity as `TravelAgency` or `Organization` with a stable `@id` and reuse it across homepage, products, articles, destinations, and seller/publisher references.
- Add a stable `WebSite` entity with `@id` and optional `SearchAction` only if site search behavior is stable.
- Add `TouristDestination` schema to Kunming, Dali, Lijiang, Shangri-La, and Xishuangbanna pages.
- Add `TouristTrip` to key tour products, connected to destinations and provider.
- Add itinerary `ItemList` only where day-by-day itinerary content is visible and stable.
- Standardize BreadcrumbList output so page, collection, article, and product breadcrumbs use consistent URL sources and `@id` patterns.

## 2. Schema Inventory Table

| Schema Type | File Path | Template/Page Type Affected | Dynamic or Hardcoded | Status | Notes |
|---|---|---|---|---|---|
| `WebSite` | `layout/theme.liquid` | Homepage only (`request.page_type == 'index'`) | Mostly hardcoded with `shop.secure_url` | Active, incomplete | Missing stable `@id`; only appears on homepage; no `SearchAction`. |
| `Organization` | `layout/theme.liquid` | Homepage only | Mostly hardcoded with optional settings logo | Active, incomplete | Should likely become stable sitewide `TravelAgency` or `Organization`; missing `@id`, contact, sameAs, service area. |
| `Product` | `snippets/seo-product-jsonld.liquid` | Product pages using product sections | Dynamic | Active, mostly valid | Uses product title, description, images, vendor, type, SKU, variants. Good central implementation. |
| `Offer` | `snippets/seo-product-jsonld.liquid` | Product pages | Dynamic | Active, risk on quote variants | Emits all variant prices, including possible zero-price custom/quote variants. |
| `Brand` | `snippets/seo-product-jsonld.liquid` | Product pages | Dynamic | Active when vendor exists | Uses `product.vendor`; acceptable if vendor is maintained. |
| Seller `Organization` | `snippets/seo-product-jsonld.liquid` | Product Offer objects | Dynamic name only | Active, incomplete | Nested seller has no `@id`; does not connect to homepage organization. |
| `BreadcrumbList` | `snippets/seo-product-jsonld.liquid` | Product pages | Dynamic | Active | Product crumb includes collection only when collection context exists; otherwise Home > Product. |
| `FAQPage` | `sections/product-route-support.liquid` | Product route-support add-ons, including Jade Dragon and Lijiang to Shangri-La templates when section has FAQ blocks | Dynamic from blocks | Active where section enabled | Matches visible FAQ blocks. FAQ rich result value is limited, but valid if visible. |
| `FAQPage` | `sections/page-route-support.liquid` | Route pages such as `/pages/dali-to-lijiang-private-tour` | Dynamic from blocks | Active where section has FAQ blocks | Matches visible FAQ blocks. |
| `BreadcrumbList` | `sections/page-route-support.liquid` | Route pages | Dynamic | Active | Two-step Home > Page breadcrumb. |
| `FAQPage` | `sections/seo-itinerary-page.liquid` | Itinerary pages such as Dali/Lijiang 2-day and 3-day pages | Dynamic from blocks | Active where section has FAQ blocks | Good content match, but no itinerary `ItemList`. |
| `BreadcrumbList` | `sections/seo-itinerary-page.liquid` | Itinerary pages | Dynamic | Active | Two-step Home > Page breadcrumb. |
| `FAQPage` | `sections/kunming-page.liquid`, `sections/dali-page.liquid`, `sections/lijiang-page.liquid`, `sections/shangri-la-page.liquid`, `sections/xishuangbanna-page.liquid` | Destination pages | Dynamic from FAQ blocks | Active where blocks exist | Matches visible FAQ content. |
| `BreadcrumbList` | Same destination page sections | Destination pages | Dynamic | Active | Two-step Home > Page breadcrumb. |
| `FAQPage` | `sections/all-tours-collection.liquid` | `/collections/yunnan-private-tours` | Hardcoded visible FAQ content | Active | Matches the visible collection FAQ section. |
| `BreadcrumbList` | `sections/all-tours-collection.liquid` | `/collections/yunnan-private-tours` | Dynamic collection fields | Active | Uses Home > collection title. |
| `FAQPage` | `sections/day-trips-collection.liquid` | `/collections/yunnan-private-day-trips` | Hardcoded visible FAQ content | Active | Matches visible FAQ content. |
| `BreadcrumbList` | `sections/day-trips-collection.liquid` | `/collections/yunnan-private-day-trips` | Dynamic collection fields | Active | Uses Home > collection title. |
| `FAQPage` | `sections/luxury-private-tour-collection.liquid` | `/collections/yunnan-luxury-private-tours` if mapped template renders this section | Hardcoded/section-level | Not directly confirmed in the line search output | Needs local line validation before implementation because this section was not returned in the targeted JSON-LD line search. |
| `FAQPage` | `sections/dali-collection.liquid`, `sections/lijiang-collection.liquid`, `sections/shangri-la-collection.liquid`, `sections/xishuangbanna-collection.liquid` | Destination collection templates | Hardcoded visible FAQ content | Active | Useful for destination collection SEO, but not part of the requested URL list except as related coverage. |
| `BreadcrumbList` | Same destination collection sections | Destination collection templates | Dynamic collection fields | Active | Uses Home > collection title. |
| `CollectionPage` | `sections/destinations-page-overview.liquid` | `/pages/destinations` | Mixed dynamic/hardcoded | Active | Uses `CollectionPage`, `isPartOf` WebSite, and `about` Place list. |
| `Place` | `sections/destinations-page-overview.liquid` | `/pages/destinations` | Hardcoded | Active inside `about` | Names Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna. Could be upgraded with linked TouristDestination pages. |
| `FAQPage` | `sections/destinations-page-overview.liquid` | `/pages/destinations` | Hardcoded visible FAQ content | Active | Visible content includes some encoded apostrophe artifacts in local output display; validate rendered source. |
| `BreadcrumbList` | `sections/destinations-page-overview.liquid` | `/pages/destinations` | Hardcoded/dynamic URL | Active | Home > Destinations. |
| `Article` | `sections/main-article.liquid` | Blog articles via `templates/article.json` | Dynamic | Active, acceptable | Could become `BlogPosting`; includes full article body, dates, author, publisher. Missing stable publisher `@id`. |
| Author/Publisher `Organization` | `sections/main-article.liquid` | Blog articles | Dynamic name/URL | Active, incomplete | Publisher has no logo or `@id`; author is `Organization`, with editorial fallback for author `lynx`. |
| `Product` with `AggregateRating` and `Review` | `sections/product-reviews.liquid` | Product pages if enabled and review blocks exist | Dynamic from section blocks | Potential duplicate risk | Can create a second Product schema without `@id`; should not be enabled until review data is verified and attached to the main Product entity. |
| App/Shopify injected schema | `layout/theme.liquid` via `{{ content_for_header }}` | Any page | Unknown | Unknown live risk | Must be checked in rendered source and validators before changing global/Product/Article schema. |
| Microdata | Audited paths | N/A | N/A | Not found | No `itemscope`, `itemtype`, or `itemprop` found. |
| `TouristDestination` | Not found | Destination pages | N/A | Missing | Important GEO opportunity. |
| `TouristTrip` | Not found | Tour product pages | N/A | Missing | Important tour-specific semantic opportunity. |
| `ItemList` | Not found | Collections and itinerary pages | N/A | Missing | Useful only if tied to stable visible lists/day-by-day content. |
| `LocalBusiness` / `TravelAgency` | Not found as top-level schema | Global/site entity | N/A | Missing | `TravelAgency` is a strong fit if LynxTour wants a travel-provider entity rather than generic Organization. |
| `BlogPosting` | Not found | Blog articles | N/A | Missing or optional | Existing `Article` is valid; `BlogPosting` may be more specific for travel guide posts. |

## 3. Page-Type Coverage Matrix

| Page Type | Existing Schema | Missing Schema | Quality | Priority | Recommended Action |
|---|---|---|---|---|---|
| Homepage | `WebSite`, `Organization` in `layout/theme.liquid` | Stable `@id`, richer `TravelAgency`, sameAs/contact/service area, connected WebPage | Valid but thin and homepage-only | P1 | Convert to one stable global entity graph after live duplicate check. |
| Collection pages | FAQPage and BreadcrumbList on `/collections/yunnan-private-tours` and `/collections/yunnan-private-day-trips`; likely similar page-level support on destination collections | `CollectionPage` or `WebPage`, stable `ItemList` of visible products, organization linkage | FAQ/breadcrumb generally valid; no product-list semantics | P2 | Keep FAQ only where visible; consider stable ItemList for collection grids after pagination/sort review. |
| Product pages | Product, Offer, Brand, seller Organization, BreadcrumbList from shared snippet; route-support FAQ on selected products | `TouristTrip`, connected provider/destination, safer quote-price handling, consistent Product `@id` references, optional itinerary ItemList | Good central Product foundation; quote-price risk | P0 for zero-price offers, P1 for TouristTrip | First fix misleading offers and duplicate risks; then add tour-specific schema by handle/template. |
| Destination pages | FAQPage and BreadcrumbList | `TouristDestination`, WebPage, links to related tours/articles, connection to LynxTour service area | Valid FAQ/breadcrumb, missing destination semantics | P1 | Add handle-scoped TouristDestination for Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna. |
| Itinerary pages | FAQPage and BreadcrumbList via `seo-itinerary-page` or `page-route-support` | `ItemList` day itinerary, WebPage, possible TouristTrip planning entity | Valid but thin for itinerary structure | P1/P2 | Add ItemList only from visible day blocks/settings; avoid inventing hidden itinerary data. |
| Blog articles | `Article` with author/publisher and mainEntityOfPage | `BlogPosting`, stable publisher `@id`, publisher logo, article breadcrumbs, about/mentions destinations and tours | Valid but not strongly connected to site entity graph | P2 | Upgrade to BlogPosting or Article+BlogPosting only after validator check; link publisher to global entity. |
| Bespoke/custom travel page | No schema found in `sections/bespoke-travel.liquid` search output | WebPage, Service or OfferCatalog-style custom travel service, BreadcrumbList, FAQPage only if visible FAQ exists | Missing schema on important lead page | P1 | Add WebPage/Service schema connected to TravelAgency, without fake price/offer claims. |

Target URL notes:

| Requested URL Group | Local Schema Assessment | Priority Notes |
|---|---|---|
| `/` | Homepage gets `WebSite` and `Organization` from `layout/theme.liquid`. | P1: make this a stable global entity graph rather than homepage-only thin schema. |
| `/collections/yunnan-private-tours` | `sections/all-tours-collection.liquid` emits FAQPage and BreadcrumbList. | P2: consider CollectionPage/ItemList after pagination and visible product order review. |
| `/collections/yunnan-private-day-trips` | `sections/day-trips-collection.liquid` emits FAQPage and BreadcrumbList. | P2: same as above. |
| `/collections/yunnan-luxury-private-tours` | `templates/collection.luxury-private-tour.json` maps to `sections/luxury-private-tour-collection.liquid`, but targeted JSON-LD search did not find schema in that section. | P1/P2: add at least BreadcrumbList, then evaluate CollectionPage/ItemList. |
| Listed multi-day products: 8-day, 10-day, and 6-day Yunnan tours | Product section family renders `snippets/seo-product-jsonld.liquid`, so Product, Offer, and BreadcrumbList should be present where the assigned product template uses these sections. `sections/lijiang-product-text-images.liquid` has handle-scoped support content but no JSON-LD. | P0: validate no zero-price offers. P1: add TouristTrip and itinerary structure where visible. Confirm live Shopify template assignment for each handle. |
| Listed day/route products: Jade Dragon, Lijiang to Shangri-La, Pudacuo/Songzanlin | Product JSON-LD is active through product sections. Jade Dragon and Lijiang to Shangri-La also use `sections/product-route-support.liquid`, which can emit FAQPage. | P1: add TouristTrip and destination links. Keep FAQ only where visible. |
| `/products/yunnan-private-car-charter-tour` | `sections/private-charter-service.liquid` renders Product JSON-LD via the shared snippet. | P0: highest quote/zero-price Offer risk. Consider Service or car-charter-specific schema without fake prices. |
| Destination pages: Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna | Destination section files emit FAQPage and BreadcrumbList when FAQ blocks exist. | P1: add TouristDestination and connect each to relevant tours/articles. |
| Itinerary and route pages: Dali/Lijiang 2-day and 3-day, Dali to Lijiang, Tiger Leaping Gorge from Lijiang | `sections/seo-itinerary-page.liquid` and `sections/page-route-support.liquid` emit FAQPage and BreadcrumbList. | P1/P2: add ItemList from visible day/route blocks; avoid hidden invented itinerary data. |
| Blog articles: Dianchi, Stone Forest, Lijiang Old Town, Jade Dragon Snow Mountain, Lijiang travel guide | `sections/main-article.liquid` emits Article JSON-LD for article templates and has handle-scoped canonical/CTA logic for several listed articles. | P2: add article breadcrumbs, stable publisher `@id`, and destination `about`/`mentions`. |
| `/pages/bespoke-custom-travel` | No JSON-LD found in `sections/bespoke-travel.liquid`. | P1: add WebPage plus conservative custom travel Service schema and BreadcrumbList. |

## 4. Detected Problems

### Invalid or risky schema

Issue: zero-price or quote-style Product offers can emit as real zero-price Offers.

- File path: `snippets/seo-product-jsonld.liquid`
- Why it matters: If custom, inquiry, quote, request, or charter variants have Shopify price `0`, the current JSON-LD emits `"price": 0.0`. This can be misleading and may look like a free purchasable tour.
- Suggested fix: Reuse or mirror the quote-variant detection from `snippets/display-variant-price.liquid`. For quote-only variants, either omit Offer price, avoid emitting that Offer, or use a schema pattern that does not imply a zero-price purchasable product.
- Priority: P0

Issue: potential duplicate Product schema with reviews.

- File path: `sections/product-reviews.liquid`
- Why it matters: When enabled with review blocks, it emits a second top-level `Product` object without the main Product `@id`. That can conflict with `snippets/seo-product-jsonld.liquid`.
- Suggested fix: Do not enable until reviews are verified. If used later, attach `aggregateRating` and `review` to the same Product `@id` or output a graph node with matching `@id`.
- Priority: P0/P1 depending on whether the section is enabled live

Issue: live app-injected schema is unknown.

- File path: `layout/theme.liquid` through `{{ content_for_header }}`
- Why it matters: Shopify apps can add Product, Organization, WebSite, BreadcrumbList, Review, or Article schema in rendered pages, causing duplicates not visible locally.
- Suggested fix: Before implementation, inspect rendered source and validators on representative live/preview URLs.
- Priority: P1

### Duplicate schema

Issue: Product duplication risk from `product-reviews`.

- File path: `sections/product-reviews.liquid`
- Why it matters: A second Product entity can split reviews/ratings from the canonical product entity or create validator warnings.
- Suggested fix: Consolidate review fields into the existing Product graph using `@id`.
- Priority: P0/P1

Issue: Organization fragments are repeated without `@id`.

- File paths: `layout/theme.liquid`, `snippets/seo-product-jsonld.liquid`, `sections/main-article.liquid`, `sections/destinations-page-overview.liquid`
- Why it matters: Search and AI systems have to infer whether homepage Organization, offer seller, article publisher, and WebSite owner are the same entity.
- Suggested fix: Define one stable entity such as `{{ shop.url }}/#organization` or `{{ shop.url }}/#travelagency` and reference it from seller/publisher/provider fields.
- Priority: P1

### Missing @id consistency

Issue: WebSite and Organization lack stable identifiers.

- File path: `layout/theme.liquid`
- Why it matters: GEO readiness depends on a clear entity graph. Without stable `@id` values, Product, Article, Destination, and Service schema cannot reliably point back to LynxTour.
- Suggested fix: Add `@id` to WebSite and TravelAgency/Organization and reuse them globally.
- Priority: P1

Issue: Article publisher/author do not reference the global organization.

- File path: `sections/main-article.liquid`
- Why it matters: Editorial authority is weaker when publisher is a standalone object instead of a stable site entity.
- Suggested fix: Use `"publisher": { "@id": "{{ shop.url }}/#organization" }` or equivalent after the global entity exists.
- Priority: P2

### Missing breadcrumbs

Issue: Blog articles do not appear to emit BreadcrumbList locally.

- File path: `sections/main-article.liquid`
- Why it matters: Blog guide pages are important discovery content, and breadcrumbs help define site hierarchy such as Home > Travel Guides > Article.
- Suggested fix: Add Article BreadcrumbList after checking no app/theme breadcrumb is injected live.
- Priority: P2

Issue: Bespoke/custom travel page lacks breadcrumb schema.

- File path: `sections/bespoke-travel.liquid`
- Why it matters: This is an important commercial lead page and should be connected into the site hierarchy.
- Suggested fix: Add a two-step BreadcrumbList or shared page breadcrumb snippet.
- Priority: P1

### Product / Offer issues

Issue: Offers are product/variant-commerce oriented, not tour-service oriented.

- File path: `snippets/seo-product-jsonld.liquid`
- Why it matters: Shopify Product schema is useful for rich results, but it does not fully explain that these are private Yunnan tours, day trips, car charters, or custom travel services.
- Suggested fix: Preserve valid Product schema for product rich-result eligibility, then add `TouristTrip` or `Service` nodes connected through `subjectOf`, `isRelatedTo`, or a graph relationship where appropriate.
- Priority: P1

Issue: Product seller is a nested Organization with only name.

- File path: `snippets/seo-product-jsonld.liquid`
- Why it matters: Seller identity is weaker and not connected to LynxTour as a Yunnan private tour provider.
- Suggested fix: Reference global TravelAgency/Organization `@id` from offers.
- Priority: P1

Issue: Product breadcrumbs may omit collection context when product is accessed directly.

- File path: `snippets/seo-product-jsonld.liquid`
- Why it matters: Direct product pages may output Home > Product instead of Home > relevant collection > Product, reducing hierarchy clarity.
- Suggested fix: Consider handle/template-scoped fallback collection mapping for key tour products, without changing URLs or handles.
- Priority: P2

### Article / BlogPosting issues

Issue: Articles use `Article`, not `BlogPosting`.

- File path: `sections/main-article.liquid`
- Why it matters: `Article` is valid, but `BlogPosting` is more specific for travel guide blog posts.
- Suggested fix: Validate whether changing `@type` to `BlogPosting` improves clarity without conflicts. Keep Article if validators and search performance are already healthy.
- Priority: P3

Issue: Article schema uses full `article.content` as `articleBody`.

- File path: `sections/main-article.liquid`
- Why it matters: This can produce large JSON-LD payloads and include navigation-like or embedded content after Liquid rendering.
- Suggested fix: Consider omitting `articleBody` or using a cleaned, truncated summary if validators show payload concerns.
- Priority: P3

Issue: Article publisher lacks logo and stable `@id`.

- File path: `sections/main-article.liquid`
- Why it matters: Publisher identity is less complete than recommended article schema.
- Suggested fix: Reference global organization with logo once that entity is standardized.
- Priority: P2

### Destination page issues

Issue: destination pages are missing `TouristDestination`.

- File paths: `sections/kunming-page.liquid`, `sections/dali-page.liquid`, `sections/lijiang-page.liquid`, `sections/shangri-la-page.liquid`, `sections/xishuangbanna-page.liquid`
- Why it matters: AI/search systems need to understand that these are destination guides for Yunnan places LynxTour serves, not just generic pages with FAQs.
- Suggested fix: Add handle-scoped `TouristDestination` nodes with `name`, `url`, `description`, `containedInPlace` or `addressRegion`, `touristType` where visible/reasonable, and links to related tours/articles.
- Priority: P1

Issue: destination overview uses generic `Place` nodes rather than linked destination entities.

- File path: `sections/destinations-page-overview.liquid`
- Why it matters: Place names are useful but not strongly connected to destination pages or LynxTour services.
- Suggested fix: Upgrade `about` entries to reference destination page `@id` values after those pages have stable TouristDestination schema.
- Priority: P2

### Tour itinerary schema issues

Issue: tour product pages are missing `TouristTrip`.

- File paths: product sections rendering `snippets/seo-product-jsonld.liquid`, especially `sections/luxury-private-tour-product.liquid`, `sections/lijiang-product.liquid`, `sections/one-day-trip-product.liquid`, `sections/private-charter-service.liquid`
- Why it matters: Product schema describes the Shopify product, but not the travel route, destinations, provider, duration, or private/custom tour nature.
- Suggested fix: Add `TouristTrip` for key route products using visible product title, description, duration, destinations, and provider. Keep it conservative and handle-scoped.
- Priority: P1

Issue: itinerary pages are missing `ItemList`.

- File paths: `sections/seo-itinerary-page.liquid`, `sections/page-route-support.liquid`
- Why it matters: Day-by-day itinerary content is visible and valuable for AI understanding, but the current schema only covers FAQ and breadcrumbs.
- Suggested fix: Emit `ItemList` from visible day blocks/settings where available, not from hidden or invented itinerary data.
- Priority: P2

### FAQ schema issues

Issue: FAQPage schema is widely used.

- File paths: collection sections, destination sections, `sections/seo-itinerary-page.liquid`, `sections/page-route-support.liquid`, `sections/product-route-support.liquid`, `sections/destinations-page-overview.liquid`
- Why it matters: FAQ rich results are limited in Google, and too much FAQ schema can add maintenance burden. However, it is acceptable if the FAQ content is visible and accurate.
- Suggested fix: Keep existing FAQPage only where it exactly matches visible FAQ content. Avoid expanding FAQPage as the main GEO strategy.
- Priority: P2

Issue: hardcoded FAQ strings must be kept synchronized with visible hardcoded FAQ text.

- File paths: `sections/all-tours-collection.liquid`, `sections/day-trips-collection.liquid`, destination collection sections, `sections/destinations-page-overview.liquid`
- Why it matters: If visible FAQ copy changes but JSON-LD copy does not, schema can become inaccurate.
- Suggested fix: Prefer generating FAQPage from the same block/settings source where possible.
- Priority: P2

### Organization / TravelAgency issues

Issue: no top-level `TravelAgency` schema found.

- File path: not currently implemented
- Why it matters: LynxTour is an inbound Yunnan private/custom tour agency. `TravelAgency` communicates the business category more clearly than a generic Organization.
- Suggested fix: Add a global `TravelAgency` or Organization with `@type: ["Organization", "TravelAgency"]` if validator-compatible, or choose `TravelAgency` as the top-level entity. Include service area and links to destinations/tour categories only when truthful and visible.
- Priority: P1

Issue: no stable entity links across organization, website, products, articles, destinations, and itineraries.

- File paths: global and page-level schema files listed above
- Why it matters: GEO readiness depends on connected facts: LynxTour provides private/custom tours in Yunnan; pages cover Kunming, Dali, Lijiang, Shangri-La, Xishuangbanna; product pages are tours; articles support planning.
- Suggested fix: Build a graph with stable `@id` values for `#organization`, `#website`, page `#webpage`, product `#product`, breadcrumb `#breadcrumb`, and destination/trip nodes.
- Priority: P1

## 5. Recommended Target Schema Architecture

Use conservative, connected JSON-LD graphs. Do not redesign templates or change URLs, handles, section names, or Shopify schema names.

Global schema:

- `TravelAgency` or `Organization` on all indexable pages, with one stable `@id`, for example `https://lynxtour.com/#organization` or the live shop URL equivalent.
- `WebSite` with stable `@id`, connected to the organization through `publisher`.
- Optional `SearchAction` only if storefront search is stable and intentionally indexable.

Homepage:

- `WebPage` for the homepage, connected to `WebSite` and `TravelAgency`.
- Keep `WebSite` and organization entity, but move toward stable `@id` references.

Product pages:

- Keep Shopify-compatible `Product` schema for rich result eligibility.
- Keep `Offer` only for real purchasable paid variants with accurate price, currency, URL, and availability.
- Avoid fake zero-price offers for custom quote products or inquiry-only variants.
- Add `TouristTrip` for true tour products, connected to the Product and provider organization.
- Use `touristType` or descriptive properties carefully for private tours, custom tours, day trips, family travel, Muslim-friendly travel, and car charter only when the page visibly supports those claims.
- Add itinerary `ItemList` only where a visible day-by-day itinerary exists.

Collection pages:

- Keep BreadcrumbList.
- Keep FAQPage where visible FAQ content exists and remains synchronized.
- Consider `CollectionPage` or `WebPage` for major collection landing pages.
- Consider `ItemList` for visible product grids only after deciding stable sort/pagination rules.

Destination pages:

- Add `TouristDestination` for Kunming, Dali, Lijiang, Shangri-La, and Xishuangbanna.
- Connect each destination to visible related tours and guides through `subjectOf`, `mainEntityOfPage`, `about`, or `mentions` where appropriate.
- Keep FAQPage and BreadcrumbList.

Itinerary pages:

- Keep BreadcrumbList.
- Keep FAQPage only if visible.
- Add `ItemList` for visible day-by-day route content.
- Consider `WebPage` with `about` destination references.

Blog articles:

- Keep `Article` or switch to `BlogPosting` after validation.
- Add stable publisher `@id` and publisher logo through the global organization.
- Add `about` or `mentions` for destinations and relevant tour types where visible in the article content.
- Add BreadcrumbList if no live injected breadcrumb exists.

Bespoke/custom travel page:

- Add `WebPage` plus a conservative `Service` or `TravelAgency` service description for custom private Yunnan travel planning.
- Do not add fake price, aggregateRating, or Offer unless visible and verifiable.
- Add BreadcrumbList.

## 6. Implementation Plan

Do not implement yet. Suggested next steps:

Phase 1: fix invalid / duplicate / risky schema.

- Validate live source for app-injected schema on representative homepage, product, collection, page, and article URLs.
- Fix zero-price quote/custom Product Offer emission.
- Keep `sections/product-reviews.liquid` disabled or refactor it to reuse the main Product `@id` before enabling.

Phase 2: add missing global entity schema.

- Create one stable `TravelAgency` or Organization entity with `@id`.
- Create one stable `WebSite` entity with `@id`.
- Reference the global organization from product seller, article publisher, trip provider, and service provider fields.

Phase 3: add breadcrumbs.

- Standardize BreadcrumbList generation across product, collection, page, itinerary, bespoke, and article templates.
- Add article and bespoke breadcrumbs if live output does not already include them.
- Keep URL sources consistent: canonical page URL for current item, stable shop URL for Home.

Phase 4: improve product tour schema.

- Preserve existing Product schema and booking UI.
- Add handle-scoped `TouristTrip` for the key tour products listed in this audit.
- Add route/destination references only when the page visibly supports them.
- Add itinerary ItemList only for products with visible day-by-day itinerary metafields/content.

Phase 5: improve destination and itinerary page schema.

- Add TouristDestination schema to Kunming, Dali, Lijiang, Shangri-La, and Xishuangbanna pages.
- Add ItemList to Dali/Lijiang itinerary pages and route-support pages where visible day blocks exist.
- Connect destination pages to relevant collection/product/article URLs conservatively.

Phase 6: improve article schema.

- Add stable publisher `@id`.
- Consider `BlogPosting` after validation.
- Add article breadcrumbs.
- Add `about`/`mentions` for major destinations and guide topics only where visible in article content.

## 7. Files Likely To Change Later

Likely future implementation files:

- `layout/theme.liquid`
- `snippets/seo-product-jsonld.liquid`
- `snippets/display-variant-price.liquid` for reference only, if quote detection is reused or mirrored
- Possible new shared snippet such as `snippets/seo-global-jsonld.liquid`
- Possible new shared snippet such as `snippets/seo-breadcrumb-jsonld.liquid`
- `sections/main-article.liquid`
- `sections/product-reviews.liquid`
- `sections/product-route-support.liquid`
- `sections/page-route-support.liquid`
- `sections/seo-itinerary-page.liquid`
- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`
- `sections/bespoke-travel.liquid`
- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `sections/dali-collection.liquid`
- `sections/lijiang-collection.liquid`
- `sections/shangri-la-collection.liquid`
- `sections/xishuangbanna-collection.liquid`
- `sections/destinations-page-overview.liquid`
- Product templates only if needed to pass handle/template context, but avoid changing template names or handles.
- Page templates only if needed to include a shared schema section/snippet, but avoid changing template names or handles.

## 8. Validation Checklist

- Shopify local preview check: verify representative homepage, collection, product, destination, itinerary, bespoke, and article pages render normally.
- View source check: inspect rendered HTML for each target URL and confirm JSON-LD blocks are present only once where expected.
- Schema.org validator check: validate rendered source or deployed URLs and record errors/warnings.
- Google Rich Results Test check: validate product pages, article pages, and collection/page examples for eligible rich result types and duplicate conflicts.
- GSC URL Inspection after deployment: inspect changed representative URLs after Google can crawl the deployment.
- Confirm schema matches visible content: product price, availability, destination claims, FAQ questions/answers, article dates, itinerary days, and custom travel service claims must match what users can see.
- Confirm no fake zero-price offers: quote/custom/inquiry variants must not appear as free purchasable offers.
- Confirm no duplicate Product schema: review/aggregateRating must attach to the same Product `@id`.
- Confirm stable entity graph: Organization/TravelAgency, WebSite, WebPage, Product, TouristTrip, TouristDestination, BlogPosting/Article, and BreadcrumbList should use consistent `@id` references.
