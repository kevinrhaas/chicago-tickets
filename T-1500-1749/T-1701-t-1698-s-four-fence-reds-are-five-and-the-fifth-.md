---
id: T-1701
title: T-1698's four fence reds are five, and the fifth is at mobile: the frontage layer's walks and posts fail with its own problem list reading [none]
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: Fixed by T-1752 (#201); the frontage check passes at mobile (parts 1-6 297/0, 2026-10-01)."
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

T-1698's four fence reds are five, and the fifth is at mobile: the frontage layer's walks and posts fail with its own problem list reading [none].

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The measurement (T-1686, 2026-09-28)

T-1698 names four checks at desktop part 1. There are **five**, and the fifth only shows
at mobile, inside part 2:

    mobile 390x780: the frontage layer lays all five records' walks and stands their posts
      — 5 record(s) [green_tree_frontage, sauganash_frontage, river_walk_frontage,
        lasalle_crossing_frontage, town_street_edge], 47 walk(s), 39 crossing(s),
        18 post(s), 31 fence run(s), 857730 vertices, 115 wall(s) refused,
        problems [none]

**The layer is BUILT and its own problem list is empty** — the same signature as
T-1698's four ("cell delta mean 0.00, worst 0, need worst>=6"), which is why this is
filed under it rather than beside it: one defect, five checks, two viewports.

**Attributed, not assumed.** Measured twice: on `steward/t1686-h1-centre-hall` at mobile
parts 1-2, 153 passed / 5 failed; and then on a CLEAN `origin/dev` worktree at
`d3260907`, published from scratch — **153 passed, 5 failed, byte for byte the same
five**. So the fifth is dev's too, and no branch introduced it.

**And the record still reads PASS for mobile part 2**, which is the second half of
T-1698's complaint: `dev-smoke-state.mjs ask --viewport mobile --stage 1-2` reported
part 1 FAIL (23:13Z) beside part 2 PASS (06:50Z), so a run asking the record before
re-running a part would have been told this leg was clean.

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** Fixed by T-1752 (#201); the frontage check passes at mobile (parts 1-6 297/0, 2026-10-01).
