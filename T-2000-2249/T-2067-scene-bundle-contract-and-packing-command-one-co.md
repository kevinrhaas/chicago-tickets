---
id: T-2067
title: Scene-bundle contract and packing command: one commit's scene packed with per-file checksums and a digest, a fresh-consumer verifier that refuses tampered, missing or extra files, and a twice-built reproducibility check
state: done
epic: PIPELINE
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1357
opened: 2026-10-04
closed: 2026-10-04
pr: 386
claimed_by: run 10/4/2026, 1:25:18 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T07:16:45Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37182479150
claimed_at: 2026-10-04T06:25:18.081Z
decision: null
decision_answer: null
---

Scene-bundle contract and packing command: one commit's scene packed with per-file checksums and a digest, a fresh-consumer verifier that refuses tampered, missing or extra files, and a twice-built reproducibility check.

Piece 1 of 2 of **T-1357 — Publish a versioned Chicago scene bundle from every successful scheduled asset bake**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. `tools/scene_bundle.py pack --scene 1835 --commit <sha>` reads every file from the git objects of ONE commit — never the working tree — so a bundle cannot mix sidecars from one commit with meshes from another. Contents: the scene file, the datum, the scene's compiled sidecars and their source records, every master GLB the sidecar index names, the epoch's ground and water GLBs and heightfield, `assets/manifest.json`, `assets/LICENSES.md`. Nothing from `data/research/`, deposits, secrets, `assets/textures/` or engine binaries.
2. `BUNDLE.json` at the archive root declares schema, scene, source commit, Blender pin, coverage (what is in it, the structures with no GLB, and every load-drawn layer of GLB-CONTRACT § Layers drawn at load as OMITTED, read from that table), the `review_required` ids, each file's licence basis, per-file bytes + sha256 and the payload digest. No wall-clock time is in the archive.
3. Rights refusals are the validator's: a GLB not recorded by a bake and with no LICENSES.md row, or a `check_required`/`restricted` source with `asset_use: geometry`, refuses the pack.
4. `scene_bundle.py verify <archive> [--expect-digest D]` is the fresh consumer: prints source SHA, scene and coverage; refuses a tampered byte, a missing file, an extra file, an unsafe path and a digest mismatch.
5. `scene_bundle.py repro` builds the same commit twice and compares archive sha256 and payload digest. `--self-test` demonstrates 4 and 5 on a small subset and runs in check.sh.
6. `docs/unreal/SCENE-BUNDLE.md` is the contract: how T-1358 consumes it and what changes when T-0252's layer exports arrive. The workflow attachment and publication are T-2068.
