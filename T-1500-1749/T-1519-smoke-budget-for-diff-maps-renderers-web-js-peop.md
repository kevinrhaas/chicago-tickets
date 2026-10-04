---
id: T-1519
title: smoke_budget --for-diff maps renderers/web/js/people.js to part 13, but the People directory's checks are guarded by stageOn(12), so a run that trusts the mapping runs the wrong leg
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-21
closed: null
pr: null
claimed_by: run 10/4/2026, 1:56:31 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37184150156
claimed_at: 2026-10-04T06:56:31.665Z
decision: null
decision_answer: null
---

smoke_budget --for-diff maps renderers/web/js/people.js to part 13, but the People directory's checks are guarded by stageOn(12), so a run that trusts the mapping runs the wrong leg.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
