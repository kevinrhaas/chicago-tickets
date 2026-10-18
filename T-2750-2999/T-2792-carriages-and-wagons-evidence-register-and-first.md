---
id: T-2792
title: Carriages and wagons: evidence register and first master specification
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
claimed_by: carriage-research agent 10/18/2026, 12:53:13 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T17:53:13.996Z
decision: null
decision_answer: null
---

## Scope and acceptance

Deliver the first vehicle evidence register and an executable modeling specification, not a new research bureaucracy.

- Inventory existing wagon geometry, data, sources, counts, dimensions, license provenance and placements; distinguish supported mechanics from static appearance. Identify what can be reused without redoing T-0084/T-0087/T-2121.
- Record every actually inspected relevant viewer image with stable ID, date interval, provenance URL, visible features, rights and candidate class. Include the pre-fire coverage result and remaining Prairie coverage. Start from identified J. P. Smith & Co. wagon and Harvey-frontage carriage leads; investigate the LoC Pullman-location high-resolution scan, recording access denial rather than inventing ownership/type.
- Select a first static wagon and passenger-carriage specimen; state evidence tiers and bounded dimensions/materials. Preserve rights-pending photographs as text citations only. Select a cleared construction basis before derived assets begin.
- Write `vehicle-master-spec.md`: components, pivots, axle/steering/shaft/pole/seats, scale/axes, portable JSON interfaces, matched-view acceptance and LOD/performance receipt expected of the next two tickets. Record unresolved source/rights work precisely.
- Provide research findings and a concrete first modeling handoff. A proxy-denied archive is an outstanding prerequisite for that source, not a completed deep-dive.

## Work started

Two independent visual audits and an implementation audit are already saved in the evidence directory. The carriage and horse agents have saved initial master specifications in parallel; source/rights clearance and production validation remain outstanding. External LoC/archive/Glessner access was denied by proxy on the current instance; domain additions are saved in the environment draft for review.

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
