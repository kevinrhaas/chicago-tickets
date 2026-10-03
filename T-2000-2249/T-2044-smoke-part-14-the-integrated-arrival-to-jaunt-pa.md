---
id: T-2044
title: Smoke part 14: the integrated arrival-to-jaunt path on the published mirror at both viewports — cold boot, welcome, a jaunt, a card and its source, a mode change, End, a second jaunt, Explore Myself
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1272
opened: 2026-10-03
closed: null
pr: null
claimed_by: run 10/3/2026, 3:14:07 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37150554286
claimed_at: 2026-10-03T20:14:07.093Z
decision: null
decision_answer: null
---

Smoke part 14: the integrated arrival-to-jaunt path on the published mirror at both viewports — cold boot, welcome, a jaunt, a card and its source, a mode change, End, a second jaunt, Explore Myself.

Piece 1 of 4 of **T-1272 — Verify arrival, jaunts and source browsing on the published mobile app**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. `SMOKE_STAGE=14` exists in `tools/smoke_renderer.mjs` and runs, on a fresh context that does NOT skip the welcome: the year never reads 1835 before `api.ready`; the welcome shows no count or percentage; entering the town from the picker takes no pointer lock; a jaunt starts at stop 1 with Previous disabled; Next, Previous, Menu → Resume and End work; a mode change changes the travel mode and its ETA; the detail card ("About this place") opens and closing it returns to the same stop; a source opens from the card; End returns to the menu in < 200 ms; a second jaunt starts at its own stop 1; Explore Myself clears a paused jaunt; zero page errors.
2. Passes at 390×780 and 1280×800 on `--published`.
3. `tools/smoke_budget.mjs` maps the files this part covers to part 14 and prices it, and `--legs` keeps every nightly leg under its cap.
