---
id: T-3291
title: 1912 Prairie's rear and roof faces, and the front, oblique, rear and roof browser views with their scene costs the envelope's acceptance asks for
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-3288
opened: 2026-11-01
closed: null
pr: 1567
claimed_by: run 11/1/2026, 5:08:29 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41300116604
claimed_at: 2026-11-01T11:08:30.010Z
decision: null
decision_answer: null
---

1912 Prairie's rear and roof faces, and the front, oblique, rear and roof browser views with their scene costs the envelope's acceptance asks for.

Piece 2 of 2 of **T-3288 — 1912 Prairie's envelope worked down to its pictures: the north flank's corbelled corner turret and stack, the storey heights both drawings read, the rear and roof faces, and the rear, roof and cost views the envelope's acceptance asks for**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3288 was split (2026-11-01T09:28:14.286Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1.2h ago, run 11/1/2026, 2:14:35 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/41287638672) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/41287638672) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Left by T-3290 (2026-11-01)

A capture tool for these views was drafted and dropped from T-3290's PR: on this runner's software GL the
published `/1904/` door boots in a few minutes and each desktop Full stand took over a minute, so five
stands at two viewports does not fit one 600 s foreground command; split it per viewport (or per stand).
Three things learned: `page.screenshot` hangs once `setAnimationHold(true)` is on (shoot the `#view`
canvas element, as `tools/critic_shots.mjs` does, and drive frames with `capture(4)`); stands derived
30 m before the front land in the opposite yard behind its fence and street trees, so set them on the
avenue's roadway (about 12-15 m out) or above the tree crowns; and use `walker.teleport` with `setFly(true)`
for any stand with an altitude.
