---
id: T-3049
title: Smoke part 14's 1904 placement list (PLACED_1904 in tools/smoke_renderer.mjs) is missing the 27 Indiana Avenue / First Presbyterian drafts already on dev, so the check 'the 1904 scene draws none of the 1835 town's layers' fails at both viewports on clean dev; add them
state: withdrawn
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-22
closed: 2026-10-23
pr: null
claimed_by: run 10/23/2026, 2:11:34 AM CT
blocked_on: duplicate of T-3057 (#1230, merged 2026-10-23 07:07Z), which added the 27 Indiana Avenue / First Presbyterian drafts to PLACED_1904; on dev bfe88a6e5 the list holds exactly the 222 ids of data/sidecars/1904/index.json, and smoke part 14 at 390x780 --published passed 140/140 with 'the 1904 scene draws none of the 1835 town's layers' green
needs_bake: false
closed_at: 2026-10-23T07:20:31.325Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39915699500
claimed_at: 2026-10-23T07:11:36.079Z
decision: null
decision_answer: null
---

Smoke part 14's 1904 placement list (PLACED_1904 in tools/smoke_renderer.mjs) is missing the 27 Indiana Avenue / First Presbyterian drafts already on dev, so the check 'the 1904 scene draws none of the 1835 town's layers' fails at both viewports on clean dev; add them.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
