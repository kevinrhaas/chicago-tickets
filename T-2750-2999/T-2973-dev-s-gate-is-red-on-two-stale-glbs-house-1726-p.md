---
id: T-2973
title: dev's gate is red on two stale GLBs: house_1726_prairie__as_mapped_1904.glb and house_1730_prairie__as_mapped_1904.glb no longer match their inputs (T-2934 #1154 moved them onto K01, then T-2931 changed the K01 recipe and re-emitted every K01 asset but these two, which were not yet on its base); re-bake both on the merged recipe (tools/bake.sh --only house_1726_prairie, house_1730_prairie) so validate.py's stale check passes
state: withdrawn
epic: SOUTH_TIME
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-20
closed: 2026-10-20
pr: null
claimed_by: run 10/20/2026, 8:42:22 PM CT
blocked_on: moot: #1164 (T-2952/T-2953, 5eb3ffd43) re-emitted every K01 asset on the merged recipe, 1726 and 1730 included; validate.py --all on dev reads 0 errors
needs_bake: false
closed_at: 2026-10-21T01:45:51.238Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39528387434
claimed_at: 2026-10-21T01:42:23.831Z
decision: null
decision_answer: null
---

dev's gate is red on two stale GLBs: house_1726_prairie__as_mapped_1904.glb and house_1730_prairie__as_mapped_1904.glb no longer match their inputs (T-2934 #1154 moved them onto K01, then T-2931 changed the K01 recipe and re-emitted every K01 asset but these two, which were not yet on its base); re-bake both on the merged recipe (tools/bake.sh --only house_1726_prairie, house_1730_prairie) so validate.py's stale check passes.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate (dataset: stale) fails every PR until these two are re-baked; this runner has no Blender

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Resolved by #1164 before this ticket was worked (2026-10-21, slice 3 of 5)

**Acceptance:** `validate.py --stale` reports both GLBs fresh on `dev`, a re-bake on the merged recipe is byte-identical to what is committed, and dev's gate is green.

#1164 (T-2952, T-2953; merged to `dev` at 5eb3ffd43, 01:36Z) changed the K01 recipe again. It re-emitted every K01 asset and refreshed the input hashes in `assets/manifest.json`, and that included these two: 1726 is now `262758f6cb86…` and 1730 `4cf9ce5e4262…`, where the red gate had 446ca350734b and 8ea78a6afc01 against the old 5e5821c9bb86 and b61ba89f4e5e. Checked on `dev` c6bb22797:

- `python3 tools/validate.py --stale`: 891 assets match their inputs, 0 stale, PASS.
- `./tools/bake.sh --only house_1726_prairie,house_1730_prairie`: k01_emit rewrote both masters (3,427,904 and 2,971,448 bytes) and their web derivatives, and the tree stayed clean (`git status` empty). So the committed GLBs, derivatives and manifest are exactly what the merged recipe builds.
- dev's `Chicago 4D — gate` passed on 5eb3ffd43 (run 39528326765) and on c6bb22797 (run 39528671661). The last red was abb6cfd2f (run 39518781303), failing on these two stale GLBs only.

No code PR, because there is nothing left to change. This ticket's receipt is #1164.
