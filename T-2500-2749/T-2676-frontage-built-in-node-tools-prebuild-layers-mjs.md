---
id: T-2676
title: Frontage built in Node: tools/prebuild_layers.mjs runs the page's own createFrontage for 1835 against terrain.js's own Heightfield and writes its buffers with an input hash, byte-equal to what the page builds (read from the live page), its determinism and stale-input refusal gated in check.sh
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2560
opened: 2026-10-16
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

Frontage built in Node: tools/prebuild_layers.mjs runs the page's own createFrontage for 1835 against terrain.js's own Heightfield and writes its buffers with an input hash, byte-equal to what the page builds (read from the live page), its determinism and stale-input refusal gated in check.sh.

Piece 1 of 3 of **T-2560 — Ship the town prebuilt: run the layer builders at publish and ship frontage and spatial-batch buffers as compressed binaries, so a phone uploads the town instead of building it at every boot**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2560 was split (2026-10-16T18:39:25.526Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 1:38:00 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38948055852) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38948055852) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
