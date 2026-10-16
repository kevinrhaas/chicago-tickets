---
id: T-2597
title: The boot fetch bounded: loadScene's per-structure loads run through a concurrency pool instead of an unbounded Promise.all, and the boot-time peak of GLB bytes held at once measured before and after and quoted
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2554
opened: 2026-10-16
closed: null
pr: 884
claimed_by: run 10/16/2026, 9:04:07 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330
claimed_at: 2026-10-16T14:04:07.082Z
decision: null
decision_answer: null
---

The boot fetch bounded: loadScene's per-structure loads run through a concurrency pool instead of an unbounded Promise.all, and the boot-time peak of GLB bytes held at once measured before and after and quoted.

Piece 1 of 2 of **T-2554 — 1904 texture residency: textured houses resident by distance under a per-tier texture budget, uploads paced per frame, and the boot fetch bounded**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2554 was split (2026-10-16T14:03:56.849Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 9:03:51 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330) may be working one of the pieces now.

**Acceptance:** (the title's ask, unchanged)

1. `loadScene`'s per-structure loads run through a bounded pool instead of one unbounded `Promise.all`.
2. The boot-time peak of GLB bytes held at once is measured before and after, per year × viewport, and quoted; it falls.

## Measured (2026-10-16), and what it refutes

`tools/measure_boot_peak.mjs` (new): the published mirror over HTTP/2 (so "unbounded" is unbounded, as on the live host), every request delayed 60 ms, `?boot-pool=N` against `?boot-pool=0` in one build. "Held" is the loader's own exact count of GLB bytes fetched and not yet parsed (`__chicago4d.bootPool`).

| year · viewport | pool | held peak | boot |
|---|---|---|---|
| 1904 phone | unbounded | 31.1 MB in 131 GLBs | 39.1 s |
| 1904 phone | 24 | 38.3 MB in 23 | 38.6 s |
| 1904 phone | 8 | 37.7–37.9 MB in 8 | 39.9–40.0 s |
| 1904 desktop | unbounded | 56.4 MB in 150 | 76.6 s |
| 1904 desktop | 24 | 63.6 MB in 23 | 74.7 s |
| 1835 phone | unbounded | 12.9–13.4 MB in 658–683 | 37.3 s |
| 1835 phone | 8 | 0.2 MB in 8 | 42.4–43.0 s |
| 1835 phone | 24 | 0.5 MB in 24 | 39.1 s |
| 1835 phone | 48 | 1.2 MB in 46 | 38.0 s |

- **On 1904 the unbounded pile is ONE file**: 56.4 MB is exactly `glessner_house__as_built_1887.glb`, 31.1 MB exactly its `.light.glb`. The small houses parse as they land. A pool holds its other slots' files *beside* Glessner, so every pool read higher, and no count pool can go under the largest file. Acceptance 2 fails for 1904 by measurement, not by implementation.
- **On 1835 the pool works and is not worth it**: 13 MB of a boot whose sampled ArrayBuffer peak is above 400 MB (3 %), for +5 s of boot at pool 8 (686 loads in 8 lanes, ~86 round trips end to end).
- The sampled tab-wide ArrayBuffer peak (`Runtime.getHeapUsage`, every 25 ms) did not separate any pool from unbounded beyond its run-to-run noise (±30 MB); the whole-boot peak sits in the layers built after `loadScene` returns.

**Outcome:** the default stays unbounded (`BOOT_POOL = Infinity`, the reading written at it). Shipped: the meter, the loader's held-bytes count, and `?boot-pool=N` for trying a pool against today. What does shrink the 1904 boot pile is the Glessner file itself: T-2596 (Glessner v4 in KTX2, light tier capped at 1024). Acceptance 1 is therefore NOT met as a default, deliberately; the PR says so.
