---
id: T-3502
title: dev's content-build smoke is red on three legs (dev c891a26d7 + PR #1873's 1904-only diff, run 42469167608): 1835 boot payload 43.017 MB over its 40.2 MB budget, 1835 'balanced' detail at West prairie 2,654,960 tris over its 2,625,000 ceiling, and the Glessner People card's why reading 'Face reconstructed after a stand-in' where the T-3265 check wants 'Inferred…'
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-08
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

dev's content-build smoke is red on three legs (dev c891a26d7 + PR #1873's 1904-only diff, run 42469167608): 1835 boot payload 43.017 MB over its 40.2 MB budget, 1835 'balanced' detail at West prairie 2,654,960 tris over its 2,625,000 ceiling, and the Glessner People card's why reading 'Face reconstructed after a stand-in' where the T-3265 check wants 'Inferred…'.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content-build smoke is red on these legs, so PR #1873 (T-3370) and every other PR's content build is refused on them

## Evidence (measured 2026-11-08, content build run 42469167608, attempt 4)

The run baked PR #1873's head 3701b36, which is 0 commits behind dev c891a26d7. Its diff touches only the 1904-mapped `house_1918_prairie` (one GLB, manifest input hashes, its records and the K01/K15 generators). The other 51 meshes it rebaked came out byte-identical. None of these three legs reads that house, so the reds are dev's. The last dev bake that ran these legs green was 2ed7d761f (run 42406509178, 2026-11-07 19:35Z): boot payload 40.051 MB. No dev content build has finished since: 0e1633798 and the seven before it were cancelled.

- **smoke (desktop, 1-2), job 128714162036**, "Enforce the first-visit boot payload budget": `BOOT PAYLOAD OVER BUDGET: 43.017 MB > 40.200 MB` across 1185 requests (40.051 MB / 1173 on 2ed7d761f). `/data/prebuilt/1835/` is 25.858 MB. ground 10.886, frontage 6.815, streets.full 3.910 and yards 3.188 MB (yards was 3.166), so most of the +2.97 MB is outside the four big bins: attribute it with `tools/measure_boot_payload.mjs` (SITE-BUDGET.md §4, as T-3300 / T-3425 did).
- **smoke (desktop, 5), job 128714162133**: `scene detail 'balanced' stays inside its own ceiling at the WORST stand — 2,654,960 tris of 2,625,000 at West prairie, east across the sward toward town, 6443 calls of 7800`.
- **smoke (mobile, 14) job 128714162558 and smoke (desktop, 14) job 128714162093**, the same check on both: `a person on Inspect's People tab opens their own card, with Back to the household (T-3265)`. `smoke_renderer.mjs` requires `/^Inferred/.test(card.why)`; the card now reads `"why":"Face reconstructed after a stand-in"` (likely since #1856's Glessner faces). Every other field passed, Back focus included. Either the card's why line or the check needs to follow the new face provenance; don't weaken the check to make it pass.

PR #1873 (T-3370) is handed on with `resume`, waiting on this ticket.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
