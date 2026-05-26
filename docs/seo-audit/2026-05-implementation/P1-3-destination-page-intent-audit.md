# P1-3 Destination Page Intent Audit

Date: 2026-05-26

Scope: `/pages/kunming`, `/pages/dali`, `/pages/lijiang`, `/pages/shangri-la`, `/pages/xishuangbanna`.

Files inspected:
- `layout/theme.liquid`
- `templates/page.kunming.json`
- `templates/page.dali.json`
- `templates/page.lijiang.json`
- `templates/page.shangri-la.json`
- `templates/page.xishuangbanna.json`
- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`

## Shared SEO Implementation Notes

Title and meta descriptions for these destination pages are controlled in code by the handle-scoped `request.page_type == 'page'` case statement in `layout/theme.liquid`. No Shopify admin SEO field changes are required for the five target pages in this pass.

Canonical, robots, OG/Twitter tags, FAQ JSON-LD, breadcrumb JSON-LD, GA4/GTM code, product booking logic, price logic, template names, section names, URLs, handles, and redirects were not changed.

## /pages/kunming

- Current title/meta source: `layout/theme.liquid`, page handle `kunming`.
- Previous title/meta: `Kunming Yunnan Travel Guide: Things to Do & Itinerary`; `Plan your Kunming Yunnan trip with Stone Forest, Dianchi Lake, Green Lake, flower markets, city walks, day trips and private tour options.`
- Current visible H1/hero heading: `Kunming Travel Guide`.
- Current primary CTA and secondary CTA: previously `VIEW PRIVATE TOURS` to `/collections/yunnan-private-tours` and `CONTACT US` to `/pages/contact-us`; patched to `COMPARE KUNMING DAY TRIPS` to `/collections/yunnan-private-day-trips` and `PLAN A CUSTOM YUNNAN ROUTE` to `/pages/bespoke-custom-travel`.
- Current internal links: Kunming day tour products, `/collections/yunnan-private-tours`, `/collections/yunnan-private-day-trips`, `/products/yunnan-private-car-charter-tour`, `/pages/bespoke-custom-travel`, Dianchi Lake guide, Stone Forest guide, `/pages/dali`, and `/pages/lijiang`.
- Destination intent mismatch: SEO title/meta were guide-focused but less aligned to the requested "things to do / private tour planning" phrase cluster.
- Commercial routing gap: CTA favored broad Yunnan private tours over the more intent-matched day-trip collection and bespoke planning path.
- Recommended patch: update handle-scoped SEO strings, route primary CTA to Kunming-relevant day trips, and route secondary CTA to bespoke planning.
- Patch status: done in code.
- Rollback risk: low. The patch changes only page-handle SEO strings and existing JSON CTA settings.

## /pages/dali

- Current title/meta source: `layout/theme.liquid`, page handle `dali`.
- Previous title/meta: `Dali Yunnan Guide: Things to Do, Erhai & Itinerary`; `Plan your Dali Yunnan trip with Erhai Lake, Dali Old Town, Xizhou, Cangshan, best seasons, itinerary ideas, and private tour options.`
- Current visible H1/hero heading: `Dali Travel Guide`.
- Current primary CTA and secondary CTA: `See Dali Private Tours` to `/collections/dali-private-tours`; secondary CTA was blank in the rendered CTA settings and is now `Plan a Custom Dali Route` to `/pages/bespoke-custom-travel`.
- Current internal links: `/collections/dali-private-tours`, `/pages/dali-itinerary-2-days`, `/pages/dali-itinerary-3-days`, `/pages/dali-to-lijiang-private-tour`, `/collections/yunnan-private-tours`, and related multi-day product links.
- Destination intent mismatch: title/meta were close, but the title did not include "private tours" and the meta did not clearly mention the Kunming-Lijiang corridor.
- Commercial routing gap: CTA did not expose bespoke planning even though route planning intent often needs customization.
- Recommended patch: update handle-scoped SEO strings and add a secondary CTA to bespoke Dali route planning.
- Patch status: done in code.
- Rollback risk: low. Existing section settings were updated without layout or schema changes.

## /pages/lijiang

- Current title/meta source: `layout/theme.liquid`, page handle `lijiang`.
- Previous title/meta: `Lijiang Travel Guide: Best Time, Itinerary & Top Things to Do | Lynxtour`; `Plan your Lijiang trip with advice on the best time to visit, how many days to stay, top attractions, and how to combine Lijiang with Shangri-La or Dali.`
- Current visible H1/hero heading: `Lijiang Travel Guide`.
- Current primary CTA and secondary CTA: `Browse Lijiang Private Tours` to `/collections/lijiang-private-tours`; `Plan a Custom Itinerary` to `/pages/bespoke-custom-travel`.
- Current internal links: `/collections/lijiang-private-tours`, `/products/jade-dragon-snow-mountain-private-tour`, `/pages/lijiang-itinerary-2-days`, `/pages/lijiang-itinerary-3-days`, `/pages/tiger-leaping-gorge-from-lijiang`, `/products/lijiang-to-shangri-la-private-tour`, and related multi-day products.
- Destination intent mismatch: SEO title/meta underweighted Jade Dragon Snow Mountain and private tours compared with the target intent.
- Commercial routing gap: no material gap; existing page-specific route block already covers the requested commercial paths.
- Recommended patch: update handle-scoped SEO strings only.
- Patch status: done in code.
- Rollback risk: very low. No template or section content changed for Lijiang.

## /pages/shangri-la

- Current title/meta source: `layout/theme.liquid`, page handle `shangri-la`.
- Previous title/meta: `Shangri-La Yunnan Travel Guide: Things to Do & Itinerary`; `Plan a Shangri-La Yunnan trip with top things to do, best seasons, altitude tips, itinerary ideas, and private route options from Lijiang.`
- Current visible H1/hero heading: `Shangri-La Travel Guide`.
- Current primary CTA and secondary CTA: `Browse Shangri-La private tours` to `/collections/shangri-la-private-tours`; secondary was `CUSTOM TRIP REQUEST` to `/pages/contact-us` and is now `Plan a Custom Highland Route` to `/pages/bespoke-custom-travel`.
- Current internal links: `/collections/shangri-la-private-tours`, `/products/lijiang-to-shangri-la-private-tour`, `/collections/yunnan-private-tours`, `/pages/tiger-leaping-gorge-from-lijiang`, and related multi-day/highland products.
- Destination intent mismatch: title/meta were close but did not foreground "Highland Route & Private Tours."
- Commercial routing gap: secondary CTA used the generic contact page instead of the bespoke planning page.
- Recommended patch: update handle-scoped SEO strings and route the secondary CTA to bespoke planning with destination-specific language.
- Patch status: done in code.
- Rollback risk: low. Existing CTA settings changed only URL/label copy.

## /pages/xishuangbanna

- Current title/meta source: `layout/theme.liquid`, page handle `xishuangbanna`.
- Previous title/meta: title override only, `Xishuangbanna Travel Guide: Best Time, Itinerary Ideas & Top Things to Do | Lynxtour`; meta description fell back outside this handle override.
- Current visible H1/hero heading: `Xishuangbanna Travel Guide`.
- Current primary CTA and secondary CTA: previously `Browse Xishuangbanna private tours` to `/collections/xishuangbanna-private-tours` and `CONTACT US` to `/pages/contact-us`; patched to `Browse Yunnan Private Tours` to `/collections/yunnan-private-tours` and `Plan a Custom Tropical Route` to `/pages/bespoke-custom-travel`.
- Current internal links: `/collections/yunnan-private-tours`, `/collections/xishuangbanna-private-tours`, `/products/yunnan-private-car-charter-tour`, `/pages/bespoke-custom-travel`, related guide links, related product links, and bespoke planning.
- Destination intent mismatch: SEO title was broad and no handle-specific meta description existed.
- Commercial routing gap: requested routing included broader Yunnan private tours, bespoke planning, and car charter, while the existing route block used a generic travel-guides link.
- Recommended patch: add handle-scoped meta description, align title with tropical private planning, route the CTA to broader Yunnan private tours, use bespoke planning for secondary CTA, and replace the generic guide route card with private car charter.
- Patch status: done in code.
- Rollback risk: low to moderate. The section edit is page-specific and only changes one existing route card's copy/link; no layout, schema, or JSON-LD was changed.
