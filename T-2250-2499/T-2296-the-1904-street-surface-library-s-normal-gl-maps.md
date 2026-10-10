---
id: T-2296
title: The 1904 street-surface library's normal_gl maps are DirectX-handed: generate_prairie_1904_pbr.py writes (-dh/dx, -dh/drow, 1), so green is inverted on every street the renderer binds
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-10
closed: 2026-10-10
pr: 630
claimed_by: run 10/10/2026, 1:29:54 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-10T07:24:30Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38030853458
claimed_at: 2026-10-10T06:29:54.279Z
decision: null
decision_answer: null
---

The 1904 street-surface library's normal_gl maps are DirectX-handed: generate_prairie_1904_pbr.py writes (-dh/dx, -dh/drow, 1), so green is inverted on every street the renderer binds.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
