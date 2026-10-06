---
id: T-2149
title: The School Section tier's Monroe face fronts no street: plat_corridors.py carries no corridor for Monroe, so the frontage census, placement policy and redeal audit read every Monroe-face roof on blocks 81/94/95/118/119 as fronting none (Madison, 98 m off, is the nearest), the audit re-families three of block 81's houses and measure_block_redeal_remedies --self-test goes red. Rule how Monroe enters the frontage reading
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-05
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

The School Section tier's Monroe face fronts no street: plat_corridors.py carries no corridor for Monroe, so the frontage census, placement policy and redeal audit read every Monroe-face roof on blocks 81/94/95/118/119 as fronting none (Madison, 98 m off, is the nearest), the audit re-families three of block 81's houses and measure_block_redeal_remedies --self-test goes red. Rule how Monroe enters the frontage reading.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 156 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> it blocks three builds (T-2145, T-2146, T-2147), not one, so a paragraph on any one of them would hide it from the other two

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> T-2147's PR #493 gate is red on it, and T-2145/T-2146 build on the same Monroe face

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
