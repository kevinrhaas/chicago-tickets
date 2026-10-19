---
id: T-2802
title: Build period riding saddles, bridles and horse gear
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
claimed_by: continuing parallel period transport team 10/19/2026, 1:49:19 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T18:49:19.852Z
decision: null
decision_answer: null
---

## Depends on

T-2799, T-2800. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Build **one** source-bounded riding saddle/bridle/reins assembly for the chosen scene date, distinct from the draft harness. A dated later photograph alone cannot establish an 1835 saddle pattern.

- Choose and record cleared period construction evidence; identify riding style and seat/stirrup arrangement without unsupported breed/class assertions. Model saddle/tree silhouette, girth, stirrup leathers/stirrups, bridle/bit/reins and any source-supported accessories.
- Fit the T-2800 body without floating leather or visible penetration; include saddle/seat, stirrup, hand/rein and bit anchors for portable-human rig fitting.
- Export modular portable gear and LODs with material/license provenance, scaled assemblies and close side/front/three-quarter comparisons. State reconstructed unseen construction and color as liberties.
- Verify the exported assembly in browser and document bytes, material slots and texture memory; rider animation/interaction remains later tickets.

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

## Parallel checkpoint — 2026-10-19

Outside-app original reconstructed 1835 saddle/bridle geometry checkpoint archived. Static rein endpoint mismatch10.957mm and unfinished visual shape retained; no rider/period/photo acceptance. See evidence/period-transport-2026-10-18/parallel-refinement-2026-10-19/ and CHECKPOINT.md. PR1041 remains draft; conditional dev merge awaits green final-head gates.


## Progress — 2026-10-19 15:29 UTC

Portable riding-rein candidate a457874a appends glTF root/head skinning to the two existing reins with exact source geometry/BIN prefix. Actual Three checks PASS84 rows (21 walk samples, both sides, identity/transformed parent); max bit residual1.92e-8m/hand3.40e-8m and old10.957mmfailure reproduced. Deterministic, Khronos0errors/2explicit NODE_SKINNED_MESH_NON_ROOT warnings; first36zero-slot warnings preserved and concretely corrected. No collision/rider/ab70/physical-force/period/photo acceptance or app installation. All source/results in github-backup-1529/riding-rein-skin-endpoints-2026-10-19.tar.gz; final independent readback pending.


## Progress — 2026-10-19 15:59 UTC

Newb683 five-shell refinement source/geometry/readback/idlefit PASS and12actualmatchedbrowserframes PASSengineering. Roundedwaist/hems improve oldsurface but exposedwoodarch/tallbox remainvisuallyUNACCEPTED. Preserved b7da source/oldinputs/model/proofs+nextsourceplan and d6df actualimages. OriginalA457rein skin/24otherparts/rig/sockets exact. No newab70/rider/periodphotoacceptance orappinstallation.


## Progress — 2026-10-19 16:20 UTC

New b870 saddle covers pass readback, wood-cover and complete idle horse intersection checks, and12 matched browser frames pass framing/controls/GL checks. All24 protected parts and prior rein binding remain exact. Evidence25258cfc is pushed in855e0378. Root inspected the close image: a pale structural band and steep boxlike profile remain visibly unfinished. Subsequent decoded geometry analysis identifies panel/leather interpenetration outside the earlier horse-only test scope; a coherent layering plan is being prepared. No production, rider, moving fit or photographic acceptance and no app installation.


## Progress — 2026-10-19: underbelly construction and remaining leather crossings

New saddle 83f7b0b9 passes the two original negative controls, actual export/readback, Khronos (zero errors; two inherited skin warnings), idle capture and all 29 self-embedding scopes. Assembly fails at pair 185/301: left quarter crosses the original stirrup leather. Whole-horse checks did not run. Saved-array diagnosis also finds both original leather routes crossing jockeys and irons. Failure archive afe90d47 is preserved.

The next source scope includes both leather routes (16 changed/13 protected parts); geometry trial is not released. Credible attachment/routing and any required small layer amendment need explicit source review. No proper crossing is waived and no riding/photo acceptance is claimed.


## Measured progress — 2026-10-19 20:55 UTC

Root-peel saddle candidateff905fee passes all7 negative stages, source/readback/Khronos/capture and all29 self scopes. The inherited billet/root crossing is repaired. Assembly stops at pair308/328 on an unclassified raw leather/iron contact with no strict-proper witness;307 pairs are complete, remaining assembly/whole-horse/visual checks are unrun. Full failure77429dc5 is preserved; exact source-owned contact diagnosis continues without waiver or automatic retry.

Recovery: `evidence/period-transport-2026-10-18/CHECKPOINT.md`, current backup `github-backup-204639`. Ticket remains open; no status/claim/PR association changed by this evidence note.


## Measured progress — 2026-10-19 21:23 UTC

Saved exact witness analysis found60 genuine proper crossings,30 per side, between ff905 folded stirrup leather and neighboring iron arch segments. A duplicate-boundary alias correction alone cannot qualify that asset. The next central-fold source narrows the fold to about25.5mm and explicitly owns two iron subdivisions, expanding coverage to18 affected parts/351 relevant interpart pairs/18 whole-horse comparisons while retaining all29 self checks. Corrected source archive dc44fe47 is frozen and undergoing full independent review; no actual central-fold candidate exists yet. Source and original failures are backed up; riding, load and photographic acceptance remain open.

Recovery: `evidence/period-transport-2026-10-18/CHECKPOINT.md`. This evidence note changes no ticket state, claim or PR association.
