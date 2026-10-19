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
claimed_by: continuing horse model agent 10/19/2026, 9:32:50 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T14:32:50.153Z
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

The outside b880 body / 078 gear pair passed its fresh 63-pose intersection/distance checks, and eight full plus two detail desktop/mobile views were captured. Root reviewed four actual current images and rejected photographic acceptance: primitive ear/head/neck silhouette, tubular limbs, angular hindquarters, flat tail and synthetic tack remain. The archive `horse-v2-pair-cpu-sidecar-visual-next-pr-2026-10-19.tar.gz` (SHA256 `e9e203ecef7d653c54ec0205efbbe13cac0a70c605a1066af93e0cf68c261456`) preserves all proof and the earlier framing failure. Sidecar-only cleanup passes 13 tests, including negative controls, under normal and optimized Python; original GLB bytes stay unchanged.

A new isolated ear-shape proposal is being compared with actually viewed, cleared Cuyer plates. Its altered ear geometry/weights and its own metadata authority are explicit; no metric, breed or Chicago identity is inferred from the diagrams. This proposal remains outside the fixed f97 merge candidate. Anatomical and photographic production acceptance stays open.


## Measured progress — 2026-10-19 10:13 UTC

Installed baselinehorse89b048 remains unchanged in pushed512f4a7e3. Next-only connectedhead090be8 material variant removes blackstripe but still inherits actualhead-ear selfcontacts and fails unchangedbridle fit; no nextgeometry installed. Concrete ear-root sourceproposal eebdefc39f2c... independently reconstructs44barycentric knots. Root approved22skull/18leaf amendment overexact6skullface complements with48protectedattributevectors unchanged; generator/test authoring outsideapp only, actualgeneration/fullSAT/browser held during town qualification. Sourcechart is not generated/animated/photo proof.


## Measured progress — 2026-10-19 11:42 UTC

The outside ear-root candidate `26027c225b0c2f3c6ed72543cb2e80238196a86815b7bb910744cbc65cb23ed3` now has two byte-identical builds (GLB, manifest, export proof and authority). Actual Khronos validation reports zero errors, zero warnings and 50 informational notices. Independent decoded checks confirm 11,452 triangles, six primitives, 15 skin joints, valid indices/bounds/unit normals/weight sums, unchanged original position/joint/weight prefixes and protected document. All attributes of the 48 protected head vertices remain exact; the only old normal changes are the declared 22 coat and 18 inner-ear ring vertices.

This is export/rest-data proof, not posed collision, gear-fit, visual or photographic acceptance. The independent mapping failure and its semantic-ownership diagnosis are preserved. Before collision execution, source review identified post-skinning float32 rounding above the unchanged 1e-8 predicate scale and an incomplete baseline negative-control guard. A separate checker revision is being prepared with binary64 world coordinates and the complete known negative cohort. No actual candidate capture/SAT/gear/browser check has run.

Source, both builds, validation receipts and failures are saved under `evidence/period-transport-2026-10-18/hair-normal-precision-2026-10-19/final-668e-qualification/`. The candidate remains outside frozen PR1041 (`668e48180`); photographic master and production acceptance remain open.


## Measured progress — 2026-10-19 11:56 UTC

After independent precision and negative-control review, ONE CPU idle0 capture/check ran against outside candidate26027c22 and parent090be8. The externally bounded trial stopped after19.05seconds with checker exit1. All12 known baseline strict source-owner negatives were detected exactly once. Candidate head/ear internal scope completed:2,960triangles,4,428 certified source edges,14,698 raw SAT contacts each proven confined to an owned source point, zero proper crossings and zero unexpected contacts.

The broader head-versus-all-rest scope FAILED at its first genuine head/neck penetration and remains incomplete. Candidate head triangle2055 is retained sourceface33 (baseline2061); neck triangle690 is unchanged. Independent source mapping confirms identical source ownership, actual world triangles and strict intersection witness in both parent and candidate. A pre-existing penetration remains a failure; it is not waived by the successful internal scope. No retries, repairs, gear checks, other poses, browser view or app installation ran.

Full failed trial archive SHA256e838ce94800efcb9f108cb8b78435283c9425f74e78bac47fdfa0fbda0ed89f7, separate source-owner diagnosis SHAb7ff11d02b590d5d51adc85a502544cf21ad3d15d5433aacb480e29ac6f751fe and independent assessment are saved in final-668e-qualification. Next geometry work must repair the source-owned neck portal, preserve the protected48 head attributes or explicitly amend their scope, and requalify actual geometry. Photographic/production acceptance remains open.


## Measured progress — 2026-10-19 12:45 UTC

ONE separately reviewed neck-side diagnostic ran with the explicit24-value quarter vector, preserving the head/ear/portal attributes and existing rig. It stopped in export phase1 after1.3754seconds: proposed movement exceeded the declared original local neck-column limit. No candidate GLB was encoded or emitted. Metadata, Khronos, independent rest readback, capture, collision, other poses, gear and browser checks did not run. No retry, alternate parameter or repair followed.

Full first-failure archive SHA256df1f5e1a130090da5d0ad445b4237e38c84d4e9d15826f7b8945f525ef92cdb8, exact vector, receipts and stderr are saved under devdfd-merge-requalification/quarter-first-actual-failure. A read-only source-feasibility analysis is now deriving whether any positive continuation parameter can satisfy the unchanged movement bound, rather than guessing another parameter. Existing26027 head/neck penetration remains unresolved; no new model or photographic/production acceptance is claimed.


### Progress 2026-10-19 12:52 UTC: infeasible neck deformation family

Read-only exact source algebra proves columns14..22 admit no positive lambda under the unchanged movement bound. Therefore a smaller positive vector cannot fix the failed quarter-vector export. Evidence archive0239b49df268030b9f2630c2aeb59d4d888c24f8fb655fb03de0fae3249824ac saved centrally in quarter-readonly-feasibility. No retry, model generation or guard relaxation. Local source-owned neck topology repair proposal and independent review now in progress outside app; feasibility/visual/posed/SAT acceptance remain unproven.


### Progress 2026-10-19 13:42 UTC

c243 topology candidate local REST/Khronos passed but actual binary64 idle FAILED at head/new-neck strict crossing; archive9e3bd699 preserved. No app install/acceptance.


## Hybrid head/neck progress — 2026-10-19 14:25 UTC

Outside-app candidate `192204d9…` replaces the folded lower rear-head/neck join: 96 neck faces and 48 lower head faces retire; 720 new vertices and 1,492 faces form the replacement. The upper poll/ear join, eyes, muzzle, all original attribute bytes and rig/clips remain exact. Local export and Khronos passed, and independent actual REST/ownership confirms the declared head disk and neck annulus. One actual animated idle check is running; no collision, anatomy, photographic or production acceptance follows from these local checks. Source and actual local evidence are saved in `evidence/period-transport-2026-10-18/next-visible-parcels-2026-10-19/actual-progress-1425/`.


### Actual idle result — 2026-10-19 14:27 UTC

Candidate `192204d9…` remains **unaccepted**. The retained head passed its internal and external checks, and the replacement neck passed internal checks. The first external neck failure is a proper crossing with retained mane triangle103, rather than the former head fold. The33.505-second run stopped at that witness; later external pairs remain untested. Failure archive `a7b4a70e…` is saved alongside the local proofs. A separate read-only inventory of the same captured arrays is diagnosing all remaining external collisions before a concrete mane-fit reconstruction. No photographic or full motion acceptance.


## Fitted mane and neck idle result — 2026-10-19 14:38 UTC

Candidate `1eee14e7…` passed all six complete binary64 idle collision scopes: retained head, new neck and replacement mane, each internally and against all other active horse triangles. No strict proper or unexpected SAT contacts; original negative controls still fail as intended. The fitted mane retires only the original240mane faces, preserving tail/dark head features and all old attribute bytes; the230vertex/456face replacement follows19actual coat roots with matched skin weights. Local export/Khronos0/0 and independent decoded REST/ownership passed. Archive `ba9d5b57…` is saved in actual-progress-1438.

This is one idle pose and a short25mm reconstructed roached hair mass. Other poses, gear, photographic grooming/anatomy and production acceptance remain open. Actual visual review follows before broader animation testing or installation.


## Combined horse and harness — 2026-10-19 15:00 UTC

Exact horse `ab70aff958bc8a2780458d37212be1866c730817f485fbebbf53bd3c0e3931c3` plus unchangedfe76 harness passed a complete bounded idle0 trial in36.13s. Decoded source binding and protectedrig/storage pass; all3,122head,1,492neck and456mane internal/external scopes pass; all36named gear parts against all13,226horse faces have0rawSAT/0proper contacts. Bit full-side unsigned clearance remains6.16167mm. Baseline negative crossings reproduce on the new horse; old baseline counts remain revision-specific.

Full source, model and evidence package `bbbe96f7…` plus authority packet `1cdfbf43…` are backed up in github-backup-1459. The eight-pose walk/trot stage and subsequent63-framegrid are being prepared; neither has executed. Photographic anatomy/grooming, continuous motion and production acceptance remain open.


## Progress — 2026-10-19 15:18 UTC

New cheek/throat shape 57d63e passed the single bounded idle0 structural/gear check with 379 moved vertices, unchanged rig/indices and 19.7675mm maximum displacement. Visual/anatomical acceptance and moving poses remain open. Source and actual proof are preserved in github-backup-1518. Immutable ab70/fe76 is starting eight quarter poses; the 63-pose grid remains conditional on all eight complete passes.


## Progress — 2026-10-19 15:29 UTC

Root inspected matched cheek57d frontquarter before/after and whole/profile images: modest cheek improvement but coarse eye/ear/body/limb/mane and open-mouth silhouette remain. Visual archive0ea4 and root review saved in github-backup-1529. Connected eye/orbit/eyelid source proposal now underway, qualified ab70 baseline unchanged. Complete declared source closure6f10 now preserved with exact licenses,153pins, twoauthor audits and root247member safety/hash audit; clean-machine replay remains unrun.


## Progress — 2026-10-19 15:42 UTC

New eye e578 passes one bounded idle/fullhead3410-neck1492-mane456/all36gear check, Khronos0/0. Protectedhalo initial pre-export refusal preserved and concretely corrected by excluding three protected nonboundary neck neighbors.16matchedframes remain VISUALLY UNACCEPTED: olive/buttoneye and inherited wideopenmouth. Root actually inspectedtightorbitbefore/after+profile. Next neutral bit-carrying mouth source investigation, no motionbaseline/appchanges.


## Progress — 2026-10-19: conforming neutral mouth, actual idle pass

Candidate e173bb8608a90e94a4f998e65ec9e09b2d2880d8639f2b1dc756f87815f485f8 passed one fixed 72.085-second trial and independent stored audit fa466871. Eight complete head/neck/mane/mouth structural scopes report zero strict proper or unexpected SAT contacts; owned contacts remain explicitly counted. All 36 harness parts clear the actual horse. Actual bit-side unsigned clearance minimum is 1.105 mm; virtual caps are analysis only. The original metadata-loss refusal is preserved and corrected by retaining the primitive's existing provenance fields. Full archive 0cbb3a06 is centrally backed up.

This qualifies one idle pose. Matched appearance review, anatomical/photo quality, motion, LODs and production acceptance remain open; no asset is installed or ticket closed.
