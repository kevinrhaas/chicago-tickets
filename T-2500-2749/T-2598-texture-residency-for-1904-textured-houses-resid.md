---
id: T-2598
title: Texture residency for 1904: textured houses resident by distance with hysteresis under a per-tier texture budget, uploads paced per frame, a scripted Prairie Avenue walk at phone profile held under the budget, and captures at the Glessner and street-eye stands unchanged
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2554
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 10:18:10 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38920829153
claimed_at: 2026-10-16T15:18:11.028Z
decision: null
decision_answer: null
---

Texture residency for 1904: textured houses resident by distance with hysteresis under a per-tier texture budget, uploads paced per frame, a scripted Prairie Avenue walk at phone profile held under the budget, and captures at the Glessner and street-eye stands unchanged.

Piece 2 of 2 of **T-2554 — 1904 texture residency: textured houses resident by distance under a per-tier texture budget, uploads paced per frame, and the boot fetch bounded**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2554 was split (2026-10-16T14:03:56.849Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 9:03:51 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding from T-2597 (2026-10-16)

The boot fetch's held-GLB pile on 1904 is the Glessner file alone (56.4 MB full / 31.1 MB light, measured by `tools/measure_boot_peak.mjs`); a load pool does not reduce it, so the default stays unbounded. Residency (this ticket) and T-2596's KTX2 Glessner are what move the 1904 phone's memory; use `__chicago4d.bootPool` and the meter for the boot half of a before/after.
