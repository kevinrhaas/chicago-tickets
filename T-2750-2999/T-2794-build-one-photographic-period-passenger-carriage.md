---
id: T-2794
title: Build one photographic period passenger-carriage master
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
claimed_by: carriage-model agent 10/18/2026, 1:49:28 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T18:49:28.861Z
decision: null
decision_answer: null
---

## Depends on

T-2792. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Build **one** period passenger-carriage master from the best cleared evidence (first investigate Harvey-frontage brougham and LoC Pullman-location carriage). Do not claim maker, owner or precise subtype unsupported by the selected record.

- Treat the C01 open-carriage engineering study as provisional, not a completed period replica. Freeze a source-bounded class/specimen choice after T-2792, with explicit date interval, license and reconstructed dimensions. Clear the rights basis before deriving an asset from a photograph.
- Model separate wheels, front steering assembly, body, suspension, shafts/pole, steps/doors and seats. Upholstery, wood, leather, iron and glass must read correctly at conversation/boarding distance; handle black-and-white colors as reconstruction.
- Include named passenger/driver seat, boarding, rein and hitch anchors, documented doors/entry clearances and a collision proxy for later interactions.
- Export portable master/LOD GLBs + sidecar through the supported pipeline; matched-camera side/front/rear/three-quarter comparisons, discrepancy register and measured phone/desktop loading receipt demonstrate acceptance.
- A small distant vehicle in a house photo cannot support hidden interiors as attested; state those liberties. Unknown maker or ownership does not prevent a labeled generic reconstruction.

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


## Latest measured checkpoint — 2026-10-19 04:52 UTC

Open C01 rounded cushions are committed in PR1041 finalcandidate e1b31c070; it remains an engineering development model. Separate reconstructed1904 C02 enclosed carriage and real hinged door are prepared OUTSIDE the app. Latest exact-source archive c02-door-mechanical-repair-review.tar.gz SHA256 fb10f0e2f9dd624831b0bf24ef9e533832dc9c847fd343721034e3703de2743a has11512triangles, deterministic/Khronos0/0 closed/open exports, eight new desktop/mobile images and zero actual moving-vs-fixed surface intersections at15 sampled angles with no exclusions. Earlier visual and full-triangle mechanical failures are retained. Whole continuous sweep, passenger fit, photographic/period-construction review and production integration remain open. Pullman ownership/subtype are unproved; dimensions/details are original reconstruction. No production closure.

Durable inputs, failed receipts and current recovery instructions: `evidence/period-transport-2026-10-18/CHECKPOINT.md` and `parallel-refinement-2026-10-19/` beneath that evidence directory. This progress update does not change the ticket state or production acceptance.
