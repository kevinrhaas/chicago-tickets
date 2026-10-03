---
id: T-0192
title: The cross streets' own frontages get the street edge
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-0127
opened: 2026-08-24
closed: null
pr: null
claimed_by: run 10/3/2026, 12:01:55 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37098340840
claimed_at: 2026-10-03T05:01:56.478Z
decision: null
decision_answer: null
---

The cross streets' own frontages get the street edge.

Piece 3 of 5 of **T-0127 — The rest of the town gets the street edge**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Acceptance, stated before working:** the seven cross streets carry the same plank walk
the covered east-west streets carry, laid by the same rule and not by a hand-placed
exception, with board crossings round the corners so the walk is walkable end to end —
and all three scene-detail tiers stay inside their ceilings at the whole T-0135 stand
set. Never by weakening a gate, and never by a sixth ceiling raise.

---
## 2026-08-29 — THE CODE HALF IS DONE; THE GEOMETRY IS REFUSED BY A MEASURED NUMBER

Two separate things refused this ticket, and only one of them was ever a number.

**The code half, and it is finished.** `_edge_faces` in
`tools/generate_frontage_works.py` enumerated a block's NORTH and SOUTH faces only. An
east-west street bounds a block on those; a cross street bounds it on its EAST and WEST.
So naming Clark Street in the covered tuple would have laid nothing at all — silently,
with no refusal on the record — whatever the frame budget said. All four faces are
enumerated now, and every ordering in that generator is axis-aware: a face's position
along Lake Street is its easting and along Clark Street its northing, so the face sort,
the along-a-side corner crossings and the across-the-road pairing all read the street's
own axis. A cross-street face carries no fence and no hitching post, and that is the
plat's answer rather than a gap — both rules are per-lot and every one of Thompson's
lots fronts an east-west street, so a cross-street face is the END of a lot row. It is
written as a refusal on the record, not left as a silence.

**The geometry half, measured rather than estimated.** All seven were generated,
published and read with `tools/measure_detail_ceilings.mjs` at T-0135's five stands,
desktop 1280x800, against `dev` at `83a4e221` in the same run. They are 34 platted faces
and **+3,557.7 m of walk** with +30 crossings — the record goes 36 faces / 3,170.7 m to
70 / 6,728.4 m, more than doubling it.

| tier | ceiling | `dev` worst | with the seven | over by | `dev`'s headroom |
|---|---:|---:|---:|---:|---:|
| `full` | 1,400,000 | 1,393,073 | **1,545,639** | 145,639 | 6,927 |
| `balanced` | 1,210,000 | 1,203,893 | **1,332,299** | 122,299 | 6,107 |
| `light` | 785,000 | 763,410 | **800,372** | 15,372 | 21,590 |

All three tiers, including the one a weak machine boots into. **And the binding fact is
not the cross streets**: `dev` itself stands 6,927 and 6,107 triangles inside `full` and
`balanced` — half of one per cent — before a board is laid. That is T-0237's finding
restated at this rung two days later. The SMALLEST of the seven, Market at 208.8 m, is
about 7,500 triangles at `balanced`'s own measured 36 a metre, so **not even one street
fits in 6,107**, and shrinking below one street is a hand-placed exception rather than
the rule this record is.

**So the ticket is blocked on the frame budget and not on anything in it.** What ships
here is the half that is done, plus the measurement on the record's own `refused` where
the next reader will find it. The east/west path would otherwise be dead code — written,
measured once and never executed again — so `tools/test_frontage_faces.py` drives the
whole seven through the rule on every commit (34 faces, both sides paired, ordered by
northing, outward normals across their street) and `check.sh` runs it with its own
self-test. The day the headroom is won back, this ticket is one tuple.

**Withdrawn from this ticket:** PR #418 (2026-08-27) laid Market Street alone on the same
code and parked on `hold` at 16,196 triangles over `balanced`. It was measured against a
`dev` 87 commits older; re-measured here, Market still does not fit. That branch is
superseded by this one.

**Links:** T-0127 (parent) · T-0190 (Randolph, built and measured and taken back out) ·
T-0193 (the West Division block, blocked on the same rung) · T-0237 (the headroom) ·
T-0135 (the stands) · T-0223 · T-0146 · T-0209.

## IT NOW COSTS SOMETHING STANDING, NOT JUST SOMETHING MISSING (T-1734, 2026-09-28)

Until this week the gap this ticket records was a gap in coverage: the seven cross streets
have no walk, no fence and no hitching post, and nothing that HAD one lost it. That is no
longer true, and the reason is a ruling somewhere else entirely.

T-1479 ruled that a cell of the Original Town's grid standing on West Division ground is
cut on the DIVISION's module — two columns of five backing onto a north-south alley. T-1733
cut `blk_lake_clinton` that way and T-1734 cut `blk_randolph_clinton`. Both blocks' lots now
front Clinton and Canal, which are north-south, so **this generator cannot reach a single lot
on either of them**: `EDGE_CROSS_STREETS` is empty for the frame budget measured above, and
`_edge_faces` matches a lot to a face by `lot["tier"] == face`.

**Measured on T-1734's own diff:** `blk_randolph_clinton` lost 3 street-lining board fence
runs, 176.2 m, and the town's `fence_m` fell 1,606.1 → 1,429.9. Those fences stood in front
of four invented cottages that had fronted Randolph and Washington; the cottages did not
move off the block and did not change, they turned ninety degrees to face the streets the
plat gives them, and the fence-laying does not follow. `blk_lake_clinton` never had any,
having carried no dealt parcel when T-1733 cut it.

**What was done about it, so nobody re-discovers it:** the silence is now a counted
assertion. `tools/test_frontage_faces.py` used to assert `no platted lot fronts a cross
street`, which was a true statement about the Original Town's module and is not one about
the grid this project now cuts. It asserts instead that every lot fronts a face its own
block is bounded by, and that the blocks whose lots front a face nothing lays are NAMED —
`blk_randolph_clinton` today. A third transposed cell arriving makes that check red until
somebody either adds it and says so or covers the street.

**What this changes about the ticket:** nothing about the block. The frame budget is still
the whole of it. But the trade is no longer "seven streets gain frontage works"; it is also
"two blocks' worth of fence and walk stops being absent from ground that had it", and that
is a stronger case for the headroom work than the one written above.

## Queue cleanup 2026-10-03 (owner: "see if there are any tickets that were blocked in the queue from before but now can be worked")

**Unblocked.** The frame budget it waited on was re-measured and re-set by T-1969/T-1975 (done 2026-10-02). Price the seven streets with measure_detail_ceilings.mjs --price --deal first; per the owner's 2026-08-21 ruling a measured raise argued where the ceiling is defined is allowed, and light stays the floor.
