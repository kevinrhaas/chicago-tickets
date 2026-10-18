---
id: T-2824
title: Phone boot upload pass: draws rejected before the first shadow map (sampler2DShadow on unit 0)
state: open
epic: META
requested_by: owner
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

Phone boot upload pass: draws rejected before the first shadow map (sampler2DShadow on unit 0).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 160 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Found while fixing T-2822: every 1904 phone boot logs ~245 GL_INVALID_OPERATION from uploadLayerNow; letting the draws through cost +40-70 MB GPU-process PSS in SwiftShader, so it needs measuring before it ships

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
