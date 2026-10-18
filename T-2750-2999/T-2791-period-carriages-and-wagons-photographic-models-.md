---
id: T-2791
title: Period carriages and wagons: photographic models, moving traffic and boarding
state: split
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: 2026-10-18
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T17:46:58.859Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

## Epic scope

Period carriages and wagons from source-bounded photographic masters to articulated running gear, moving distant traffic and boarding/riding. This is the grouping record; six children own implementation and retain the requested order. Existing T-0084/T-0087/T-2121 running-gear and visual work is reused, not repeated.

Initial audit: `town_trade_goods.json` contains 80 wagons (25 farm boxes, 17 covered, 38 carts), plus the separate water cart dataset. `yard.js` merges static geometry and does not supply mobile glTF masters. Their dimensions and colors are reconstructed. Strong photo leads: clear Chrimes carriages, branded J. P. Smith & Co. ICE wagon, Harvey-frontage carriage, and carriage beside the Pullman residence. Rights and identity limits are recorded in evidence.

## Children and sequence

T-2792 evidence + specification; T-2793 one wagon master; T-2794 one passenger carriage; T-2795 articulated movement/hitches; T-2796 distant traffic; T-2797 boarding/ride. Model children may proceed independently after their evidence/rights gates. Motion waits on matching horse/harness interfaces.

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
