---
id: T-3656
title: Browser-only classroom tools: photos, notebook, understanding checks and lesson guides
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: null
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
