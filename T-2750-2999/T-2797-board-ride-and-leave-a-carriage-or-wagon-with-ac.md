---
id: T-2797
title: Board, ride and leave a carriage or wagon with accessible controls
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
claimed_by: parallel vehicle boarding 10/18/2026, 10:06:57 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T03:06:57.543Z
decision: null
decision_answer: null
---

## Depends on

T-2795, T-2796, T-2804. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Implement a complete **one-vehicle** board -> ride -> stop -> leave interaction using the licensed wagon or carriage, with passenger riding first and explicit driver/steering mode only where supplied.

- Use model boarding/seat/driver anchors and collision-safe approach/exit; doors/steps and seated camera height agree with the model. Leaving a moving vehicle safely stops or defers exit with a clear choice.
- Desktop keyboard and touch controls cover board, camera/look, stop and leave; respect reduced motion and allow immediate cancellation. Prevent camera clipping and inaccessible exit positions.
- Route following, seat occupancy and user control do not duplicate an NPC driver or strand the camera when switching years/destinations or reloading. Reuse portable-human seating where bodies are shown.
- Verify a complete board/ride/leave round trip in the actual scene on desktop/mobile, including obstructed exit, canceled boarding and destination switch. Record visual receipt and loading/frame costs.
- Existing camera-only wagon travel mode remains distinguishable from physically boarding this vehicle.

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
