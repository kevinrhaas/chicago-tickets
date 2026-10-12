---
id: T-2393
title: Glessner granite: a material occlusion map from the split face's own height field (generate.py), carried through the export and held by ao_export.py
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2390
opened: 2026-10-11
closed: 2026-10-11
pr: 716
claimed_by: run 10/11/2026, 9:19:15 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-12T03:29:10Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38193697523
claimed_at: 2026-10-12T02:19:15.327Z
decision: null
decision_answer: null
---

Glessner granite: a material occlusion map from the split face's own height field (generate.py), carried through the export and held by ao_export.py.

Piece 1 of 2 of **T-2390 — Glessner granite relief in shade: an occlusion channel for the rock faces (generators/ao_export.py), so shaded north/west faces show their relief without changing the light**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2390 was split (2026-10-12T02:19:06.065Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 19m ago, run 10/11/2026, 9:00:29 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38193697523) — held by the run that split it
- branch `steward/t2390-granite-occlusion` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38193697523) may be working one of the pieces now.

**Acceptance:** (stated before the measurement was read)
- Glessner v4's split-face granite slots (granite, granite_1..4, rough_stone_trim) carry a glTF
  `occlusionTexture` computed from the SAME height field as `granite_normal.png`, in the master,
  the web derivative and the light LOD.
- The occlusion acts on the sky fill only: the sun's light is untouched (three.js aoMap is
  indirect-only), and nothing is brightened or re-tinted.
- `generators/ao_export.py --gate` tells a committed material map from a bake and holds the map
  to its committed file (not uniform, mean within 2 %), with self-tests that break each arm.
- The shaded stands are re-captured before/after on the same cameras and the numbers are
  published, whatever they show.
