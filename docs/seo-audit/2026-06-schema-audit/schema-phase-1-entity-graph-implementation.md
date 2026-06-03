# Schema Phase 1 Entity Graph Implementation

Implementation date: 2026-06-03

Branch: `feat/schema-phase-1-entity-graph`

## Files Changed

- `layout/theme.liquid`
- `snippets/seo-product-jsonld.liquid`
- `sections/main-article.liquid`
- `sections/product-reviews.liquid`
- `sections/bespoke-travel.liquid`
- `sections/luxury-private-tour-collection.liquid`
- `docs/seo-audit/2026-06-schema-audit/schema-phase-1-entity-graph-implementation.md`

## Schema Types Changed

- `Organization`
- `TravelAgency`
- `WebSite`
- `Product`
- `Offer`
- `Article`
- `BreadcrumbList`
- `Review` publisher reference only, inside the existing conditional review Product schema

## What Was Fixed

- Replaced the thin homepage-only `Organization` and `WebSite` JSON-LD with a stable global JSON-LD graph in `layout/theme.liquid`.
- Added stable live-domain entity IDs:
  - `https://lynxtour.cn/#organization`
  - `https://lynxtour.cn/#website`
- Kept the organization description focused on private and custom Yunnan tours for international travelers.
- Added conservative `areaServed` entries for Yunnan, Kunming, Dali, Lijiang, Shangri-La, and Xishuangbanna.
- Used existing footer social links for `sameAs`.
- Added public business fields to the global `TravelAgency`/`Organization` schema: telephone, email, address, customer-service contact point, opening hours, and `image` when `settings.logo` exists.
- Did not add rating, reviews, awards, or `SearchAction`.
- `priceRange` was intentionally not added because no explicit price range is visible on the audited public pages.

## Quote / Custom Zero-Price Variant Handling

`snippets/seo-product-jsonld.liquid` now mirrors the booking UI's quote-style detection for zero-price variants.

Zero-price variants are excluded from priced `Offer` schema when variant title/options contain:

- `custom`
- `bespoke`
- `request`
- `quote`
- `inquiry`
- `charter`

Those variants are treated as inquiry placeholders and are not emitted as `"price": 0.0` Offers. Normal paid variants remain unchanged.

## Product Seller Reference

Each emitted Product `Offer` now uses:

```json
"seller": {
  "@id": "https://lynxtour.cn/#organization"
}
```

This replaces the prior nested seller Organization object and connects product commerce schema to the stable Lynxtour entity.

Product `@id` remains the canonical live product URL plus `#product`, for example:

```text
https://lynxtour.cn/products/example-product#product
```

## Article Publisher Reference

`sections/main-article.liquid` keeps the existing `Article` schema and now changes publisher to:

```json
"publisher": {
  "@id": "https://lynxtour.cn/#organization"
}
```

This avoids outputting a second standalone publisher Organization object in article JSON-LD.

## Breadcrumbs Added

Added only the missing important BreadcrumbList schema identified in the audit:

- Blog articles in `sections/main-article.liquid`: Home > Blog > Article
- Bespoke/custom travel page in `sections/bespoke-travel.liquid`: Home > Current Page
- Luxury private tour collection in `sections/luxury-private-tour-collection.liquid`: Home > Collection Title

Existing product, destination, itinerary, route-support, and non-luxury collection breadcrumbs were not duplicated.

## Product Review Schema Safety

`sections/product-reviews.liquid` still only emits schema if the existing section condition is met (`product and review_count > 0`).

If enabled later, its Product schema now uses the same product `@id` pattern as `snippets/seo-product-jsonld.liquid`, and review publishers reference `https://lynxtour.cn/#organization`.

No reviews, ratings, or aggregate ratings were invented or expanded.

## Intentionally Not Changed

- No `TouristDestination` schema was added.
- No `TouristTrip` schema was added.
- No `ItemList` schema was added.
- No `Service` schema was added for the bespoke/custom travel page.
- No `CollectionPage` or product-grid `ItemList` schema was added.
- No `priceRange` was added.
- No `SearchAction` was added.
- No visible layout, CSS, JavaScript behavior, URLs, handles, template names, section names, Shopify schema names, booking UI, variant logic, price display logic, cart behavior, or checkout behavior was changed.

## Manual Validation Checklist

Before merge, preview and inspect rendered source for:

- Homepage
- One normal paid product
- One quote/custom product
- `/products/yunnan-private-car-charter-tour`
- One blog article
- `/pages/bespoke-custom-travel`
- `/collections/yunnan-luxury-private-tours`

For each relevant page, confirm:

- JSON-LD is valid JSON.
- No fake `"price": 0` appears for quote/custom variants.
- Main Product has an `@id` ending in `#product`.
- Review Product, if present, uses the same `#product` `@id` as the main Product.
- Seller and publisher references use `https://lynxtour.cn/#organization`.
- No duplicate Product or Organization schema is injected by `content_for_header` or apps.
- Brand/entity name remains `Lynxtour`.

- Preview the homepage and confirm exactly one global JSON-LD graph includes `TravelAgency`/`Organization` and `WebSite`.
- View source on a product page with normal paid variants and confirm paid Offers still render with price, currency, availability, URL, and seller `@id`.
- View source on a product page with quote/custom/request/charter zero-price variants and confirm those variants do not render as `"price": 0.0` Offers.
- View source on a blog article and confirm Article publisher references `https://lynxtour.cn/#organization`.
- View source on a blog article and confirm BreadcrumbList is Home > Blog > Article.
- View source on `/pages/bespoke-custom-travel` and confirm BreadcrumbList is Home > Current Page.
- View source on `/collections/yunnan-luxury-private-tours` and confirm BreadcrumbList is Home > Collection Title.
- Run Schema.org Validator on representative homepage, product, blog article, bespoke page, and luxury collection page.
- Run Google Rich Results Test on representative product and article pages.
- Confirm no app-injected duplicate Product, Organization, WebSite, Article, or BreadcrumbList schema conflicts appear in rendered source.
