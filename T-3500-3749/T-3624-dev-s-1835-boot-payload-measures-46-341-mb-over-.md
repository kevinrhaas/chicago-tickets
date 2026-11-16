---
id: T-3624
title: dev's 1835 boot payload measures 46.341 MB over its 45.7 MB budget, so every PR's content build is red on smoke (desktop, 1-2) — measure what grew since T-3609's 45.437 reading and re-budget or cut
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: null
pr: null
claimed_by: run 11/16/2026, 5:44:39 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43980921923
claimed_at: 2026-11-16T23:44:40.698Z
decision: null
decision_answer: null
---

dev's 1835 boot payload measures 46.341 MB over its 45.7 MB budget, so every PR's content build is red on smoke (desktop, 1-2) — measure what grew since T-3609's 45.437 reading and re-budget or cut.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red: smoke (desktop, 1-2) refuses every PR's content build on the boot payload budget (PR #2125 refused on it, run 43974971949)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by steward slice 5/5, 2026-11-16, lapping PR #2125)

- `node tools/measure_boot_payload.mjs` on a local publish of dev `b80e51efc`: **46.341 MB** across 1331 requests, against the 45.7 MB budget (docs/SITE-BUDGET.md § 4o, T-3609, which read 45.437 MB across 1238 requests).
- CI content build run 43974971949 on PR #2125 (head 69e93b9d, dev through c640f9c46 plus a 1904-only diff) went red on `smoke (desktop, 1-2)` › *Enforce the first-visit boot payload budget* at **46.268 MB**. The PR changes only 1904 Prairie GLBs/records, which the 1835 first visit does not load.
- Heaviest folder `/data/prebuilt/1835/` at 26.121 MB (26.055 on the PR head; T-3609's reading had it near 25.86). The request count rose by about 93 since T-3609; dev took T-3621 (#2123, jaunt grade bands), #2122 and T-3605 (#2124, store back lots) since then. Use `--entries`/`--against` against a reading at T-3609's tree to say which.
