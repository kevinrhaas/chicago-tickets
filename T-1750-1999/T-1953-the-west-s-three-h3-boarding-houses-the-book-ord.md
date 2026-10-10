---
id: T-1953
title: The West's three H3 boarding houses the book orders, on the platted ground T-1414 seats, each with its stable and privy, keepers and lodgers seated
state: open
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1810
opened: 2026-10-01
closed: null
pr: null
claimed_by: run 10/2/2026, 12:06:59 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36967233005
claimed_at: 2026-10-02T05:06:59.063Z
decision: null
decision_answer: null
---

The West's three H3 boarding houses the book orders, on the platted ground T-1414 seats, each with its stable and privy, keepers and lodgers seated.

Piece 4 of 4 of **T-1810 — Raise the H3 boarding houses the book still orders beyond the two Washington-tier seats — the South's remaining eight and the West's and North's, whose placement no banded keeper has claimed yet — each with its stable and privy, keepers and lodgers seated**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Queue cleanup 2026-10-10 (owner: "are there any other held tickets that can be cleared")

Unblocked: **T-1414 is done** (PR #341, closed 2026-10-03), so the ground it owed is seated. Read on `dev` at b281f6d9 before anything else:

- In `data/reconstruction/1835_665_roof_programme.json` the `west_division_beyond_committed_control` unit is `complete` with 0 roofs and **28 roofs of surplus headroom** on named West blocks. Open West blocks with room: `blk_washington_clinton` (39 capacity, 20 standing), `blk_west_washington_des_plaines` and `blk_west_washington_jefferson` (6 each, 0 standing).
- **But the programme's `remaining.by_district.west` is 0 and `by_district_family.west` is empty.** The West's last owed H3 left the remainder at c0d76927 (T-2148, 2026-10-06). The only H3 still owed anywhere is one in the South.

So the first step is a reading, not a build: does the book still order the West's three H3s? If it does, raise them on the open West blocks above. That also seats T-2023's 7 West adults, who are still `ordered_with_no_bed`. If it does not, say so here and withdraw this ticket, and re-point T-2023 at whatever now owes the West a lodging roof.
