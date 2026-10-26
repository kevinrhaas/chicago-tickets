---
id: T-3173
title: 1904 desktop memory 1171.2 MB over its 1125 MiB ceiling: unmeasured since 2026-10-24 while the frame-time nightly died installing Playwright on ubuntu-26.04 (T-3169 un-blinded it on PR #1339); bring the 1904 scene down or argue a new ceiling in tools/memory_ceilings.json with its reading
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-26
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

1904 desktop memory 1171.2 MB over its 1125 MiB ceiling: unmeasured since 2026-10-24 while the frame-time nightly died installing Playwright on ubuntu-26.04 (T-3169 un-blinded it on PR #1339); bring the 1904 scene down or argue a new ceiling in tools/memory_ceilings.json with its reading.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #1339 (T-3169, which unblocks every content build) is refused on this check; dev's frame-time nightly will be red on it too

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
