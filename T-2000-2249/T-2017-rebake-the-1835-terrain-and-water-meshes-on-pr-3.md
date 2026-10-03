---
id: T-2017
title: Rebake the 1835 terrain and water meshes on PR #329's branch, for South Water's carried 22 m
state: review
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: 329
claimed_by: run 10/3/2026, 1:37:51 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37103533927
claimed_at: 2026-10-03T06:37:51.445Z
decision: null
decision_answer: null
---

Rebake the 1835 terrain and water meshes on PR #329's branch, for South Water's carried 22 m.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 214 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> PR #329 (T-2012, owner-approved) cannot pass its gate without it, and only a pinned-Blender runner can rebuild the meshes

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #329's gate is red on terrain__e1834_harbor_cut and water__e1834_harbor_cut, stale against the regenerated heightfield

**Acceptance:** `terrain__e1834_harbor_cut.glb` and `water__e1834_harbor_cut.glb` are rebuilt under the pinned Blender from the heightfield committed on branch `claude/road-grass-artifacts-96hemx` (PR #329), with their web derivatives, and pushed to THAT branch, so `python3 tools/validate.py --all` reports neither as stale and the terrain fit gates pass. Nothing else on the branch changes.

**What to run** (on a checkout of `claude/road-grass-artifacts-96hemx`, from `chicago/4d`):

```
"$BLENDER" -b -noaudio --factory-startup --python generators/terrain_gen.py -- --epoch e1834_harbor_cut --glb
tools/web_derivatives.sh --only terrain__e1834_harbor_cut.glb
tools/web_derivatives.sh --only water__e1834_harbor_cut.glb
./tools/check.sh
```

Commit as `T-2017: rebake the 1835 terrain and water for South Water's carried 22 m` and push to the branch. The heightfield is already regenerated there (commit 42503f5a: 50 cells under the new stretch move by -0.29 to +0.13 m). Do not open a second PR; T-2012's PR carries the change. If the gate shows anything else red, report it on PR #329 rather than widening this.
