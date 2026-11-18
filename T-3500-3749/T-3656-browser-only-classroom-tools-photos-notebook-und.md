---
id: T-3656
title: Browser-only classroom tools: photos, notebook, understanding checks and lesson guides
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: 2197
claimed_by: run 11/18/2026, 12:14:46 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-18T18:14:48.664Z
decision: null
decision_answer: null
---

Browser-only classroom tools: photos, notebook, understanding checks and lesson guides.

**Acceptance:** Demonstrate an entirely browser-local capture → notebook → cited jaunt reflection → printable group lesson workflow, with bounded photo memory/storage, explicit storage failures, keyboard-labelled controls and no new service. Shared URLs contain public scene context only. Check real catalogs, grades and source references, and report validation limits honestly.

## Owner scope — 18 November 2026

Start the top no-new-server items in parallel and account for the whole attached list. Prioritize #2 photo/share, #3 field notebook, #4 ungraded understanding checks and #5 lesson guides. Deprioritize #1: Navigator session choices may eventually replace/release the current session or explicitly open a new browser tab; never automatically retain multiple worlds. Time travel and Google view already exist; device resource use is a concern.

The broader list and disposition are recorded in `chicago/4d/docs/CLASSROOM-FEATURES.md`. This ticket owns the first browser-only classroom workflow; it does not claim all twenty features are complete. No server purchase, cloud service activation, multiplayer or production promotion is included.


## Current recovery checkpoint — 18 November 2026, 21:05 UTC

Latest pushed first-delivery head is `45b35a2c7d910ec1e73f5a60489b1b22c4aff278` in
draft PR #2197. This changes runtime: caption fitting now uses bounded text measurements,
notebook drafts drop confirmed deleted IDs, classroom CSS loads on view mount, and the
shared-person callback uses an explicit `person` alias for the sidecar scanner.

Parts 1–7 passed before these resource repairs. Part 8 failed the person alias scan and
the era-page duplicate threshold (65,638 bytes). The publisher now confirms 65,534 bytes
after removing 104 bytes of global stylesheet links; full partition 8 is rerunning.
Preserve `/tmp/t3656-validator-failure-part8of8.log`. Latest-head source CI is
`44397687385`, moving/upload CI is `44397687404`. Superseded bb593 source was force-cancelled
after its aggregate stayed queued. Merge is still blocked on required green checks.

Actual Glessner caption Canvas2D measurements fell from 9,241 calls / 2–5.6 seconds to
17 calls / 3.6–4.9 ms, preserving full metadata. These are canvas-only local timings.
Browser regressions cover 120 cross-tab deleted/recreated notebook IDs, preserved drafts
on storage errors, actual lazy CSS, deduplication and iframe isolation. Evidence is in
`/tmp/t3658-resource-review/` and `/tmp/t3656-notebook-lazy-css.log`; code/tests are committed.

Old mobile all-15 and final photo/notebook reports cover runtime 6c83e8cf9. The baseline
desktop run `44372747109` is still in progress. Do not call those exact-current runtime
checks after this patch. Prepared fresh first-delivery harness:
`/tmp/t3656-resource-photo-notebook-smoke.mjs`, with QA_MANIFEST support. Once source8
finishes and CPU is quiet, snapshot the official mirror into
`/workspace/chicago-classroom-final-published`, verify authored files against Git with
`/tmp/t3656-resource-manifest.py`, and run each width to separate new report folders.
Original frozen build, manifest, harness and reports remain intact.

Combined follow-up branch remains based on `03ecd9678`. It includes docked-Home image
cleanup `2f42e3c60` and the resource-fix checkpoint `e579424f0`; hunt CSS is being made lazy
before final integration. Root must port the first delivery's latest style/person/tour
repairs before its full-town tests. After #2197 merges, rebase ONLY commits after 03ecd
onto actual DEV, preserving hunt/accessibility changes and avoiding duplicate first-delivery
history/changelog. No production promotion or new service activation.

Evidence checkpoint is `d57c0fdbd13c56995bc2af922d9cadb30e1daab3` in chicago-evidence.

## Previous recovery checkpoint — 18 November 2026, 20:44 UTC

Latest pushed code is `bb59311bfba32067a6f4ca3c8175deea2f05af38`; PR #2197 remains draft.
Runtime is unchanged from 6c83e8cf9. Local source partition 7 failed one test because its
fixed 200-character source regex no longer spanned the inserted notebook host. The test
now mounts the real Guide and checks that the original tour element leads controls and
hosted sections. Focused tour/Guide tests pass; isolated source mutations that move or
omit the tour are rejected. Official remeasurement records no in-tree writes; isolation
audit and self-tests pass. Full partition 7 is rerunning, then partition 8. Preserve the
original failure at `/tmp/t3656-tour-span-failure-part7of8.log` and negative-check receipts
at `/tmp/t3656-tour-order-negative-checks.json`.

Latest-head source CI is `44393940378`; moving/upload CI is `44393940359`. The superseded
03ecd source run was force-cancelled after the push left its aggregate queued. Desktop
renderer run `44372747109` is still running; all fifteen mobile stages remain green on
identical runtime. No DEV merge until remaining checks are green.

The combined follow-up branch `steward/t3657-t3658-hunt-accessibility` is pushed at
`f1f2229f0879c4f1771b07fd9409f994cfc6a986`, based on `03ecd9678`. It contains the daily
five-photo hunt and native zoom/modal accessibility work. Focused fixtures pass at both
widths; actual historical thumbnails have been visually checked. Full-town integration
is being prepared. After #2197 merges, rebase ONLY commits after 03ecd9678 onto actual
DEV, so the first delivery is not duplicated or its folded changelog reintroduced.

## Previous recovery checkpoint — 18 November 2026, 20:31 UTC

Latest pushed code head is `03ecd9678e15988abe44c50e27c2bd9fec569530`, PR #2197 still
draft. Runtime remains 6c83e8cf9. Source partitions 1–6 have passed locally; 7–8 are
running sequentially with four workers and no full browsers. Part 5 passed 175 checks
and part 6 passed 174. CI on previous head found the four new gate tests lacked rows
in `tools/step_isolation.json`. All four were genuinely measured with
`measure_step_isolation.mjs --tool`; each wrote nothing in-tree. Audit and self-tests
pass, and complete local part 6 now passes. Original CI failure log is preserved at
`/tmp/t3656-ci-part6-step-isolation-failure.log` (old run 44384392510, job135087069672).

ALL FIFTEEN published mobile stages are now green: local 1–12,14,15 plus unchanged
GitHub stage 13 run `44385930725`, job `135090381320`, which passed157/0 in8m28 with
zero page errors. Combined staged runs have921 passing assertions (726 staged and195
repeated scaffolding). Original capped local13 remains incomplete historical evidence,
not a pass. Current source CI is `44390718841`; current moving/upload CI is44390718901.
Desktop renderer run44372747109 remains in progress on identical runtime. New-head CI
must pass; superseded CI was cancelled and is not used to satisfy the new head.

Final actual published photo/person/notebook/link flows pass at BOTH390×780 and1280×800,
five checks each: canonical person citations, normal-frame bounded photo, actual Save
to notebook, note edit, exact photo/note/citations persistence on real shared navigation,
person/view restore and saved jaunt retained inactive. Zero errors/404s/overflow. Both
browsers closed. Evidence is pushed at2bbbc015cb3f0d865408a19d5405e612ce09d616 under the
same evidence folder; raw reports, hashes, harnesses and screenshots are retained.

Follow-up lanes are fully pushed and browser-fixture green: hunt final45f822b6e,
accessibility final8c291d0d8174f09278bcdf2dbf0c03d4128b10c6. They include real multi-touch
zoom, stable GPU buffer, magnified two-thumb roles and native horizontal panning fixes,
plus modal keyboard/isolation/cleanup. Hunt fixture covers five rounds with real catalog
but tiny test images. Full town/release gates for the combined group remain pending.
The photo agent is preparing `steward/t3657-t3658-hunt-accessibility` in chicago-hunt
from integration base03ecd9678. Before opening its DEV PR, first merge2197, then rebase
ONLY commits after03ecd9678 onto actual origin/dev; do not reintroduce the classroom
commits or folded changelog. First PR merge remains gated, no production promotion.

## Mobile stage 13 completion path — 18 November 2026, 20:00 UTC

The quiet local stage 13 reached 149 passing assertions and then hit the unchanged
595-second command cap (exit 124). Its final report has one failure, suite body
completion, because timeout termination closed the browser. It is **not a pass**;
the What's New reload tail remains unverified. Original log is
`/tmp/t3656-renderer-mobile-13.log`. No application assertion failed before the cap,
and no test or timeout was changed. Unchanged stage 13 is dispatched on current
head 7969031f0 as GitHub run `44385930725`, job `135090381320` (queued at this writing).
Mobile stages 14–15 continue locally with quiet CPU. Source parts 5–8 resume afterward.
Current-head moving-frames/upload-release jobs have started; source CI is queued.

Follow-up code is pushed: photo hunt branch has `90a8a38ce` and `b3b8a490b`;
accessibility branch has `4668c0cd5` and `bf0bc1af0`. Their pure checks pass, but browser
fixtures still wait for the quiet smoke window. Both isolated worktrees are clean.
Evidence repo latest is `51c0767f64385e6bb08fdc65c8ec6d3af7d89399`, including source 4,
mobile 11–12 and `/tmp/t3656-final-photo-notebook-smoke.mjs` prepared but unrun. Run that
final-runtime integration harness one viewport at a time after quiet smoke; it covers
actual photo save, person citations, notebook edits/persistence and share restoration.

## Current pushed head — 18 November 2026, 19:50 UTC

`7969031f049fb2d54df2ce8a6bccd014c5ea1a1e` is pushed on the classroom branch.
This third checkpoint changes only STATUS and verification records; runtime remains
`6c83e8cf9`. Source partitions 1–4 and published mobile stages 1–12 are green. Source
5–8 are deliberately paused for quiet mobile 13–15. Current exact-head PR workflows:
source gate `44384392510`, moving frames `44384392451`; the push supersedes earlier
PR CI, whose partial results cannot satisfy the new head. Full desktop renderer run `44372747109` continues on unchanged runtime 6c83.
Duplicate remote mobile run `44373274865` was deliberately cancelled to free runner
capacity; it is not counted as a completed pass. Local staged mobile coverage remains
the completion path. Superseded source run `44375593498` was force-cancelled after its
always-run aggregate job remained queued and held the newer run in concurrency-pending;
only this session’s superseded run was cancelled.
PR #2197 remains draft and unmerged. The corrected evidence scope is in STATUS and the
PR body; later receipts go to the evidence repo/ticket to avoid repeatedly restarting CI.

## Recovery and evidence checkpoint — 18 November 2026

Code remains pushed at `cbf3408e032eb6341df9d52bfbb289810035f412` on
`steward/t3656-browser-classroom`, draft PR #2197. Runtime is unchanged from
`6c83e8cf9558c0d6f9ffb422f299764837fc4ed2`. Source parts 1–3 and published mobile
stages 1–11 passed. A second workspace transition interrupted source part 4, which
is rerunning; mobile 11 survived and finished without a duplicate run. Stage 12 is
running. Source workers will pause between partitions while mobile 13–15 need quiet
CPU. The full desktop and mobile GitHub runs remain in progress; exact-head source
CI has passed its first partition, with the rest queued at the last reading.

Completed evidence is now backed up in `kevinrhaas/chicago-evidence`, commit
`3ed0baa57bd8708cf2cdf5f74c68b0ea35ddcbb1`, folder
`evidence/t3656-browser-classroom-2026-11-18/`. Its README distinguishes checked
coverage, pending work and runtime provenance. This archive currently includes source
1–3 and mobile 1–10; later results still need adding.

**Evidence correction:** the older full-town photo harness had `photoOnly = true`.
Its notebook-persistence report label was too broad: that assertion was skipped and
notebook was null. Notebook persistence passed in the separate two-width browser
fixture, not those town reports. The photo reports also precede the final person
selection and lesson reader-text changes. A reconstructed hash-matching diff in the
evidence archive proves the capture/render path stayed unchanged; do not describe
those historical reports as exact-final-runtime full-town notebook coverage.

The next bounded server-free group is claimed as T-3657 (five-photo hunt) and T-3658
(browser magnification and keyboard picture dialogs). Work is isolated in
`/workspace/chicago-hunt` and `/workspace/chicago-accessibility`, branches
`steward/t3657-t3658-photo-hunt` and `steward/t3657-t3658-accessibility`, based on cbf3408e0.
Prepare/checkpoint it while this PR validates, but merge the classroom PR first when
green, then integrate the follow-up onto dev. No production promotion.

## Latest green coverage — 18 November 2026, 19:33 UTC

PR2197 remains draft at pushed headcbf3408e0; no application source changed.
Local source partitions1/8,2/8,3/8 are green (175,174,174checks). The complete3/8 rerun
clears the ticket-layout issue. Part4/8 is running, then5–8; use three workers and pause
between partitions when the smoke operator needs a second full world.

All published mobile stages1–8 are green, including the unchanged quiet recovery retry.
Stage9 is running. Full renderer workflows44372747109 (desktop) and44373274865 (mobile)
are in progress on GitHub. Required PR gate44375593498 and moving-frames44375593479 were
still queued at the last reading. Both earlier local issues are cleared; do not infer
that the remaining queued/unrun stages have passed. Keep the PR draft until complete.

## Recovery test cleared — 18 November 2026, 19:26 UTC

Unchanged official mobile6 passed in5m32s with source-check workers stopped:24checks,
zero failures, second town ready in198.6s within the unchanged240s limit, both real
context losses/reloads verified, and zero secondary-page errors. Original contention
failure remains `/tmp/t3656-renderer-mobile-6-contention-failure.log`; the passing quiet
retry is now canonical `/tmp/t3656-renderer-mobile-6.log`. No app or assertion changes.

Mobile1–7 are now all green:455 assertions include91 repeated scaffolding checks, so
364staged-section checks are covered. Mobile8 is next. The standard ticket-directory
layout has also passed its targeted roof-pin check; complete source3/8 is rerunning.
Local source1/8 and2/8 remain green;4–8 still pending. PR2197 remains draft atcbf3408e0.

## Current validation issues — 18 November 2026, 19:16 UTC

Source part3/8 found one local-layout failure: roof_id_pins.py could not see tickets
through the directory symlink. The actual tickets clone now lives in the standard
`/workspace/chicago/chicago/4d/tickets` directory; `/workspace/chicago-tickets` is an
alias back to it, so existing commands still work. No tracked application files changed.
The targeted check now passes all14 pins over26799 source files. Full part3/8 rerun is
pending; its original failed log remains `/tmp/t3656-green-part3of8.log`.

Mobile renderer stage6 timed out at240s while its crash-recovery subtest launched a second
Balanced town alongside the original page and three source-check workers. This is a real
incomplete stage, not a pass: the secondary context never reached its page-error assertion.
The original stage6 log is preserved. Source workers are now stopped. Finish current
mobile7, then rerun official6 with the same assertions and caps but no source gate running;
if it still fails, inspect the secondary loader diagnostics before changing anything.
Completed mobile1–5 remain green. No renderer/application source changed.

PR2197 stays draft and unmerged until the full source and renderer aggregate is green.

## Validation milestone — 18 November 2026, 19:08 UTC

PR2197 remains draft at pushed head `cbf3408e032eb6341df9d52bfbb289810035f412`.
Local source partitions1/8 and2/8 are green (175 and174 steps, no red steps);
part3/8 is next. Complete PR source CI run44375593498 remains required, along with
its moving-frames workflow44375593479. Do not count queued jobs as passes.

Published mobile renderer stages1–5 are complete and green: respectively95,115,107,
45 and30 checks; runtimes4:55,6:47,4:17,6:50,8:11. Every stage reports zero page errors.
Stage5 completed the full/balanced/light scene-detail sweep and passed its budgets.
Total392 assertions include65 repeated scaffolding checks, so327 staged-section checks
are covered. Current stage is6. Canonical logs are
`/tmp/t3656-renderer-mobile-{1,2,3,4,5}.log`; the source ledger holds1–3 so far.
Desktop full workflow44372747109 passed setup/publication and is now running its renderer
body; full mobile workflow44373274865 was queued. All15 stages at both sizes are needed
before merge. Application source has not changed since6c83; later checkpoints record
verification only, and do not invalidate the frozen published build's source bytes.

## PR checkpoint — 18 November 2026, 18:59 UTC

Draft DEV PR: https://github.com/kevinrhaas/chicago/pull/2197 . Latest pushed head:
`cbf3408e032eb6341df9d52bfbb289810035f412`; this follow-up to implementation commit
`6c83e8cf9` updates only STATUS and the recorded mobile smoke results. No application
source changed between these checkpoints. Preflight1/8 passed 175 checks, changelog-entry
and ticket-ID checks passed, and the smoke ledger self-test passed33 checks.

Published mobile stages1–4 are now complete and green (95,115,107,45 checks respectively,
zero failures/page errors); stage5 is running. The code ledger currently records1–3;
subsequent milestones will be committed/pushed. The PR triggers the complete eight-part
source CI gate on its exact head. Full desktop/mobile renderer workflows above remain
necessary; desktop has acquired a runner and begun checkout, mobile was still queued.
Keep PR draft until the complete source+renderer aggregate is green, then update its
validation description, mark ready, and merge to DEV. Ticket review is not completion;
the tickets repo settles done only after actual merge. Continue next #7/#10 work afterward.

## Validation recovery — 18 November 2026, 18:47 UTC

A workspace transition preserved the clean source checkout and logs but interrupted the
active local processes. The pushed code checkpoint is still `6c83e8cf9558c0d6f9ffb422f299764837fc4ed2`.
The final four-way part 1 rerun stopped without a final verdict and does not count as a
pass. Earlier pre-review part 1 passed 347 checks. Recovery subsequently found the original
mobile renderer stage 2 had completed before process cleanup: its canonical log ends
SMOKE PASS, 115 checks, zero failures/page errors. Final mobile stage 1 passed 95 checks.
Completed mobile coverage is therefore stages 1–2; continue at stage 3.

Local source validation now uses eight shorter partitions, as `tools/check.sh` instructs
when a part exceeds 540 seconds; the four-way run took roughly 13 minutes. First run:
`CHECK_PART=1/8 tools/preflight.sh`, with Node22/bc PATH and CHECK_JOBS=4. On passing
preflight, open a draft PR into DEV to retain the required complete eight-part CI gate.
Every partition must pass in aggregate; no four-part completion is claimed.

Both full published renderer viewports are retained as existing GitHub workflow runs on
this exact checkpoint, with all 15 stages selected:
- Desktop: https://github.com/kevinrhaas/chicago/actions/runs/44372747109
- Mobile: https://github.com/kevinrhaas/chicago/actions/runs/44373274865

Both were queued at the latest reading. Local mobile stages continue from stage 3 while
waiting; preserve completed stages 1–2. The source branch remains unmerged. Do not promote
production. After a green DEV merge, proceed with bounded #7 photo hunt and #10 reading
accessibility work; a full ticket audit found no existing live ticket owns those scopes.

## Recovery checkpoint — 18 November 2026, 18:33 UTC

Code is committed and pushed to GitHub: `6c83e8cf9` on
`steward/t3656-browser-classroom` in `kevinrhaas/chicago`, based on DEV `169af6421`.
The owner explicitly requested checkpoints so another session can resume; this commit
is a backup checkpoint, not a completed release. There is no PR or merge yet.

All 36 source/document/test files are included. Four classroom features are implemented:
bounded photo/share, local notebook, cited ungraded reflections, and printable group
lessons. Final review repaired lesson reading overlays, selected-person retention through
Home, and notebook saves from the legacy 1835 People screen. Focused tests pass, including
actual town photo/share at both 390x780 and 1280x800 on source and published trees; scene
pixels are nonblank, saved jaunts survive shared arrival without auto-resume, and the
renderer retains `preserveDrawingBuffer: false`. Native capture tests pause continuous
software-GPU rendering between interactions and step one real normal frame per shutter;
this is not a low-end hardware performance certification.

First repository partition passed all 347 steps. Final-tree partitions 1–4 are now being
rerun at the committed checkpoint; part 4 invokes preflight. Full published renderer smoke
stages 1–15 at both sizes is also running. Do not merge before the required checks pass.
Desktop full published smoke (all 15 stages) is also running on GitHub at the exact
checkpoint: https://github.com/kevinrhaas/chicago/actions/runs/44372747109 .
Mobile stage 1 passed 95 checks with zero failures and page errors.
Local logs: `/tmp/t3656-green-part{1,2,3,4}.log`; smoke `/tmp/t3656-renderer-*`.
Frozen published build: `/workspace/chicago-classroom-published`.
Focused photo reports: `/tmp/photo-town-{source,published}/report.json`;
person-link callback report: `/tmp/person-moment-fixture/report.json`.

Next actions: finish gates and renderer checks, fix any real failures, push further
checkpoints, create PR into DEV, mark this ticket review with the PR number, and merge
only when green. Then take bounded server-free photo-hunt (#7) and accessibility (#10)
work in separate worktrees. No production promotion, server spending, or shared service
activation. #1 remains lower priority with one active world by default.

## Implementation progress — 18 November 2026

Four parallel worktrees produced the first photo/share, local notebook, cited-reflection
and group-lesson implementation, integrated locally on `steward/t3656-browser-classroom`
in `/workspace/chicago`, based on dev `bec8fd8d3`. No production deployment or shared-service
activation. Full list disposition: `chicago/4d/docs/CLASSROOM-FEATURES.md`.

All four focused logic suites pass on Node 22. Checks cover 240 available jaunt tellings,
five bands, 192 school tellings and all 10 available year/group lesson combinations.
Mobile/desktop browser fixtures verify notebook and lesson export/print, reflection UI,
keyboard focus, safe source links and no overflow. Actual town checks verify notebook
save/export and completed-jaunt reflections on phone, plus position/season restoration
from a shared URL; fresh published desktop notebook and lesson/PDF flows also pass.

This is not marked done: changes remain uncommitted while release verification is pending.
The full four-part repository gate and full published renderer smoke have not passed.
Node 22 was installed locally after the workspace's Node 24 hit the existing native-human
geometry runtime assertion. The fresh part 1 completed 347 steps with one daybook-DOM
regression, now repaired and verified by the affected license test and reflection tests;
the whole part has not been rerun and parts 2–4 remain. Published desktop notebook,
lesson/PDF and real-jaunt checks pass with zero page errors/404s/overflow. Production photo
modules pass a real WebGL/PNG fixture at both widths, but whole-town photo scheduling timed
out under the software GPU and remains unverified. STATUS.md records final evidence. No broader server-backed features are claimed.

**Released 2026-11-18** (claim of run 11/18/2026, 11:31:32 AM CT): First implementation retained locally on steward/t3656-browser-classroom in /workspace/chicago; focused and browser checks recorded in STATUS.md. Whole-town photo scheduling and the complete four-part release gate remain; no commit or deployment yet.
