---
id: T-2832
title: Shops & work: the 94 authored firms' cards fetch businesses/<id>.json, which 404s; the record lives under businesses/authored/
state: open
epic: RENDERING
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-18
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Shops & work: the 94 authored firms' cards fetch businesses/<id>.json, which 404s; the record lives under businesses/authored/.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 153 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a visitor-facing failure measured on the dev preview: 94 of 287 firm cards fail to load their record

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What is wrong (measured 2026-10-19)
`tools/compile_businesses.py` `index_row` writes `"file": "<id>.json"` for every firm, and
`js/businesses.js` fetches `businesses/${r.file}` when a card opens. The 94 authored records
live in `data/businesses/authored/`, so for those 94 of 287 rows the fetch 404s. On the dev
preview: `data/businesses/biz_andrus_thomas_carpenter.json` → 404,
`data/businesses/authored/biz_andrus_thomas_carpenter.json` → 200,
`data/businesses/biz_a_garrett.json` (a register firm) → 200. Found by the T-2825 run.

## Acceptance
- [ ] Every row's `file` resolves: a check (compile_businesses --check, or a test) fails if any index row's file is missing under data/businesses/.
- [ ] An authored firm's card opens with its record on 390x780 and desktop; a smoke check opens one.
- [ ] No visitor-visible change except the card now loading.
