---
id: T-3224
title: K01 contract: web-tier metric_uv reads 16-bit position quantization on brick-unit relief once a K14 yard widens the mesh (1612 Goodman 1.054 vs 0.05 tolerance)
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-27
closed: null
pr: 1399
claimed_by: run 10/27/2026, 9:31:57 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/40620945873
claimed_at: 2026-10-28T02:31:57.781Z
decision: null
decision_answer: null
---

K01 contract: web-tier metric_uv reads 16-bit position quantization on brick-unit relief once a K14 yard widens the mesh (1612 Goodman 1.054 vs 0.05 tolerance).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #1395 (T-3214) cannot pass check.sh's K01 contract step: 1612's rebake with its walk is measured honestly and its web metric_uv verdict is not ok

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured (lap of #1395, 2026-10-28)

- `node tools/k01_contract.mjs --check` on #1395's tree first failed on stale hashes. T-3214 rebaked 1612 with its K14 yard and walks, and never re-measured. CI's gate on c926c57ed was red on that step alone (1 of 1088).
- `--measure-asset goodman_house_1612_prairie` then writes a measure whose **web** `metric_uv` is not ok: `brick_unit_body` 1.0537, `brick_unit_grey_tan` 1.0554, `brick_unit_hard_burnt` 1.0524, `brick_unit_salmon_soft` 1.0539 (tolerance 0.05). The **full** tier is 1.000 on all four. Dev's measure (no yard) read 0.9855 on the web tier.
- `bake.sh --only goodman_house_1612_prairie` re-emits the committed GLBs byte-identical, so this is not a stale file.
- **Cause.** The K01 GLB is one node and one mesh. `web_derivatives.sh` runs `gltf-transform meshopt --quantize-position 16`, which quantizes against that one mesh's bounds. The yard extends the mesh about 4 m toward the street: the node scale goes from 12.697 to 14.647, so the quantum goes from 0.39 mm to 0.45 mm. The brick units' return faces have a relief of a few millimetres, so rounding them to that quantum changes their area by about 10%. Because every brick shares the same relief, the error is systematic, and the median of sqrt(uvArea/area) moves by about 5%. **The UVs themselves are metric.** The instrument is reading position quantization.
- 16 bits is already the maximum, and one node means one quantization volume. So no setting inside the current derivative fixes it.

## Options (pick one; both are contract-level)

a. **Instrument.** On the web tier, measure UV density only over triangles whose shortest altitude spans at least N quanta (say 20, which keeps error per coordinate at or under 2.5%). Add a self-test that pins a few-millimetre relief at two quanta. The full tier stays exactly as it is. This does not weaken the assertion about UVs; it stops it from reading the quantizer.
b. **Emitter.** K01 emits the K14 yard as its own node and mesh, so the house's quantization volume no longer includes the yard. This touches docs/GLB-CONTRACT.md (bilateral: propose first) and rebakes every house that has a yard.

Every K01 house that gains a yard and is measured (1808 Keith is the other measured asset) will hit the same wall. When this lands, re-run `--measure-asset goodman_house_1612_prairie` on #1395.
