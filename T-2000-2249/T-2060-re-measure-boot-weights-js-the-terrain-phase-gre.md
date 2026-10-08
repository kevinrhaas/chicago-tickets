---
id: T-2060
title: Re-measure boot-weights.js: the terrain phase grew 0.7 to 3.7 s and the boot moved 25-70 % since its reading
state: review
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: 517
claimed_by: run 10/8/2026, 1:57:14 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37739222202
claimed_at: 2026-10-08T06:57:14.629Z
decision: null
decision_answer: null
---

Re-measure boot-weights.js: the terrain phase grew 0.7 to 3.7 s and the boot moved 25-70 % since its reading.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 203 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1272's acceptance requires every unmet budget to leave as a named successor, and no open ticket owns this: T-2047 measured it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Found by T-2047 (2026-10-04), the measurement this ticket starts from

T-1272's acceptance re-measures `renderers/web/js/boot-weights.js` when the boot moves
more than 10 %. It moved. `measure_boot_phases.mjs --published --json`, all 12 cells, dev
@ `cb56e2e4` against `c2dd2ea1` (the tree before the arrival section) on the SAME steward
runner: time to ready **+25 % to +70 %** per cell (mobile light cold 12.06 → 17.89 s), and
every phase but census moved more than 10 % in most cells. The largest single move is the
**terrain phase, 0.72 → 3.71 s**, one ~2.9 s long task at its start; it was already
3.72 s on `49d0a226` (2026-10-02), so it came in with the ground/terrain work of 09-26 to
10-02 (the T-1797, T-1812, T-1819, T-1825 band), not with the arrival.

T-2047 did NOT rewrite the weights. They were read on an Apple M5 Max (the file's own
header); this runner draws with software WebGL and reads every phase 4-8× slower. The
weights pace the arrival's progress for a visitor with no timing history, so swapping in
the runner's seconds would re-pace every first visit on an inference about a machine
nobody has measured. Decide the machine first: re-read on the reference machine, or
argue (in this ticket) that the runner's PROPORTIONS may stand in, and then regenerate
with `tools/measure_boot_phases.mjs --published --json` and its receipt
`tools/boot_phase_measurements.json` together. Receipts of both runs are in
`docs/measurements/arrival_jaunts_acceptance_2026-10.md`.
