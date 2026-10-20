---
id: T-2824
title: Phone boot upload pass: draws rejected before the first shadow map (sampler2DShadow on unit 0)
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: 2026-10-19
pr: 1112
claimed_by: run 10/19/2026, 7:57:45 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-20T03:06:03Z
claimed_run: null
claimed_at: 2026-10-20T00:57:45.796Z
decision: null
decision_answer: null
---

Phone boot upload pass: draws rejected before the first shadow map (sampler2DShadow on unit 0).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 160 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Found while fixing T-2822: every 1904 phone boot logs ~245 GL_INVALID_OPERATION from uploadLayerNow; letting the draws through cost +40-70 MB GPU-process PSS in SwiftShader, so it needs measuring before it ships

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (PR #1112, 2026-10-20)

The cost T-2822 saw is the boot draws themselves, not the shadow map: lending the sun a 1x1 comparing depth map for the pass makes every draw valid and costs nothing on its own, but executing the unculled boot draws keeps +67-74 MB in SwiftShader's GPU process after settling (three interleaved rounds, /1904/, 390x780 dpr 3; `docs/measurements/t-2824-boot-upload-pass.json`). Plausibly ANGLE converting vertex/index formats per drawn chunk, which iOS might share; not proven. So the pass now holds the context's draw calls for its length: uploads unchanged (memory meter 354.2 -> 354.3 MB), 267 -> 0 GL_INVALID_OPERATION. The boot pass never warmed draw-time state (pipelines), before or after; the code comment says so. Possible band-9 follow-up: `measure_memory.mjs` reading GPU-process PSS and a GL-error count, so readings like these need no scratch probe.
