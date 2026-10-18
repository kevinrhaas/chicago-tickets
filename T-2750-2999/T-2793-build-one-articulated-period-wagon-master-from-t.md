---
id: T-2793
title: Build one articulated period wagon master from the existing wagon families
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
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
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
