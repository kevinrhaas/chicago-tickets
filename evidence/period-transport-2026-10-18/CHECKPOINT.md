# Session recovery checkpoint — 2026-10-18

**Current human checkpoint: `0577792dc5b4107fcf4aeab0014d0b9fb3f44ab6`, pushed on `steward/generic-teamster-humans`, PR1046. Full preflight PASS:975steps/0failed; postcommit changelog PASS. Canonical resident workflow39173614006 PASSED at that exact SHA (all3masters/24GLBs/24desktop-mobile inspections); artifactvisualreview remains blocked. Transport PR1041 frozenhead e5e726ba8d8030216ad7769f0878e99fe8dbe43d passed978-step preflight;18full-coverage legs dispatched, outcome pending. Keep draft/no merge until actualcoverage +requiredchecks green. No local Blender. Never export CHICAGO_TICKETS_DIR into gates.**

Code repository: `kevinrhaas/chicago`, branch `steward/period-transport-2793`.
Latest transport commit: `1b3c73d22016596d07b133019df24422c2b54790` (merged dev `7d5daca7d82748acce0fda541c638b260bdd3be4`).
Previous modeling checkpoint: `6b51f65ca01921cfcdf447566774205671aca43d`.
First checkpoint: `7c61614c8f197e42da3720f6628d62722f6a560e`.

Start with `chicago/4d/docs/RESEARCH/period-transport-2026-10-18/README.md` in that commit. It records regeneration, inspection, browser checks, source limitations and next work. The transport collection is at `renderers/web/transport/`; it includes articulated wagon and carriage, a genuinely skinned horse with idle/walk, modular breastcollar harness, and a coupled moving hitch fixture. Generators, parameters, GLBs, screenshots, test receipts and compressed hitch observations are committed together.

Validation before commit: clean full `tools/check.sh` passed all 971 steps, exit 0 (374 intentional self-tests). All four GLBs passed independent Khronos validation with zero errors/warnings; regeneration matched bytes. Desktop/mobile specimen and hitch checks passed. Actual skinned sole vertices were sampled over 1,001 walk frames; compensated stance drift is now 0.0201 mm (first checkpoint 6.43 mm). These checks establish development-study behavior, not photographic or historical production acceptance.

No production ticket is closed. T-2792/T-2799 research and T-2793/T-2794/T-2800/T-2801 models/gear are started. T-2795 coupling is partially explored. Preserve queue bands 8D/8E below portable humans. Continue source-plate and measured-construction review, anatomical/material quality, harness routing and robust fit margins (former 45 mm shaft-loop mismatch resolved by reconstructed tugs; breastcollar/upperlimb sampled margin only 0.589 mm), LODs and collision qualification before town traffic, riders or boarding. Carriage/hitch motion now reads exported dimensions and stride, verified by metadata perturbation and actual wheel-center travel. Changes to geometry still require renewed fit checks. Existing static town wagons remain intact.

Research reports here distinguish inspected photographs, actually read OCR, and unread catalog/plate leads. Pullman ownership is unproven. Stubbs edition metadata is `1766 [i.e. 1815?]`; plates remain unseen. OCR component dimensions are not page-verified measurements.

GitHub API access recovered. Draft PR [#1041](https://github.com/kevinrhaas/chicago/pull/1041) targets dev at exact transport head `1b3c73d22016596d07b133019df24422c2b54790`. The owner explicitly authorized merging to dev once all checks are green. Keep it draft until the full desktop/mobile smokes and required checks pass; then ready and merge that exact head. Production promotion is outside this authorization. Do not bypass the proxy.

## Follow-up recovery

Read [fit-followup.md](fit-followup.md) for the second checkpoint. Its exact full precommit gate passed 971 steps, none red, exit 0; local log `/tmp/transport-followup-check-complete.log`. Horse silhouettes/gait, physical tugs, actual front-turntable rolling and collar fit are refined. Full triangle checks replaced misleading nearest-face signs in the limb test. Corrected and failed receipts are preserved. No photographic, continuous-collision, animal-suitability, braking/holdback or production scene acceptance is claimed.

## Validation and human work (updated after terminal CI results)

The exact merged-tree local preflight passed 972 steps, none red. Published fixed
desktop stage 1 passed 95/0; other interrupted earlier runs retain their failures and
are not full passes. The existing smoke harness cold device probe now runs before
the first town render; timing limits and application device behavior are unchanged.
Full desktop smoke [39164186323](https://github.com/kevinrhaas/chicago/actions/runs/39164186323),
and full mobile [39164260098](https://github.com/kevinrhaas/chicago/actions/runs/39164260098)
have finished on that exact head. Fast gate
[39164182373](https://github.com/kevinrhaas/chicago/actions/runs/39164182373) passed.
All nineteen checks are terminal. Mobile FAILED (680 passed / 1 failed): stage 5 far-merge triangle delta -10,353. Desktop CANCELLED at the 90-minute job timeout, with 353 passes / 4 failures observed before incomplete stage coverage: yard restoration pixels, confidence restoration pixels, far-merge triangle delta -20,415, and stage 6 Guide sheet readiness. No merge is permitted on this evidence. Terminal logs and hash receipts are saved here.

Local code checkout is now on `steward/generic-teamster-humans`, branched from
transport head1b3c73d. T2672 policy, T1789 body preparation/canonical builder, and
T2823 documented anonymous-fallback mechanics are committed and pushed at
**6ae3c766f174546a53c34db02c024abfd2667517** (first checkpoint e6f72ceb4), draft
[PR1046](https://github.com/kevinrhaas/chicago/pull/1046). Full preflight passed:
973 check.sh steps, zero failed, plus changelog and ticket-ID checks. The postcommit
changelog check also passed. No local Blender was run. Canonical human workflow
[39169918123](https://github.com/kevinrhaas/chicago/actions/runs/39169918123) was
dispatched with build_teamsters=true on that exact SHA and FAILED during the first resident export. All prepared files reproduced exactly, then Otis master and all eight source/web GLBs were built. The unchanged human guard rejected float32 thigh scale residue and source/web skin-palette multiplicity. The first
manual build failed before Blender; see the runtime preparation repair below. Download
its actual artifacts and inspect them before accepting model quality. The owner subsequently directed
existing attested/inferred/reconstructed people first, anonymous only if no choice.
The first actual references are existing reconstructed 1835 residents
`rc_bardwell_otis`, `rc_dufresne_joseph`, `rc_flynn_martin`. Do not fabricate new
resident biographies, backdate 1839 occupations, or claim photographic likeness.

Read code `docs/RESEARCH/resident-teamsters-2026-10-18/README.md` for the canonical
CI build route, output IDs and remaining acceptance. Blender is forbidden locally;
CI outputs must be downloaded, independently inspected and then checked/committed.
No new scene placements, seated driver, actual riding tack, photographic human,
or production ticket completion has occurred. The original official CC0 Toigo bronze 2048² PNG and exact source receipts are
ingested and packed by the builder. No fabricated 4K/detail maps or portrait
likeness is claimed. Its actual Blender/glTF appearance remains pending the CI
output. Upstream source bytes are pinned; LICENSE.md.gz preserves its original
notice bytes exactly and is hash-verified before preparation.

Reduced original eye components and the unapplied integration patch are preserved
in human-next-drafts/eyes-reduced. Whole-person added triangles by LOD are
1584/736/288/128. CPU diagnostics and topology checks are not Blender/glTF
acceptance. Review the initial CI output before integrating this follow-up.

## Canonical CI preparation repair committed

Human workflow39168738942 completed: existing fixture byte reproduction and
desktop/mobile actor checks PASS; resident study FAILED before Blender at neutral
prepared input byte40084. The retained failure log and resident-prep-runtime-diff.json
show Python3.11 left-fold sum reproduces that exact offset (max6.66e-16). No actual
resident masters/GLBs were built. Do not report that run green.

Committed follow-up6ae3c766f uses explicit math.fsum reductions and regenerated neutral,
adult25 and adult35 inputs/reports. Eleven actual-source tests pass, including full
serialized-byte comparison under emulated legacy sum. System Python3.13 independently
regenerated all three exact bytes. Full preflight PASS (973 steps, zero failed), plus postcommit changelog PASS.
Code is committed/pushed; corrected canonical workflow39169918123 confirmed the input byte fix on6ae3c766f but failed later as recorded above. Full passing transcripts and hashes are saved as resident-check-6ae3c766f
receipts here. Keep the exact-byte CI assertion. No local Blender.

## Export repair and next validation

A subsequent bounded authored-only repair is staged on the human branch and full local preflight is running. It verifies actual Blender rigid authoring state before correcting bounded float32 joint-scale residue; it never relaxes the existing human contract. Exact equivalent skin bindings are consolidated before scene-volume quantization. Existing fixture behavior remains on its original path. Twelve frame-repair and nine skin tests pass. Actual Blender runtime, skin deformation and visual acceptance are pending the next CI run. Do not accept these changes merely from this checkpoint; record the committed SHA and actual gate result next.

The ordinary artifact download for run39169918123 is blocked with HTTP403 at the exact host productionresultssa13.blob.core.windows.net. This host was added to the saved cloud configuration draft; user Review/Save/Publish is still needed to apply that draft. No proxy bypass or uninspected model acceptance.

Smoke instrument proposals remain outside the app: synchronous same-camera on/off/on sampling retains zero-triangle and reverse-restoration assertions; Guide readiness matches the existing stage12 60-second budget without changing content assertions. A bounded published yard probe passed exact restoration (mean0/worst0); confidence remained incomplete and no pixel-threshold/readiness change is justified by that probe. Full coverage will use the existing nine stage groups for both viewports (18 runs), one frozen transport SHA, with aggregate receipts; original failed/timed-out results remain retained.

## Ticket override isolation correction

Never export CHICAGO_TICKETS_DIR globally or into preflight/check.sh. Prefix ONLY intended ticket mutations with CHICAGO_TICKETS_DIR=/workspace/chicago-tickets. Root mistakenly exported it into a full gate; 11 sandbox-ticket steps failed and three test commits reached the real tickets main. QUEUE/T0001/T0002 were restored byte-for-byte to f858c31f and the synthetic T2826 was removed. Repair commit4c718c8c is pushed, without rewriting history. Audit and failed gate logs are preserved here. The corrected full gate is rerunning with the override explicitly unset; no green claim yet. The cloud startup draft was corrected accordingly (saved, still requires Review/Save/Publish).

Actual-function AST wiring tests also caught and repaired a dictionary/string mismatch in exported proof references. Fourteen frame/wiring and nine skin tests now pass. Code remains staged pending the corrected full gate. Next commit/CI SHA must replace this staged checkpoint.

Dev has advanced to a99f3623849bb2e7ce6c7d255ff3adecc66d5dcd (at last read), including an upstream120s Guide readiness fix and new rendering/UI content. Merge latest dev into transport before replacement full coverage; preserve upstream Guide fix. Source gait study now quantifies unsupported feet at4/7walkkeys from actual adult25/35 rigs and shoe geometry. The unintegrated diagnostic/proposal is saved under human-next-drafts/resident-gait-draft.tar.gz; it is not exported skin or photographic gait acceptance.

## Export repair checkpoint committed and pushed

0577792dc5b4107fcf4aeab0014d0b9fb3f44ab6 includes the strict authored rigid-frame proof, bounded scale repair, exact skin consolidation, scene-volume quantization and actual-function wiring regression. Clean full preflight passed975steps with0failed after unsetting the ticket override. All14frame/wiring +9skin tests pass. Postcommit changelog PASS. Full passing logs and hashes saved here. Canonical workflow39173614006 (build_teamsters=true) is running at that exact SHA; inspect real results before reporting green or accepting models. Original fixture path unchanged.

Unintegrated mature1904body for existing attested glessner_john_j is saved under human-next-drafts/resident-1904-body-draft.tar.gz. Appearance/wardrobe/actions remain reconstructed, not a portrait or professional coachman claim. Gait draft now has actual 1001-phase IK/contact source prototypes for both body ages; no BPy/export/visual gait acceptance. Inspection hardening is being independently reviewed, including actual texture binding/temporal motion and raw-vs-cleaned skin comparison; use its latest corrected proposal, not older copies.

## Active transport merge/preflight recovery

Local checkout is back on steward/period-transport-2793, merging current dev a99f3623849bb2e7ce6c7d255ff3adecc66d5dcd with --no-commit. The only conflict was generated1835sources/index.json; node tools/rederive.mjs --resolve rebuilt its declared tail (50steps,2laps, last moved nothing), staged outputs, and cleared the conflict. Both current-dev and transport inputs are retained. Smoke now has fresh synchronous far-merge on/off/on with unchanged zero-triangle requirement and new exact restoration assertions, plus diagnostic-only state fingerprints around yard/confidence captures. Upstream120-second Guide wait retained; outside60-second proposal NOTapplied. Full preflight is RUNNING at /tmp/transport-current-dev-preflight.log with CHICAGO_TICKETS_DIR explicitly unset. Commit/push only if final PASS, then freezehead and dispatch18existing manual smoke legs. Do not discard staged incoming dev edits or claim a merge yet.

Human canonical workflow39173614006 at0577792dc passed existingfixture/browseractor, all3 canonicalmasterbuilds/source+webcontracts and independentKhronos container step; measure/inspection still running at last read. No artifact downloaded or photographic acceptance.

Grounded-gait integration proposal is saved under human-next-drafts/resident-grounded-gait-integration.tar.gz, frozen against0577792dc. Six tests pass; actual37key30fps SLERP+LINEAR source sampling over1001phases has~0.336mm plantedsole drift and~0.222mm maximum source penetration. It remains outsideapp and unverified in Blender/export/browser. Do not substitute dense-solver nearzero values for sampled interpolation metrics.

## Canonical resident CI passed

Workflow39173614006 at0577792dc5b4107fcf4aeab0014d0b9fb3f44ab6 completedSUCCESS. Existingfixture/actor passed; actualPython3.11 preparations reproduced; all3canonicalmasters and24source/webGLBs built and passed unchangedhumancontract; independentKhronos reported0errors/7warnings each;24desktop/mobile inspection runs mechanical_passed=true, photographic_gate=open. All12frame receipts parsed from log (use JSONDecoder.raw_decode because some log lines have trailing output), binary-preservation flags true. Full log/summary/hash receipts saved here. These are current mechanical checks; stronger texture/temporal/surface-comparison proposals remain unapplied.

Artifact12153626816 is148681132bytes. One ordinary download failed at productionresultssa17.blob.core.windows.net (newhost, exactHTTP403notobserved on that attempt). Saved configuration draft nowincludes exacthost17, preserving host13 and allothercustomdomains/startupguidance; revision15, requiresReview/Save/Publish, notapplied. No bypass/retry. Do not claim visual/photographic acceptance or classify the7warnings without actualreports.

## Transport local mirror cleanup and retry

The first current-dev full gate completed978steps with exactly1failure: check_published found12orphaned outputs in ignoredsite/4d/data/humans from the priorhumanbranch (8metadataJSON +4fixturewebGLBs). All12 were verified byte-for-byte against0577792dc source, archived outsideapp, then only that ignoredsubtree was removed. Receipt savedhere; no trackedsource was changed to resolve this failure. Full preflight rerunning in session55407, /tmp/transport-current-dev-preflight.log; source remains the staged a99f362+transport merge. No green/commit claim until finalresult. When switchingbranches with differentpublishrules, prevent orphaned outputs in the sharedgeneratedmirror; preserve/verify before targetedcleanup.

Latest savedhuman-inspection-hardening.patch is the6-file frozen057 proposal: realThreeCPUregression/checkstep, resident labels, temporal/texture/framing checks, morph-default preservation, per-resident21phase raw/source skinpairs inworkflow and actualKhronos issuecode logging. It remains UNAPPLIED; root stillneedsmeasuredisolationmetadata/fullgate/CI. Its REVIEW.md was rewritten around finalbehavior and knownlimitations; ignore superseded earlynotes.

## Transport current-dev checkpoint committed and smoke grid dispatched

Transport e5e726ba8d8030216ad7769f0878e99fe8dbe43d is committed/pushed, mergingdev a99f362. Finalclean fullpreflight PASS978steps/0failed/376intentionalselftests, postcommit changelog PASS. Passinglogs/hashes savedhere. Exactly18 existingmanualsmokeworkflowPOSTs succeeded and18actualruns were discovered withthishead, saved intransport-smoke-dispatch-e5e726ba8.json. BranchisFROZEN; do notpush/advance it while collectingcoverage. Eachlegpartial; aggregatecoverage remainsUNPROVEN. Agent environment_validation monitorslogs/pairing/coverage; root mustverifyrequiredchecksandmergepolicy beforePR1041ready/merge. Originalfailed/timedoutlogsretained.

Root can now switch back tohuman057branch, merge thistransportcheckpoint withoutcommitting early, integrate reviewedQA/groundedgait proposal, measureisolationmetadata, fullgate/commit/CI. No local Blender. Actualbodyartifactvisualreview remainsblocked pendingapplyingnetworkdraft15; human057canonicalCIpassedmechanicalonly. Preserve bothhead commits andunfinishedproductiontickets.

## Resident integration in progress

Current checkout is steward/generic-teamster-humans at0577792dc, merging frozen transport e5e726ba8 with --no-commit. Preserve incoming staged dev/transport changes. QA6-file and grounded-gait4-file patches ARE NOW APPLIED. Generated conflicts liberties.json/source_use_coverage.md are being rebuilt by node tools/rederive.mjs --resolve from chicago/4d; log /tmp/resident-current-dev-rederive.log, root execsession6078. An initial command from repository root failed before derivation (module path missing), corrected without reapplying patches. No new code commit/gate acceptance yet. Add gait test to check.sh, measure both new test tools isolation, fullpreflight beforecommit; actualBPy/GLB contact still pendingnextCI. Transport18legs running/queued on unchanged e5; validationagent watches exacthead.

## Resident conflict rebuild and further saved proposals

Full --resolve stopped at unrelated manifest step24 measure_north_branch_banks.py --write: iiif.digitalcommonwealth.org HTTP tunnel403, original pinned raster absent. Do not substitute map bytes or bypass policy. Earlier steps produced no additional tracked diffs. Tools/rederive.mjs --tail tools/compile_liberties.py now runs manifest142..198 from committed merged inputs; second stabilization lap active in /tmp/resident-current-dev-tail.log (exec27642). This is a narrower rebuild, NOT a claimed full198step rederive. Generated conflicts remain unmerged until finaltailpass; fullcheck.sh must prove all mergedpopulation/model outputs still reproduce.

Focused app source checks pass:14frame/wiring,9skin,6groundedgait plus actualvendoredThreeCPUinspection regression. Actual dormant-morph extension and final12test loadedsolecontact patches are saved in human-next-drafts but not yetapplied. Portable contact patch requires actualloadedwalkspeed/duty/duration metadata and correctssinglematerialgroups; rootmustaddworkflowmaster+webinvocations and measure newtestisolation. Source-only residentwagon seatedIK draft and clearedshort04hairintegration draft also saved; neitherapplied/accepted, no localBlender. Currentnetworkstatus unchangedspec1/customhostsEMPTY; noartifactretry.

Transportfastgate39175867681 manuallyrequested once atfrozenshae5; validationagentwatches it separately from18smokelegs. First4acceptedlegs mobile1-2,3-4,5,8, includingoldfailedfarmergeleg. Remainingfullcoveragepending. PR1041bodyupdatedtoexacte5/978localpreflight; stilldraft.
