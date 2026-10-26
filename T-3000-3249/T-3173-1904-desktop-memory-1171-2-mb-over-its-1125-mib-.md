---
id: T-3173
title: 1904 desktop memory 1171.2 MB over its 1125 MiB ceiling: unmeasured since 2026-10-24 while the frame-time nightly died installing Playwright on ubuntu-26.04 (T-3169 un-blinded it on PR #1339); bring the 1904 scene down or argue a new ceiling in tools/memory_ceilings.json with its reading
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-26
closed: null
pr: null
claimed_by: Codex root transport memory recovery continuing original measured target and safe DEV integration 10/26/2026, 5:29:46 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-26T22:29:47.125Z
decision: null
decision_answer: null
---

1904 desktop memory 1171.2 MB over its 1125 MiB ceiling: unmeasured since 2026-10-24 while the frame-time nightly died installing Playwright on ubuntu-26.04 (T-3169 un-blinded it on PR #1339); bring the 1904 scene down or argue a new ceiling in tools/memory_ceilings.json with its reading.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #1339 (T-3169, which unblocks every content build) is refused on this check; dev's frame-time nightly will be red on it too

**Acceptance:** (state it before working — the definition of done, never weakened to pass)


## Acceptance and transport delivery findings

The current transport delivery also hits this existing memory blocker. Reduce actual native 1904 memory below the unchanged 1125 MiB desktop and 400 MiB mobile limits. Preserve Full-quality texture pixels and sampler behavior, apply the already documented Light texture tier consistently, and verify texture eviction/refill and context recovery without browser errors. A source-only or mocked-loader PASS is insufficient: require actual native browser memory readings, the complete source gate, and current normal CI before DEV merge.

Exact wagon source35f64 CI run40373250666 failed1904 desktop1174.7 MiB and mobile454.0 MiB; other1812/1835 readings and still-frame jobs passed. The guarded historical local carriage E97 mobile baseline measured446.8 MiB; its source, mirror, metric breakdown and cleanup are retained. Existing source arrays are already released in several paths, so estimates alone do not establish a new saving.

A concrete external proposal applies Light mip selection to embedded GLB KTX2 images and releases uploaded desktop compressed levels while retaining encoded recovery data. It remains unadopted and unqualified by the actual browser meter. No ceiling increase, unchanged CI rerun or waiver is proposed. Checked transport source/evidence checkpoint: kevinrhaas/chicago-evidence, commit73375c5ba46b892f0e56b56278e9b5d1665e6292, evidence/transport-photoquality-2026-10-26/CHECKPOINT-07-CHECKED-SOURCES-AND-CANONICAL-OUTPUTS.
