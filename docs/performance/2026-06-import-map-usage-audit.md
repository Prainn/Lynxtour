# Import Map Usage Audit

Date: 2026-06-09

Scope: Audit first. No production behavior, Liquid, CSS, JavaScript, schema, section, template, URL, handle, checkout, tracking, app logic, Tailwind, or Google Fonts changes were made.

## Current Lighthouse Mobile Metrics

| Metric | Current result after Phase 1 |
| --- | ---: |
| Performance | 73 |
| FCP | 4.1s |
| LCP | 4.4s |
| TBT | 160ms |
| Speed Index | 4.1s |
| CLS | 0 |

## Files Searched

Searched all theme source under:

- `layout/**/*.liquid`
- `sections/**/*.liquid`
- `snippets/**/*.liquid`
- `templates/**/*.json`
- `config/**/*.json`
- `locales/**/*.json`

Total files scanned in those areas: 107.

Search terms:

- `@google/genai`
- `importmap`
- `genai`
- `GoogleGenAI`
- `esm.sh`
- `type="module"`
- `import(`
- `from '`
- `from "`
- AI-related supporting terms including `AI`, `itinerary`, `generate`, `apiKey`, `api_key`, `GEMINI`, `OpenAI`, and `Google`

## Exact Matches Found

### Import Map And `@google/genai`

| Search term | Exact match |
| --- | --- |
| `importmap` | `layout/theme.liquid:767` contains `<script type="importmap">` |
| `@google/genai` | `layout/theme.liquid:770` maps `"@google/genai": "https://esm.sh/@google/genai@^1.38.0"` |
| `genai` | `layout/theme.liquid:770` only |
| `esm.sh` | `layout/theme.liquid:770` only |
| `GoogleGenAI` | No matches |

The only import map in the source is:

```liquid
<script type="importmap">
{
  "imports": {
    "@google/genai": "https://esm.sh/@google/genai@^1.38.0"
  }
}
</script>
```

### ES Module Syntax

| Search term | Result |
| --- | --- |
| `type="module"` | No theme-source matches |
| `import(` | No theme-source matches |
| `from "` | No theme-source matches |
| `from '` | No JavaScript module import matches. The only matches were Liquid copy strings using English text such as `Browse ... from ...`; these are false positives and not module imports. |

### AI-Related Functionality

| File | Exact match | Meaning |
| --- | --- | --- |
| `config/settings_schema.json:15-17` | `gemini_api_key`, label `Google Gemini API Key` | Theme setting for Gemini API key. |
| `config/settings_data.json:12` | `"gemini_api_key": ""` | Current setting value appears empty in the local theme config. |
| `sections/ai-contact-split.liquid:209` | `const API_KEY = {{ settings.gemini_api_key | json }};` | AI section reads the Gemini API key setting. |
| `sections/ai-contact-split.liquid:219` | `fetch(\`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}\`, ...)` | AI section calls the Gemini REST API directly with `fetch()`. |
| `sections/bespoke-travel.liquid:1199` | `endpoint: 'https://ai-server-n87x.onrender.com/api/generate'` | Bespoke AI planner calls a backend endpoint, not `@google/genai`. |
| `sections/bespoke-travel.liquid:1383` | `const res = await fetch(CONFIG.endpoint, { ... })` | Bespoke AI planner uses plain `fetch()` to the backend endpoint. |
| `templates/page.bespoke-travel.json:32` | `"type": "bespoke-travel"` | Public bespoke page uses the `bespoke-travel` section, which does not import `@google/genai`. |

## Is `@google/genai` Used?

No theme-source usage was found beyond the import map declaration itself.

There are no matching imports such as:

- `import { GoogleGenAI } from '@google/genai'`
- `import ... from '@google/genai'`
- `await import('@google/genai')`
- `GoogleGenAI`

The AI-related storefront code currently uses plain `fetch()`:

- `sections/bespoke-travel.liquid` posts to `https://ai-server-n87x.onrender.com/api/generate`.
- `sections/ai-contact-split.liquid` posts directly to the Gemini REST endpoint.

That means current AI behavior does not appear to depend on the import map.

## Is The Import Map Needed Globally?

No evidence was found that the import map is needed globally by public storefront theme code.

The import map lives in `layout/theme.liquid`, so it is emitted on every storefront page using the global layout. However, no public theme source searched in `layout`, `sections`, `snippets`, `templates`, `config`, or `locales` imports `@google/genai` or uses module import syntax that would consume this map.

Current assessment: globally unnecessary based on source search.

## Is The Import Map Needed On The Homepage?

No evidence was found that the homepage needs it.

The active homepage sections in `templates/index.json` are:

- `luxury-hero-header`
- `destinations`
- `brand-features`
- `testimonials`
- `footer`

None of those sections use `@google/genai`, `GoogleGenAI`, `type="module"`, `import(`, `esm.sh`, or direct module imports.

The homepage also does not include `sections/bespoke-travel.liquid` or `sections/ai-contact-split.liquid`.

Current assessment: not needed for homepage functionality.

## Does It Affect The Homepage Head?

Yes.

Because the import map is in `layout/theme.liquid`, it appears in the rendered homepage head. The previous rendered head inventory also found Shopify injecting an import-map polyfill script near the top of the head:

```html
<script async crossorigin fetchpriority="high" src="/cdn/shopifycloud/importmap-polyfill/es-modules-shim.2.4.0.js"></script>
```

The likely cause is the presence of `<script type="importmap">` in the theme. Even though the import map itself is inline and small, it appears to trigger an additional Shopify platform script in the rendered head. That polyfill has `async`, but it is still an extra high-priority head resource and network request on the homepage.

## AI Dependency Assessment

| Feature/file | Depends on import map? | Notes |
| --- | --- | --- |
| Homepage hero/header | No | No AI module usage. |
| Homepage destinations/brand/testimonials/footer | No | No AI module usage. |
| `bespoke-travel` page | No evidence | Uses backend endpoint via `fetch()`, not `@google/genai`. |
| `ai-contact-split` section | No evidence | Uses Gemini REST API via `fetch()`, not `@google/genai`. |
| Theme-wide JavaScript | No evidence | No `type="module"`, `import(`, `from "`, or valid `from '` module syntax found. |

## Risk Of Removing The Import Map

Risk rating: low, but should be implemented in a separate branch with live verification.

Why risk appears low:

- No source code imports `@google/genai`.
- No `GoogleGenAI` usage exists.
- AI features use direct REST calls or a backend endpoint.
- Homepage does not include the AI sections.
- The mapping is global despite no found consumer.

Residual risks:

- Shopify admin/customizer content or app-injected code outside the local theme could theoretically rely on a global import map, although no evidence was found in theme source.
- Removing the import map could change whether Shopify injects the import-map polyfill. That is desired for performance if unused, but it should be verified on the rendered homepage head.
- If unpublished or future theme code expects `@google/genai`, removal would break that future code unless it adds its own import strategy.

## Recommended Next Action

Do not remove it in this audit branch.

Recommended next implementation branch: remove only the unused import map from `layout/theme.liquid`, then verify rendered homepage head and AI-related pages.

Validation checklist for that branch:

1. Confirm `layout/theme.liquid` no longer emits `<script type="importmap">`.
2. Fetch rendered homepage head and confirm Shopify no longer injects `/cdn/shopifycloud/importmap-polyfill/es-modules-shim.2.4.0.js`, if that injection was caused only by the import map.
3. Re-test homepage visual rendering and navigation.
4. Re-test `/pages/bespoke-custom-travel` if available, especially instant planner behavior.
5. Confirm no console errors mentioning import maps, `@google/genai`, or `GoogleGenAI`.
6. Run Lighthouse mobile before/after and compare FCP, LCP, TBT, and Speed Index.

## Separate Implementation Prompt For Next Branch

```text
Implementation branch, single safe change only.

Remove the unused import map from layout/theme.liquid:
- the <script type="importmap"> block
- the @google/genai mapping to https://esm.sh/@google/genai@^1.38.0

Do not change Tailwind, Google Fonts, content_for_header, collection sections, schema, URLs, handles, checkout, tracking, app logic, or AI fetch behavior.

After removal:
1. Search again for @google/genai, importmap, genai, GoogleGenAI, esm.sh, type="module", import(, from ', and from ".
2. Fetch the rendered homepage head and confirm whether Shopify still injects the importmap polyfill.
3. Test homepage rendering and /pages/bespoke-custom-travel behavior.
4. Report changed files, old logic, new logic, rollback risk, and verification output.
```

## Risky Changes To Avoid

- Do not change Tailwind CDN loading.
- Do not change Google Fonts.
- Do not edit `{{ content_for_header }}`.
- Do not change Shopify-injected scripts, app scripts, checkout behavior, privacy banner, Web Pixels Manager, Monorail, or tracking logic.
- Do not edit collection sections.
- Do not edit schema, URLs, handles, canonical tags, robots, product booking UI, or variant logic.
- Do not change AI endpoint behavior in `sections/bespoke-travel.liquid`.
- Do not change direct Gemini REST behavior in `sections/ai-contact-split.liquid`.
- Do not bundle this with font optimization or Tailwind migration.

## Audit Conclusion

The import map in `layout/theme.liquid` appears unused by current public storefront code. No `@google/genai`, `GoogleGenAI`, dynamic import, static module import, or module script consumer was found outside the import map declaration itself. AI-related features use plain `fetch()` calls instead. The import map is not needed by the current homepage content, but because it is global it affects the homepage head and likely causes Shopify to inject an import-map polyfill. Removal appears low risk, but should be done in a separate implementation branch with rendered-head and AI-page verification.
