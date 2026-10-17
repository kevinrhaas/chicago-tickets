---
id: T-2697
title: The near ring's slot lattice in GLSL: scatter's world-anchored cells, xorshift jitter, hash3 and the stratified Feistel draw computed per gl_InstanceID in a three-free shader module, read back from Chromium against flora.js's own scatter at every near slot of a set of stands (positions to the millimetre, the draw u exact), with the instance-to-slot mapping the draw will use
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2557
opened: 2026-10-16
closed: 2026-10-16
pr: 926
claimed_by: run 10/16/2026, 7:25:36 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T02:58:36Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38985727841
claimed_at: 2026-10-17T00:25:36.892Z
decision: null
decision_answer: null
---

The near ring's slot lattice in GLSL: scatter's world-anchored cells, xorshift jitter, hash3 and the stratified Feistel draw computed per gl_InstanceID in a three-free shader module, read back from Chromium against flora.js's own scatter at every near slot of a set of stands (positions to the millimetre, the draw u exact), with the instance-to-slot mapping the draw will use.

Piece 1 of 3 of **T-2557 — GPU-procedural near grass: the near ring dealt in the vertex shader from the lattice's own hash, the heightfield and the ground masks, with no CPU lattice and no re-deal on move**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2557 was split (2026-10-17T00:25:27.235Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 7:25:15 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38985727841) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38985727841) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Acceptance (stated by the run that took it, 2026-10-17):** one readback, never weakened to pass.

1. `renderers/web/js/flora-gpu-lattice.js` — three-free, no imports — carries `scatter`'s walk as GLSL ES 3.00 (`flLatticeSlot(id, …)`) and `latticeUniforms(job)`, the CPU's whole share per camera move, with the instance-to-slot mapping the draw will use.
2. `node tools/check_flora_gpu_lattice.mjs --gpu` reads every slot back from Chromium against `jobs/lattice-kernel.js` (cone off) at every layer's lattice at all 18 1835 anchors and 200 random walks: the kept slots and their order identical, a ring disagreement only within 0.1 mm of an edge, cell seed and stream equal to the bit, position within 1 mm, deal rank within 2^-20. Its `--self-test` refuses a shader with the stream salt or the block shift one bit off.
3. The bare command (no browser) in `check.sh` holds the shader's walk constants to flora.js's, with a self-test.
