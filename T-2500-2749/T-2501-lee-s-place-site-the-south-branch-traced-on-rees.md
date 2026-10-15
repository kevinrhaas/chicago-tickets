---
id: T-2501
title: Lee's Place site: the South Branch traced on Rees & Rucker 1849 from the 1812 box floor to the forks at Bridgeport, and the farm's site ruled from the four placings measured against it
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2488
opened: 2026-10-15
closed: null
pr: 806
claimed_by: run 10/15/2026, 1:11:36 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38689931010
claimed_at: 2026-10-15T06:11:36.569Z
decision: null
decision_answer: null
---

Lee's Place site: the South Branch traced on Rees & Rucker 1849 from the 1812 box floor to the forks at Bridgeport, and the farm's site ruled from the four placings measured against it.

Piece 1 of 3 of **T-2488 — 1812: build Lee's Place (Hardscrabble), the farm cabin and field on the South Branch three to four miles from the fort, beyond the west edge of the 1812 ground**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2488 was split (2026-10-15T06:11:15.402Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 5m ago, run 10/15/2026, 1:06:00 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38689931010) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38689931010) may be working one of the pieces now.

**Acceptance:** The South Branch's centreline and banks are traced off Rees & Rucker 1849 by a committed tool, from the box floor (N -3800, where `south_branch_below_twelfth` stops) to the forks at Bridgeport, and the trace is graded `inferred`. A committed reading file (`data/terrain/1812_hardscrabble_site.json`) does three things. It measures each of the four placings against that trace: Heald's "about three miles from the garrison", Currey's "some four miles from the mouth", Hurlbut's "about half a mile below Bridgeport ... on the north side", and Moses and Kirkland's "northwestern side ... near its forks". It says where they agree and where they do not. And it rules one site with a stated uncertainty, on the north-west bank. The site is never a pin. `check.sh` re-derives the reading with a `--check` that needs no raster. Each distance and quote resolves to a source record; any source not yet in `data/sources/` gets a record first, or the reading says it is not used. Nothing is visible yet: this is the measurement half of the split, and T-2502 and T-2503 build on it.
