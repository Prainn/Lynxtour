# Render-Blocking Resource Audit

Date: 2026-06-09

Scope: Phase 2 audit only. No Liquid, section, JavaScript, CSS, schema, URL, handle, or collection-section changes were made.

## Current Lighthouse Mobile Metrics

| Metric | Current result after Phase 1 |
| --- | ---: |
| Performance | 73 |
| FCP | 4.1s |
| LCP | 4.4s |
| TBT | 160ms |
| Speed Index | 4.1s |
| CLS | 0 |

## Files Inspected

- `layout/theme.liquid`
- `templates/index.json`
- `sections/destinations.liquid`
- Repository-wide search across `layout`, `sections`, `snippets`, `templates`, and `config` for stylesheet links, Tailwind CDN usage, Google Fonts, synchronous external scripts, import maps, and Shopify asset stylesheet usage.

## Summary Findings

- Tailwind is currently loaded globally from `https://cdn.tailwindcss.com` in `layout/theme.liquid`.
- The Tailwind CDN resource is loaded as a synchronous `<script>`, not as a CSS stylesheet.
- Because the Tailwind script is unguarded in the global Shopify layout, it should be treated as production-loaded for all storefront page types that use `layout/theme.liquid`.
- Google Fonts are loaded globally from `fonts.googleapis.com` in the head.
- `layout/theme.liquid` does not currently link a global Shopify CSS asset through `asset_url` or `stylesheet_tag`.
- The theme has a large inline global `<style>` block in the head.
- `{{ content_for_header }}` appears before the Tailwind and Google Fonts resources. Its final output is Shopify-controlled and may include Shopify platform and app-injected head resources that are not visible as exact static source lines in this repository.
- The homepage includes `sections/destinations.liquid`, which adds another Google Fonts stylesheet inside a homepage section. It is not in `layout/theme.liquid`, but it is present on the current homepage route after the hero section.

## Exact Blocking Resources Found

| Location | Resource | Type | Blocking behavior | Risk to change |
| --- | --- | --- | --- | --- |
| `layout/theme.liquid:401` | `{{ content_for_header }}` | Shopify injected head output | Potentially injects Shopify/app scripts, styles, preload hints, analytics, or app bridge resources before first paint. Exact output must be checked on the rendered storefront because it is not fully represented in theme source. | Medium to high. Shopify relies on this tag; do not remove. App-level optimization should be done by disabling unnecessary apps or changing app settings, not by editing this tag. |
| `layout/theme.liquid:403` | `<script src="https://cdn.tailwindcss.com"></script>` | External synchronous script | Parser-blocking JavaScript in the head. The browser must fetch, parse, and execute it before continuing HTML parsing. Tailwind CDN also generates CSS in the browser, adding main-thread work before render stabilization. This can directly delay FCP and contribute to LCP delay. | High. Tailwind powers many existing utility classes. Do not remove in Phase 2 without a full CSS inventory and visual regression pass. Do not replace it with a stylesheet link to `cdn.tailwindcss.com`; this CDN endpoint is a script workflow, not a compiled CSS file. |
| `layout/theme.liquid:406` | `https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&family=Inter:wght@400;500;700&display=swap` | External CSS stylesheet | Stylesheets are render-blocking by default. This CSS must be downloaded and parsed, then it triggers additional font-file requests from `fonts.gstatic.com`. `display=swap` helps text paint with fallback fonts, but the stylesheet request itself still competes in the critical path. | Medium. Fonts shape the global brand look and Chinese/English typography. Changes are possible but need careful fallback, CLS, and visual checks. |
| `layout/theme.liquid:408-765` | Inline global `<style>` block | Inline CSS | Inline CSS does not require a network request, but it is still render-blocking because the browser must parse it before constructing the CSSOM. The block is large and global, so it adds head parse cost before first paint. | Medium. It appears to provide shared Lynx UI tokens, CTA/card utilities, focus states, body font, and prose styling. Splitting or deferring incorrectly could cause flash of unstyled content or broken above-the-fold styles. |
| `layout/theme.liquid:767-773` | `<script type="importmap">` mapping `@google/genai` to `https://esm.sh/@google/genai@^1.38.0` | Inline import map | Import maps are parsed in the head and must be available before module scripts that use them. This block has no network fetch by itself, but it adds head work and references a third-party module URL for later use. It is not likely the primary FCP/LCP blocker compared with Tailwind and Google Fonts. | Low to medium. If no storefront module imports `@google/genai`, removal or route-scoping may be possible later, but first confirm all AI-related sections and scripts. |
| `sections/destinations.liquid:2-4` | Google Fonts preconnect plus `Cormorant Garamond` and `Montserrat` stylesheet | Section-level external CSS stylesheet | This is not in `layout/theme.liquid`, but the homepage uses the `destinations` section after the hero. The stylesheet can still compete for network and font resources during early page load and may delay rendering of subsequent homepage content. | Medium. This is section-scoped typography. Do not change in this audit branch. Any implementation should be homepage-tested and avoid collection-section edits. |

## Non-Blocking Or Lower-Priority Head Items

- `layout/theme.liquid:29` preconnect to `https://cdn.shopify.com` is not render-blocking. It is likely helpful for Shopify-hosted assets.
- `layout/theme.liquid:404-405` preconnects to `fonts.googleapis.com` and `fonts.gstatic.com` are not render-blocking. They are hints that can reduce connection setup cost for the blocking Google Fonts stylesheet.
- `layout/theme.liquid:327-399` JSON-LD is inline structured data. It has parse cost but no external network dependency and is not a normal render-blocking stylesheet or executable script.
- `snippets/ga4-custom-events` is rendered near the end of `body` after `content_for_layout`, so it is not a head render blocker from `theme.liquid`.

## Why These Resources Affect FCP And LCP

FCP and LCP are currently close together at 4.1s and 4.4s, which suggests the first meaningful paint and the final hero paint are both constrained by early critical-path work. After Phase 1 improved the hero image LCP path, the next likely bottlenecks are head resources that delay parsing, CSSOM construction, font discovery, or main-thread availability.

The Tailwind CDN script is the highest-priority finding because it is a synchronous third-party script in the head. Unlike a stylesheet, it executes JavaScript before the parser can continue. It also generates CSS client-side, so it can affect both network timing and CPU timing before the page has a stable render tree.

The global Google Fonts stylesheet is the second highest-priority finding. CSS stylesheets block rendering until the CSSOM can be built. Even with `display=swap`, the browser still needs the Google Fonts CSS response to know which font files to request.

The inline global style block is not a network problem, but it is still critical-path CSS. Its risk is mostly parse size and maintainability rather than external latency.

## Recommended Phase 2 Implementation Plan

1. Capture rendered production head output first.
   - Use the live storefront HTML or a Shopify preview URL to record the actual output around `{{ content_for_header }}`.
   - Identify app-injected scripts/styles that appear before Tailwind and Google Fonts.
   - Do not edit `content_for_header`; use app settings or app removal only if an app resource is confirmed unnecessary.

2. Audit Tailwind class usage before changing Tailwind loading.
   - Build an inventory of Tailwind utility classes used across `layout`, `sections`, `snippets`, and `templates`.
   - Confirm whether Tailwind CDN is required globally or only for legacy sections.
   - If moving away from CDN later, use a compiled Tailwind build or extracted critical CSS plan. Do not replace `https://cdn.tailwindcss.com` with a stylesheet link.

3. Test a conservative font-loading branch.
   - Keep visual fallbacks stable.
   - Consider reducing global font families/weights if unused above the fold.
   - Consider route-scoping or consolidating duplicate Google Fonts where safe.
   - Measure FCP, LCP, CLS, and visual font shifts before and after.

4. Review inline global CSS for above-the-fold criticality.
   - Separate truly critical global tokens and above-the-fold hero/navigation styles from lower-priority shared utilities only after a selector usage audit.
   - Avoid broad restyling. Any extraction should preserve existing selectors and section schema.

5. Verify each change independently.
   - One implementation branch per resource class: Tailwind, fonts, injected third-party/app scripts, inline CSS.
   - Run Lighthouse mobile after each branch so the source of improvement is measurable.

## Safe Quick Wins For A Future Branch

- Add a rendered-head audit artifact before implementation so Shopify/app-injected blockers are visible.
- Confirm whether the `@google/genai` import map is used on public storefront pages; route-scope or remove only if unused.
- Consolidate duplicate Google Fonts only where the same page loads multiple Google Fonts stylesheets and visual output is confirmed unchanged.
- Keep existing preconnects for Shopify CDN and Google Fonts unless measurement proves they are harmful.
- Document Tailwind utility coverage before attempting any loading change.

## Risky Changes To Avoid

- Do not remove Tailwind globally without a complete class inventory and visual regression pass.
- Do not replace `<script src="https://cdn.tailwindcss.com"></script>` with `<link rel="stylesheet" href="https://cdn.tailwindcss.com">`; that endpoint is not a production CSS file.
- Do not remove `{{ content_for_header }}`.
- Do not edit collection sections as part of this performance phase.
- Do not combine Tailwind, font, app-script, and inline-CSS changes in one broad branch.
- Do not change Shopify section schema, template names, URLs, handles, canonical tags, robots directives, booking UI, or product variant logic while testing render-blocking changes.

## Suggested Codex Prompts For Next Implementation Branch

### Prompt 1: Rendered Head Inventory

```text
Phase 2 implementation prep only. Do not change Liquid yet.

Fetch or capture the rendered Shopify homepage HTML head for Lynxtour and compare it with layout/theme.liquid. Identify every stylesheet, synchronous script, app-injected resource, and third-party request before first paint. Create docs/performance/2026-06-rendered-head-inventory.md with exact resources, source owner, blocking risk, and whether the resource is controlled by theme code, Shopify, or an app.
```

### Prompt 2: Tailwind Usage Inventory

```text
Audit only. Do not remove Tailwind and do not replace cdn.tailwindcss.com with a stylesheet link.

Inventory Tailwind utility class usage across layout, sections, snippets, and templates. Identify which homepage above-the-fold elements depend on Tailwind, which sections appear to rely heavily on Tailwind, and whether a future compiled Tailwind build would be feasible. Write the findings to docs/performance/2026-06-tailwind-usage-inventory.md.
```

### Prompt 3: Conservative Font Optimization Branch

```text
Implementation branch, conservative changes only.

Inspect global and homepage Google Fonts usage. Propose the smallest safe change to reduce render-blocking font CSS without changing visual identity. Do not touch collection sections. Do not change Tailwind. Make one focused change, then report changed files, old logic, new logic, rollback risk, and Lighthouse metrics to re-check.
```

### Prompt 4: Import Map Scope Check

```text
Audit first, implementation only if clearly unused.

Find all uses of @google/genai and the import map in the Shopify theme. Determine whether the import map in layout/theme.liquid is needed on the public homepage. If unused globally, propose a route-scoped or section-scoped alternative with no behavior change. Do not implement until the usage audit is complete.
```

## Phase 2 Priority Recommendation

Highest priority for the next implementation branch: rendered production head inventory, then Tailwind usage inventory. The Tailwind CDN script is the largest obvious head blocker, but it is also the riskiest to change because it likely supports broad utility-class styling across the theme. Font optimization is likely safer than Tailwind removal, but it should still be measured separately because global typography is brand-sensitive and can affect CLS if handled poorly.
