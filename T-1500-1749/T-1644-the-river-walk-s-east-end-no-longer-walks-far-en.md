---
id: T-1644
title: The river walk's east end no longer walks far enough west: T-1630's recut south bank leaves the walker at E 811.5 where the check wants past E 802
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-26
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

`dev` is red on one smoke check, and has been since T-1630 (PR #97) merged on
2026-09-26. Part 1-2 at mobile, measured on a steward runner:

    FAIL  mobile 390x780: the east end reads as planks underfoot, and walks on along the bank
          — 2976 plank vertice(s) in the east end's band, walked west to E 811.5,
            0 blocked stride(s), worst step 0.04 m

The assertion (`tools/smoke_renderer.mjs`, the river-walk east-end block) wants
`boardVerts >= 100 && walkedToE < 802 && blocked === 0 && worstStride <= 0.35`. Three of
the four are comfortably met: the planks are there (2976 of them), nothing blocks the
walker, and the ground under every stride is smooth to 4 cm. The one that fails is
DISTANCE — 220 strides of 0.05 s walking west carry the walker only to E 811.5, and the
check wants it past E 802. It is 9.5 m short, not broken.

**It is T-1630's, and that is measured rather than guessed.** Found while re-gating
PR #95 (T-1637) after merging dev. A pristine `origin/dev` worktree at 75babf4a,
published and run on the same runner, fails the same check with BYTE-IDENTICAL numbers —
2976 vertices, E 811.5, 0 blocked, 0.04 m — so nothing in T-1637's diff moves it. T-1630
recut the south bank below the bend to Hathaway and ran the outer plank walk straight
along it, which is exactly the geometry this check walks.

**The two readings this needs, in order.**

1. WHERE THE WALK NOW STARTS AND HOW FAST IT RUNS. The walker begins from a teleport and
   walks west for 11 s. Either the recut moved the start point east, or it lengthened the
   path the walker has to follow, or the recut bank slows the stride. Say which, with the
   before and after, before touching anything.
2. WHETHER E 802 IS STILL THE RIGHT NUMBER. `walkedToE < 802` was written against the
   pre-recut bank. If the recut is correct — and the owner ruled it in — then the target
   may simply be a stale constant, in which case the fix is to re-derive it from the
   recut walk's own published extent and say so beside it. If the recut left a real
   9.5 m of unwalkable or slower bank, the fix is in the geometry and the constant stays.
   **Do not relax the threshold to quiet the gate without reading 1 first** — that is the
   failure this project refuses by name.

**Acceptance.** The check passes at mobile AND desktop on a published tree; whichever of
the two readings above resolved it is written down with its numbers; and if the constant
moved, it is derived from something committed rather than chosen to fit.
