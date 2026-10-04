---
id: T-2047
title: Budgets, legacy surfaces and the arrival-jaunts acceptance report, with a STATUS section and named successors
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1272
opened: 2026-10-03
closed: null
pr: 377
claimed_by: run 10/3/2026, 7:59:50 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37166472201
claimed_at: 2026-10-04T00:59:50.420Z
decision: null
decision_answer: null
---

Budgets, legacy surfaces and the arrival-jaunts acceptance report, with a STATUS section and named successors.

Piece 4 of 4 of **T-1272 — Verify arrival, jaunts and source browsing on the published mobile app**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## 2026-10-04 — acceptance, stated before the work (slice 3/5)

One report, `docs/measurements/arrival_jaunts_acceptance_2026-10.md`, and a STATUS.md
section, that read on dev the four things this piece owns and leave nothing relabelled:
1. **Payload** — `measure_boot_payload.mjs --check` on the published mirror, attributed
   per path against T-1973's tree where the 13 MB budget was set; the section's lazy files
   (catalog, jaunt files, source index) shown absent from the boot list.
2. **Boot phases** — `measure_boot_phases.mjs --published --json`, all 12 cells, dev
   against the tree before the arrival section, on one machine; `--check`'s heartbeat read.
3. **Frame cost** — the detail ceilings at the gate's stands against `DETAIL`.
4. **Legacy surfaces** — the existing smoke parts for the popup, Evidence and People
   pass, run in the foreground on this branch.
Each budget that fails is either fixed here (if the section caused it) or leaves as a
named successor with its measurement written into it. Budgets are not raised.


## Finding from T-2046 (layouts) — a successor for the report to name

`tools/measure_arrival_layouts.mjs` gates the controls the path owns (the welcome, the
jaunt panel, the context card) at 44px and **reports, without gating**, the ones owned by
other surfaces that the path still reaches on touch. Reading of 2026-10-04
(`docs/measurements/arrival-layouts.json`, `elsewhere` per layout):

- HUD chips are 38px tall at every touch layout (Start / Jaunts, Confidence, ▾ 26px wide,
  Walk, Fly, theme, Menu). Raising them to 44 moves the wrapped HUD's foot from ~92px to
  ~104px, so the jaunt panel's and the overlays' `100px` top at ≤900px moves with it.
- The drawer's Back and Close are 30x30; its eight tabs are 37px wide at 320px.
- The place card's inline `why` toggles are 19x17 (its firm buttons were raised to 44 on
  touch by T-2046).

These belong to the HUD, drawer and card contracts, not the path's, so T-2046 did not
change them. The acceptance report should name them as one successor (or fold them into
an existing HUD/drawer ticket) rather than as a tail line.
