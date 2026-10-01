---
id: T-1209
title: Build the boarding houses to their beds: the H1–H3 houses the lodging model sized, each with the window rhythm, service wing and stovepipes its capacity implies, its stable and privies, on the seats near the landings and approaches — and re-size the named hotels' outbuildings to their guests
state: split
epic: TOWN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-16
closed: 2026-09-30
pr: null
claimed_by: run 9/30/2026, 11:11:01 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-01T04:14:43.996Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36813543008
claimed_at: 2026-10-01T04:11:01.389Z
decision: null
decision_answer: null
---

Tenth build ticket, same contract as T-1200, cutting across districts because the
boarding houses are one economy: the lodging model (T-1164) sized every house by its
beds, T-1187 gave each a keeper and T-1175 filled it. The 42-house
programme has 12 standing.

**Acceptance:** as T-1200, for the boarding-house slot list town-wide — H3 service-wing
two-storey houses (the crosswalk: "remove tavern cues; add 6–10 upper-window rhythms, service
wing and varied stovepipes"), H1/H2 for the smaller houses, each record's `form` carrying
`fenestration` and `chimneys` sized from its `capacity` block (the derivation on the record), A1
stables and A3 privies per house, the named hotels' stables and wagon yards re-checked against
their guest counts (the Western's stable "for ~8 horses" vs its beds); the frame-budget clause;
a screenshot of a boarding-house row; successor T-1214.

**Stop condition:** every boarding house in the lodging model stands at its size, with its
household in it.

**Links:** T-1200 · T-1164 · T-1187 · T-1175 ·
`data/structures/brown_boarding_house.json` · `docs/RESEARCH/western_hotel.md`.

## Handed on from T-1208 — the West's remainder (T-1799, 2026-10-01)

T-1208 (the West Division's outer clusters and Wabansia) closed its last piece with T-1799;
its reading is `data/render/west_close_out.json` in the code repo. What the West still owes,
from the order book, each row already ordered from a live ticket:

- `larger_boarding_houses/west` — 6 set, 2 standing, **4 to build** → T-1779 (this ticket's own row)
- `ordinary_dwellings/west` — 75 / 56, **19** → T-1783
- `barns_stables/west` — 20 / 14, **6** → T-1212; `small_outbuildings/west` — 14 / 6, **8** → T-1212
- `stores_mixed_use/west` — 6 / 4, **2** and `workshops/west` — 8 / 5, **3** → T-1766
- inns/taverns, freight and institutional rows are full (0 left)
- 42 more roofs are gated on `ground/west_division_beyond_committed_control`, waiting for committed street control west of Clinton and Canal

**The frame budget the West is building against:** the worst stand for `full` and `balanced` is
now Lake Street at Canal at both viewports. Desktop `full` clears by 32,056 triangles (2.20 %),
and the frame draws 205 of 215 calls there. Price any West parcel inside that stand's frustum
with `tools/measure_detail_ceilings.mjs --price` before it deals.
