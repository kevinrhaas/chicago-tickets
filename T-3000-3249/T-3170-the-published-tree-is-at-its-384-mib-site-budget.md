---
id: T-3170
title: The published tree is at its 384 MiB site budget: dev stands about 3.4 MiB under it after T-3158's 1729 landed, so #1331 (T-3162, 1823 Prairie's textured web GLB, +3.43 MB over its 47 KB draft) reads 384.058 MB and fails check.sh's dataset step, green on all else; measure where the growth since T-2958/T-2959's 319.99 MiB went, hand bytes back (site_budget.py's largest and duplicate groups, the textured web GLBs) or re-budget with the whole-tree arithmetic (two allowances plus other site content under the 1 GiB Pages ceiling) and write the figure and why into validate.py's SITE_BUDGET_MB note and docs/SITE-BUDGET.md
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-26
closed: null
pr: 1338
claimed_by: run 10/26/2026, 7:33:29 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-26T12:33:30.317Z
decision: null
decision_answer: null
---

The published tree is at its 384 MiB site budget: dev stands about 3.4 MiB under it after T-3158's 1729 landed, so #1331 (T-3162, 1823 Prairie's textured web GLB, +3.43 MB over its 47 KB draft) reads 384.058 MB and fails check.sh's dataset step, green on all else; measure where the growth since T-2958/T-2959's 319.99 MiB went, hand bytes back (site_budget.py's largest and duplicate groups, the textured web GLBs) or re-budget with the whole-tree arithmetic (two allowances plus other site content under the 1 GiB Pages ceiling) and write the figure and why into validate.py's SITE_BUDGET_MB note and docs/SITE-BUDGET.md.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> #1331 (T-3162) is complete and green but for the site budget; every next textured Prairie house will fail the same step

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
