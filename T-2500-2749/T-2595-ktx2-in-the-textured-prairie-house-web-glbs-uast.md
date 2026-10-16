---
id: T-2595
title: KTX2 in the textured Prairie house web GLBs: UASTC for normal, ORM and occlusion, ETC1S for basecolor, sizes capped at 2048 in power-of-two, a KTX2 loader on every GLB path, and measure_web_derivatives refusing a PNG or JPEG in any derivative but the Glessner v4 set
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2553
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 8:38:15 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38908068294
claimed_at: 2026-10-16T13:38:15.589Z
decision: null
decision_answer: null
---

KTX2 in the textured Prairie house web GLBs: UASTC for normal, ORM and occlusion, ETC1S for basecolor, sizes capped at 2048 in power-of-two, a KTX2 loader on every GLB path, and measure_web_derivatives refusing a PNG or JPEG in any derivative but the Glessner v4 set.

Piece 1 of 2 of **T-2553 — KTX2 in every textured web GLB: UASTC and ETC1S in web_derivatives.sh, the light tier capped at 1024, Glessner v4 repacked, and every photo-match still matches**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2553 was split (2026-10-16T13:38:06.214Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/16/2026, 8:34:14 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38908068294) — held by the run that split it
- branch `steward/t2553-ktx2-web-glbs` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38908068294) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. No web derivative of a textured Prairie house carries a PNG or JPEG image: every one ships `KHR_texture_basisu` (UASTC on normal/ORM/occlusion, ETC1S on basecolor/emissive), and `tools/measure_web_derivatives.py` refuses an image in any derivative except the Glessner v4 set, which it names with T-2596.
2. Every such GLB still loads on every path: the scene's loader on a GPU with no block format and under `?ktx2=0` (a KTX2 loader is always handed to a GLTFLoader that may meet one), the photo-match harness, and the smoke parts covering the diff with zero pageerrors.
3. The look holds: each house rendered from its old JPEG derivative and its KTX2 derivative at the same camera, PSNR quoted per house; any material that needs UASTC instead of ETC1S to hold is named.
4. GPU texture bytes for the 20 houses, before and after, and the published payload bytes before and after, stated.
