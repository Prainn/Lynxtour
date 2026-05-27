# P2-B Canonical / OG / Twitter / Robots SEO Audit

Date: 2026-05-27
Branch: `feat/seo-meta-canonical-audit-p2`
Scope: audit-only, documentation-only.

## Guardrails

- No Liquid behavior changed.
- No JSON templates changed.
- No CSS changed.
- No snippets changed.
- No structured data or JSON-LD changed.
- No Product JSON-LD changed.
- No GA4/GTM tracking changed.
- No redirects created.
- No canonical logic changed.
- No robots/noindex logic changed.
- No MCP tools used.
- Local repository files only.

## Exact Files Inspected

Primary SEO head file:
- `layout/theme.liquid`

Snippets searched for SEO, meta, OG, Twitter, canonical, robots, social sharing, and related terms:
- `snippets/seo-product-jsonld.liquid`
- `snippets/ga4-custom-events.liquid`
- `snippets/display-variant-price.liquid`

Article and blog templates:
- `templates/article.json`
- `templates/blog.json`
- `templates/blog.day-trips.json`

Collection templates:
- `templates/collection.all-tuors-collection.json`
- `templates/collection.day-trips-collection.json`
- `templates/collection.luxury-private-tour.json`
- `templates/collection.dali-collection.json`
- `templates/collection.lijiang-collection.json`
- `templates/collection.shangri-la-collection.json`
- `templates/collection.xishuangbanna-collection.json`
- `templates/collection.json`

Product templates:
- `templates/product.luxury-private-tour.json`
- `templates/product.jade-dragon-snow-mountain-private-tour.json`
- `templates/product.lijiang-to-shangri-la-private-tour.json`
- `templates/product.private-charter.json`
- `templates/product.lijiang.json`
- `templates/product.json`
- `templates/product.one-day-trip.json`
- `templates/product.dali.json`
- `templates/product.shangri-la.json`
- `templates/product.xishuangbanna.json`

Page templates for destination, itinerary, bespoke, and route-support pages:
- `templates/page.bespoke-travel.json`
- `templates/page.destinations.json`
- `templates/page.kunming.json`
- `templates/page.dali.json`
- `templates/page.lijiang.json`
- `templates/page.shangri-la.json`
- `templates/page.xishuangbanna.json`
- `templates/page.dali-itinerary-2-days.json`
- `templates/page.dali-itinerary-3-days.json`
- `templates/page.lijiang-itinerary-2-days.json`
- `templates/page.lijiang-itinerary-3-days.json`
- `templates/page.dali-to-lijiang-private-tour.json`
- `templates/page.tiger-leaping-gorge-from-lijiang.json`
- `templates/page.contact-us.json`
- `templates/page.help-center.json`
- `templates/page.hc-category.json`
- `templates/page.about-us.json`
- `templates/page.json`

Sections inspected because templates map to them or search showed SEO/canonical-adjacent behavior:
- `sections/main-article.liquid`
- `sections/main-blog.liquid`
- `sections/all-tours-collection.liquid`
- `sections/day-trips-collection.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `sections/dali-collection.liquid`
- `sections/lijiang-collection.liquid`
- `sections/shangri-la-collection.liquid`
- `sections/xishuangbanna-collection.liquid`
- `sections/bespoke-travel.liquid`
- `sections/main-page.liquid`
- `sections/destinations-page-overview.liquid`
- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`
- `sections/seo-itinerary-page.liquid`
- `sections/page-route-support.liquid`
- `sections/luxury-private-tour-product.liquid`
- `sections/lijiang-product.liquid`
- `sections/lijiang-product-text-images.liquid`
- `sections/one-day-trip-product.liquid`
- `sections/private-charter-service.liquid`
- `sections/product-route-support.liquid`
- `sections/product-reviews.liquid`

Existing audit docs inspected:
- `docs/seo-audit/2026-05-implementation/P0-0-contact-url-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P0-2-jade-dragon-bespoke-internal-links.md`
- `docs/seo-audit/2026-05-implementation/P0-3-car-charter-cta-tracking-audit.md`
- `docs/seo-audit/2026-05-implementation/P0-4-homepage-internal-links-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-0-contact-url-consistency-follow-up.md`
- `docs/seo-audit/2026-05-implementation/P1-1-commercial-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-2-product-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-3-destination-page-intent-audit.md`
- `docs/seo-audit/2026-05-implementation/P1-4-closeout-and-p2-readiness.md`
- `docs/seo-audit/2026-05-implementation/P2-0-structured-data-audit.md`

Search terms used:
- `canonical`
- `canonical_url`
- `robots`
- `noindex`
- `nofollow`
- `og:`
- `og_title`
- `og_description`
- `twitter:`
- `twitter:card`
- `seo_title`
- `seo_description`
- `page_title`
- `meta_description`
- `current_page`
- `request.page_type`
- `request.path`
- `handle`
- `alternate`
- `hreflang`

## Current SEO Head Inventory

| Item | Source file | Logic source | Page types affected | Global or conditional | Risk level |
|---|---|---|---|---|---|
| Title | `layout/theme.liquid` | Starts from Shopify `page_title`; then applies homepage, search, pagination, handle-scoped collection/page/article/product overrides; appends `| shop.name` unless already present. | All pages using the layout. | Global output with conditional overrides. | Medium. Centralized logic affects all page types. |
| Meta description | `layout/theme.liquid` | Starts from Shopify `page_description`; falls back by page type to product description, collection description, article content, page content, blog/search/index/shop text; then handle-scoped overrides replace target page descriptions. | All page types where a description resolves. | Global output with conditional overrides. | Medium. Fallbacks are broad; handle overrides reduce risk on target URLs. |
| Canonical | `layout/theme.liquid` | `resolved_canonical_url = canonical_url`; three duplicate article slugs override to preferred article URLs. | All pages. | Global, with article-only duplicate overrides. | Medium. Default is stable Shopify logic, but article overrides affect canonical and OG URL. |
| Robots | `layout/theme.liquid` | Emits `noindex,follow` only when `request.page_type == 'search'`, collection parameter page is detected, or duplicate article variant is detected. | Search pages, tagged/sorted collection pages, selected duplicate article variants. | Conditional only. | Medium. Commercial pages appear indexable, but live validation is needed for parameter/tag behavior. |
| Open Graph title | `layout/theme.liquid` | Uses final `seo_title`. | All pages. | Global. | Low to medium. Inherits title strengths and weaknesses. |
| Open Graph description | `layout/theme.liquid` | Uses final `seo_description` when not blank. | All pages with resolved description. | Conditional on description. | Low to medium. Inherits meta description strengths and weaknesses. |
| Open Graph image | `layout/theme.liquid` | `collection.image` for collection pages; otherwise Shopify `page_image`; otherwise `settings.logo`; emitted only if resolved. | Collections, products, articles, pages, homepage when Shopify `page_image` or logo exists. | Conditional. | Medium. Stable fallback exists only if `settings.logo` is configured; live page images depend on Shopify objects/admin content. |
| Open Graph URL | `layout/theme.liquid` | Uses `resolved_canonical_url`. | All pages. | Global. | Low to medium. Mirrors canonical behavior. |
| Twitter card | `layout/theme.liquid` | Hard-coded `summary_large_image`. | All pages. | Global. | Low. Standard card type, but image availability still matters. |
| Twitter title | `layout/theme.liquid` | Uses final `seo_title`. | All pages. | Global. | Low to medium. Inherits title strengths and weaknesses. |
| Twitter description | `layout/theme.liquid` | Uses final `seo_description` when not blank. | All pages with resolved description. | Conditional on description. | Low to medium. Inherits meta description strengths and weaknesses. |
| Twitter image | `layout/theme.liquid` | Uses same `seo_share_image` as OG image. | Same as OG image. | Conditional. | Medium. Same fallback/image-source risk as OG image. |

No separate local SEO/social-sharing snippet was found. `snippets/seo-product-jsonld.liquid` uses a local `seo_description` variable for Product JSON-LD only and does not generate meta tags, canonical tags, robots tags, OG tags, or Twitter tags.

## Canonical Audit

### Current behavior

- `layout/theme.liquid` uses Shopify `canonical_url` globally by assigning it to `resolved_canonical_url`.
- The rendered canonical tag is `<link rel="canonical" href="{{ resolved_canonical_url }}">`.
- Three article slug variants have special canonical rewrites:
  - `jade-dragon-snow-mountain-travel-guide` -> `/blogs/travel-guides/jade-dragon-snow-mountain-guide`
  - `lijiang-old-town-travel-guide` -> `/blogs/travel-guides/lijiang-old-town-guide`
  - `dali-old-town-travel-guide` -> `/blogs/day-trips/dali-old-town-day-trip-guide`
- The same duplicate article variants set `article_is_duplicate_variant = true`, which also triggers `noindex,follow`.
- No handle-specific canonical overrides were found for product, collection, destination page, bespoke page, itinerary page, or route-support page handles.
- No `alternate` or `hreflang` tags were found in local theme files.

### Target URL examples

| Target URL | Expected local canonical source | Audit note | Risk |
|---|---|---|---|
| `/` | Shopify `canonical_url` | Homepage has no custom canonical override. | Low |
| `/collections/yunnan-private-tours` | Shopify `canonical_url` | Title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/collections/yunnan-private-day-trips` | Shopify `canonical_url` | Title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/collections/yunnan-luxury-private-tours` | Shopify `canonical_url` | Title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/bespoke-custom-travel` | Shopify `canonical_url` | Page title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/kunming` | Shopify `canonical_url` | Destination title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/dali` | Shopify `canonical_url` | Destination title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/lijiang` | Shopify `canonical_url` | Destination title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/shangri-la` | Shopify `canonical_url` | Destination title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/xishuangbanna` | Shopify `canonical_url` | Destination title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour` | Shopify `canonical_url` | Product title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/products/jade-dragon-snow-mountain-private-tour` | Shopify `canonical_url` | Product title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/products/lijiang-to-shangri-la-private-tour` | Shopify `canonical_url` | Product title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/products/yunnan-private-car-charter-tour` | Shopify `canonical_url` | Product title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/blogs/travel-guides/dianchi-lake-guide` | Shopify `canonical_url` | Article title/meta are handle-scoped by slug; no duplicate canonical override for this slug. | Low |
| `/blogs/travel-guides/jade-dragon-snow-mountain-guide` | Shopify `canonical_url` | Preferred article slug; duplicate old slug rewrites here. | Low |
| `/pages/lijiang-itinerary-2-days` | Shopify `canonical_url` | Page title/meta are handle-scoped; canonical remains Shopify default. | Low |
| `/pages/lijiang-itinerary-3-days` | Shopify `canonical_url` | Page title/meta are handle-scoped; canonical remains Shopify default. | Low |

### Pagination and parameters

- Collection pagination affects title and meta description through `current_page > 1`.
- Handle-scoped collection overrides include page-number title variants for several collections.
- Canonical logic does not explicitly modify paginated collection canonical output. It relies on Shopify `canonical_url`.
- Search result pages receive page-number title/meta handling and `noindex,follow`.
- Tagged collections and non-default sorted collections are treated as collection parameter pages and receive `noindex,follow`.
- Query parameter inclusion/exclusion is controlled by Shopify `canonical_url` unless one of the duplicate article rewrites applies. Local code does not manually append query strings to canonicals.

### Wrong-URL risk

No obvious local canonical bug was found for the target commercial, destination, product, article, or itinerary URLs. The main monitor items are:

- Confirm live Shopify `canonical_url` output on paginated collections and sorted/tagged collection URLs.
- Confirm the three duplicate article variants resolve to the intended preferred canonical URLs and also show `noindex,follow`.
- Confirm no app or Shopify `content_for_header` output injects a second canonical tag.
- Confirm no historical page such as `/pages/contact-information` remains live with an unintended self-canonical; local theme has no dedicated template for it and no handle-specific canonical override.

## Robots / Noindex Audit

### Current behavior

`layout/theme.liquid` emits:

```liquid
<meta name="robots" content="noindex,follow">
```

only when one of these conditions is true:

- `request.page_type == 'search'`
- `collection_is_parameter_page`
- `article_is_duplicate_variant`

`collection_is_parameter_page` becomes true when:

- `current_tags` exists and has one or more tags, or
- `collection.sort_by` is present and differs from `collection.default_sort_by`.

### Findings

- No local noindex logic was found for the homepage.
- No local noindex logic was found for primary commercial collections such as `/collections/yunnan-private-tours`, `/collections/yunnan-private-day-trips`, or `/collections/yunnan-luxury-private-tours`.
- No local noindex logic was found for the target product pages.
- No local noindex logic was found for destination, itinerary, bespoke, or route-support pages.
- Duplicate/deprecated article variants are handled with both canonical rewrite and `noindex,follow`.
- Search pages are handled with `noindex,follow`.
- Tagged or custom-sorted collection URLs are handled with `noindex,follow`.
- Paginated collection pages are not noindexed solely because they are paginated.
- No `nofollow` behavior was found outside the `noindex,follow` robots meta.

### Commercial noindex risk

No commercial target page appears accidentally noindexed by local theme logic. Live validation should still confirm:

- Primary collections without tags/sort are indexable.
- Product pages are indexable.
- Destination and bespoke pages are indexable.
- Parameter/tag/sort pages receive `noindex,follow` as intended.
- Search pages receive `noindex,follow` as intended.

## OG / Twitter Audit

### Current behavior

- OG/Twitter title uses final `seo_title`.
- OG/Twitter description uses final `seo_description` when present.
- OG URL uses `resolved_canonical_url`, so it follows canonical URL behavior.
- OG type is `product` for product pages, `article` for article pages, and `website` for all other page types.
- Twitter card is always `summary_large_image`.
- OG/Twitter image uses one shared `seo_share_image` fallback chain:
  - collection pages: `collection.image` if present
  - otherwise: Shopify `page_image` if present
  - otherwise: `settings.logo` if present
  - otherwise: no OG/Twitter image tag is emitted

### Page-type image notes

| Page type | Local image source | Audit note | Risk |
|---|---|---|---|
| Homepage | Shopify `page_image`, then `settings.logo` | Homepage template contains hero images, but OG image does not read section hero settings directly. | Medium |
| Collections | `collection.image`, then `page_image`, then `settings.logo` | Best coverage when collection admin image exists. | Low to medium |
| Products | Shopify `page_image`, then `settings.logo` | Shopify often maps product featured image into `page_image`, but this must be live-validated. | Medium |
| Pages | Shopify `page_image`, then `settings.logo` | Destination templates contain section images, but OG image does not read section-specific image settings directly. | Medium |
| Articles | Shopify `page_image`, then `settings.logo` | Article templates render `article.image`; live validation should confirm it maps to `page_image`. | Low to medium |

### Missing social field risks

- Title risk is low because `seo_title` always falls back to Shopify `page_title` or shop name and then gets a brand suffix if needed.
- Description risk is low to medium because most page types have fallbacks, but generic pages with thin `page.content` can still produce thin descriptions.
- Image risk is medium because local code only emits image tags if the fallback chain resolves. If both Shopify `page_image` and `settings.logo` are absent, social images can be missing.
- Homepage social image stability depends on Shopify `page_image` or `settings.logo`, not the local hero image setting.
- Product, page, and article social image quality should be live-checked because the local theme relies on Shopify's `page_image` object rather than directly selecting `product.featured_image`, `article.image`, or destination section images.

## Title / Meta Override Consistency

### Handles controlled in `layout/theme.liquid`

Homepage:
- `/`

Collections:
- `yunnan-private-tours`
- `yunnan-private-day-trips`
- `yunnan-luxury-private-tours`
- `dali-private-tours`
- `lijiang-private-tours`

Pages:
- `kunming`
- `dali`
- `lijiang`
- `shangri-la`
- `xishuangbanna`
- `dali-itinerary-3-days`
- `lijiang-itinerary-3-days`
- `dali-itinerary-2-days`
- `lijiang-itinerary-2-days`
- `tiger-leaping-gorge-from-lijiang`
- `dali-to-lijiang-private-tour`
- `bespoke-custom-travel`

Articles by slug:
- `dianchi-lake-guide`
- `jade-dragon-snow-mountain-guide`
- `stone-forest-shilin-guide`
- `lijiang-old-town-guide`

Products:
- `kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `jade-dragon-snow-mountain-private-tour`
- `lijiang-to-shangri-la-private-tour`
- `yunnan-private-car-charter-tour`

### Likely Shopify admin field dependencies

- Collections not listed above depend on Shopify `page_title`, `page_description`, collection title, and collection description fallbacks.
- Products not listed above depend on Shopify `page_title`, `page_description`, product title, and product description fallbacks.
- Pages not listed above depend on Shopify `page_title`, `page_description`, page content, page title fallback, or shop description fallback.
- Blog pages depend on Shopify blog title plus the hard-coded blog description fallback.
- Article pages outside the slug overrides depend on Shopify `page_title`, `page_description`, or article excerpt/content fallback.
- Social images depend partly on Shopify admin resource image data and theme settings.

### Current consistency notes

- Target P0/P1 commercial, product, destination, itinerary, route-support, and article pages have no obvious visible page intent mismatch documented in local files.
- The final brand suffix guard appends `| Lynxtour` unless the resolved title already contains the shop name.
- Several code-level titles intentionally omit the brand suffix in their assigned string because the global suffix guard adds it later.
- Titles that already include `| Lynxtour` are not duplicated because the downcased title is checked against the downcased shop name.
- `Custom Yunnan Itinerary | Bespoke Private Travel Planning` intentionally receives the brand suffix through the guard.
- `Request a custom Yunnan itinerary... Get private planning support from Lynx Tour.` uses `Lynx Tour` with a space in the meta description. This may be a brand consistency monitor item, but it is not a blocker.
- Most target meta descriptions are specific and not obviously duplicated.
- Some meta descriptions are close to the longer end for snippets, especially route/itinerary pages, but no code change is recommended from the local audit alone.

## Duplicate / Conflict Risks

| Risk | Local finding | Severity | Audit position |
|---|---|---|---|
| Duplicate title/meta sources | `layout/theme.liquid` emits custom title/meta; Shopify `content_for_header` may also inject app output. | Medium | Live source validation needed. |
| Shopify admin SEO fields vs code overrides | Code overrides replace admin title/meta on listed handles after initial Shopify variables are read. | Low to medium | Expected for target handles; document as source of truth. |
| App-injected SEO tags through `content_for_header` | `{{ content_for_header }}` appears after the local SEO tags. Local files cannot show app output. | Medium | Check live page source for duplicate canonical/meta/social tags. |
| OG/Twitter conflict risk | Local OG/Twitter tags are centralized. Any app-injected social tags could conflict. | Medium | Live social preview and source checks needed. |
| Canonical conflict risk | Local canonical is centralized, but `content_for_header` or apps could inject additional canonical tags. | Medium | Live source validation needed. |
| Structured data conflict | Out of scope for this P2-B audit; P2-0 covered local schema and P2-A1 covered Product JSON-LD live validation. | Low for this task | Do not modify JSON-LD here. |
| Review schema conflict | `product-reviews` has potential Product/review schema but was documented as disabled in relevant context in P2-0. | Low to medium | Do not add review or aggregateRating unless verified product-level reviews exist. |

## P2 Implementation Recommendations

### P2-B1: Live Canonical Validation

- Goal: Confirm canonical output for target pages, paginated collections, sorted/tagged collections, search pages, and duplicate article variants.
- Risk level: Medium.
- Likely files: documentation first; possible future `layout/theme.liquid` only if a confirmed defect exists.
- Must not be touched: redirects, handles, template names, section names, Product JSON-LD, robots logic, booking logic, price logic, variant logic, GA4/GTM.
- Recommendation: Implement later only if live validation finds a confirmed canonical defect.

### P2-B2: Robots / Noindex Validation

- Goal: Confirm commercial pages are indexable and search/parameter/duplicate article URLs are `noindex,follow`.
- Risk level: Medium.
- Likely files: documentation first; possible future `layout/theme.liquid` only if live validation finds a confirmed robots defect.
- Must not be touched: canonical rewrites, redirects, handles, product logic, structured data, GA4/GTM.
- Recommendation: Implement later only if live validation finds a confirmed indexation defect.

### P2-B3: OG / Twitter Image Fallback Audit

- Goal: Confirm homepage, collection, product, page, and article social previews have stable image/title/description output.
- Risk level: Medium.
- Likely files: documentation first; possible future `layout/theme.liquid` or Shopify theme settings/admin assets if image fallback is missing.
- Must not be touched: canonical logic, robots logic, Product JSON-LD, booking/price/variant logic, GA4/GTM.
- Recommendation: Audit live first. Prefer admin/theme-setting fixes before code if only images are missing.

### P2-B4: Title / Meta Brand Suffix Consistency Decision

- Goal: Decide whether every assigned SEO title should include `| Lynxtour` manually or continue relying on the global suffix guard.
- Risk level: Low to medium.
- Likely files: `layout/theme.liquid` only if a future consistency change is approved.
- Must not be touched: canonical, robots, JSON-LD, URLs, handles, redirects, templates, sections.
- Recommendation: Not recommended now. Current guard prevents duplicate brand suffixes and target titles appear coherent.

### P2-B5: Deprecated URL Canonical / Noindex / Redirect Decision

- Goal: Decide how to handle historical or alternate URLs such as old article slugs and `/pages/contact-information`.
- Risk level: Medium to high if redirects/noindex are changed without live GSC/admin confirmation.
- Likely files: documentation and Shopify admin first; possible future `layout/theme.liquid` only for noindex/canonical handling, and Shopify URL redirects for redirects.
- Must not be touched: current target page handles, canonical defaults, Product JSON-LD, product booking logic, GA4/GTM.
- Recommendation: Later only after GSC URL Inspection and Shopify admin verification. Prefer Shopify admin redirects for true deprecated URLs rather than theme-level rewrites.

## Manual Validation Checklist

### View page source checks

- Confirm exactly one canonical tag.
- Confirm canonical URL matches the intended preferred URL.
- Confirm no unwanted query parameters appear in canonical URLs.
- Confirm `meta name="robots"` is absent on primary commercial, destination, product, article, and itinerary pages.
- Confirm `noindex,follow` appears on search pages, sorted/tagged collection URLs, and duplicate article variants.
- Confirm title and meta description match the expected code/admin source.
- Confirm OG title, description, and URL match final title, description, and canonical.
- Confirm `og:image`, `og:image:secure_url`, and `twitter:image` exist where expected.
- Confirm `twitter:card` is `summary_large_image`.
- Confirm no app-injected duplicate canonical, robots, OG, or Twitter tags appear through `content_for_header`.

### Google Search Console URL Inspection checks

- Inspect primary target URLs as live URLs.
- Confirm Google-selected canonical matches user-declared canonical.
- Confirm indexability is allowed for commercial pages.
- Confirm duplicate article variants, search pages, and parameter pages are not selected as primary indexable URLs.
- Confirm no unexpected "Alternate page with proper canonical tag" issue on intended primary pages.
- Confirm no unexpected "Excluded by noindex" issue on target commercial pages.

### Social preview checks

- Test representative pages in social preview tools for Facebook/Open Graph and Twitter/X cards.
- Confirm preview title uses the final `seo_title`.
- Confirm preview description uses the final `seo_description`.
- Confirm preview image is relevant, not missing, and not only a tiny logo where a page-specific image should appear.
- Confirm product pages show product-relevant imagery.
- Confirm article pages show article imagery.
- Confirm homepage image is stable and not missing.

### Sample URLs to validate

- `https://lynxtour.cn/`
- `https://lynxtour.cn/collections/yunnan-private-tours`
- `https://lynxtour.cn/collections/yunnan-private-tours?page=2`
- `https://lynxtour.cn/collections/yunnan-private-tours?sort_by=price-ascending`
- `https://lynxtour.cn/collections/yunnan-private-day-trips`
- `https://lynxtour.cn/collections/yunnan-luxury-private-tours`
- `https://lynxtour.cn/pages/bespoke-custom-travel`
- `https://lynxtour.cn/pages/kunming`
- `https://lynxtour.cn/pages/dali`
- `https://lynxtour.cn/pages/lijiang`
- `https://lynxtour.cn/pages/shangri-la`
- `https://lynxtour.cn/pages/xishuangbanna`
- `https://lynxtour.cn/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `https://lynxtour.cn/products/jade-dragon-snow-mountain-private-tour`
- `https://lynxtour.cn/products/lijiang-to-shangri-la-private-tour`
- `https://lynxtour.cn/products/yunnan-private-car-charter-tour`
- `https://lynxtour.cn/blogs/travel-guides/dianchi-lake-guide`
- `https://lynxtour.cn/blogs/travel-guides/jade-dragon-snow-mountain-guide`
- `https://lynxtour.cn/blogs/travel-guides/jade-dragon-snow-mountain-travel-guide`
- `https://lynxtour.cn/pages/lijiang-itinerary-2-days`
- `https://lynxtour.cn/pages/lijiang-itinerary-3-days`
- `https://lynxtour.cn/search?q=lijiang`

### Errors that must block implementation

- Primary commercial page has `noindex`.
- Primary product page has `noindex`.
- Canonical points to the wrong page or wrong handle.
- More than one canonical tag appears live.
- App-injected SEO tags conflict with local tags.
- Duplicate article variant does not canonicalize to the preferred article.
- Sorted/tagged/search URLs are indexable when they should be `noindex,follow`.
- OG/Twitter title or description is blank on target pages.
- Social image is missing across broad page classes despite available Shopify assets.

### Warnings that can be monitored

- Meta description is slightly long but accurate.
- Title relies on global brand suffix guard rather than manual `| Lynxtour` in the assigned string.
- Social image falls back to logo on a small number of low-priority pages.
- Google-selected canonical temporarily differs during recrawl after recent changes.
- Parameter URLs appear in GSC history but are currently declared noindex/canonical correctly.

## Audit Conclusion

No P2-B code change is recommended from the local audit alone.

The current implementation is centralized and mostly conservative: Shopify `canonical_url` is used globally, target P0/P1 pages use handle-scoped title/meta overrides, robots noindex is limited to search, collection parameter pages, and selected duplicate article variants, and OG/Twitter tags inherit the resolved SEO fields.

Proceed with live validation before any implementation. Monitor canonical, robots, and social image output first, especially around `content_for_header`, paginated collections, sorted/tagged collections, product social images, article duplicate variants, and historical/deprecated URLs.

## Safety Note

This branch is audit-only and validation-only.

No code behavior changed.
