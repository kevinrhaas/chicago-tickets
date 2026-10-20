---
id: T-2959
title: The published tree stands at 319.99 of its 320 MiB site budget on dev (0.01 MiB left, dev gate 2026-10-20 19:17Z), so any PR that adds bytes fails validate.py's site check: #1152 (1812 Prairie's gable, +19 KB on its web GLB) is complete and green but for this; win back headroom (site_budget.py's largest and duplicate groups, the textured web GLBs) or re-budget with the measured whole-tree arithmetic T-2595 used (two allowances plus other site content under the 1 GiB Pages ceiling), and write the new figure and why into validate.py and docs/SITE-BUDGET.md
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-20
closed: 2026-10-20
pr: 1155
claimed_by: run 10/20/2026, 2:26:56 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-20T20:04:47Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39482826693
claimed_at: 2026-10-20T19:26:56.799Z
decision: null
decision_answer: null
group: T-2958,T-2959
---

The published tree stands at 319.99 of its 320 MiB site budget on dev (0.01 MiB left, dev gate 2026-10-20 19:17Z), so any PR that adds bytes fails validate.py's site check: #1152 (1812 Prairie's gable, +19 KB on its web GLB) is complete and green but for this; win back headroom (site_budget.py's largest and duplicate groups, the textured web GLBs) or re-budget with the measured whole-tree arithmetic T-2595 used (two allowances plus other site content under the 1 GiB Pages ceiling), and write the new figure and why into validate.py and docs/SITE-BUDGET.md.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 140 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a dev-wide wall no open ticket owns: every PR that adds a byte to site/4d fails validate.py until headroom is won or the budget re-measured, so it cannot be a paragraph on one building's ticket

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate passes with 0.01 MiB left, so T-2951's PR #1152 and every other PR that publishes bytes is red on the site budget

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
