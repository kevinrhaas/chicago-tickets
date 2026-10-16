---
id: T-2565
title: Keith's carved loggia from the 1888 plate and the 1965 close view: balcony and pedestal carving, Ionic volutes, stair-head scrolls, bow-window heights and the stair-cheek curve
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-1883
opened: 2026-10-16
closed: null
pr: 866
claimed_by: run 10/16/2026, 1:36:43 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38861789454
claimed_at: 2026-10-16T06:36:44.231Z
decision: null
decision_answer: null
---

Keith's carved loggia from the 1888 plate and the 1965 close view: balcony and pedestal carving, Ionic volutes, stair-head scrolls, bow-window heights and the stair-cheek curve.

Piece 2 of 4 of **T-1883 — Finish 1808 Keith-Field neighbour of Glessner architecture**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1883 was split (2026-10-16T05:03:00.374Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 12:02:57 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38852568409) — held by the run that split it
- branch `steward/t1883-keith-photographic-finish`

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38852568409) may be working one of the pieces now.

**Acceptance:**

1. From the 1888 plate (`inland-1888`, `a18-rba-ia-1888-keith-1808`, `cgn-1808-inland-1888-keith-copy`) and the 1965 close view (`a18-gh-1808-porch-1965`): the balcony and pedestal carving, the Ionic volute sections and the stair-head scrolls follow the photographed profiles; the bow-window heights and the stair-cheek curve and extent align with the 1965 view.
2. Rebaked with `--only keith_house_1808_prairie`, every view re-rendered, and those differences set `fixed` only where the side-by-side shows it.
3. `check.sh` and the `--for-diff` smoke legs green at both viewports.

The parent's owner reports (2026-10-13 and 2026-10-16, including the permission to use the 1888 Inland Architect Keith plate) and its research page `docs/RESEARCH/k01-1808-keith-1883/README.md` in the code repo are the brief; read them first.
