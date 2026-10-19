---
id: T-2796
title: Move horse-drawn traffic through distant streets with measured LOD budgets
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-2791
opened: 2026-10-18
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

## Depends on

T-2795, T-1792. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Add a bounded first route with **one** period-correct horse-drawn vehicle in the distance, then a small capped population using the same path. It must visibly move in the actual selected scene, not just in a fixture.

- Use road masks/route affordances rather than sidewalk pedestrian paths; respect scene date, stopped/turning behavior, street crossings, building and static-wagon collision proxies.
- Distance LOD and animation update tiers share mobile budgets with portable humans; do not spawn new full-resolution textures per animal/vehicle. Test culling, return to near view, pause and reduced-motion choice without popping into collisions.
- Keep stable selection/dossier identity and source/liberty metadata; no unsupported daily schedule, owner or named driver is invented.
- Show the same street view before/after with moving vehicle, screenshots/video and measured phone/desktop p95, bytes and memory. A real browser functional test must demonstrate route progress and correct hitch motion.

## Shared requirements

Owner request, 2026-10-18: two epics below portable humans; inspect both research viewers and existing wagons; build photographic-quality period models first, then distant movement, riders/drivers, and eventually boarding/riding. Explicitly authorized parallel work. Implementation target is `kevinrhaas/chicago` **dev**; use the existing isolated checkout, no worktree unless requested.

- Keep 1812/1835, pre-fire (through 1871), and Prairie Avenue 1904 eligibility separate. Later images may support a labeled period analogy, never establish earlier Chicago presence. Do not call the Pullman-location carriage Pullman-owned without evidence.
- Resolve every implementation source ID in `data/sources/`; distinguish attested, inferred with reasoning, and bounded reconstruction. Unknown dimensions/color/breed do not block a defensible reconstruction; record bounds and liberties. Never promote a guess to attested.
- Text citation of rights-pending sources is permitted; assets must not be derived from them. Every shipped asset/input carries license provenance. Prefer project-authored or institutionally cleared references and no paid acquisition without owner authorization.
- Photographic quality is an acceptance target, not a status label. Compare actual renders against dated source views at matched cameras, record discrepancies and what is hidden/inferred. Do not close on a placeholder silhouette or unseen screenshot. Keep black-and-white sources distinct from reconstructed color.
- Canonical deliverables follow the existing portable export pipeline: authored masters where supported, glTF/GLB + engine-neutral JSON, metres and explicitly tested axes, licensed materials and near/mid/far LODs. No Blender installation on the improve runner; mark `needs_bake` honestly.
- Preserve existing placed static wagons; route/actor integration is additive. Existing camera horse/wagon paces do not count as a rendered animal/vehicle or a working riding interaction.
- Measure GLB/texture bytes, triangles, draw calls, texture memory and frame cost for the selected desktop/mobile specimen. Reuse materials and population budgets; do not regress the phone memory work above this band.
- Rider/driver work reuses portable humans and follows the owner's current depiction rulings (T-2672); isolated test fixtures can validate attachments before scene release. No invented named likenesses, dialogue or ceremonies.

## Evidence

Read `evidence/period-transport-2026-10-18/carriages.md`, `horses.md`, and `viewer-survey.md`. They distinguish pixel inspection from metadata, record coverage and rights, and explain external archive access blockers. The Prairie visual pass was targeted, not all 944 source records were visually reviewed. Read the master specifications as they are added; they are a first-pass design, not proof of finished models.


## Current traffic pricing constraint — 2026-10-19

The complete split fresh diagnostic (36unique rows, sixstands xthreetiers xtwoviewports) measures Light's global worst at1,154,091triangles and89drawcalls. The strict limits remain1,190,000triangles and90calls; general330callbudget does not override Light's separatefloor. Only1call/35,909triangles remain at the sampledworst. The measurements contain no newtownhumans or movingtraffic; full/balanced repricing buys no unmeasured futureactors. Before adding traffic, measure sharedmaterials/instancing/LOD costs and actual savings, then qualify completepublished desktop/mobile coverage. Existing placedstaticwagons remain intact. Receipts: evidence/period-transport-2026-10-18/ci379-and-transport-repairs/combined36.md.
