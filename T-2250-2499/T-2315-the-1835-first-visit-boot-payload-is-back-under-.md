---
id: T-2315
title: The 1835 first-visit boot payload is back under its 13 MB budget — dev publishes 14.513 MB, so smoke (desktop, 1-2) is red on every PR
state: open
epic: META
requested_by: loop
seen: false
effort: S
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

The 1835 first-visit boot payload is back under its 13 MB budget — dev publishes 14.513 MB, so smoke (desktop, 1-2) is red on every PR.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's own published mirror fails measure_boot_payload.mjs --check (14.513 MB > 13.000 MB), so the content build's smoke (desktop, 1-2) is red on every PR whatever its diff — #643 measured byte-identical to dev

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
