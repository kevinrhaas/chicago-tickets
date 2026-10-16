---
id: T-2592
title: Frame governor's moving reading: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read where a frame costs inside the governor's range (the steward runner's SwiftShader draws one in 2.3 to 3.6 s)
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2555
opened: 2026-10-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Frame governor's moving reading: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read where a frame costs inside the governor's range (the steward runner's SwiftShader draws one in 2.3 to 3.6 s).

Piece 2 of 2 of **T-2555 — A frame governor: dynamic resolution under the Sharpness ceiling, steady 30 fps pacing where 60 cannot hold, and shadow refresh halved while moving**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2555 was split (2026-10-16T11:49:48.076Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 35m ago, run 10/16/2026, 6:15:10 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38892038527) — held by the run that split it
- branch `steward/t2555-frame-governor` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38892038527) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. `measure_walk_frames.mjs --live` (T-2591 adds it: the moves driven through the page's own loop, draw on, Adaptive then Fixed in one page) at the phone profile and `light`: frame-time standard deviation AND p95 both fall for walk, turn and flight under Adaptive against Fixed. Quote both.

## Finding (T-2591's run, 2026-10-16) — why this is its own piece

The steward runner has no GPU. Driven through the live loop in the town (welcome dismissed) with the draw on, the 1835 phone frame (390×780, ratio 1, `light`) came **every 2.3 to 3.2 s unthrottled, and about 3.6 s at the 4× throttle** — while the `renderer.render` call itself returned in a median **7 to 10 ms** (`docs/measurements/t-2555-governor-live-mobile.json`, `draw median`). So the time is outside the submitted draw: SwiftShader rasterising in the GPU process, which the next rAF waits on, is the likely owner (not yet proved). Either way it is about a hundred times outside the range a frame governor works in: every interval is over the governor's 250 ms gap cut and is read as a gap, so it decides nothing and Adaptive and Fixed read alike (walk sd 25 → 37 ms, turn 550 → 551, flight 109 → 100, at five or six draws each: noise). A reading that "fell" there would be measuring the noise. This needs a renderer whose frame costs tens of milliseconds: a real phone or a GPU runner, or a cheaper software path that is argued for as a stand-in before it is read.
