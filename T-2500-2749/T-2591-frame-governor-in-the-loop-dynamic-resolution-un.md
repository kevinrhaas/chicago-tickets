---
id: T-2591
title: Frame governor in the loop: dynamic resolution under the Sharpness ceiling, steady 30 fps pacing and halved shadow refresh while moving on light, its state in __chicago4d and Settings, Fixed, and still frames unchanged
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2555
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 6:50:00 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38892038527
claimed_at: 2026-10-16T11:50:00.939Z
decision: null
decision_answer: null
---

Frame governor in the loop: dynamic resolution under the Sharpness ceiling, steady 30 fps pacing and halved shadow refresh while moving on light, its state in __chicago4d and Settings, Fixed, and still frames unchanged.

Piece 1 of 2 of **T-2555 — A frame governor: dynamic resolution under the Sharpness ceiling, steady 30 fps pacing where 60 cannot hold, and shadow refresh halved while moving**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2555 was split (2026-10-16T11:49:48.076Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 35m ago, run 10/16/2026, 6:15:10 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38892038527) — held by the run that split it
- branch `steward/t2555-frame-governor` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38892038527) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. `renderers/web/js/frame-governor.js`, wired into `main.js`'s animation loop: while the camera moves, the drawing-buffer ratio scales between 0.67× and 1× of the visitor's Sharpness (the ceiling, never passed), with hysteresis; a device that cannot hold 60 at the floor and can hold 30 is paced to a steady 30 and probes 60 again; on `light` the shadow map refreshes every second moving frame. `tools/test_frame_governor.mjs`, a check.sh step, proves each of those on synthetic frame times.
2. At rest (three still frames), and always under Settings → Frame pacing → Fixed, the governor is neutral: `measure_walk_frames.mjs --live --stills` shows at every anchor of 1835 on the phone profile that a lowered ratio returns to the ceiling with a shadow every frame, and that the held frame under Adaptive is the same signature as under Fixed.
3. `__chicago4d.governor` reports mode, scale, ratio, ceiling, paced rate, shadow cadence and motion; Settings → Performance carries the choice and a line saying what it is doing; the smoke asserts both, with zero page errors, at 390×780 and 1280×800.
