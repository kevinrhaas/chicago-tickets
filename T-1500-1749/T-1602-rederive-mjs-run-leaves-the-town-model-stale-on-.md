---
id: T-1602
title: rederive.mjs --run leaves the town model stale on any branch that adds residents: model_town_1835.py reads the sidecar compile_scene rebuilds after it, and the second pass does not carry it, so a clean full rebuild still fails check.sh
state: open
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
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

rederive.mjs --run leaves the town model stale on any branch that adds residents: model_town_1835.py reads the sidecar compile_scene rebuilds after it, and the second pass does not carry it, so a clean full rebuild still fails check.sh.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
