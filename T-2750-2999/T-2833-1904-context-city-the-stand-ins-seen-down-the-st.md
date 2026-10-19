---
id: T-2833
title: 1904 context city: the stand-ins seen down the streets read as period buildings and trees, not boxes and blobs
state: open
epic: META
requested_by: owner
seen: false
effort: M
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

1904 context city: the stand-ins seen down the streets read as period buildings and trees, not boxes and blobs.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 151 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The owner asked for it directly in the project thread (2026-10-19, with two iPhone screenshots); it is being worked now in an interactive session.

Owner, 2026-10-19 02:18 UTC, project thread (two iPhone screenshots: north up Prairie from 1626, a flat pink box across the street's end; west along 18th from 266 E 18th, boxes and an octahedron crown down the street): "So at the ends of the blocks it's very abrupt with the fake buildings as just boxes and the bad trees, where these exist, and you can see them from the developed prairie area, can you replace these with real trees and real appearing logical, follow from any historical guidance just a light structures that look fine don't look bad but are not a gigantic box". Then: "Any end of blocks not just these two shots".

**Acceptance:**
1. Every context-city stand-in (data/context/1904.json, renderers/web/js/context.js) reads as a period building, not a plain box: storeys and window rows, a cornice on a flat roof, eaves on a pitched one, and a run of lots reading as separate houses, from the rules the file already records (heights, materials, roofs), still faded and lower-detail than Prairie Avenue.
2. The 110 m row Robinson's plate 10 draws on 16th Street's north side (Mortimer and Tappan's sub., sixteen lots) is drawn as that row of houses, not a five-storey block.
3. The stand-in trees near enough to be seen down a street are the grown species trees the parkway uses (tree-model.js), cheaply; no octahedron or icosahedron crowns where a visitor in the worked band can see them.
4. Phone (390x780, light): boot peak memory and triangles no worse than dev by more than the T-2491 allowance (25 MB); no new per-frame work. Desktop 1904 stays under its triangle ceiling.
5. Gate green; before and after shots of the two owner views plus another street end, on phone and desktop.
