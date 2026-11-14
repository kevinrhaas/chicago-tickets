---
id: T-3598
title: dev's content-build smoke red on mobile 1-2: the plank decks tie into the ground they cross (deepest -0.601 m below grade, 1345 vertices past their relief allowance, worst by 0.241 m), red on dev's 5367f0fd6 and on every PR merged up to it
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-14
closed: null
pr: 2040
claimed_by: run 11/14/2026, 6:11:48 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43593182989
claimed_at: 2026-11-14T12:11:49.296Z
decision: null
decision_answer: null
---

dev's content-build smoke red on mobile 1-2: the plank decks tie into the ground they cross (deepest -0.601 m below grade, 1345 vertices past their relief allowance, worst by 0.241 m), red on dev's 5367f0fd6 and on every PR merged up to it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by the run that lapped #2028)

- `smoke (mobile, 1-2)` on dev's own `5367f0fd6` (T-3562): `FAIL [5:39] mobile 390x780: the plank decks tie into the ground they cross — deepest -0.6010 m below grade, highest flat-ground deck vertex 0.9957 m above it, 1345 vertice(s) past even their own relief allowance (worst by 0.241 m)`, 197 passed, 1 failed.
- The same line, with the same numbers, on chicago#2028's head `12f70ad7f` (job 132440405941). That PR changes only 1936 Prairie (1904) and does not touch frontage or deck data, so the red is dev's and it blocks #2028's merge.
- The check is `tools/smoke_renderer.mjs:6263`. This ticket is not in T-3597's list (mobile 6-7, 13, desktop 14).
