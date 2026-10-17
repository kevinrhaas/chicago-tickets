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
