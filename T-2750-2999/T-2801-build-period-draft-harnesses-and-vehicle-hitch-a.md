---
id: T-2801
title: Build period draft harnesses and vehicle hitch assemblies
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
claimed_by: harness-model agent 10/18/2026, 1:52:28 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T18:52:28.343Z
decision: null
decision_answer: null
---

## Depends on

T-2799, T-2800, T-2792, T-2793. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Build **one** period working-harness set with single-shaft and pair/pole assembly variants on T-2800; match the intended load/vehicle and documented date.

- Model collar/hames or source-supported alternative, traces, back/saddle and belly/breeching elements, bridle/bit/reins and correct shaft/pole connections only as evidence supports. Publish terminology, routing and uncertainty per visible part; avoid a decorative saddle mistaken for draft harness.
- Collars fit the animal, straps avoid penetrating the body, traces carry the modeled pull and breeching/stopping system connects coherently. Pair spacing and pole clearance agree with vehicle master.
- Export modular licensed PBR gear and named anchors/constraints in the shared engine-neutral sidecar. Close-up photographs/diagrams from cleared sources bound materials and buckle/joinery choices.
- Show front/profile/hitch views on the actual horse+vehicle with validation of anchors at rest and sampled steering/stance extremes in a static fit fixture (animated pull validation belongs to T-2795); export budgets documented. Missing photographs of hidden straps are labeled reconstructed, not fabricated citations.

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

## Development checkpoint, 2026-10-18

See `evidence/period-transport-2026-10-18/fit-followup.md` and `CHECKPOINT.md` for the pushed code revision, measured progress and remaining gates. These are bounded original development studies; no photographic-quality, complete physical-fit or production acceptance is claimed. T-2795 work is dependency exploration while its master/gear/gait acceptance remains unfinished.


## Headstrap trial checkpoint, 2026-10-19

Unapplied original head/gear source and actual controlled views are archived in `evidence/period-transport-2026-10-18/combined-transport-resident-wip/horse-head-next-evidence-2026-10-19.tar.gz` (SHA2566f02b1ea392679d56d11ac73af9aebbda8dc34f2fa5c0dac286689716cf7b046). Full triangle SAT checks across21 sampled walk phases found118crossing pairs/phase on baseline head/original headstraps,50on first new head/original gear. A tighter route then failed58pairs/phase despite positive sampled vertex signs; this failure is preserved. Final paired V2head/V3gear has0pairs at21phases and a separately computed2.146834mm unsigned triangle minimum. These are discrete surface tests against a nonwatertight whole horse: no containment, comfort, continuous motion, load or historical fit acceptance follows.

Root actually inspected head profile/three-quarter and coupled gear three-quarter images. Cheek geometry and strap routing improve, but thick ears, grommet eyelid, head/neck notch, angular straps and near-eye check-rein remain visible. Candidate remains outside the application while the head/neck join is refined. Widths/thicknesses, bit/rein endpoints and31unaffected mesh buffers are preserved in the candidate; paired gear must not be applied independently to the baseline horse. Production ticket remains claimed/open.


## Broader measured follow-up — 2026-10-19 05:00 UTC

A broader exact-input scope found confirmed ORIGINAL baseline torso/harness crossings, not just touching. Against all36 unchanged harness meshes over42 walk/trot poses, the108-corresponding-torso-triangle mask has1386 proper-interior crossing pairs (collar336/support_l630/support_r420); a separate84-face mask has168 left-support pairs. Counts repeat by pose and are not unique physical defects. Edge-plane opposite signs and interior edge/barycentric coordinates retained, with original1e-8 predicates. Earlier head/neck/upper-forelimb checks did not prove whole-body fit. Actualinput hashes: horse89b048b7cda748e6f3a7111aa8e4f3198b01fabf6015cae644c78ed02d385bc6, gearb4a7318053e8508617a24fff64f02beb7eee77684db689dc04771d209a54fa8b. Strict receipts/source archive horse-forechest-baseline-gear-finding-2026-10-19.tar.gz SHA256dd6595acc5a37cc5be7bd63715d54d0ee38c4523af1b0a38d76bbce54baa411e. An independent OUTSIDE baseline breastcollar/support-routing repair is assigned; no exclusions or guard waiver. Currente1 development study is not whole-body harness qualified; production gear remains open.

See `evidence/period-transport-2026-10-18/parallel-refinement-2026-10-19/` and `CHECKPOINT.md` for exact recovery. Queue/state unchanged.


## Measured progress — 2026-10-19 05:48 UTC

Four-part chest repair committed/pushed1cbcfb84e after full1007-step preflight and postchecks passed. Current actual63-pose whole-horse surface proof: zero intersections, minimum5.113260mm against declared5mm; original frozen negative control reproduces100proper crossings. Eight actual paired views inspected; no pressure/continuous-motion/photographic acceptance. Current dev1920 integration and separate required resident facial morph repair are pending before combined dev merge; no final smoke coverage or ticket closure.
