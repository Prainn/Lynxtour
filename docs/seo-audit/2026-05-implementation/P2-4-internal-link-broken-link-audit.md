# P2-C Internal Link / Broken-Link Audit

Date: 2026-05-27
Branch: `feat/seo-internal-link-audit-p2`
Scope: audit-only, documentation-only.

## Guardrails

- No Liquid changed.
- No JSON templates changed.
- No snippets changed.
- No CSS changed.
- No redirects changed.
- No SEO title/meta/canonical/robots logic changed.
- No structured data or JSON-LD changed.
- No GA4/GTM changed.
- No URLs, handles, CTAs, or link targets changed.
- Live CSV files were not staged or committed.

## Exact Files Inspected

Live filtered link scan files:
- `docs/seo-audit/2026-05-live-links/internal-link-check-filtered.csv`
- `docs/seo-audit/2026-05-live-links/internal-link-watch-filtered.csv`
- `docs/seo-audit/2026-05-live-links/private-tours-link-check-filtered.csv`
- `docs/seo-audit/2026-05-live-links/private-tours-link-watch-filtered.csv`

Supporting unfiltered false-positive context:
- `docs/seo-audit/2026-05-live-links/internal-link-watch.csv`

Existing implementation docs:
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
- `docs/seo-audit/2026-05-implementation/P2-1-product-jsonld-live-validation.md`
- `docs/seo-audit/2026-05-implementation/P2-2-canonical-og-twitter-audit.md`
- `docs/seo-audit/2026-05-implementation/P2-3-live-meta-validation.md`

## Audit Scope

### Source pages checked

- `https://lynxtour.cn/`
- `https://lynxtour.cn/collections/yunnan-private-tours`
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
- `https://lynxtour.cn/pages/lijiang-itinerary-2-days`
- `https://lynxtour.cn/pages/lijiang-itinerary-3-days`

The separate private tours filtered check also covered:
- `https://lynxtour.cn/collections/yunnan-private-tours`

### Link types included

- Filtered internal/content links on the checked live pages.
- Root-relative Lynxtour URLs.
- Absolute `https://lynxtour.cn/...` URLs.
- Content links relevant to SEO crawl paths, page-to-page navigation, products, collections, pages, blogs, and articles.

### Link types excluded

The filtered live link scan excluded non-content links:

- Anchor-only links.
- `mailto:`, `tel:`, `javascript:`, WhatsApp, and `data:` links.
- Protocol-relative CDN links.
- `/cdn/shop` assets.
- Customer authentication links.
- Account links.
- Image, CSS, JS, and font asset URLs.

### Why the filtered scan is the source of truth

The filtered scan is the source of truth for this SEO internal-link audit because it focuses on crawlable content/internal links and removes non-content assets, customer-authentication endpoints, and utility protocols that are not P0/P1 SEO internal-link blockers.

## Status Summary

| Scan file | Scope | Checked links | HTTP 200 | Other statuses | Watch rows | Status |
|---|---|---:|---:|---:|---:|---|
| `internal-link-check-filtered.csv` | Main target page set | 707 | 707 | 0 | 0 | Pass |
| `private-tours-link-check-filtered.csv` | Separate `/collections/yunnan-private-tours` check | 54 | 54 | 0 | 0 | Pass |

- Total checked filtered internal/content links in the main scan: 707.
- Count by HTTP status in the main scan: `200 = 707`.
- Blockers found: 0.
- Watch rows in filtered watch files: 0.
- All filtered checked links returned HTTP 200.
- The separate `/collections/yunnan-private-tours` filtered check returned 54 checked links, all HTTP 200, with an empty watch file.

## False-Positive Explanation

The first unfiltered scan showed 404/406 results.

Those results came from protocol-relative favicon/CDN asset URLs and Shopify customer authentication URLs, including examples like malformed scanned CDN favicon paths and `customer_authentication/redirect` endpoints.

These URLs were excluded from the filtered SEO content-link scan because they are not content links between indexable SEO pages.

They are not P0/P1 SEO internal-link blockers.

## Blocker Table

No 404, 403, 500, `FETCH_ERROR`, or wrong-final-URL blockers were found in the filtered content-link scan.

| Blocker type | Count | Status |
|---|---:|---|
| 404 content/internal links | 0 | Pass |
| 403 content/internal links | 0 | Pass |
| 500 content/internal links | 0 | Pass |
| `FETCH_ERROR` content/internal links | 0 | Pass |
| Wrong-final-URL blockers | 0 | Pass |

## P0/P1 SEO Link Validation

The filtered scan supports the following P0/P1 link validation outcomes:

- Homepage commercial links: checked in the main filtered scan; all filtered links returned HTTP 200.
- `/collections/yunnan-private-tours` links: checked in both the main filtered scan and the separate private-tours filtered scan; all filtered links returned HTTP 200.
- Commercial collection support links: checked across private tours, day trips, and luxury private tours pages; all filtered links returned HTTP 200.
- Bespoke CTA links: `/pages/bespoke-custom-travel` appeared in the filtered scan and returned HTTP 200.
- Destination page CTA links: checked across Kunming, Dali, Lijiang, Shangri-La, and Xishuangbanna source pages; all filtered links returned HTTP 200.
- Product support links: checked across the 8-day Yunnan product, Jade Dragon Snow Mountain product, Lijiang to Shangri-La product, and car charter product pages; all filtered links returned HTTP 200.
- Jade Dragon guide/product links: `/blogs/travel-guides/jade-dragon-snow-mountain-guide` and `/products/jade-dragon-snow-mountain-private-tour` appeared in the filtered scan and returned HTTP 200.
- Car charter links: `/products/yunnan-private-car-charter-tour` appeared in the filtered scan and returned HTTP 200.
- Dianchi guide internal links: `/blogs/travel-guides/dianchi-lake-guide` appeared in the filtered scan and returned HTTP 200.

## Contact URL Consistency Check

`/pages/contact-information` appears in the main filtered checked links.

- Main filtered scan occurrences: 18.
- Status for those occurrences: all HTTP 200.
- Sources include the homepage, commercial collections, destination pages, target product pages, the two checked guide articles, and the two checked Lijiang itinerary pages.
- The separate private tours filtered check also includes `/pages/contact-information`, returning HTTP 200.

This is not a broken-link blocker because the filtered scan shows HTTP 200. It remains a contact URL consistency watch item because earlier P0/P1 documentation identified `/pages/contact-us` as the locally linked primary contact page and `/pages/contact-information` as a legacy/alternate contact URL risk.

No code change or redirect change is recommended from this filtered broken-link audit alone.

## Recommendation

- No code change needed.
- No redirect change needed.
- Monitor only.
- Proceed next to P2-D GA4 event naming / conversion attribution audit.

## Safety Note

This branch is audit-only.

No code behavior changed.

Live CSV files should not be committed.
