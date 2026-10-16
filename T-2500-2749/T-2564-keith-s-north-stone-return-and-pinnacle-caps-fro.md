---
id: T-2564
title: Keith's north stone return and pinnacle caps from the Glessner-side photographs: the large ashlar courses, the curved coping and the cap profiles
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1883
opened: 2026-10-16
closed: null
pr: 863
claimed_by: run 10/16/2026, 12:03:10 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38852568409
claimed_at: 2026-10-16T05:03:10.833Z
decision: null
decision_answer: null
---

Keith's north stone return and pinnacle caps from the Glessner-side photographs: the large ashlar courses, the curved coping and the cap profiles.

Piece 1 of 4 of **T-1883 — Finish 1808 Keith-Field neighbour of Glessner architecture**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1883 was split (2026-10-16T05:03:00.374Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 12:02:57 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38852568409) — held by the run that split it
- branch `steward/t1883-keith-photographic-finish`

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38852568409) may be working one of the pieces now.

**Acceptance:**

1. In the seven views that see Keith's short north return beside Glessner (`a18-gh-glessner-front-with-keith`, `a18-gho-house-under-construction-1887`, `a18-inland-architect-1888-02-glessner-plate`, `a18-rba-taylor-2135-glessner-ne`, `taylor-2135-ne`, `a18-gh-florian-1948-northeast-overall`, `a18-gh-1800-block-looking-sw-c1888`, `a18-owner-1800-block-looking-sw`), the return reads as the photographs show it: large horizontal ashlar courses rather than a smooth slab, a curved coping on its top, and pinnacle caps with the photographed profile rather than a simplified block.
2. Rebaked with `tools/bake.sh --only keith_house_1808_prairie`; every reference view re-rendered with `tools/photo_match.mjs`; the north-return and pinnacle differences in each match record set to `fixed` only where the side-by-side shows it, and left `open` otherwise.
3. `check.sh` green and the `--for-diff` smoke legs green at 390x780 and 1280x800.

The parent's owner reports (2026-10-13 and 2026-10-16, including the permission to use the 1888 Inland Architect Keith plate) and its research page `docs/RESEARCH/k01-1808-keith-1883/README.md` in the code repo are the brief; read them first.
