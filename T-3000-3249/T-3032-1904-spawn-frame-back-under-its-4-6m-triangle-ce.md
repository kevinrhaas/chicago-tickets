---
id: T-3032
title: 1904 spawn frame back under its 4.6M triangle ceiling after the vase elms
state: done
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-22
closed: 2026-10-22
pr: 1205
claimed_by: run 10/22/2026, 12:38:49 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-22T20:17:56Z
claimed_run: null
claimed_at: 2026-10-22T17:38:50.985Z
decision: null
decision_answer: null
---

1904 spawn frame back under its 4.6M triangle ceiling after the vase elms.

**Finding (2026-10-22, smoke desktop part 14 after T-3017 / PR 1199):** "the frame at the 1904
spawn is inside the draw budget (T-1739)" failed: 4,603,239 triangles against 4,600,000.
Measured at the spawn on the same published build: dev before T-3017 4,482,761 (street trees
200,900); after 4,603,239 (street trees 302,902). The spawn sees 1 near, 23 mid, 500 far and
2,630 distant elms; per template the vase elm's far level is 90 wood + 184 leaf triangles
(timber elm 71 + 51), so the far ring carries most of the growth (+76k).

**Acceptance:** the desktop 1904 spawn frame reads under 4.6M triangles in the smoke's own
check, with the cut taken where it does not show: the mid level (what a walker sees from
10-44 m) keeps its share; the far ring (44 m on) draws fewer, larger sprays. A far-row A/B
render shows the crowns' mass unchanged.
