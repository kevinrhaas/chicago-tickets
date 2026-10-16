---
id: T-2552
title: Prairie from the air: break the ground's even plaid with a world-scale variation map and a distance fade (owner, 2026-10-16)
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: 857
claimed_by: run 10/15/2026, 10:02:35 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T03:02:35.805Z
decision: null
decision_answer: null
---

Prairie from the air: break the ground's even plaid with a world-scale variation map and a distance fade (owner, 2026-10-16).

The owner, 2026-10-16, with a phone screenshot at 1835, 1,197 ft up, looking ENE: *"When flying above ground you can see a grid of your variable surface. It looks like an even plaid. Close up it looks great, but from above it looks like a grid."* He offered the hat aperiodic monotile as the idea; the reply was that the repetition is in the texture, not the triangles, and that the hat itself is too structured and too costly per fragment. He said yes to the cheaper plan: this ticket is its first half (hex-tiling the 11 m tile is a separate follow-up).

## Diagnosis (renderers/web/js/terrain.js, PRAIRIE_FRAGMENT)

1. The colour tile repeats every 11 m; the mosaic's ~1.5 m shear bends that lattice but does not break it.
2. The "community mosaic" is `sin(x*0.1496)*sin(z*0.1309) + 0.6*sin(diag)` — an axis-aligned egg-crate, a literal plaid of 42 x 48 m cells. Most of the plaid in the screenshot.
3. The 1.6 m sward grain is below what an aerial view resolves.

## Acceptance

- The three-sine mosaic is replaced by ONE fetch of a world-scale variation map: seeded, multi-octave, domain-warped, not axis-aligned, with no repeat inside the haze reach. It carries the patch tone and the tile's lookup shear. Its mean leaves the prairie's mean albedo where it is (`tools/measure_ground_albedo.mjs --gate` unchanged).
- The tile's contrast fades toward its own measured mean with distance from the eye, so its 11 m lattice is not drawn where it would read as one; walking-height ground within ~100 m is unchanged in character.
- The same prairie on all three surfaces that splice PRAIRIE_FRAGMENT (terrain, ground strip, working bank) — no seam.
- Before/after screenshots from the owner's stand (1835, ~365 m up, ENE) at 390x780, plus a walking-height pair showing near ground unchanged.
- A LIBERTIES entry: the patchiness is reconstructed, like the mosaic it replaces.
- Smoke parts covering terrain green; fps at the prairie_west pose not materially worse than dev.
