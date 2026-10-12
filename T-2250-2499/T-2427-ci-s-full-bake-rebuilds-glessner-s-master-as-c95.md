---
id: T-2427
title: CI's full bake rebuilds Glessner's master as c95d93560e34 (web 2bfe5e7e3939) while T-2416 (#741) committed 303b5cb63b5e (web 92315d701c2a), so k01_contract fails and dev's bake check reds
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-12
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

CI's full bake rebuilds Glessner's master as c95d93560e34 (web 2bfe5e7e3939) while T-2416 (#741) committed 303b5cb63b5e (web 92315d701c2a), so k01_contract fails and dev's bake check reds.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by the run lapping #739, 2026-10-12)

The `bake` check (a full `./tools/bake.sh`, then `check.sh`) failed identically on dev and on a PR:
dev at c10232a38, the #741 merge (content build run 38303866796), and #739 at 6bf19136b (lapped
onto dev dba5cf604). Each time it is the same two red steps and nothing else: `k01_contract`
reports `✗ full: the baseline measured 303b5cb63b5e but the package holds c95d93560e34` and
`✗ web: … 92315d701c2a but the package holds 2bfe5e7e3939` (plus the light, which is derived from
that master), and its self-test `the committed baseline answers every measure and matches the
package` fails with it. The full and web hashes CI derives are the same on both trees, so this is a
stable gap between what the pinned bake derives for `glessner_house__as_built_1887.glb` and what
#741 committed, not noise in one PR. It is T-2311's failure (done, #645) again, on the master this time.

**Acceptance:** a full bake on dev leaves `node tools/k01_contract.mjs --check` green. Either commit
the master the bake derives (then web, light, `recover_glessner_v4.py --pack`, `k01_contract.mjs
--measure`), or make the master reproduce the committed bytes, and say in the PR which, and why the
two diverged.
