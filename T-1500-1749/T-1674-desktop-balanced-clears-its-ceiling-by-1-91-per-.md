---
id: T-1674
title: Desktop `balanced` clears its ceiling by 1.91 per cent at the forks: the next downtown parcel needs the headroom measured before it deals, not after it bakes
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 9/27/2026, 11:01:27 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36331173426
claimed_at: 2026-09-27T16:01:27.383Z
decision: null
decision_answer: null
---

Desktop `balanced` clears its ceiling by 1.91 per cent at the forks: the next downtown parcel needs the headroom measured before it deals, not after it bakes.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)


Read by T-1641, closing South Water's books, on the mirror `tools/publish.sh` built from
dev at `c164f8ae`. `node tools/measure_detail_ceilings.mjs --only both` passes every tier
at both viewports — the town is back inside T-1154's ceilings and T-1244/T-1245's trim is
why — but the desktop margins are not comfortable:

| tier | ceiling | worst desktop | margin | per cent |
| --- | --- | --- | --- | --- |
| `full` | 1,460,000 | 1,410,306 (the forks) | 49,694 | 3.40 |
| `balanced` | 1,280,000 | 1,257,120 (the forks) | 22,880 | **1.79** |
| `light` | 825,000 | 773,206 (the open aerial) | 51,794 | 6.28 |

Mobile is comfortable at every tier (205,201 / 173,369 / 125,813). The reading is committed
at `data/render/south_water_close_out.json`.

**And the price of a roof is now measured, which is the part that makes this urgent.** The
same sweep was run twice an hour apart, before and after T-1640 merged. That pull request
added ONE freight shed on the south bank, and desktop `balanced` at the forks went from a
24,420 margin to 22,880: **1,540 triangles for one shed**. The remaining margin is about
fifteen sheds wide.

**Why this is a ticket and not a table.** The next build parcel in the queue is T-1201 —
the Lake Street and Dearborn–Clark–LaSalle core — and it raises roofs inside the same
downtown frusta the forks stand looks through. Twenty-two thousand triangles is fifteen
freight sheds, and a block core is more than fifteen roofs. T-1200's own procedure puts the ceiling reading at the END of a parcel, before
the push, which means a parcel discovers it has breached after it has dealt, generated and
baked. On a 1.91 per cent margin that is the wrong end.

**Acceptance:** a parcel can find out what it may spend BEFORE it deals. Concretely, one
of: `measure_detail_ceilings.mjs` grows a mode that prices a parcel's deal from the
committed family footprints and the tier's own decimation, and says how many roofs of which
families the tightest stand will carry; or the reading is taken at the start of a build
parcel as well as the end, with the difference attributed. Either way the answer is a
number T-1201 can act on, and this ticket does NOT move a ceiling — T-1154 argued that and
its ruling stands.

**Links:** T-1641 · T-1200 · T-1201 · T-1154 · T-1244 · T-1245 · T-1148 ·
`data/render/south_water_close_out.json` · `data/render/southern_stand_ceilings.json`.
