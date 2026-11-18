---
id: T-3655
title: dev's Full X-RAY view in 1835 draws 3,842,482 triangles against its 3,785,000 budget (smoke desktop 13, T-2981)
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: null
claimed_by: run 11/18/2026, 9:43:01 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/44334675206
claimed_at: 2026-11-18T15:43:01.866Z
decision: null
decision_answer: null
---

dev's Full X-RAY view in 1835 draws 3,842,482 triangles against its 3,785,000 budget (smoke desktop 13, T-2981).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by the loop, 2026-11-18)

- dev's own content build, run 44296188805 on aadceb658, job `smoke (desktop, 13)`:
  `FAIL Full X-RAY triangles stay inside the declared view budget (T-2981) —
  {"year":"1835","detail":"full","ghosting":true,"calls":8188,"triangles":3842482,
  "budget":{"drawCalls":8900,"triangles":3785000}}` (the job was then cancelled).
- The identical reading, to the triangle, on PR #2111's content build (run 44302630485,
  0d463bd72): that PR adds a 1904 building and nothing to 1835, so this is dev's red.
- `tools/dev-smoke-state.json` still records desktop part 13 PASS from 2026-11-11, so the
  overage arrived between then and aadceb658.
