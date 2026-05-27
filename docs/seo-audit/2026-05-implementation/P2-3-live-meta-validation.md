# P2-B1 Live Canonical / Robots / OG / Twitter Validation

Date: 2026-05-27
Branch: `feat/seo-live-meta-validation-p2`
Scope: live validation documentation only.

## Guardrails

- No Liquid changed.
- No JSON templates changed.
- No snippets changed.
- No CSS changed.
- No structured data or JSON-LD changed.
- No canonical logic changed.
- No robots/noindex logic changed.
- No OG/Twitter logic changed.
- No GA4/GTM changed.
- No redirects created.
- Downloaded HTML source files were not staged or committed.

## Inputs Used

- `docs/seo-audit/2026-05-live-source/source-1.html` through `docs/seo-audit/2026-05-live-source/source-13.html`
- `docs/seo-audit/2026-05-live-source/meta-tag-scan.txt`
- `docs/seo-audit/2026-05-implementation/P2-2-canonical-og-twitter-audit.md`

## Validation Summary

| # | URL | Source file | Title count | Description count | Canonical count | Robots count | Expected robots behavior | OG title count | OG image count | Twitter card count | Twitter image count | Status | Notes |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---|---|
| 1 | `https://lynxtour.cn/` | `source-1.html` | 1 | 1 | 1 | 0 | Primary homepage should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | Canonical, title/meta, OG, and Twitter tag counts match expected output. |
| 2 | `https://lynxtour.cn/collections/yunnan-private-tours` | `source-2.html` | 1 | 1 | 1 | 0 | Primary commercial collection should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | No accidental noindex detected in count scan. |
| 3 | `https://lynxtour.cn/collections/yunnan-private-tours?page=2` | `source-3.html` | 1 | 1 | 1 | 0 | Paginated collection page is not expected to be noindexed solely due to pagination. | 1 | 1 | 1 | 1 | Pass | Pagination count behavior matches the P2-B audit expectation. |
| 4 | `https://lynxtour.cn/collections/yunnan-private-tours?sort_by=price-ascending` | `source-4.html` | 1 | 1 | 1 | 1 | Sorted collection parameter URL should have robots meta, expected `noindex,follow`. | 1 | 1 | 1 | 1 | Pass | Robots meta present as expected for sorted collection URL. |
| 5 | `https://lynxtour.cn/collections/yunnan-private-day-trips` | `source-5.html` | 1 | 1 | 1 | 0 | Primary commercial collection should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | No accidental noindex detected in count scan. |
| 6 | `https://lynxtour.cn/collections/yunnan-luxury-private-tours` | `source-6.html` | 1 | 1 | 1 | 0 | Primary commercial collection should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | Collection social image tag is present. |
| 7 | `https://lynxtour.cn/pages/bespoke-custom-travel` | `source-7.html` | 1 | 1 | 1 | 0 | Primary bespoke commercial page should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | No accidental noindex detected in count scan. |
| 8 | `https://lynxtour.cn/pages/kunming` | `source-8.html` | 1 | 1 | 1 | 0 | Primary destination page should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | No accidental noindex detected in count scan. |
| 9 | `https://lynxtour.cn/products/jade-dragon-snow-mountain-private-tour` | `source-9.html` | 1 | 1 | 1 | 0 | Primary product page should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | Product social image tag is present. |
| 10 | `https://lynxtour.cn/products/yunnan-private-car-charter-tour` | `source-10.html` | 1 | 1 | 1 | 0 | Primary product page should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | Product social image tag is present. |
| 11 | `https://lynxtour.cn/blogs/travel-guides/jade-dragon-snow-mountain-guide` | `source-11.html` | 1 | 1 | 1 | 0 | Preferred article URL should be indexable; no robots noindex expected. | 1 | 1 | 1 | 1 | Pass | Preferred article source counts match expected output. |
| 12 | `https://lynxtour.cn/blogs/travel-guides/jade-dragon-snow-mountain-travel-guide` | `source-12.html` | 1 | 1 | 1 | 0 | Old duplicate article URL should redirect or otherwise resolve safely to the preferred guide. | 1 | 1 | 1 | 1 | Pass / watch | `curl -L` was used, so the downloaded HTML may represent the final redirected preferred page. Robots = 0 is not a blocker if redirect behavior is confirmed. Optional future confirmation: `curl -IL`. |
| 13 | `https://lynxtour.cn/search?q=lijiang` | `source-13.html` | 1 | 1 | 1 | 1 | Search URL should have robots meta, expected `noindex,follow`. | 1 | 1 | 1 | 1 | Pass | Robots meta present as expected for search URL. |

## Canonical Validation

- All tested pages have exactly one canonical tag.
- No duplicate canonical tag was detected in the live source count scan.
- Primary pages passed canonical count validation.
- Exact canonical target values can be monitored separately if needed.
- `source-12.html` should be treated as pass/watch because the old duplicate article URL appears to redirect to the preferred article, `/blogs/travel-guides/jade-dragon-snow-mountain-guide`.

## Robots Validation

- Primary commercial, product, destination, homepage, and preferred article pages had no robots noindex tag.
- The sorted collection URL had robots meta present as expected.
- The search URL had robots meta present as expected.
- No primary target page was found accidentally noindexed in the count scan.
- `source-12.html`, the old Jade Dragon article URL, needs no extra action if redirect behavior is confirmed.

## OG / Twitter Validation

- All tested source files had OG title and OG image tags.
- All tested source files had Twitter card and Twitter image tags.
- No broad missing social image issue was found.
- No code change is recommended.

## Blockers And Watch Items

Blockers:
- None found from this live source count validation.

Watch items:
- Exact canonical `href` values can be spot-checked later.
- Exact robots content for sorted collection and search should remain `noindex,follow`.
- `source-12.html` old article URL should remain redirected to the preferred guide URL.
- Social image quality should be checked visually for high-value pages, but image tags are present.

## Recommendation

- No P2-B code change needed now.
- Do not modify `layout/theme.liquid`.
- Proceed next to P2-C internal link / broken-link audit.
- Do not commit downloaded HTML source files.

## Safety Note

This branch is validation-only.

No code behavior changed.
