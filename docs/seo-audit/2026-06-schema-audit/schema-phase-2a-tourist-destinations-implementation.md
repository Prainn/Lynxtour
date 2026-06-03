# Schema Phase 2A: TouristDestination Implementation

## Files Changed

- `snippets/seo-tourist-destination-jsonld.liquid`
- `sections/kunming-page.liquid`
- `sections/dali-page.liquid`
- `sections/lijiang-page.liquid`
- `sections/shangri-la-page.liquid`
- `sections/xishuangbanna-page.liquid`

## Destination Pages Covered

- `https://lynxtour.cn/pages/kunming`
- `https://lynxtour.cn/pages/dali`
- `https://lynxtour.cn/pages/lijiang`
- `https://lynxtour.cn/pages/shangri-la`
- `https://lynxtour.cn/pages/xishuangbanna`

## TouristDestination @id Patterns

- `https://lynxtour.cn/pages/kunming#touristdestination`
- `https://lynxtour.cn/pages/dali#touristdestination`
- `https://lynxtour.cn/pages/lijiang#touristdestination`
- `https://lynxtour.cn/pages/shangri-la#touristdestination`
- `https://lynxtour.cn/pages/xishuangbanna#touristdestination`

## WebPage @id Patterns

- `https://lynxtour.cn/pages/kunming#webpage`
- `https://lynxtour.cn/pages/dali#webpage`
- `https://lynxtour.cn/pages/lijiang#webpage`
- `https://lynxtour.cn/pages/shangri-la#webpage`
- `https://lynxtour.cn/pages/xishuangbanna#webpage`

## Fields Included

- `@context`
- `@type: TouristDestination`
- `@id`
- `name`
- `url`
- `description`
- `containedInPlace` for Yunnan, China
- `touristType`
- `includesAttraction`
- `mainEntityOfPage`
- `subjectOf` referencing `https://lynxtour.cn/#website`

`image` is supported by the reusable snippet but not passed by these destination sections because the pages use visible block-level story images rather than a single stable destination-level image setting.

## Attraction Lists Used

### Kunming

- Stone Forest
- Green Lake
- Dianchi Lake
- Kunming Old Street
- Nanqiang Night Market
- Jinma Biji
- Qianwang Old Street
- Dounan Flower Market
- Yunnan Provincial Museum
- Western Hills

### Dali

- Cangshan
- Erhai Lake
- Xizhou
- Dali Old Town
- Bai Heritage Villages
- Lakeside Villages

### Lijiang

- Jade Dragon Snow Mountain
- Lijiang Old Town
- Black Dragon Pool
- Blue Moon Valley
- Baisha
- Shuhe
- Dongba Culture
- Naxi Cultural Sites
- Tiger Leaping Gorge

### Shangri-La

- Songzanlin Monastery
- Pudacuo National Park
- Dukezong Ancient Town
- Napa Lake
- Meili Snow Mountain
- Lamuyangcuo Lake
- Tiger Leaping Gorge

### Xishuangbanna

- Wangtianshu
- Rainforest Landscapes
- Dai Villages and Temples
- Nannuo Mountain
- Tea Country Experiences
- Local Night Scenes

## Fields Intentionally Omitted

- Geo coordinates omitted because exact coordinates were not already present in page/theme data.
- AggregateRating and reviews omitted because no verified destination ratings exist.
- OpeningHours omitted because these are destinations, not Lynxtour business hours.
- Product, TouristTrip, ItemList, and Service schema are intentionally out of scope.
- Attraction URLs omitted because the PR should not invent attraction URLs; only visibly linked attraction URLs should be used.

## Validation Checklist

- Preview each destination page.
- View source and confirm exactly one TouristDestination block per destination page.
- Confirm existing FAQPage and BreadcrumbList still render.
- Confirm JSON-LD is valid.
- Validate these URLs in Schema.org Validator:
  - `https://lynxtour.cn/pages/kunming`
  - `https://lynxtour.cn/pages/dali`
  - `https://lynxtour.cn/pages/lijiang`
  - `https://lynxtour.cn/pages/shangri-la`
  - `https://lynxtour.cn/pages/xishuangbanna`
- Confirm no visual/UI changes.
