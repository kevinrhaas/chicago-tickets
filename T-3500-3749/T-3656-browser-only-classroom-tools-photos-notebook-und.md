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
