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
claimed_by: continuing parallel period transport team 10/19/2026, 1:49:16 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T18:49:16.875Z
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


## Measured progress — 2026-10-19 08:26 UTC

Current PR1041 baseline gear 45930f41 / horse 89b048b7 retains its 63-pose whole-horse four-part clearance proof: minimum 5.113260 mm, zero tested surface intersections. Outside next pair 078ed2ce / b880 has a fresh minimum 5.488604 mm for the four guarded parts; all 36 gear parts against the changed body patch have zero tested crossings and positive 3.254303 mm minimum, which is explicitly not a 5 mm claim for all gear. Corrected socket cap registration and six actual attachment overlaps pass, with all prior failed trials preserved.

The new actual views still show unaccepted pad/girth gaps, thick layered straps and unsupported static trace/rein rods. Vertex stand-off reaches about 54 mm; no acceptable upper-gap threshold or containment claim is invented. Loaded tack, dynamic reins/contacts, continuous motion, historical construction and photographic fit remain open. Both current and next-pair receipts are saved under the central transport evidence; next-pair bytes remain outside PR1041.


## Measured progress — 2026-10-19 10:13 UTC

Installedgear45930f41... remains the current validated baseline: fourchangedparts over63actualwholehorse idle/walk/trot samples0propercrossings,minimum5.113260mm; other32parts unchanged. Next-only078gear versus connectedhead854/090 FAILED firstidle with262rawSAT/258strictpairs; laterposes untested and no reroute accepted. Head-ear root repair source work is separate; no newgear installed and no pressurefit/containment/loadedtack/photo acceptance.


## Measured progress — 2026-10-19 11:42 UTC

The saved first-idle failure is now isolated by actual part and witness triangle: left cheekpiece 67 raw/67 proper pairs, right cheekpiece 63/63, browband 92/88 and noseband 40/40; crownpiece has zero in this one row. Total 262 raw SAT pairs and 258 proper crossings. The other 62 poses remain untested for this failed pair. Exact input hashes and triangle IDs are in the central `final-668e-qualification/next-headgear-source-analysis/` receipt.

These head straps are separate from the four qualified breastcollar/support/pad parts. The new ear-root candidate has only source/export/rest-data checks so far; it has not renewed any gear-fit proof. The proposed next repair follows actual cheek/orbital, frontal and muzzle contours while preserving unaffected parts, widths, thicknesses and attachments. No reroute, containment, loaded fit, full-motion or photographic acceptance is claimed. Current application gear and ticket state remain unchanged.


### Progress 2026-10-19 13:42 UTC

f89 preserves32otherparts; actual all36 idle globally FAILED152proper(bit44,breeching88,hips20), while fiveheadstraps0onlyidle0. Full598712archive saved. No63pose/visualacceptance.


### Progress 2026-10-19 14:11 UTC

fe76 actualbinary64idle globalFAIL44proper ONLYbitbar; all35nonbitparts0atidle0. Fullsource/rest/projection/witness/archivebf97 saved. No63pose/positiveclearance/visualacceptance; closedmouthbit interface remainsrealblocker.


## Mouth and combined fit progress — 2026-10-19 14:55 UTC

Oral candidate `21cadaa8…` passes decoded source binding and strict rest head self/bit checks: zero bit-side/head intersections,6.16167mm minimum full-side unsigned distance. Virtual caps are analysis only; actual bit mesh remains open-ended. Earlier FK-checker and three-corner-crossing failures are preserved; a reviewed two-face diagonal correction solved the latter without coordinate/tolerance changes.

A combined oral+repaired neck/mane+fe76gear candidate is now in its single bounded actual idle trial after executable source review. No combined fit, other pose, photographic or production acceptance yet. Exact rest-pass and reviewed source evidence are saved in actual-progress-1455.


## Combined horse and harness — 2026-10-19 15:00 UTC

Exact horse `ab70aff958bc8a2780458d37212be1866c730817f485fbebbf53bd3c0e3931c3` plus unchangedfe76 harness passed a complete bounded idle0 trial in36.13s. Decoded source binding and protectedrig/storage pass; all3,122head,1,492neck and456mane internal/external scopes pass; all36named gear parts against all13,226horse faces have0rawSAT/0proper contacts. Bit full-side unsigned clearance remains6.16167mm. Baseline negative crossings reproduce on the new horse; old baseline counts remain revision-specific.

Full source, model and evidence package `bbbe96f7…` plus authority packet `1cdfbf43…` are backed up in github-backup-1459. The eight-pose walk/trot stage and subsequent63-framegrid are being prepared; neither has executed. Photographic anatomy/grooming, continuous motion and production acceptance remain open.


## Progress — 2026-10-19 15:18 UTC

The new 57d63e anatomy variant clears all 36 unchanged fe76 harness parts at idle0 in the bounded strict check. This does not qualify moving fit/pressure. Motion qualification continues on immutable ab70/fe76, first eight quarter poses then conditional 63-grid. Complete external replay closure is being assembled separately; bbbe terminal archive alone is insufficient.


## Progress — 2026-10-19 15:29 UTC

Reviewed nonindexed capture correction enabled actual walk0. Complete structural head/neck/mane scopes PASS, then all36-part check found70proper breeching crossings ONLY against original right upper hind limb (tenfaces1620..1633); other35parts clear. FirstfailureSTOP: zero fullyqualifiedposes, remaining7/full63 NOTRUN, bitvolume not reached. Preserved e0c1 archive and exact70 ownership/witnesses. Capture-only63 now explicitly diagnostic to derive swept-hull breeching route, not fit approval.


## Progress — 2026-10-19 15:59 UTC

New swept-breeching3bb45 +immutableab70 actual idle0 and oldfailedwalk0 FULLPASS; then all8distinct walk/trotquarterposes FULLPASS269.63s, all36gear+fullhead/neck/mane/bit checks complete, independent artifact/hash auditPASS. Other35parts unchanged. Full63 nowrunning once, NOTaccepted yet. Complete source/model/actualproof e730/5c312f/991 and diagnosticcaptures backed github-backup-1559. Oldfe76walk70FAIL preserved; no pressure/continuous/photo/riding acceptance.


## Progress — 2026-10-19 16:20 UTC

The original ab70+3bb45 sampled-fit run continued through the executor interruption.35of63 poses have completed with all selected checks passing; the entire21-frame idle sequence is complete. Full-grid acceptance is pending terminal results. Immutable evidence chunks00–27 have been pushed;28–34 is ready for the next backup. The failed original archiver was confirmed defunct, and a reviewed exclusive atomic archiver resumed persistence without restarting or modifying the fit run. No continuous collision, force/pressure, grounding or photographic acceptance.


## Sampled-fit milestone — 2026-10-19 16:40 UTC

The original ab70+3bb45 run completed all63 selected poses successfully in2456.2018s:21eachidle/walk/trot, includingclipendpoints. All2268namedgearpart/pose checks report zero raw/proper intersections. Authorstoredreadback rehashed1575actualartifacts, source inventories and11archives. Finalindependentstoredreview is pending; no rerun. Nineimmutablechunks plus terminalcontrols are backed across the current GitHub evidence batches. This establishes sampled fit only; continuous collision, foot grounding, forces/pressure, vehicle traces and photographic acceptance remain open. Ticket remains active.


## Measured progress — 2026-10-19 20:55 UTC

Combined fitted-rear plus corrected-girth gear43bc48a5 passed idle source/decoded/dimension/self checks, all35 interpart comparisons and all36 parts against the whole horse. Independent stored audit replayed all76 inner faces/523 certificate leaves (maximum29.895mm under the declared30mm bound). Upper ends remain38.3–44.3mm away from existing hardware and explicitly unbound. Matched visual capture is active; new motion, complete hitch and photographic acceptance remain open.

Recovery: `evidence/period-transport-2026-10-18/CHECKPOINT.md`, current backup `github-backup-204639`. Ticket remains open; no status/claim/PR association changed by this evidence note.


## Final handover — 2026-10-19 22:40 UTC

Six-part upper attachment actual0752b0b1 failed affected pair86 after85 completed: pad178/support_l145 genuine transverse crossing. Independent audit proves this equals inherited parent pad34/support145; inherited overlap remains fatal. Later pairs/wholehorse/078negative/full532facefit UNRUN. Complete source/input/failure/audits f0b6172 saved in final backup224031. Next eight-part/252pair support-route reconstruction is a proposal only. Qualified lowergirth43bc static+visual retained; no complete harness/motion/photo acceptance.

Photographic/interaction acceptance remains open; this evidence note changes no ticket state or claim.
