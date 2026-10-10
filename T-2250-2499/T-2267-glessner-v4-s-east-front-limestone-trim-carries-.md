---
id: T-2267
title: Glessner v4's east-front limestone trim carries coincident faces — 6 in the full master (4 doubled, 2 back to back, near x 49.2-49.4 m at y 3.36-3.55 and 7.50 m) and 31 in the web tier once quantized — which the K01 contract's measure finds and a regenerated asset must not
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/9/2026, 9:35:19 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38017233387
claimed_at: 2026-10-10T02:35:19.467Z
decision: null
decision_answer: null
---

Glessner v4's east-front limestone trim carries coincident faces — 6 in the full master (4 doubled, 2 back to back, near x 49.2-49.4 m at y 3.36-3.55 and 7.50 m) and 31 in the web tier once quantized — which the K01 contract's measure finds and a regenerated asset must not.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Measured (T-2265, 2026-10-10) — tools/k01_contract.mjs --measure

The K01 contract's coincident-face measure (vertices on a 1 mm grid; two triangles on the same three grid points are coincident) found these on the canonical Glessner v4 package. The record is `data/components/prairie_1904/glessner_baseline.json` § verdicts.coincident_faces in the code repo.

- **Before T-2205 (package 111fac11…):** full master 6, web 31, light 0. All six in the full master are `limestone_trim` on the Prairie Avenue (east) front near x 49.2-49.4 m: four doubled (same winding), two back to back, slivers at y 3.36-3.55 m and one ledge at y 7.50 m.
- **After T-2205 (package eb00c3fc…, ridge caps, finials and roof edges refined):** full master **15**, web **40**, light **8**. The six above remain; nine more are back to back between `roof_plane_1` and `roof_plane_2` in the plane x = 11.54 m, y 10.33-10.59 m, z -17.97 to -18.24 m — a hidden end face where two of the new roof parts meet.

**Acceptance:** after a regenerating bake, `node tools/k01_contract.mjs --measure` reports 0 coincident faces in the full master (web and light then follow from it, or their remainder is explained by quantization alone), the baseline's `coincident_faces` verdict is ok with no `finding`, and the Glessner fixed-camera views show no change other than the removed faces. Needs a bake.
