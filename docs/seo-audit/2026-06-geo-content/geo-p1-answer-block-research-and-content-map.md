# GEO P1 Answer Block Research and Content Map

Date: 2026-06-04
Branch: `docs/geo-p1-answer-block-research`
Brand spelling: `Lynxtour`

## Scope

This is a documentation-only plan for visible GEO-friendly answer blocks. Schema work is already complete; this phase is about concise on-page content that helps real travelers and can also be extracted cleanly by AI answer systems.

No Liquid code, templates, sections, snippets, JSON-LD, schema, CSS, JavaScript, product prices, forms, cart, checkout, URLs, handles, or existing content files should be changed in this documentation phase.

## Research Basis

Competitor pages for "Yunnan private tour" commonly answer:

- Route duration.
- Destination sequence.
- Tour cost and inclusions.
- Tailor-made/private tour positioning.
- Tour type segmentation.
- Route categories such as classic, in-depth, Muslim-friendly, family, cycling, overland, and long routes.

Forum and community questions commonly ask:

- How many days are needed in Yunnan.
- Whether 10 or 14 days is too long.
- Whether to add Lugu Lake or Shangri-La.
- Dali vs Lijiang and how to split time.
- Private tour vs self-guided travel.
- Whether foreigners need a guide.
- Family, kids, and senior pacing.
- Altitude and Shangri-La/Meili planning.
- Reliability, hidden fees, forced shopping, and guide quality.

Current Lynxtour site findings:

- The Yunnan Private Tours collection already has route length, starting point, private vs group, and FAQ sections.
- The 8-Day product page already has best-for, 8 vs 6 days, customization, season, and FAQ content, but it should be summarized higher as a compact planning snapshot.
- Destination pages already use "Know at a Glance" style content and should be refined rather than duplicated.
- The Stone Forest article already has strong practical guide content and needs a top Quick Answer summary.
- The Dianchi article should get a concise top Quick Answer block.

## Shared Implementation Guardrails

- Do not add schema.
- Do not hide text.
- Do not keyword-stuff.
- Do not duplicate FAQ content.
- Do not add more than one compact answer block per page.
- Keep the content useful for real travelers, not just AI systems.
- Keep copy concise and visible.
- Prefer refining existing blocks where the page already has the right content pattern.
- Keep all internal links to existing URLs only.

## P1 Content Map

### 1. `/collections/yunnan-private-tours`

Current content already present:

- Route length guidance.
- Starting point guidance.
- Private vs group positioning.
- Existing FAQ sections.
- Internal links to destination pages, private tour products, day trips, bespoke planning, and travel guides.

User questions it should answer:

- How many days do I need for a Yunnan private tour?
- Which route should I choose if I have 6, 8, 10, or 14 days?
- Should I choose Kunming-Dali-Lijiang only, or add Shangri-La?
- Is this private and tailor-made, or a group tour?
- What route type fits families, seniors, Muslim travelers, cyclists, or longer overland trips?

Add or refine:

- Refine an existing block.

Recommended block name:

- `Yunnan Private Tour Route Comparison`

Recommended placement:

- In the existing route-length/planning area, above product cards if possible, or directly before the existing route-length explanation if the product list must stay first.

Fields to include:

- Days available.
- Best route type.
- Typical destination sequence.
- Best for.
- Planning note.

Draft English copy:

| Days | Best route type | Typical destination sequence | Best for | Planning note |
| --- | --- | --- | --- | --- |
| 5-6 days | Classic short route | Kunming, Dali, Lijiang | First-time travelers with limited time | Keep the route focused and avoid long highland detours. |
| 8 days | Classic Yunnan private tour | Kunming, Dali, Lijiang, Shangri-La | First-time travelers who want the main highlights | This is the most balanced route for scenery, culture, and pace. |
| 10-12 days | In-depth or family-paced route | Kunming, Dali, Lijiang, Shangri-La, plus a slower stay or side trip | Families, seniors, photographers, and travelers who dislike rushing | Add buffer time for Old Town walks, lake scenery, and mountain weather. |
| 14+ days | Long Yunnan or overland route | Main Yunnan highlights plus Lugu Lake, Meili Snow Mountain, or cross-border-style overland extensions | Travelers who want deeper minority culture, landscapes, and remote areas | Use a private route plan to manage altitude, drive times, and overnight stops. |

Suggested intro copy:

If you are choosing a Yunnan private tour, start with your available days rather than a fixed package name. Most first-time travelers choose a Kunming-Dali-Lijiang-Shangri-La route, while shorter trips usually remove Shangri-La and longer trips can add Lugu Lake, Meili Snow Mountain, family-friendly pacing, Muslim-friendly arrangements, cycling days, or overland extensions.

Internal links to include:

- `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`
- `/pages/kunming`
- `/pages/dali`
- `/pages/lijiang`
- `/pages/shangri-la`
- `/pages/bespoke-custom-travel`

What NOT to change:

- Do not change collection handle, template, product card layout, product order, prices, booking links, collection schema, FAQ schema, canonical, or robots behavior.
- Do not add a second FAQ-like block that repeats existing FAQ answers.

Risk level:

- Low. This is a visible content refinement on an already relevant collection page. Main risk is making the page too long or duplicating FAQ content.

### 2. `/products/kunming-dali-lijiang-shangri-la-8-day-private-tour`

Current content already present:

- Best-for guidance.
- 8 vs 6 days comparison.
- Customization messaging.
- Season guidance.
- FAQ content.
- Product booking UI and variant logic.

User questions it should answer:

- Is 8 days enough for Kunming, Dali, Lijiang, and Shangri-La?
- Who is this route best for?
- Is the tour private and customizable?
- What should I know about altitude and pacing?
- What is included, and are there hidden shopping stops?

Add or refine:

- Add or raise a compact block near the upper body.

Recommended block name:

- `Trip Planning Snapshot`

Recommended placement:

- Near the upper product body after the main intro/overview and before the detailed itinerary or deeper FAQ content. Do not interfere with booking UI, variant selectors, price display, forms, or add-to-cart behavior.

Fields to include:

- Ideal length.
- Route sequence.
- Best for.
- Pace.
- Customization.
- Altitude note.
- Trust note.

Draft English copy:

**Trip Planning Snapshot**

This 8-day private Yunnan tour is best for first-time travelers who want the classic Kunming-Dali-Lijiang-Shangri-La route without rushing the main highlights. The usual sequence is Kunming, Dali, Lijiang, and Shangri-La, with private transfers and flexible daily pacing.

- Ideal length: 8 days for the full classic route; 6 days is better if you skip Shangri-La.
- Best for: couples, families, seniors, and first-time visitors who want a guided private route.
- Pace: balanced, with time for old towns, lake scenery, mountain views, and local culture.
- Customization: hotel level, start city, activities, dietary needs, and slower pacing can be adjusted.
- Highland note: Shangri-La is higher than Kunming, Dali, and Lijiang, so the route should avoid overly rushed arrival-day sightseeing.
- Shopping policy: the itinerary should stay private and travel-focused, without forced shopping stops or hidden detours.

Internal links to include:

- `/collections/yunnan-private-tours`
- `/pages/kunming`
- `/pages/dali`
- `/pages/lijiang`
- `/pages/shangri-la`
- `/pages/bespoke-custom-travel`

What NOT to change:

- Do not change product handle, template, price, variants, booking form, cart behavior, product JSON-LD, FAQ JSON-LD, availability, media, or itinerary structure.
- Do not replace the existing FAQ; this block should summarize the decision points higher on the page.

Risk level:

- Low to moderate. Content is useful and product-specific, but product pages are commercially sensitive. The block must not touch booking UI or imply inclusions not already supported by the actual itinerary.

### 3. `/pages/kunming`

Current content already present:

- Destination guide content.
- "Know at a Glance" style content.
- Internal links to Kunming day trips, Yunnan private tours, car charter, bespoke travel, Dianchi Lake guide, Stone Forest guide, Dali, and Lijiang.

User questions it should answer:

- How many days do I need in Kunming?
- Is Kunming worth staying in, or only a gateway?
- Should I visit Stone Forest or Dianchi Lake?
- What destinations combine naturally with Kunming?
- Who may not need extra Kunming time?

Add or refine:

- Refine existing "Know at a Glance" content.

Recommended block name:

- `Kunming at a Glance`

Recommended placement:

- Keep within the existing top destination summary area. Add the new fields inside the current concise planning block rather than creating a separate new module.

Fields to include:

- Recommended stay.
- Best for.
- Best combined with.
- Not ideal for.
- Private planning note.

Draft English copy:

**Kunming at a Glance**

Kunming is the easiest starting point for a Yunnan private tour, especially if you want Stone Forest, Dianchi Lake, flower markets, or a smoother first day before continuing to Dali and Lijiang.

- Recommended stay: 1-2 days for most first-time travelers.
- Best for: arrival recovery, Stone Forest day trips, Dianchi Lake, city walks, and starting a private Yunnan route.
- Best combined with: Dali, Lijiang, and Shangri-La on a classic route.
- Not ideal for: travelers with very limited time who only want old towns and mountain scenery.
- Private planning note: Kunming works well as a soft landing before longer drives and higher-altitude destinations.

Internal links to include:

- `/blogs/travel-guides/stone-forest-shilin-guide`
- `/blogs/travel-guides/dianchi-lake-guide`
- `/collections/yunnan-private-day-trips`
- `/collections/yunnan-private-tours`
- `/pages/dali`

What NOT to change:

- Do not change page handle, template, H1, CTA URLs, schema, canonical, robots, or existing destination sections.
- Do not duplicate the full Stone Forest or Dianchi guide content.

Risk level:

- Low. The page already has this content pattern; this is a refinement.

### 4. `/pages/dali`

Current content already present:

- Destination guide content.
- "Know at a Glance" style content.
- Internal links to Dali private tours, Dali itineraries, Dali to Lijiang routing, Yunnan private tours, and related multi-day products.

User questions it should answer:

- Is Dali better than Lijiang?
- How many days should I spend in Dali?
- Should I split time between Dali and Lijiang?
- What is Dali best for?
- Who may not need a long Dali stay?

Add or refine:

- Refine existing "Know at a Glance" content.

Recommended block name:

- `Dali at a Glance`

Recommended placement:

- Keep within the existing destination summary area near the top of the page.

Fields to include:

- Recommended stay.
- Best for.
- Best combined with.
- Not ideal for.
- Private planning note.

Draft English copy:

**Dali at a Glance**

Dali is usually the slower, softer part of a Yunnan private tour, with Erhai Lake, Dali Old Town, Xizhou, Cangshan, and relaxed village scenery. It is often paired with Lijiang rather than treated as a replacement.

- Recommended stay: 2 days for most first-time routes; 3 days if you want a slower lake and village pace.
- Best for: Erhai Lake, Bai culture, old town walks, light cycling, family pacing, and less hurried travel.
- Best combined with: Kunming before Dali and Lijiang after Dali.
- Not ideal for: travelers looking mainly for dramatic snow mountain views or highland Tibetan culture.
- Private planning note: Dali is a good place to slow the route before continuing to busier Lijiang or higher Shangri-La.

Internal links to include:

- `/pages/lijiang`
- `/collections/dali-private-tours`
- `/collections/yunnan-private-tours`
- `/pages/bespoke-custom-travel`

What NOT to change:

- Do not change page handle, template, H1, itinerary pages, CTA structure, schema, canonical, or robots behavior.
- Do not create a Dali vs Lijiang FAQ duplicate if that answer already exists elsewhere.

Risk level:

- Low. The refinement answers common planning questions without changing the page structure.

### 5. `/pages/lijiang`

Current content already present:

- Destination guide content.
- Existing route and private tour links.
- Internal links to Lijiang private tours, Jade Dragon Snow Mountain, Lijiang itineraries, Tiger Leaping Gorge, Lijiang to Shangri-La, and related multi-day products.

User questions it should answer:

- How many days should I spend in Lijiang?
- Should I choose Dali or Lijiang?
- Should I add Shangri-La after Lijiang?
- Is Lijiang suitable for families or seniors?
- What is the best way to include Jade Dragon Snow Mountain?

Add or refine:

- Refine existing "Know at a Glance" style content.

Recommended block name:

- `Lijiang at a Glance`

Recommended placement:

- In the existing top destination summary area, before deeper attraction or route sections.

Fields to include:

- Recommended stay.
- Best for.
- Best combined with.
- Not ideal for.
- Private planning note.

Draft English copy:

**Lijiang at a Glance**

Lijiang is one of the strongest bases for a Yunnan private tour, especially for Jade Dragon Snow Mountain, old town scenery, Naxi culture, Tiger Leaping Gorge, and routes onward to Shangri-La.

- Recommended stay: 2-3 days for most first-time travelers.
- Best for: Jade Dragon Snow Mountain, Lijiang Old Town, cultural walks, day trips, and starting the highland route to Shangri-La.
- Best combined with: Dali before Lijiang and Shangri-La after Lijiang.
- Not ideal for: travelers who want only quiet countryside and minimal crowds.
- Private planning note: A private route helps manage mountain tickets, early starts, family pacing, and the drive toward Shangri-La.

Internal links to include:

- `/products/jade-dragon-snow-mountain-private-tour`
- `/pages/dali`
- `/pages/shangri-la`
- `/products/lijiang-to-shangri-la-private-tour`
- `/collections/lijiang-private-tours`

What NOT to change:

- Do not change page handle, template, H1, product links, existing route blocks, schema, canonical, or robots behavior.
- Do not overstate crowd avoidance; phrase this as pacing and planning support.

Risk level:

- Low. The block summarizes existing route intent and internal links.

### 6. `/pages/shangri-la`

Current content already present:

- Destination guide content.
- Existing private tour and highland route links.
- Internal links to Shangri-La private tours, Lijiang to Shangri-La, Yunnan private tours, Tiger Leaping Gorge, and related highland products.

User questions it should answer:

- Should I add Shangri-La to a Yunnan route?
- Is Shangri-La worth it if I have 8 days?
- How should I plan around altitude?
- Is Shangri-La suitable for kids, seniors, or slower travelers?
- Should I continue to Meili Snow Mountain?

Add or refine:

- Refine existing "Know at a Glance" content.

Recommended block name:

- `Shangri-La at a Glance`

Recommended placement:

- In the existing top destination summary area before detailed attractions or route sections.

Fields to include:

- Recommended stay.
- Best for.
- Best combined with.
- Not ideal for.
- Private planning note.

Draft English copy:

**Shangri-La at a Glance**

Shangri-La adds Tibetan culture, highland scenery, monasteries, grasslands, and a different feel from Kunming, Dali, and Lijiang. It is usually best after Lijiang, with enough time to manage altitude and road travel comfortably.

- Recommended stay: 2 days for the classic route; 3 or more days if adding Meili Snow Mountain or slower highland pacing.
- Best for: Tibetan culture, Songzanlin Monastery, highland landscapes, photography, and travelers who want a deeper Yunnan route.
- Best combined with: Lijiang, Tiger Leaping Gorge, and longer private Yunnan itineraries.
- Not ideal for: very rushed trips, travelers highly sensitive to altitude, or routes with no buffer for weather and road time.
- Private planning note: Plan arrival-day sightseeing gently and avoid packing the first highland day too tightly.

Internal links to include:

- `/products/lijiang-to-shangri-la-private-tour`
- `/pages/lijiang`
- `/pages/tiger-leaping-gorge-from-lijiang`
- `/collections/shangri-la-private-tours`
- `/collections/yunnan-private-tours`
- `/pages/bespoke-custom-travel`

What NOT to change:

- Do not change page handle, template, H1, route URLs, schema, canonical, robots, or existing CTA behavior.
- Do not give medical advice; keep altitude copy practical and non-medical.

Risk level:

- Low to moderate. Altitude language must stay cautious, practical, and non-medical.

### 7. `/blogs/travel-guides/dianchi-lake-guide`

Current content already present:

- Dianchi guide content that should be summarized with a concise top answer.

User questions it should answer:

- Is Dianchi Lake worth visiting?
- How much time do I need?
- What is the best way to visit from Kunming?
- Should I combine it with other Kunming sights?
- Is it better as a private day trip or self-guided visit?

Add or refine:

- Add a compact Quick Answer block near the top.

Recommended block name:

- `Quick Answer`

Recommended placement:

- Directly below the article introduction or first paragraph, before detailed sections.

Fields to include:

- Worth it?
- Time needed.
- Best for.
- Best combined with.
- Private planning note.

Draft English copy:

**Quick Answer**

Dianchi Lake is worth visiting if you have at least half a day in Kunming and want open lake views, easy city access, Western Hills scenery, or a gentle first stop before a longer Yunnan route. Most travelers need 2-4 hours for a simple visit, or a half day if combining the lake with Western Hills or nearby city sights.

- Best for: first-time Kunming visitors, relaxed walks, lake views, photography, and easy arrival-day sightseeing.
- Best combined with: Western Hills, Kunming city sights, or a private Kunming day trip.
- Not ideal for: travelers with only one full Kunming day who strongly prioritize Stone Forest.
- Private planning note: A private driver or guide is helpful when combining Dianchi Lake with several Kunming stops in one day.

Internal links to include:

- `/pages/kunming`
- `/collections/yunnan-private-day-trips`
- `/blogs/travel-guides/stone-forest-shilin-guide`
- `/collections/yunnan-private-tours`

What NOT to change:

- Do not change article handle, title, template, blog structure, article schema, canonical, robots, existing headings, or body sections.
- Do not duplicate a full itinerary if the article already explains logistics later.

Risk level:

- Low. The block is a concise summary of existing practical guide content.

### 8. `/blogs/travel-guides/stone-forest-shilin-guide`

Current content already present:

- Strong practical Stone Forest guide content.
- Existing detailed guidance that should not be duplicated.

User questions it should answer:

- Is Stone Forest worth visiting from Kunming?
- How long does a visit take?
- Should I visit independently or with a private guide?
- Can it fit into a Yunnan private tour?
- What should families or seniors know?

Add or refine:

- Add a compact Quick Answer block near the top.

Recommended block name:

- `Quick Answer`

Recommended placement:

- Directly below the article introduction or first paragraph, before detailed logistics and attraction sections.

Fields to include:

- Worth it?
- Time needed.
- Best for.
- Best combined with.
- Private planning note.

Draft English copy:

**Quick Answer**

Stone Forest is one of the best day trips from Kunming and is worth visiting if you want a distinctive landscape before continuing to Dali, Lijiang, or Shangri-La. Most travelers should plan a half day to a full day, depending on hotel location, walking pace, and whether the visit is combined with other Kunming stops.

- Best for: first-time Yunnan travelers, photographers, families, seniors with a comfortable pace, and travelers who want a signature Kunming-area sight.
- Best combined with: Kunming city time, Dianchi Lake, or the first day of a longer private Yunnan route.
- Not ideal for: travelers with very limited mobility unless the route is planned carefully.
- Private planning note: A private guide and driver can reduce transfer friction, avoid rushed timing, and adapt the walking route to weather and energy level.

Internal links to include:

- `/pages/kunming`
- `/blogs/travel-guides/dianchi-lake-guide`
- `/collections/yunnan-private-day-trips`
- `/collections/yunnan-private-tours`

What NOT to change:

- Do not change article handle, title, template, article schema, canonical, robots, existing detailed guide content, or route URLs.
- Do not repeat detailed ticket, transport, or step-by-step guide sections already present later in the article.

Risk level:

- Low. The article already has the supporting detail; the new block only improves answer extraction and user scanning.

## Rollout Notes for a Future Implementation Phase

- Implement one compact answer block per page only.
- Prefer existing section settings, blocks, and Liquid patterns if a future implementation changes theme files.
- Use handle-scoped logic only where implementation cannot be done through existing page-specific content settings.
- Keep each block short enough to scan on mobile.
- Re-check title, meta description, H1, canonical, robots, OG/Twitter, JSON-LD, internal links, and indexation risk after any future implementation, even though this documentation phase changes none of them.

## Rollback Risk

Documentation-only risk is very low. No theme behavior changes are proposed in this phase. Future implementation risk should remain low if changes are limited to visible copy inside existing page-specific blocks and no schema, URL, template, section, booking, product, or tracking logic is modified.
