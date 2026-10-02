---
id: T-1975
title: The full and balanced ceilings and the draw-call budget re-measured at every stand at both viewports and set where they are defined, T-1154 reconciled
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1974
opened: 2026-10-02
closed: 2026-10-02
pr: 281
claimed_by: run 10/2/2026, 9:49:09 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T15:30:12Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37018377388
claimed_at: 2026-10-02T14:49:09.580Z
decision: null
decision_answer: null
---

The full and balanced ceilings and the draw-call budget re-measured at every stand at both viewports and set where they are defined, T-1154 reconciled.

Piece 1 of 2 of **T-1974 — The detail ceilings and the draw-call budget re-measured at every stand and set where they are defined, T-1154 reconciled, smoke green at both viewports**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

`tools/measure_detail_ceilings.mjs` read on the published mirror of dev at both release viewports,
committed beside T-1154's reading; `full` and `balanced` set in `renderers/web/js/main.js` `DETAIL`
to the measured worst stand plus the absolute headroom T-0672 recorded (18,059 / 16,806), rounded
up to the nearest 5,000, with the reasoning written at the definition; the draw-call budget set the
same way in `BUDGET` and in the smoke's pinned check, in the same commit; T-1154's figures
reconciled against today's reading in its own ticket. `light` does not move — it is T-1976's, by
AGENTS.md's floor rule — and check.sh is green.
