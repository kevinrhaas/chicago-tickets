---
id: T-2492
title: bake.sh --only on pure-Python archetypes (K01/K12/K13/K16/draft) dies in build.py's 'built nothing' exit 1 before their emitters run — so a content build dispatched with only=<K16 id> is red on every such PR (#770, run 38454631755); let build.py signal 'nothing for Blender' distinctly and leave bake.sh's empty-WROTE guard as the refusal
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: run 10/15/2026, 7:28:05 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38734305774
claimed_at: 2026-10-15T12:28:05.972Z
decision: null
decision_answer: null
---

bake.sh --only on pure-Python archetypes (K01/K12/K13/K16/draft) dies in build.py's 'built nothing' exit 1 before their emitters run — so a content build dispatched with only=<K16 id> is red on every such PR (#770, run 38454631755); let build.py signal 'nothing for Blender' distinctly and leave bake.sh's empty-WROTE guard as the refusal.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
