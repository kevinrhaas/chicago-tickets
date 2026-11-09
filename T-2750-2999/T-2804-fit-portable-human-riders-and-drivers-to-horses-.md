---
id: T-2804
title: Fit portable-human riders and drivers to horses and vehicles
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-2798
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

## Queue acceptance audit — 9 November 2026

Reopened for the remaining mounted-rider and synchronized gait/fit requirements. PR #1733 improved seated-driver clothing; that delivery remains accepted. The reviewed runtime has seated drivers but no mounted horse rider, fitted saddle/stirrups or accepted rider idle/walk/trot assembly. Riding gear (T-2802) and mounting controls (T-2805) remain separate open work; preserve the accepted driver/clothing increments. Reviewed against DEV `dc998577d76a09a31a5519b7deb0c0c0f6e1f869` and the merged PR evidence. This restores unfinished acceptance; it does not revert delivered code or revoke the completed increments.


## Verified incremental progress — 2026-11-04 09:58 UTC

PR [#1649](https://github.com/kevinrhaas/chicago/pull/1649) merged as `9881d782370d612c3ca521df383d67b1bb48487f`. PR [#1693](https://github.com/kevinrhaas/chicago/pull/1693) merged as `7e1445624ac1c642c8337269023c90dac9bf3e56`; its Full/Balanced seated head/neck glance was subsequently verified in 20 exact public DEV responses. Production was not promoted. This dated update supersedes the older pending/partial delivery notes below.

PR [#1700](https://github.com/kevinrhaas/chicago/pull/1700), head `79e302ee4b8648b2b89e81ef504049010de4cb7e`, is pushed and open with the four lower-detail driver clothing assets. All four local native gate parts passed with the recorded final metadata bridge; CI native8, humans and moving/release passed. Frame measurements passed 8/9: 1904 mobile memory was 403.635 MiB against the unchanged 400 MiB ceiling. An exact unchanged DEV-parent control also exceeded 400 MiB (403.195 MiB), with byte-identical GPU geometry/texture totals; a lossless repeated-scalar buffer optimization is being validated separately. The two full smoke runs were still active at the checkpoint; no all-green claim or merge is made. Current-horse native rest geometry is measured on the actual 26-joint horse. Saddle/rider fitting is a prepared proposal, not accepted geometry; Joseph still needs a proper named portable export.

[Immutable evidence checkpoint](https://github.com/kevinrhaas/chicago-evidence/blob/2f6393a27913ad33c68fc87d87728036c83975df/evidence/transport-pr1697-pr1700-validation-repairs-and-current-horse-2026-11-04/MANIFEST.json). Broad animation, clothing/photographic, natural gait and boarding/riding acceptance remain open. This progress note preserves the ticket's existing claimed state, claim owner/time, `pr:null`, acceptance and queue position.

## Incremental DEV delivery — PR #1693 merged, 2026-11-04 UTC

PR [#1693](https://github.com/kevinrhaas/chicago/pull/1693) merged normally at 06:25:52 UTC as `7e1445624ac1c642c8337269023c90dac9bf3e56`, TREE `49418a270db689dfaf25a2d9426f31f165461aa2`. Its 30 selected checks closed with 23 successes and 7 expected skips on qualified synthetic `db938eee7b58fb17dbecabd55dacc1815d9b1b87`, TREE `f80f1f497c337205a3b39304b14682e019b589b3`; these measurements are not relabelled as a fresh run of the later merged tree. This increment adds independent seated head/neck looking in Full/Balanced only. Public DEV verification remains pending.

NEXT pace/cold-Find is staged in six files; the immutable checkpoint records the first two of four native gate parts passing, not a complete gate or delivery. [Immutable merge and partial-NEXT checkpoint](https://github.com/kevinrhaas/chicago-evidence/blob/6a3b186f7f7c1a65c370fc27db8b510a97aea61f/evidence/transport-pr1693-dev-merge-and-next-increment-checkpoint-2026-11-04/MANIFEST.json). Broad animation, horse gait, boarding/riding, photographic and clothing acceptance remain open. This ticket stays `claimed` with `pr:null`; no claim renewal or settlement is made.

## Incremental DEV delivery — PR #1649 merged, 2026-11-04 UTC

PR [#1649](https://github.com/kevinrhaas/chicago/pull/1649) merged normally into DEV at2026-11-04T01:29:50Z as `9881d782370d612c3ca521df383d67b1bb48487f`. Its merged TREE equals the checked a620 TREE. All30 current CI checks completed:23success/7expectedskips, zero failures; the complete native gate covers1155distinct steps and401self-tests across8parts, plus all9frame/memory jobs, native release32 and moving-frame gates. [Immutable merge/CI/failure evidence](https://github.com/kevinrhaas/chicago-evidence/blob/a0881166e495048956c642924f30cbc04a44dded/evidence/transport-pr1649-merged-dev-9881-final-ci-and-original-world-negatives-2026-11-04/MANIFEST.json).

Otis drives the reconstructed 1835 wagon circle and Hans drives the 1904 Brougham circuit in Full/Balanced. The feature adds shared Interact Stop/Continue/Step back and current-driver person lookup. Moving horses use the genuine current26 careful-walk clip (.135m per1.6s; routes .084375m/s), separate from standing quiet motion. Natural pace/stride, rider/boarding/contact and photographic acceptance remain open; no faster gait is claimed.

Supplemental world checks remain incomplete: current1904phone correct person card passes25.882s/30, but first Find touchStart acknowledgement takes32.886s/30; late cleanup Find movement is postdeadline only. The1835desktop route/independent circuit pass, while keyboard approach times out before Interact. Neither case proves full interaction acceptance. The direct1904desktop Stop/Continue case is still active at this update. Original failures and limits are preserved.

This ticket stays `claimed` with `pr:null`, so this partial merge does not settle it as fully done.

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

## Parallel checkpoint — 2026-10-19

Outside-app named-resident driver adapter and source arm-IK/seat fit prepared. Preserve existing identity/date, no invented occupation/likeness, no keyframed scale. Actual canonical export/clothed contact/loaded reins remain pending. See evidence/period-transport-2026-10-18/parallel-refinement-2026-10-19/ and CHECKPOINT.md. PR1041 remains draft; conditional dev merge awaits green final-head gates.


### Progress 2026-10-19 13:42 UTC

Supported W01 geometry and desktop/mobile8-view browser checks pass; visiblebench now installed in uncommitted app. Namedseatedv2 still outside; canonicalclothed result pendingCI, no occupant/photoacceptance.


### Progress 2026-10-19 14:11 UTC

Supported bench and named sit_drive authoring committed/pushed09a3ad1d4;1016localsteps+publishedbenchbothviewportsPASS. Freshcanonical BOTHflagsrun39266264143 pending; actualclothedseated/master/contact acceptance remainsopen. PR1041draft/unmerged, devmergeonlywhengreen.


## Progress — 2026-10-19 15:59 UTC

Root corrected Otis proposed page source/published data+assetbase using actualproject resolveBases and fixed nonexistentThree/build import. Threeactualresolverlayoutcases/queryoverrides+independent sourcereviewPASS; full sourcefca804 backed. Actualapprovednamed4LODbytes/hashes remainunavailable and notsubstituted. Useraskedapplyalready-preparedcloudnetworkdraft16; no blockedassetdownload retry/relay oractualperson/render/driverfit acceptance.


## Measured progress — 2026-10-19 20:55 UTC

Named1812/1904 source studies in draftPR1099 preserve identified records and appearance reconstruction limits. Kinzie currently supplies standing/walking studies; Glessner standing/walking/passenger, with no invented coachman assignment. Actual export build failed and is being diagnosed. Existing1835 named seated-driver authoring remains historical input evidence; occupied rider/driver fit, real rein grip, scene placement and riding/boarding are not accepted.

Recovery: `evidence/period-transport-2026-10-18/CHECKPOINT.md`, current backup `github-backup-204639`. Ticket remains open; no status/claim/PR association changed by this evidence note.


## Final handover — 2026-10-19 22:40 UTC

Portable1835 human/driver-study foundation landed with PR1041 into DEV; actual occupied wagon or riding deployment remains unfinished. Kinzie1812/Glessner1904 source remains draftPR1099 with a diagnosed failed normal check and reviewed uninstalled recovery, not working world people. Glessner remains standing/walking/passenger only, not a coachman/rider. Complete next-agent instructions are in root HANDOVER.md.

Photographic/interaction acceptance remains open; this evidence note changes no ticket state or claim.

**Released 2026-10-21** (claim of continuing parallel period transport team 10/19/2026, 1:49:22 PM CT): Claims audit: reopen stale inactive work; reference and carriage work immediately reassigned individually for independent parallel completion

**Released 2026-10-23** (claim of Codex resumed parallel people and transport completion 2026-10-23 22:45 UTC 10/23/2026, 5:45:15 PM CT): Bardwell seated source and all-eight engineering fit proofs are checkpointed in chicago-evidence bdbac39 transport-refinement-resume-2026-10-23; canonical Blender regeneration, fresh export contact and released rider/driver portrayal remain next. Shipping group is T3083/T3086/T3087, not this broad ticket.


## Owner steering — 2 November 2026: visible driven loops and interaction

Owner: “Keep going and please make some visible progress … you can make incremental progress”. Owner also asks to use the fort gate interaction pattern for people, horses, wagons and carriages, and: “a person driving a wagon or carriage on a circle loop on 1904 and 1835, and also be able to walk up to one and interact with it”.

Extend this existing driver ticket rather than file more tickets. Work toward one bounded, visible driven loop in each year with a real period-clothed seated driver and a keyboard/touch approach action (stop/continue), preserving scene-date eligibility and the generic interaction engine. Routes, activity and appearances are reconstructed where unsupported. Incremental DEV delivery is explicitly authorized; photographic perfection is not a prerequisite for each partial delivery. Full riding, complete gear, photographic and whole-town traffic acceptance remain open. No runtime implementation or DEV merge is claimed by this note.
