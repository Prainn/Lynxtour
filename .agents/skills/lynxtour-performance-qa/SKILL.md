---
name: lynxtour-performance-qa
description: Use to audit Lynxtour Shopify Liquid pages for Core Web Vitals, mobile UX, layout shift, image loading, unused CSS/JS, and accessibility risks.
---

Goal:
Find performance and UX issues before publishing Shopify theme changes.

Check:
- LCP image candidates
- hero image size and loading priority
- lazy loading
- CLS from images, accordions, sticky header, product forms, footer
- unused global CSS/JS
- duplicate scripts
- mobile navigation risk
- button and link accessibility
- image alt text
- form usability
- Core Web Vitals risk

Rules:
- No redesign.
- Recommend minimal Liquid/CSS changes.
- Do not remove scripts unless the dependency is confirmed.
- Prefer safe, reversible changes.
- Explain user impact and SEO impact.

Output:
- Page/template inspected
- P0/P1/P2 issues
- Recommended fixes
- Files likely affected
- Testing checklist
