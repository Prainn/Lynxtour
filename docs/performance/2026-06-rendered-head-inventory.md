# Rendered Homepage Head Inventory

Date: 2026-06-09

Live URL inspected: `https://lynxtour.cn/`

Scope: Phase 2 implementation prep only. No Liquid, CSS, JavaScript, schema, section, template, URL, handle, app logic, or Shopify setting changes were made.

## Current Lighthouse Mobile Metrics

| Metric | Current result after Phase 1 |
| --- | ---: |
| Performance | 73 |
| FCP | 4.1s |
| LCP | 4.4s |
| TBT | 160ms |
| Speed Index | 4.1s |
| CLS | 0 |

## Files And Sources Compared

- Live rendered homepage HTML head from `https://lynxtour.cn/`
- `layout/theme.liquid`
- `sections/destinations.liquid` for homepage section-level Google Fonts context

## Comparison Summary

- `layout/theme.liquid` contains the core SEO metadata, canonical tag, favicon tags, organization JSON-LD, `{{ content_for_header }}`, Tailwind CDN script, global Google Fonts, a large inline global style block, and an import map.
- The rendered homepage head contains all expected theme-owned resources from `layout/theme.liquid`.
- The rendered homepage head also contains a large Shopify-injected `content_for_header` block with checkout metadata, Shop app modules, captcha, dynamic checkout, privacy banner, accelerated checkout CSS, Shopify analytics, Web Pixels Manager, Monorail, and Shopify perf-kit resources.
- Shopify also injects an async import-map polyfill near the top of the head, before the theme JSON-LD. This is not handwritten in `layout/theme.liquid`; it appears to be Shopify platform support for the theme import map.
- No explicit app-owned third-party marketing pixel URL, such as a Google Tag Manager or Meta Pixel script URL, was visible as a standalone external script in the rendered head snapshot. Shopify Web Pixels Manager and Shopify analytics are present.
- The homepage `destinations` section adds another Google Fonts stylesheet in the body after the hero section; it is not part of the rendered `<head>`, but it can still compete for early page resources on the homepage.

## Exact Rendered Head Resource Inventory

Risk key: high = parser/render blocking or critical-path CSS/JS; medium = async/defer or inline head work that can still compete for CPU/network; low = metadata, hints, or non-blocking resources.

| Order | Rendered resource | Owner | Blocking risk | Control path |
| ---: | --- | --- | --- | --- |
| 1 | `<link rel="canonical" href="https://lynxtour.cn/">` | theme code | Low | Theme code, but do not change for performance. |
| 2 | `<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>` | theme code | Low | Theme code. Likely beneficial for Shopify CDN assets. |
| 3 | Favicon PNG: `//lynxtour.cn/cdn/shop/files/lynxtour_favicon_48.png?...width=48` | theme code plus Shopify CDN | Low | Theme setting controls favicon; not a Phase 2 target. |
| 4 | Apple touch icon: `//lynxtour.cn/cdn/shop/files/lynxtour_favicon_48.png?...width=180` | theme code plus Shopify CDN | Low | Theme setting controls favicon; not a Phase 2 target. |
| 5 | Theme JSON-LD: `<script type="application/ld+json">` organization and website graph | theme code | Low | Theme code, but schema was out of scope and should not be changed here. |
| 6 | `/cdn/shopifycloud/importmap-polyfill/es-modules-shim.2.4.0.js` with `async`, `crossorigin`, `fetchpriority="high"` | Shopify platform | Medium | Not safely controlled in theme directly; likely injected because the theme uses an import map. |
| 7 | `window.performance.mark('shopify.content_for_header.start')` | Shopify platform | Low | Shopify controlled through `content_for_header`; do not edit or remove. |
| 8 | Google Search Console verification meta | Shopify setting or theme/app admin setting | Low | Admin/search verification setting. No performance action. |
| 9 | Shopify digital wallet meta: `/80446521559/digital_wallets/dialog` | Shopify platform | Low | Shopify checkout/payment settings, not theme code. |
| 10 | Shopify checkout API token meta | Shopify platform | Low | Shopify platform; not safely controlled. |
| 11 | In-context PayPal metadata | Shopify platform/payment integration | Low | Shopify payment settings. |
| 12 | `/checkouts/internal/preloads.js?locale=en-CN` with `async` | Shopify platform | Medium | Shopify checkout platform. Not safely controlled in theme. |
| 13 | `shopify-features` JSON script | Shopify platform | Low | Shopify platform. |
| 14 | Inline Shopify global object/bootstrap script | Shopify platform | Medium | Shopify platform. Not safely controlled in theme. |
| 15 | Inline `type="module"` Shopify modules flag | Shopify platform | Low to medium | Shopify platform. |
| 16 | Inline Shopify `loadFeatures` and `autoloadFeatures` queues | Shopify platform | Medium | Shopify platform. |
| 17 | Inline `Shopify.SignInWithShop` eligibility/asset metrics script | Shopify platform | Medium | Shopify customer account / Shop settings. |
| 18 | `shop-js-analytics` JSON script | Shopify platform analytics | Low | Shopify platform. |
| 19 | `//lynxtour.cn/cdn/shopifycloud/shop-js/modules/v2/loader.init-shop-cart-sync.en.esm.js` with `defer`, `async`, `type="module"` | Shopify platform | Medium | Shopify customer account / cart sync platform; not theme-controlled. |
| 20 | Inline module importing `loader.init-shop-cart-sync.en.esm.js` with top-level `await import(...)` | Shopify platform | Medium | Shopify platform. Could affect main-thread timing, but not safely controlled in theme. |
| 21 | Inline `window.Shopify.featureAssets['shop-js']` feature map | Shopify platform | Low to medium | Shopify platform. |
| 22 | Inline `__st` Shopify analytics metadata | Shopify platform analytics | Low | Shopify platform. |
| 23 | Inline PayPal visibility tracking flag | Shopify platform/payment integration | Low | Shopify payment settings. |
| 24 | Inline `captcha-bootstrap` script | Shopify platform/forms captcha | Medium to high | Shopify forms/customer account protection. Do not remove in theme. |
| 25 | `//lynxtour.cn/cdn/shopifycloud/storefront/assets/storefront/load_feature-1bd60354.js` with `defer` | Shopify platform | Medium | Shopify platform. |
| 26 | Inline `shopify.dynamic_checkout.dynamic.init` script that appends portable wallets module | Shopify platform/payment integration | Medium | Shopify dynamic checkout/payment settings. |
| 27 | Inline `shopify.dynamic_checkout.buyer_consent` script | Shopify platform/payment integration | Low to medium | Shopify dynamic checkout/payment settings. |
| 28 | Inline `shopify.dynamic_checkout.cart.bootstrap` script | Shopify platform/payment integration | Low to medium | Shopify dynamic checkout/payment settings. |
| 29 | `//cdn.shopify.com/shopifycloud/storefront/assets/storefront/origin_trials-67b41cb9.js` with `async` | Shopify platform | Low to medium | Shopify platform. |
| 30 | `https://lynxtour.cn/cdn/shopifycloud/privacy-banner/storefront-banner.js` with `async`, id `scb4127` | Shopify platform or Shopify privacy app/settings | Medium | Likely controlled by Shopify customer privacy/banner settings, not theme code. |
| 31 | `https://lynxtour.cn/cdn/shopifycloud/portable-wallets/latest/accelerated-checkout-backwards-compat.css` stylesheet | Shopify platform/payment integration | High | Shopify accelerated checkout/payment settings. Render-blocking stylesheet in head; do not remove in theme. |
| 32 | Inline accelerated checkout cart style block, id `shopify-accelerated-checkout-cart` | Shopify platform/payment integration | Medium | Shopify accelerated checkout/payment settings. |
| 33 | `window.performance.mark('shopify.content_for_header.end')` | Shopify platform | Low | Shopify controlled through `content_for_header`; do not edit or remove. |
| 34 | `https://cdn.tailwindcss.com` synchronous script | theme code | High | Theme code, but explicitly do not change in this branch. Must not be replaced with a stylesheet link. |
| 35 | `<link rel="preconnect" href="https://fonts.googleapis.com">` | theme code | Low | Theme code. Likely beneficial if Google Fonts remain. |
| 36 | `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` | theme code | Low | Theme code. Likely beneficial if Google Fonts remain. |
| 37 | Google Fonts stylesheet: `https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&family=Inter:wght@400;500;700&display=swap` | theme code plus Google Fonts | High | Theme code, but explicitly do not change in this branch. |
| 38 | Large inline global `<style>` block from `layout/theme.liquid` | theme code | Medium | Theme code. Any extraction requires selector inventory and visual testing. |
| 39 | Theme import map mapping `@google/genai` to `https://esm.sh/@google/genai@^1.38.0` | theme code plus third-party module CDN | Medium | Theme code. Audit usage first; do not change in this branch. |
| 40 | DNS prefetch: `https://monorail-edge.shopifysvc.com` | Shopify platform analytics | Low | Shopify platform analytics. |
| 41 | Inline Monorail beacon setup script | Shopify platform analytics | Low to medium | Shopify platform analytics. |
| 42 | Inline `window.__TREKKIE_SHIM_QUEUE` script | Shopify platform analytics | Low | Shopify platform analytics. |
| 43 | Inline `web-pixels-manager-setup` script | Shopify platform plus configured pixels | Medium | Shopify customer events/pixels admin. Theme should not edit this directly. |
| 44 | Inline `ShopifyAnalytics` metadata script | Shopify platform analytics | Low to medium | Shopify platform analytics. |
| 45 | Inline `<script class="analytics">` Shopify analytics loader | Shopify platform analytics | Medium | Shopify platform analytics and customer events settings. |
| 46 | `https://lynxtour.cn/cdn/shopifycloud/perf-kit/shopify-perf-kit-3.5.0.min.js` with `defer` | Shopify platform performance telemetry | Low to medium | Shopify platform. Not safely controlled from theme. |

## Theme Source Matches

| Rendered item | Theme source |
| --- | --- |
| Canonical link | `layout/theme.liquid:28` |
| Shopify CDN preconnect | `layout/theme.liquid:29` |
| Favicon and apple touch icon | `layout/theme.liquid:31-41` |
| SEO title/meta/OG/Twitter metadata | `layout/theme.liquid:295-321` |
| Organization/WebSite JSON-LD | `layout/theme.liquid:327-399` |
| `content_for_header` insertion point | `layout/theme.liquid:401` |
| Tailwind CDN script | `layout/theme.liquid:403` |
| Google Fonts preconnects | `layout/theme.liquid:404-405` |
| Global Google Fonts stylesheet | `layout/theme.liquid:406` |
| Inline global style block | `layout/theme.liquid:408-765` |
| Import map | `layout/theme.liquid:767-773` |

## Homepage Body Resource Note

The homepage template includes `sections/destinations.liquid` immediately after the hero. That section contains:

- `sections/destinations.liquid:2` Google Fonts preconnect to `fonts.googleapis.com`
- `sections/destinations.liquid:3` Google Fonts preconnect to `fonts.gstatic.com`
- `sections/destinations.liquid:4` Google Fonts stylesheet for `Cormorant Garamond` and `Montserrat`

These are not rendered inside the `<head>` snapshot, so they are not classified as head resources. They may still compete for network and font work during early homepage rendering and should be considered in a later font-consolidation audit. The current task forbids section changes.

## Highest-Risk Findings

1. Tailwind CDN script: `https://cdn.tailwindcss.com`
   - Owner: theme code.
   - Risk: high.
   - Reason: synchronous head script. It blocks parsing while it downloads and executes, then generates CSS client-side.
   - Control: theme code only, but do not change without a Tailwind usage inventory and visual regression plan.

2. Google Fonts stylesheet: `Noto Serif SC` and `Inter`
   - Owner: theme code plus Google Fonts.
   - Risk: high.
   - Reason: render-blocking stylesheet that triggers font-file discovery.
   - Control: theme code, but do not change until a conservative font-loading branch is approved.

3. Shopify accelerated checkout stylesheet
   - Owner: Shopify platform/payment integration.
   - Risk: high.
   - Reason: render-blocking stylesheet inside the head.
   - Control: likely Shopify accelerated checkout/payment settings, not safe to remove from theme.

4. Shopify captcha/bootstrap and dynamic checkout inline scripts
   - Owner: Shopify platform.
   - Risk: medium to high.
   - Reason: inline head JavaScript adds parse and execution work before the page reaches theme-owned Tailwind and font resources.
   - Control: Shopify/platform settings only. Do not edit `content_for_header`.

## Recommended Next Implementation Branch

Recommended next branch: Tailwind usage inventory plus a conservative theme-owned critical-path plan.

Suggested scope:

1. Do not edit production behavior yet.
2. Inventory Tailwind utility usage across `layout`, `sections`, `snippets`, and `templates`.
3. Identify which above-the-fold homepage elements depend on Tailwind.
4. Identify whether Tailwind CDN can later be replaced by a compiled, theme-owned build process or by a scoped extracted CSS plan.
5. Separately inventory font usage before making any Google Fonts change.
6. Keep Shopify `content_for_header` resources out of theme-code refactors; only document admin/app setting options if they are clearly available.

## Risky Changes To Avoid

- Do not remove or edit `{{ content_for_header }}`.
- Do not change Tailwind loading in this branch.
- Do not replace `https://cdn.tailwindcss.com` with a stylesheet link; it is a script workflow, not a CSS file.
- Do not change Google Fonts in this branch.
- Do not remove Shopify accelerated checkout, captcha, customer account, privacy banner, Web Pixels Manager, Monorail, or perf-kit scripts from theme code.
- Do not edit collection sections.
- Do not combine Tailwind, font, Shopify-injected resource, and analytics changes in one implementation branch.
- Do not change schema, URLs, handles, templates, app logic, checkout/payment behavior, or tracking logic as part of render-blocking cleanup.

## Audit Conclusion

The rendered production head confirms that the largest theme-controlled render-blocking candidates are still the synchronous Tailwind CDN script and the global Google Fonts stylesheet. The rendered head also contains significant Shopify platform output from `content_for_header`, including accelerated checkout CSS and multiple checkout, captcha, analytics, privacy, and pixel scripts. These Shopify-owned resources should not be edited in theme code. The safest next step is a Tailwind and font usage inventory, followed by one narrowly scoped implementation branch at a time.
