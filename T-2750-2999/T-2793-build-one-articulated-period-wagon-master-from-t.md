---
id: T-2793
title: Build one articulated period wagon master from the existing wagon families
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
claimed_by: wagon-model agent 10/18/2026, 1:45:25 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T18:45:25.994Z
decision: null
decision_answer: null
---

## Depends on

T-2792. Read each dependency before claiming; do not silently skip its proof.

## Scope and acceptance

Build **one** reusable articulated farm-box wagon master, as a bounded reconstruction for the earlier scene, retaining the existing wagon's documented provenance and proportions unless better evidence changes them explicitly. Covered/cart variants remain later follow-ups, not hidden acceptance.

- Read the existing 3.05 x 1.07 x 0.55 m reconstructed body and running gear in yard.js/data before changing it. Separate body, four wheels, front bogie/kingbolt, reach, tongue and hitch nodes; preserve correct axle/track and wheel clearance through a low-speed turn.
- Match a licensed construction reference and reviewed period analogue; wood grain, joinery, iron tires/hardware, paint wear and load attachments survive a close view without pretending colors or dimensions are attested.
- Produce canonical authored master + portable GLB/sidecar, license record and declared liberties. Supply neutral material variants within one bounded specimen, with compressed near/mid/far exports.
- Render close, side, front-three-quarter and distant views with a scale reference; compare against approved evidence and list remaining differences. Export/load it through the actual web path and measure budget.
- Existing 80 static wagons remain placed and operational; do not replace all of them or rebake unrelated buildings for this ticket.

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


## W01 visible refinement checkpoint, 2026-10-19

Reviewed original tapered octagonal spokes and1.2mm board/stave chamfers are integrated in the current combined source WIP, not yet committed. Exact bundle is saved alongside CHECKPOINT.md.9000→10792triangles,22mesh batches/47nodes and wheel bounds/pivots/socket frames unchanged; source wrapper regenerates exact reviewed GLB7749a0199b93bd196ecf6c3482af8ec537f1420a38f6fac88ab79fd8f34d44aa. Two-run determinism and independent Khronos0/0 passed on proposal bytes; controlled close/clay/mobile images were inspected. Full-view gain is modest; geometry cost and eventual LOD decision remain explicit. All dimensions/material variation are reconstructed engineering, no photographic/historical joinery acceptance. Combined full gate/commit pending; production ticket remains open.


## Measured progress — 2026-10-19 08:26 UTC

Combined PR1041 is committed and pushed at `f97ee94970385d35f469c449c6b111b0d8488057`, reconciled with dev c7770e99. Full local preflight passed 1,012 checks, and the remote required gate and canonical human workflow passed. The final 18-leg published desktop/mobile smoke matrix is running at that exact head; merge to dev remains conditional on all remaining checks and strict coverage. No production ticket closure. The separate C02 door/body portable package and actual browser proof remain saved for a later PR; construction/photo acceptance is still open.


## Measured progress — 2026-10-19 10:13 UTC

Saved implementation checkpoint512f4a7e3 is pushed, including reviewed C02 and devfb6a; fullpreflight1015/0 and postcommit checks pass. PR1041 remains draft: earlierf97 desktop13 failed draw331/330 and HUD31.23%/10; current targeted actual512f camera trace passes tint287,rowghost327,XRAY316 twice each, but does not reproduce331 or qualify wholematrix. HUDmeasurement correction is uncommitted under actualdiagnosis; no finalmatrix/merge yet. Wagon photographic/period/production acceptance remains open.


## Progress — 2026-10-19 14:20 UTC

Supported W01 bench and named-driver authoring are committed and pushed at `09a3ad1d4`; full local preflight passed 1,016 steps and the published bench passed desktop/mobile views. PR1041 remains draft while its 19 selected qualification runs complete. No photographic ticket closure.

Outside-app timber A/B candidate `9af2109f…` passed common-camera framing and geometry checks; root inspected actual desktop bench comparisons. Grain improves the flat baseline but remains broad/soft, and the full wagon still needs coherent wood, paint and iron detail. Eight actual captures are saved in `evidence/period-transport-2026-10-18/next-visible-parcels-2026-10-19/material-review-1420/`; the browser helper lacked a console listener, so console-error absence is unproven. Existing procedural maps have cleared project provenance; they are not photographic scans. A whole-wagon finish candidate is being developed outside the frozen release.


## Whole-wagon finish result — 2026-10-19 14:38 UTC

Outside-app filtered candidate `464e430d…` passed12actual desktop/mobile matched A/B captures, keeping23draw batches and an estimated6MiB decoded mapped texture memory with mipmaps. Root inspected the actual bench image: finer irregular grain improves the flat baseline, while photographic timber, cut ends/hubs and optical calibration remain open. Earlier48MiB and regular-comb candidates are preserved as unaccepted. An original bounded fastener refinement is now under development, with no changes to current release09a.


## Progress — 2026-10-19 15:42 UTC

Frozen09a is already pushed. PR1041 merge still blocked on remaining mandatory workflows plus contradictory required-step metadata in two otherwise successful jobs39266459095/39266463876. Aggregate, single refresh and direct immutable job details all retain published-test in_progress/postpending. Preserved evidence in github-backup-1542. No finalv6/merge/waiver. A source-only exacttwo-attempt2 freshqualification plan is being reviewed; no rerunPOST yet.


## Merge recovery — 2026-10-19 16:20 UTC

PR1041 is already pushed. Fresh GitHub reconciliation found 16 old-head workflows successful, one cancelled after90m22s, and two running. Meanwhile dev advanced to28c53 and introduced a real smoke HUD conflict. Root merged dev locally, preserving both navigatorDock and confLegend. Independent index review confirms no assets or liberties were lost. Existing dev also carries its150-minute smoke policy. Local preflight is running after restoring three stale ignored Glessner files from dev's verified package; no new application commit yet. Fresh checks must qualify the eventual updated SHA. Old two-rerun recovery authority is invalidated; no bypass/merge occurred. Durable evidence is pushed in backup commits8a066c58 and855e0378. Photographic acceptance remains open.
