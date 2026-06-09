# Tailwind Usage Inventory

Date: 2026-06-09

Scope: Audit only. No production behavior, Liquid, CSS, JavaScript, schema, section, template, URL, handle, Google Fonts, Tailwind loading, or app logic changes were made.

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

Searched these theme areas:

- `layout/**/*.liquid`
- `sections/**/*.liquid`
- `snippets/**/*.liquid`
- `templates/**/*.json`
- `config/**/*.json`

Inventory coverage:

| Area | Files inspected | Tailwind-style usage found |
| --- | ---: | --- |
| `layout` | 2 | Yes, global body and skip-link utilities in `layout/theme.liquid`; Tailwind CDN script in `layout/theme.liquid`. |
| `sections` | 50 | Yes, concentrated in a few older/utility-heavy sections. |
| `snippets` | 8 | No meaningful Tailwind dependency found in the class-token scan. |
| `templates` | 42 | No meaningful direct Tailwind dependency found in JSON templates; dependency comes through assigned sections. |
| `config` | 2 | No meaningful Tailwind dependency found. |

Search method: scanned `class="..."` tokens and counted Tailwind-like utility patterns including color, spacing, layout, typography, border, radius, shadow, responsive prefixes, hover/focus variants, and common utility tokens such as `sr-only` and `prose`.

## Is Tailwind CDN Globally Required?

Yes, Tailwind currently appears globally required in practical terms.

The only Tailwind CDN reference found is in `layout/theme.liquid`:

```liquid
<script src="https://cdn.tailwindcss.com"></script>
```

Because this script is in the global layout head, it loads on every storefront page that uses `layout/theme.liquid`. The current theme also uses Tailwind utilities outside any single optional page, including:

- `layout/theme.liquid`: body classes `bg-stone-900 text-stone-300`.
- `layout/theme.liquid`: skip link class `sr-only`.
- Several sections with extensive utility composition, especially form and about pages.

Removing Tailwind globally would therefore risk immediate visual and accessibility regressions unless those utility classes are replaced by local CSS or a compiled Tailwind asset first.

## Homepage Above-The-Fold Tailwind Dependency

The active homepage order in `templates/index.json` is:

1. `header` section, disabled.
2. `luxury-hero-header` section, active above the fold.
3. `destinations`
4. `brand-features`
5. `testimonials`
6. `footer`

### Nav/Header

Active homepage nav/header: `sections/luxury-hero-header.liquid`.

Dependency level: low.

The active header/navigation is mostly custom CSS with classes such as `main-nav-bar`, `header-container`, `flex-layout`, `desktop-nav`, `nav-item`, `mobile-drawer`, and `mega-menu`. It does use shared `lynx-*` helpers in the hero area, but those helpers are defined in the inline global style block in `layout/theme.liquid`, not by Tailwind.

Inactive alternate header: `sections/header.liquid`.

Dependency level: medium if enabled.

The disabled `header` section contains Tailwind utilities in the slogan bar, including `relative`, `overflow-hidden`, `bg-stone-950`, `absolute`, `inset-0`, `bg-gradient-to-r`, `py-2`, `text-center`, `text-[10px]`, `md:text-xs`, `font-medium`, `tracking-[0.3em]`, `uppercase`, `italic`, `text-amber-500/90`, `font-sans`, and `m-0`.

### Hero Content

Active homepage hero: `sections/luxury-hero-header.liquid`.

Dependency level: low.

The hero image, overlay, H1, subtitle, intro copy, scroll guide, and layout are covered by custom section CSS: `hero-section`, `hero-bg-container`, `hero-bg-image`, `hero-overlay`, `hero-content`, `hero-title`, `hero-subtitle`, `hero-brand-intro`, and related selectors.

The hero content also uses `lynx-container` and `lynx-readable`, which are defined in `layout/theme.liquid` inline global CSS.

### Buttons

Dependency level: low for the active homepage hero.

Hero buttons use custom classes `hero-btn`, `hero-btn-primary`, and `hero-btn-secondary`. These styles are defined inside `sections/luxury-hero-header.liquid`, with focus-visible support also referenced in the global inline style block.

### Layout Utilities

Dependency level: medium globally, low inside active hero/header.

The active homepage hero/header relies on custom layout CSS. However, the global `<body>` depends on Tailwind for `bg-stone-900 text-stone-300`, and the skip link depends on `sr-only`. Those are global layout utilities and would break if Tailwind were removed without replacement.

### Typography Utilities

Dependency level: medium globally.

The active homepage hero uses custom typography classes and global font declarations. Elsewhere, Tailwind typography utilities are common: `uppercase`, `text-[9px]`, `text-[10px]`, `text-white`, `font-light`, `font-bold`, `font-serif`, `tracking-[0.2em]`, `tracking-[0.3em]`, `tracking-[0.4em]`, and `leading-*`.

### Spacing Utilities

Dependency level: medium globally.

The active homepage hero/header mostly uses custom CSS spacing. Older sections and forms rely heavily on Tailwind spacing utilities including `p-3`, `p-8`, `px-6`, `py-2`, `py-4`, `mb-3`, `mb-4`, `mb-8`, `mt-4`, `gap-3`, `gap-4`, and `gap-8`.

## Most Common Tailwind Utilities Found

Approximate counts from class-token scan:

| Utility | Count |
| --- | ---: |
| `uppercase` | 47 |
| `w-full` | 37 |
| `border` | 34 |
| `text-[9px]` | 29 |
| `flex` | 29 |
| `block` | 27 |
| `text-stone-500` | 22 |
| `font-light` | 20 |
| `tracking-[0.2em]` | 20 |
| `border-stone-800` | 20 |
| `bg-transparent` | 18 |
| `border-b` | 18 |
| `relative` | 18 |
| `text-white` | 17 |
| `text-[10px]` | 16 |
| `rounded-sm` | 16 |
| `text-stone-300` | 15 |
| `items-center` | 14 |
| `text-center` | 14 |
| `focus:border-amber-500/50` | 14 |
| `p-3` | 13 |
| `bg-stone-700` | 13 |
| `transition-all` | 13 |
| `border-stone-600` | 13 |
| `text-stone-200` | 13 |
| `transition-colors` | 13 |
| `mx-auto` | 12 |
| `mb-3` | 11 |
| `tracking-widest` | 11 |
| `border-white/[0.05]` | 10 |

Common patterns:

- Color system: `stone`, `amber`, `white`, `red`, plus opacity modifiers.
- Layout: `flex`, `grid`, `items-center`, `justify-center`, `relative`, `absolute`, `inset-0`.
- Spacing: `p-*`, `px-*`, `py-*`, `mb-*`, `mt-*`, `gap-*`.
- Forms: `border-b`, `bg-transparent`, `focus:border-*`, `focus:ring-*`.
- Typography: `uppercase`, bracketed text sizes, tracking utilities, `font-light`, `font-serif`, `font-mono`.
- Effects: `transition-all`, `transition-colors`, `shadow-2xl`, `rounded-sm`, `rounded-full`.

## High-Dependency Files And Sections

| File | Approximate utility tokens | Dependency level | Notes |
| --- | ---: | --- | --- |
| `sections/bespoke-travel.liquid` | 395 | High | AI/planner form layout, inputs, tags, panels, buttons, status/result areas, spacing, borders, and typography depend heavily on Tailwind utilities. |
| `sections/customization-form.liquid` | 267 | High | Form structure, grid layout, fields, buttons, hidden/result states, `prose`, and responsive columns depend heavily on Tailwind utilities. |
| `sections/ai-contact-split.liquid` | 266 | High | Split layout, form controls, buttons, notification panel, loading state, and responsive layout use many utilities. |
| `sections/about-us.liquid` | 231 | High | Page structure, Swiper wrappers, image sizing, positioning, typography, spacing, overlays, and responsive behavior are mostly utility-driven. |
| `sections/anchor-nav.liquid` | 26 | Medium | Sticky anchor nav depends on Tailwind for positioning, spacing, overflow, colors, and hover states. |
| `sections/header.liquid` | 17 | Medium if enabled | Disabled on current homepage, but its slogan bar uses Tailwind utilities. |
| `layout/theme.liquid` | 3 | Medium globally | Only a few utilities, but they are global: body background/text color and `sr-only`. |
| `sections/product-reviews.liquid` | 1 | Low | Mostly custom CSS; negligible utility dependency. |

## Sections Or Pages Likely To Break If Tailwind CDN Is Removed

High breakage risk:

- Pages using `sections/bespoke-travel.liquid`.
- Pages using `sections/customization-form.liquid`.
- Pages using `sections/ai-contact-split.liquid`.
- Pages using `sections/about-us.liquid`.

Medium breakage risk:

- Pages using `sections/anchor-nav.liquid`.
- Any page where the disabled `sections/header.liquid` is re-enabled.
- All pages using `layout/theme.liquid` because body colors and the skip link rely on Tailwind utilities.

Lower breakage risk:

- Active homepage hero/header in `sections/luxury-hero-header.liquid`, because most above-the-fold styles are custom CSS.
- Active homepage destinations and brand sections, because they are mostly custom CSS plus `lynx-*` helpers already defined in global inline CSS.

## Inline Global CSS That Already Reduces Tailwind Dependency

`layout/theme.liquid` already includes a broad inline global style block that duplicates or partially replaces common Tailwind roles:

- `body { font-family: 'Inter', sans-serif; }`
- `.font-noto-serif-sc` covers the custom font-family role for Chinese serif text.
- `.prose h3`, `.prose p`, `.prose li` partially cover typography behavior for content rendered inside `.prose`.
- `.lynx-btn`, `.lynx-btn--primary`, `.lynx-btn--secondary`, and `.lynx-text-cta` cover button display, alignment, padding, radius, weight, uppercase, transitions, hover states, disabled states, and focus-visible states.
- `.lynx-card`, `.lynx-card--soft`, `.lynx-card--image`, `.lynx-card__media`, `.lynx-card__content`, `.lynx-card__title`, `.lynx-card__text`, `.lynx-card__meta`, and `.lynx-card__tag` cover card surfaces, borders, radius, shadow, overflow, media sizing, typography, and tags.
- `.lynx-section`, `.lynx-container`, `.lynx-readable`, `.lynx-section-header`, `.lynx-eyebrow`, `.lynx-section-title`, `.lynx-section-text`, and `.lynx-rich-text` cover common section spacing, max-width containers, readable text widths, centered headers, muted text, uppercase labels, and rhythm.

Gaps if Tailwind were removed:

- No global replacement for `bg-stone-900` or `text-stone-300` on `<body>`.
- No global replacement for `sr-only`.
- No comprehensive replacement for high-use Tailwind utilities in form-heavy sections.
- No compiled set of responsive variants such as `md:*`, `lg:*`, bracketed arbitrary values, opacity colors, or focus/hover variants.

## Migration Options

| Option | Description | Risk rating | Notes |
| --- | --- | --- | --- |
| Option A | Keep Tailwind CDN temporarily and optimize safer non-Tailwind blockers first, such as Google Fonts strategy or import-map usage audit. | Low | Safest short-term path. Does not reduce the synchronous Tailwind script cost yet, but avoids breaking utility-heavy pages. |
| Option B | Compile Tailwind into a local Shopify asset later. | Medium | Best long-term path if the theme will keep Tailwind utilities. Requires build setup, content scanning for Liquid/JSON, safelisting dynamic/arbitrary classes, asset inclusion strategy, and visual regression testing. |
| Option C | Extract only homepage critical utilities as a transitional step. | Medium to high | Could reduce homepage dependence, but the global Tailwind script cannot be removed unless all other pages/sections are protected. Risk of duplicating utilities inconsistently and missing state/responsive variants. |

## Recommended Safe Migration Path

1. Keep Tailwind CDN for now.
2. Optimize or audit safer high-risk blockers first:
   - Google Fonts loading strategy.
   - Import map and `@google/genai` usage.
   - Shopify/app resources only through settings or documentation, not theme removal.
3. Create a Tailwind build feasibility branch:
   - Add no production behavior initially.
   - Inventory all utility tokens, including arbitrary values and responsive/hover/focus variants.
   - Identify dynamic classes that need safelisting.
   - Confirm which pages use `bespoke-travel`, `customization-form`, `ai-contact-split`, and `about-us`.
4. If proceeding, compile Tailwind into a local Shopify asset in a separate branch.
5. Only after visual regression testing should the CDN script be considered for removal.

## Suggested Next Implementation Branch

Recommended next branch: import-map usage audit or conservative Google Fonts optimization, not Tailwind removal.

Reason: Tailwind removal has high page-break risk because high-dependency sections still exist. The current homepage above-the-fold area is mostly custom CSS, but the global layout and several pages remain utility-dependent. A safer performance branch can target font loading or unused import-map behavior first while Tailwind build planning continues separately.

Suggested prompt:

```text
Audit first, implementation only if clearly safe.

Find all uses of @google/genai and the import map in the Shopify theme. Determine whether the import map in layout/theme.liquid is needed on the public homepage. Do not change Tailwind, Google Fonts, collection sections, schema, templates, URLs, handles, or app logic. If unused globally, create a docs-only implementation recommendation with rollback risk.
```

## Risky Changes To Avoid

- Do not remove Tailwind CDN globally.
- Do not replace `https://cdn.tailwindcss.com` with a stylesheet link.
- Do not create a Tailwind build in this audit branch.
- Do not change `layout/theme.liquid` in this audit branch.
- Do not change Google Fonts in this audit branch.
- Do not edit collection sections.
- Do not assume the active homepage hero/header proves Tailwind is safe to remove; other sections remain high dependency.
- Do not remove `sr-only` behavior without replacing it with accessible hidden-text CSS.
- Do not remove global body color utilities without replacing body background and text color.
- Do not combine Tailwind migration with Shopify `content_for_header`, app, analytics, checkout, or pixel changes.

## Audit Conclusion

Tailwind CDN is globally loaded and still practically required by the current theme. The active homepage above-the-fold hero/header has low direct Tailwind dependency because it is mostly custom CSS, but the global layout and several form/about sections depend heavily on Tailwind utilities. The safest Phase 2 path is to keep Tailwind CDN temporarily, optimize lower-risk blockers first, and plan a separate compiled Tailwind asset branch with full utility inventory and visual regression coverage.
