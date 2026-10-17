---
id: T-2723
title: The gaze target's GPU pick stops stalling the frame: target.js's look reads back asynchronously (or raycasts on the CPU while moving) instead of a synchronous readPixels on the main thread every 500 ms of movement, with the moving p95 read before and after
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-17
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

The gaze target's GPU pick stops stalling the frame: target.js's look reads back asynchronously (or raycasts on the CPU while moving) instead of a synchronous readPixels on the main thread every 500 ms of movement, with the moving p95 read before and after.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 140 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> no open ticket owns it: a synchronous GPU readback in the moving frame loop is a periodic stall on every device, the kind of uneven frame the governor (T-2555) exists to remove and cannot, and it is a code change of its own, not a paragraph on T-2721's measurement

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (T-2721's run, 2026-10-17) — where it was found

`measure_walk_frames.mjs --live --gl llvmpipe --profile 10` (phone profile, `light`, walk, turn
and flight, Adaptive then Fixed, 72 s of moves) put **63 of 72 s** of the main thread in
`readPixels`, reached as `tick main.js` → `look target.js` → `pick main.js` → `pickAt` →
`gpuPick gpu-pick.js:171`: the gaze target's one-pixel pick, one per structure layer
(buildings, enclosures, frontage), every 500 ms while the eye moves. A synchronous readback
waits for the GPU to finish everything queued before it, so on this software runner it is
the whole multi-second frame; on a phone it is a pipeline flush on the main thread twice a
second of walking — a late frame on a rhythm, which is what "uneven" means and what the frame
governor (T-2555) cannot trim. Readings: `docs/measurements/t-2721-live-llvmpipe-mobile.json`
(`profiles.mobile.totalMs`) and, with `--no-gaze` holding the look off, `…-no-gaze.json`.

**Before/after for this ticket:** the same command with and without the change, on hardware
whose frame costs tens of milliseconds if T-2722's answer provides it; on this runner, the
`--no-gaze` reading is the floor the change can reach (no `readPixels` in the profile).
