---
id: T-2555
title: A frame governor: dynamic resolution under the Sharpness ceiling, steady 30 fps pacing where 60 cannot hold, and shadow refresh halved while moving
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
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

A frame governor: dynamic resolution under the Sharpness ceiling, steady 30 fps pacing where 60 cannot hold, and shadow refresh halved while moving.

## Why

"Jittery" is often not a slow frame but an **uneven** one. A phone that alternates 16 ms and 33 ms frames reads as stutter, while a phone held at a steady 33 ms reads as smooth. Nothing in the renderer adapts to the device: pixel ratio is fixed by the Sharpness setting (`main.js` ≈ 1517, T-2110), shadow maps re-render every frame, and the loop draws as fast as rAF fires. T-2105 / T-2106 measured and cut the worst moving costs. This ticket holds the frame steady on whatever device is left.

## What

- **A frame governor in `main.js` `tick`:** read frame time (`EXT_disjoint_timer_query_webgl2` for GPU time where present, rAF delta otherwise) into a short window.
  - **Dynamic resolution:** scale the drawing-buffer ratio between a floor (e.g. 0.67 × the Sharpness ratio) and the visitor's Sharpness ratio as a **ceiling**, with hysteresis. The ratio always returns to the ceiling when the camera is still, so still frames and every capture are unchanged.
  - **Frame pacing:** on a device that cannot hold 60, pace to a steady 30 (render every other rAF) instead of oscillating.
  - **Shadow refresh:** while moving on `light`, update the sun's shadow map every 2nd frame (the sun does not move during a walk). Always on rest.
- Report what it did in `__chicago4d` (current ratio, paced rate) and as a small line in Settings → Performance. Settings keep the last word, and a "Fixed" choice disables the governor.

## Acceptance

1. `measure_walk_frames.mjs` at the throttled phone profile: **frame-time standard deviation and p95 both fall** for walk, turn and flight at `light`, against today's committed reading. Quote both.
2. Still-frame captures at every anchor are byte-identical to today (the governor is at the ceiling at rest).
3. The smoke asserts the governor's state API and zero page errors at both viewports.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

