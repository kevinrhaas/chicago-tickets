---
id: T-2804
title: Fit portable-human riders and drivers to horses and vehicles
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-2798
opened: 2026-10-18
closed: null
pr: null
claimed_by: parallel named driver rider fit 10/18/2026, 10:07:02 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T03:07:02.960Z
decision: null
decision_answer: null
---

## Depends on

T-2672, T-1789, T-1790, T-1792, T-2801, T-2802, T-2803. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Fit **one portable-human rider and one driver pose using suitable existing attested, inferred or reconstructed residents** to the approved horse and carriage/wagon interfaces, reusing the existing human rig and period wardrobe. Use an anonymous person only when no suitable existing resident can be used, with that choice documented.

Owner clarification, 2026-10-18: "Ok generally if you can use assign existing attested inferred or reconstructed people as the reference and model, don’t make generic people unless you have no other choice". Resident identity and appearance have separate evidence: assigning a model to a resident does not establish an attested portrait likeness. The first 1835 authoring references are the existing reconstructed teamsters Otis Bardwell and Martin Flynn and stable keeper Joseph Dufresne; use them only in their eligible period and retain their reconstructed status.

- Seat, stirrup, hands/reins, pelvis/legs and gaze align with horse/driver anchors. Body animation follows horse gaits or vehicle movement without penetrating saddle, seat, wheel or animal.
- Demonstrate idle/walk/trot with mounted rider and seated driver, transitions and rein slack/tension; no unsupported historical named likeness is introduced.
- Respect T-2672 and portable-human pipeline dependencies before scene population; an isolated fixture is a technical proof, not a released portrayal. Preserve research provenance and date eligibility for clothing/gear.
- Export/play synchronized clips in browser, compare near/profile/three-quarter/distant views, and document shared skeleton/LOD costs. Do not build an unrelated human engine.

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


## Existing resident driver study — 2026-10-19

The outside-app W01 proposal includes a reconstructed removable bench and footboard with actual surface sockets. Source-body `sit_drive` poses are bound to `rc_bardwell_otis`, `rc_dufresne_joseph` and `rc_flynn_martin`, retaining their existing identity, scene, grade and body hashes. W01's former driver socket was not an installed seat and supplies no seating proof. Baseline wagon output remains byte-identical without explicit study opt-in.

The proposed canonical builder clip converts source global poses through actual Blender rest bases, preserving idle/walk unless explicitly enabled. Pure source FK/LBS tests preserve seat and foot contact through independent rest-roll frames. Actual Blender export, clothing triangles, palm/rein contact, continuous motion and photographic acceptance remain open. No mounted rider or saddle is implemented. This is development work under the dependencies, with no new scene placement or ticket completion.

[Saved proposal archive](../evidence/period-transport-2026-10-18/ci379-and-transport-repairs/resident-wagon-driver-draft-latest.tar.gz).
