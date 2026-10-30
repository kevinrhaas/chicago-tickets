---
id: T-3248
title: Dev's moving-frames leg red since T-2376: the desktop GPU pick disagrees with the raycast on one of the 12 fixed 1835 yard-goods taps
state: done
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-29
closed: 2026-10-29
pr: 1461
claimed_by: run 10/29/2026, 5:52:32 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-30T01:31:29Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/40968523979
claimed_at: 2026-10-29T22:52:33.242Z
decision: null
decision_answer: null
---

Dev's moving-frames leg red since T-2376: the desktop GPU pick disagrees with the raycast on one of the 12 fixed 1835 yard-goods taps.

## Finding (2026-10-29, while finishing PR #1458)

`node tools/check_upload_release.mjs` (the `A phone keeps the town on the GPU, not twice` step of
`chicago-4d-moving-frames.yml`) fails one check, the same way in CI (run 40956240809, 21:34Z) and
locally on the dev-merged #1458 head (dba21ab3b):

    FAIL desktop: the GPU pick answers 12 fixed taps on yard as the raycast does —
      [{"k":0,"cast":["green_tree_tavern",0.0862],"gpu":["green_tree_tavern",1.2080}]

Same structure, different hit distance on tap 0. The leg only fires on PRs touching
`renderers/web/js/**`, `data/flora/**` or its tools, so a data-only change to the yard goods does
not run it. T-2376 (f26355491, merged 16:46Z) rewrote `data/yard/town_trade_goods.json`,
`data/yard/town_woodpiles.json` and `generate_yard_goods.py` at that building, and is the likely
cause; #1458 (a 1904 street-tree card change) does not touch 1835 or the yard layer. The same
step passed on 2026-10-28's runs.

**Acceptance:** `node tools/check_upload_release.mjs` passes all its checks on dev's published
mirror: either the GPU pick and the raycast agree on all 12 yard taps again (the moved yard goods'
pick geometry fixed), or the fixed tap is re-chosen with the reason written where the taps are
defined. Not by loosening the distance tolerance.
