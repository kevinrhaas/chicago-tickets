---
id: T-2899
title: The smoke's boot wait is the 90 s page default, not its 30 s: smoke_renderer.mjs:1778 passes { timeout: 30000 } as waitForFunction's arg, not its options; desktop boots on a loaded 4-core runner take 107-170 s and fail 'scene reaches ready' with zero page errors - pass the options in their slot and set the wait from a measured boot
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-19
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

The smoke's boot wait is the 90 s page default, not its 30 s: smoke_renderer.mjs:1778 passes { timeout: 30000 } as waitForFunction's arg, not its options; desktop boots on a loaded 4-core runner take 107-170 s and fail 'scene reaches ready' with zero page errors - pass the options in their slot and set the wait from a measured boot.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> found by three runs in PR #1112, each losing desktop smoke to it; no open ticket owns the smoke's boot wait

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
