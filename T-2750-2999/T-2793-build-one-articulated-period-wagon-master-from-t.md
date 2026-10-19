---
id: T-2793
title: Build one articulated period wagon master from the existing wagon families
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-2791
opened: 2026-10-18
closed: null
pr: null
claimed_by: wagon-model agent 10/18/2026, 1:45:25 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T18:45:25.994Z
decision: null
decision_answer: null
---

## Depends on

T-2792. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Build **one** reusable articulated farm-box wagon master, as a bounded reconstruction for the earlier scene, retaining the existing wagon's documented provenance and proportions unless better evidence changes them explicitly. Covered/cart variants remain later follow-ups, not hidden acceptance.

- Read the existing 3.05 x 1.07 x 0.55 m reconstructed body and running gear in yard.js/data before changing it. Separate body, four wheels, front bogie/kingbolt, reach, tongue and hitch nodes; preserve correct axle/track and wheel clearance through a low-speed turn.
- Match a licensed construction reference and reviewed period analogue; wood grain, joinery, iron tires/hardware, paint wear and load attachments survive a close view without pretending colors or dimensions are attested.
- Produce canonical authored master + portable GLB/sidecar, license record and declared liberties. Supply neutral material variants within one bounded specimen, with compressed near/mid/far exports.
- Render close, side, front-three-quarter and distant views with a scale reference; compare against approved evidence and list remaining differences. Export/load it through the actual web path and measure budget.
- Existing 80 static wagons remain placed and operational; do not replace all of them or rebake unrelated buildings for this ticket.

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


## W01 visible refinement checkpoint, 2026-10-19

Reviewed original tapered octagonal spokes and1.2mm board/stave chamfers are integrated in the current combined source WIP, not yet committed. Exact bundle is saved alongside CHECKPOINT.md.9000→10792triangles,22mesh batches/47nodes and wheel bounds/pivots/socket frames unchanged; source wrapper regenerates exact reviewed GLB7749a0199b93bd196ecf6c3482af8ec537f1420a38f6fac88ab79fd8f34d44aa. Two-run determinism and independent Khronos0/0 passed on proposal bytes; controlled close/clay/mobile images were inspected. Full-view gain is modest; geometry cost and eventual LOD decision remain explicit. All dimensions/material variation are reconstructed engineering, no photographic/historical joinery acceptance. Combined full gate/commit pending; production ticket remains open.


## Measured progress — 2026-10-19 08:26 UTC

Combined PR1041 is committed and pushed at `f97ee94970385d35f469c449c6b111b0d8488057`, reconciled with dev c7770e99. Full local preflight passed 1,012 checks, and the remote required gate and canonical human workflow passed. The final 18-leg published desktop/mobile smoke matrix is running at that exact head; merge to dev remains conditional on all remaining checks and strict coverage. No production ticket closure. The separate C02 door/body portable package and actual browser proof remain saved for a later PR; construction/photo acceptance is still open.


## Measured progress — 2026-10-19 10:13 UTC

Saved implementation checkpoint512f4a7e3 is pushed, including reviewed C02 and devfb6a; fullpreflight1015/0 and postcommit checks pass. PR1041 remains draft: earlierf97 desktop13 failed draw331/330 and HUD31.23%/10; current targeted actual512f camera trace passes tint287,rowghost327,XRAY316 twice each, but does not reproduce331 or qualify wholematrix. HUDmeasurement correction is uncommitted under actualdiagnosis; no finalmatrix/merge yet. Wagon photographic/period/production acceptance remains open.
