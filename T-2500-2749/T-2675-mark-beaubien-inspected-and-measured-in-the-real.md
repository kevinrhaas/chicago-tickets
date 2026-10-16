---
id: T-2675
title: Mark Beaubien inspected and measured in the real 1835 scene at desktop and mobile: close, conversation and street distances checked for contact, scale, shadows, foot slide and LOD popping, with shipped size, triangles, draw calls, texture memory and frame cost recorded and defects fixed
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1791
opened: 2026-10-16
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

Mark Beaubien inspected and measured in the real 1835 scene at desktop and mobile: close, conversation and street distances checked for contact, scale, shadows, foot slide and LOD popping, with shipped size, triangles, draw calls, texture memory and frame cost recorded and defects fixed.

Piece 3 of 3 of **T-1791 — Build Mark Beaubien as Chicago 4D's first historical portable human, from Blender master to interactive browser actor**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

Read the parent first: **T-1791** keeps the full ask, the read-first list (`data/residents/households/hh_beaubien_mark.json`, `data/businesses/authored/biz_beaubien_mark_tavern_keeper.json`, `data/sources/encyclopedia_chicago_mark_beaubien.json`, `docs/RESEARCH/sauganash_hotel.md`, `docs/RESEARCH/exchange_coffee_house.md`, the T-0462 row for `beaubien_mark`). Split on the owner's word, 2026-10-16 ("ok to split the mark ticket"), because the parent was effort L.

Owner, 2026-10-16: *"I think human figures are ok once we are able to render them and go through those tickets"* and *"ok … for native and Métis depictions based on your fair and reasonable judgement"*. T-2672 rewrites AGENTS.md's standing constraint to match; it sits above T-1789 and lands first.

## Depends on

- T-2674 — the browser actor; do not claim before it has merged.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

- [ ] Mark rendered and inspected in the real 1835 browser scene at desktop and mobile, at close, conversation and street distances: terrain contact, scale against doors, shadows, hair and clothing artefacts, foot slide, LOD popping, textures and historical read. A Blender beauty render alone does not close it.
- [ ] Shipped size, triangles per LOD, materials and draw calls, texture memory, animation cost and frame impact recorded; visible and performance defects corrected rather than the scene budget weakened to admit the first person.
- [ ] Stop condition (the parent's): a visitor can encounter a credible, explicitly sourced or reconstructed Mark Beaubien in the browser, and the whole path stays portable to a future Unreal import from the same Blender source.
