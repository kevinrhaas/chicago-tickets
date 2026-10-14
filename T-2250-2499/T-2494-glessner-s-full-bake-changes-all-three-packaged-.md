---
id: T-2494
title: Glessner's full bake changes all three packaged hashes without refreshing its measured baseline after #793
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: Glessner reproducibility diagnosis 10/14/2026, 1:37:06 AM CT
blocked_on: null
needs_bake: true
closed_at: null
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

