---
id: T-2311
title: CI's full-town bake rebuilds Glessner's light tier as bd1a614c67b3 while glessner_baseline.json and the committed package hold 8a51eea20569, so k01_contract fails and every PR's bake check reds (#631 x2, #632)
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-10
closed: null
pr: null
claimed_by: run 10/10/2026, 4:58:02 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38042968262
claimed_at: 2026-10-10T09:58:02.092Z
decision: null
decision_answer: null
---

CI's full-town bake rebuilds Glessner's light tier as bd1a614c67b3 while glessner_baseline.json and the committed package hold 8a51eea20569, so k01_contract fails and every PR's bake check reds (#631 x2, #632).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> the bake check is red on it for every K01 PR; #631 cannot merge on a green gate until it is fixed

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by the run lapping #631, 2026-10-10)

The `bake` check (a full `./tools/bake.sh`, then `check.sh`) failed identically on three PR heads:
#632 at 14439e54d (job 114168884414), #631 at 5074489b0 (job 114169096310), and #631 at
f50eaed45 (job 114182808191). Each time there are two red steps and nothing else: `k01_contract`
reports `✗ light: the baseline measured 8a51eea20569 but the package holds bd1a614c67b3 — the
asset was rebaked`, and its self-test `the committed baseline answers every measure and matches
the package` fails with it. None of those PRs touches Glessner, `web_derivatives.sh` or
`glessner_baseline.json`, and the rebuilt hash is the same every time, so this is a stable gap
between what the full bake derives for `glessner_house__as_built_1887.light.glb` and what dev has
committed, not noise in one PR. #632 merged on a later head that ran no bake check, so dev carries it.

**Acceptance:** a full bake on dev leaves `node tools/k01_contract.mjs --check` green. Either commit
the light tier the bake derives and re-measure (`--measure`), or make the derivation reproduce the
committed bytes; then #631 (T-2293) can re-gate and merge.
