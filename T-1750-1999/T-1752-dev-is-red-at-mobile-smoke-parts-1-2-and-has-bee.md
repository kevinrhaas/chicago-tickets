---
id: T-1752
title: dev is RED at mobile smoke parts 1-2 and has been since 2026-09-28: the frontage census has drifted a walk, a crossing and two fence runs past the exact counts the suite asserts, and no CI check looks at it
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
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

dev is RED at mobile smoke parts 1-2 and has been since 2026-09-28: the frontage census has drifted a walk, a crossing and two fence runs past the exact counts the suite asserts, and no CI check looks at it.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A standing red on the integration branch that no automated gate can see: chicago-4d-check.yml runs no smoke at all, so only a steward run that pays for mobile parts 1-2 finds it, and until 2026-09-29 the register had no reading for part 2 since 02:00 the previous day. Measured twice tonight on clean origin/dev worktrees (1b01e8b8 and 88298203) with byte-identical figures, and confirmed NOT caused by the T-1547 branch that found it. It blocks nothing today and fits no existing ticket, but every run from here that touches the frontage layer will re-derive it at 3 minutes a time.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## WHAT WAS MEASURED, SO NOBODY PAYS FOR IT AGAIN

`SMOKE_VIEWPORT=mobile SMOKE_STAGE=1-2 node tools/smoke_renderer.mjs --published`,
155 passed / 3 failed in ~3 m 10 s, on THREE trees: a clean `origin/dev` worktree at
1b01e8b8 (`sha256:5ac5ddd5db6c72fe`), and the T-1547 branch before and after dev gained
T-0474 (`sha256:63df416ceaeb86ba`, `sha256:054f15e75afe3d85`). The figures are
BYTE-IDENTICAL on all three:

| the three failing checks | measured | the suite asserts |
| --- | ---: | ---: |
| the frontage layer lays all five records' walks and stands their posts | 48 walks, 40 crossings, 18 posts, 29 fence runs, 852960 vertices, 122 refusals, problems [none] | 47 walks, 39 crossings, 18 posts, 31 fences |
| the frontage layer draws the meshes it authored | 55 authored (frontage, frontage-chunk x54), 0 far-merge artefacts, 55 drawn | — |
| the street edge is generated from the plat, not placed on one block | 37 block faces, 3323.3 m of walk, 29 fence runs, 262 walking decks | — |

`problems [none]` is the tell: nothing in the scene is wrong. The counts baked into
`tools/smoke_renderer.mjs` are a commit behind the town, which is the same "left a count
behind" failure its own comment block records against T-0024, T-0028 and T-0244.

WHERE THE DRIFT CAME FROM, most likely: the last tier's building programme. A roof
arriving on a platted lot retires a street fence whenever its wall stands inside the
3.0 m a fence needs (the clause T-0028, T-0380 and T-0461 are each recorded against),
and dev took T-1717, T-1734 and T-1736 between the register's last PASS on part 1
(2026-09-28T21:18) and this reading. Two fences down and a walk and a crossing up is
that shape. **Verify it before writing it down** — the census is not `problems`, and a
count that moved for a second reason would be missed by assuming the first.

IT IS INVISIBLE TO CI ON PURPOSE-ISH: `.github/workflows/chicago-4d-check.yml` runs
`check.sh` and no smoke at all, so the dev gate is green while this is red. That is why
it went four merges without being seen, and why the fix should land the counts AND a
line in the register.

**Acceptance:** mobile parts 1-2 are SMOKE PASS on a clean `origin/dev` worktree; every
count moved in `tools/smoke_renderer.mjs` carries a comment naming the ticket and the
cause that moved it, in the style the surrounding block already uses; and no count is
changed to match a scene that is actually wrong — each of the four figures is argued
from the rule that produced it, not fitted.
