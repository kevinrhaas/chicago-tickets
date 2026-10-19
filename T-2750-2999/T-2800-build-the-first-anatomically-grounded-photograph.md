---
id: T-2800
title: Build the first anatomically grounded photographic horse master
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
claimed_by: horse-model agent 10/18/2026, 1:45:58 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T18:45:58.871Z
decision: null
decision_answer: null
---

## Depends on

T-2799. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Build **one** project-authored generic working horse master, anatomically credible and source-bounded for the selected date. This is not a claim of a particular breed or a portrait of an identified animal.

- Define scale, body proportions, head/eyes/ears/muzzle, neck, shoulder, limbs/joints, hooves, mane and tail from cleared anatomical/period sources; neutral stance has correct weight-bearing hoof contact and no disconnected joints.
- Skin/coat, eyes, muzzle, hair and hooves read at near view; use browser-suitable hair geometry/materials rather than unsupported expensive strand rendering. Coat color and grooming are declared reconstructions where not attested.
- Produce canonical master, license provenance, liberties, clean topology for T-2803, compressed near/mid/far exports and tested axes/metres. Reuse materials within bounded memory cost.
- Compare actual front/profile/three-quarter/detail renders against approved reference plates at the same views; record discrepancies and acceptance. Load exported GLB in the browser and measure triangles/materials/textures/bytes.
- Do not claim animation, tack or ride controls passed on a static animal.

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


## Broader measured follow-up — 2026-10-19 05:00 UTC

Actual shared-surface shoulder V1 eliminated detached caps topologically but rendered as an angular/webbed sheet: VISUALFAIL/unapplied. V2/V2b ellipse variants had actual self/body or collar collisions; V2c was CPU-safe but still visually webbed. All source/16capture/failure archives retained. Approved next LOCAL forechest sculpt permits declared torso changes while protecting head/neck, skeleton, clips, sockets and lower/sole positions. First localforechestV1 passes sampled body/self/topology/Khronos/sole checks but gear fit FAIL; exactbaseline controls identified preexisting strap crossings rather than blaming all newbody. Bare-body diagnostic review and independent original-baseline gear repair are separate outside-app lanes. No photographic/anatomical or production acceptance.

See `evidence/period-transport-2026-10-18/parallel-refinement-2026-10-19/` and `CHECKPOINT.md` for exact recovery. Queue/state unchanged.


## Measured progress — 2026-10-19 08:26 UTC

The outside b880 body / 078 gear pair passed its fresh 63-pose intersection/distance checks, and eight full plus two detail desktop/mobile views were captured. Root reviewed four actual current images and rejected photographic acceptance: primitive ear/head/neck silhouette, tubular limbs, angular hindquarters, flat tail and synthetic tack remain. The archive `horse-v2-pair-cpu-sidecar-visual-next-pr-2026-10-19.tar.gz` (SHA256 `e9e203ecef7d653c54ec0205efbbe13cac0a70c605a1066af93e0cf68c261456`) preserves all proof and the earlier framing failure. Sidecar-only cleanup passes 13 negative-control tests under normal and optimized Python; original GLB bytes stay unchanged.

A new isolated ear-shape proposal is being compared with actually viewed, cleared Cuyer plates. Its altered ear geometry/weights and its own metadata authority are explicit; no metric, breed or Chicago identity is inferred from the diagrams. This proposal remains outside the fixed f97 merge candidate. Anatomical and photographic production acceptance stays open.
