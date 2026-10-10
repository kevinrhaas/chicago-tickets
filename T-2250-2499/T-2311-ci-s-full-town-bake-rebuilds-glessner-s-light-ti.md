---
id: T-2311
title: CI's full-town bake rebuilds Glessner's light tier as bd1a614c67b3 while glessner_baseline.json and the committed package hold 8a51eea20569, so k01_contract fails and every PR's bake check reds (#631 x2, #632)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-10
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

CI's full-town bake rebuilds Glessner's light tier as bd1a614c67b3 while glessner_baseline.json and the committed package hold 8a51eea20569, so k01_contract fails and every PR's bake check reds (#631 x2, #632).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> the bake check is red on it for every K01 PR; #631 cannot merge on a green gate until it is fixed

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
