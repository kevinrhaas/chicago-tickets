---
id: T-2774
title: The near ring's remaining sets on the GPU, so the near re-deal reaches zero: the heads hung from the GPU's deal and the CPU near walk retired (T-2717 read it unchanged at 2.6-3.4 ms a pass, because it still deals every near slot for the heads), then mid, forbs and far shrubs, each read with measure_walk_frames.mjs's near re-deal line at the throttled phone profile
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
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

The near ring's remaining sets on the GPU, so the near re-deal reaches zero: the heads hung from the GPU's deal and the CPU near walk retired (T-2717 read it unchanged at 2.6-3.4 ms a pass, because it still deals every near slot for the heads), then mid, forbs and far shrubs, each read with measure_walk_frames.mjs's near re-deal line at the throttled phone profile.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 144 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2708's acceptance (and T-2717's title) require the remaining sets filed as ONE follow-up; this is that filing, not new scope

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What T-2717 read (PR for T-2717; docs/measurements/t-2717-near-redeal-*.json)

Phone profile (390x780, 4x CPU throttle, `light`), SwiftShader, `measure_walk_frames.mjs --source`,
the commit before T-2716 against T-2716 itself, two interleaved runs each:

- **The near re-deal is not at zero.** A near pass's main thread: 2.6-2.9 ms median before,
  2.7-3.4 ms after (walk); 4.0 against 3.4-4.1 (turn). The CPU walk still deals every near slot
  (`dealNearSlot` + `placeGraminoid`, into `nearSink`) because the heads hang off the height it
  returns; the CPU profile shows those two at 61 + 79 ms before and 84 + 103 ms after over the
  three moves. The GPU deal pass adds 0.4-0.6 ms a pass on the main thread (42-65 ms over a
  walk's ~100 passes), and the kept tile's strip landings (`near-field.js` `land`) about 200 ms
  over the moves.
- The flight deals the GPU ring 9 times and uploads the tile 8 times with no near pass at all
  (the aerial has no near ring on screen): work the follow-up can drop.

**Acceptance:** the heads hung from the GPU's deal (no CPU `placeGraminoid` for a near tuft), the
CPU near walk retired, and `measure_walk_frames.mjs --only mobile --tiers light`'s `near re-deal`
line reading the main thread at the GPU pass's own cost alone; then mid, forbs and far shrubs
each moved and read the same way; critic captures passing, zero page errors.
