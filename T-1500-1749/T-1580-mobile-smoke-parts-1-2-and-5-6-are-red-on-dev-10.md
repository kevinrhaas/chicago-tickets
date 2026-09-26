---
id: T-1580
title: Mobile smoke parts 1-2 and 5-6 are red on dev: 10 frontage and far-merge checks fail on a clean origin/dev, most likely since T-0141 moved the Green Tree off its corner post
state: review
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: 54
claimed_by: run 9/25/2026, 6:07:20 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36198919206
claimed_at: 2026-09-25T23:07:20.589Z
decision: null
decision_answer: null
---

Mobile smoke parts 1-2 and 5-6 are red on dev: 10 frontage and far-merge checks fail on a clean origin/dev, most likely since T-0141 moved the Green Tree off its corner post.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The measurement (2026-09-25, found while landing #39)

On a clean `origin/dev` at `cfd98446` (after #42), published, 390×780:

```
SMOKE_VIEWPORT=mobile SMOKE_STAGE=1-2  → 147 passed, 7 failed
  FAIL the frontage layer lays all five records' walks and stands their posts
  FAIL the named board hangs on a post that stands on the ground
  FAIL the frontage layer draws the meshes it authored
  FAIL the board carries the record's own name, painted — "null" on 0 vertices, record says "null"
  FAIL the walk and its board reach the screen from the street — cell delta worst 0 (need >= 6)
  FAIL aiming at the frontage opens the inn it belongs to — 25 aims returned [nothing]
  FAIL the eighteen hitching posts stand on their own ground, carrying nothing
SMOKE_VIEWPORT=mobile SMOKE_STAGE=5-6  → 29 passed, 3 failed
  FAIL the far merge gives back draw calls down the axial street and moves no triangle doing it — 0 of 21 clusters
  FAIL the furniture reach is what makes the light tier cheaper down that street — +1,272 tris / 2 calls (need 120,000 and 50)
  FAIL the furniture reach is what makes the balanced tier cheaper down that street — +0 tris (need 34,000)
```

PR #39's branch fails exactly the same ten, line for line, so none of them is #39's. Mobile parts 3-4 and 7-13 are green on both.

**Most likely cause (to confirm, not assumed):** T-0141 (#16, 2026-09-24) moved the Green Tree 116 m to Lake and West Water. Its own PR says the move left the inn with NO corner post and NO board: the frontage record now refuses the post, and generate_business_signboards withholds the wall board. Six of the seven part 1-2 checks are about the Green Tree's walk, post, board and aim (`"null"` painted, 0 cells changed, 25 aims return nothing). T-0141 ran only the smoke parts its diff priced. The draw-call pair in 5-6 reads the Lake-at-Canal axial stand, which the same move and the frontage chunks feed. The last mobile 1-2 reading in `dev-smoke-state.json` is green (2026-09-21), before T-0141.

**Why it is band 0.** A leg that is red on dev is reported by `smoke_budget` as "already red on dev", and runs skip it, so a real regression in parts 1-2 or 5-6 would look exactly like these reds. T-1547 owns getting the Green Tree's corner post back. This ticket owns the smoke: either the checks follow the post-T-0141 truth (a refused post and a withheld board, stated), or T-1547 lands and they go green. The checks may not be weakened to pass.

**Acceptance:** mobile parts 1-2 and 5-6 green on dev, and the readings are filed in `dev-smoke-state.json`. For every check changed, say what the record now says and why the old expectation no longer held. The desktop legs for the same parts are measured too.
