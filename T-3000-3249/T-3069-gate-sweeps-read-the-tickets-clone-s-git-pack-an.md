---
id: T-3069
title: Gate sweeps read the tickets clone's git pack and run CI runners out of memory
state: done
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-23
closed: 2026-10-23
pr: 1238
claimed_by: run 10/23/2026, 7:26:26 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-23T13:08:31Z
claimed_run: null
claimed_at: 2026-10-23T12:26:27.440Z
decision: null
decision_answer: null
---

Gate sweeps read the tickets clone's git pack and run CI runners out of memory.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate and steward runs die mid-check: execute_roof_redeal.py --check-migration and --check-blocks each read tickets/.git's 1.9 GB pack as text (~10 GB apiece), so a 16 GB runner is shut down

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
