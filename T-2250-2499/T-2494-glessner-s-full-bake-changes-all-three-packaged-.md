---
id: T-2494
title: Glessner's full bake changes all three packaged hashes without refreshing its measured baseline after #793
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-14
pr: 798
claimed_by: Glessner reproducibility diagnosis 10/14/2026, 1:37:06 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-14T09:50:14Z
claimed_run: null
claimed_at: 2026-10-14T06:37:06.411Z
decision: null
decision_answer: null
---

Glessner's full bake changes all three packaged hashes without refreshing its measured baseline after #793.

## Evidence (PR maintenance, 2026-10-14 UTC)

The failure reproduces identically on dev and on the combined #770 branch:

- dev `0b233706c8ee3307933f6442543c18b40119e499`, after #780 landed: [content build 38498564271](https://github.com/kevinrhaas/chicago/actions/runs/38498564271).
- #770 `33a4d4691e537f1bf0f3b637a31681b285290ed3`: [content build 38497642120](https://github.com/kevinrhaas/chicago/actions/runs/38497642120).

Both rebuilt trees fail the same two of 875 gate steps: the K01/Glessner component contract and its baseline self-test. The hashes match across the two independent rebuilds:

| Tier | Committed/measured package | Rebuilt package |
|---|---|---|
| Full | `12fc4bff7254` | `92e844ebb5ae` |
| Web | `8967e96d4f76` | `9a929344d109` |
| Light | `dd7620a9e05c` | `74b9d15ca1df` |

The guard correctly reports: “the asset was rebaked; re-measure with `node tools/k01_contract.mjs --measure`.” Why the pinned rebuild and the committed package diverge still needs diagnosis. This repeats the failure pattern from completed T-2311 (#645) and T-2427 (#747), now after #793.

The committed package itself passes `k01_contract --check`, the complete 875-step gate, and published browser coverage at both viewports. The failures above occur on the newly regenerated bake output, and also occur on dev without #770's changes.

## Acceptance

- Explain why the canonical full bake produces different Glessner bytes from the committed package and identify the responsible source/producer step.
- Make the canonical package and its measured baseline agree after a full `tools/bake.sh` on dev; both failing contract steps must pass as part of the whole gate.
- Preserve the stale-package guard and its self-test. If a new asset set is intentional, measure the actual full/web/light outputs and validate their geometry and published rendering against the current source and image evidence.
- Demonstrate a green full bake and published mobile/desktop checks with the existing geometry and performance assertions intact.


## Root cause and repair — 2026-10-14 UTC

PR [#798](https://github.com/kevinrhaas/chicago/pull/798), head `04add1ecd9be06a95fd4c859aa3fac330182ef23`, retains the canonical UV layout alongside each committed stone-occlusion atlas. The exact mesh, topology, granite mask, Blender version and unwrap recipe key it; stale or corrupt layouts are refused. The complete atlas key and K01 stale-package guard remain unchanged.

The instrumented full CI build [38529855483](https://github.com/kevinrhaas/chicago/actions/runs/38529855483) isolates the difference to UV coordinates. A local controlled rebuild with Ubuntu glibc 2.39's math library reproduces its exact key, while all geometry inputs remain identical. After the repair, both math libraries produce byte-identical canonical Full, Web and Light files. Full/Web retain T-2218's approved bytes; Light retains its exact binary geometry/texture payload and changes only its producer recipe stamp.

Local preflight passes all 878 steps, including 356 self-tests, and the post-commit changelog check passes. Canonical full rebuild [38539402022](https://github.com/kevinrhaas/chicago/actions/runs/38539402022) and PR gate [38539360610](https://github.com/kevinrhaas/chicago/actions/runs/38539360610) are pending. The PR remains draft until the full rebuilt package and both published browser viewports pass. This is not yet a completed ticket. T-2220 remains the next serialized house ticket.
