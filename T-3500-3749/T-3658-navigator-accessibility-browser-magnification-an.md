---
id: T-3658
title: Navigator accessibility: browser magnification and keyboard-safe picture dialogs
state: review
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: 2197
claimed_by: run 11/18/2026, 1:41:34 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-18T19:41:36.836Z
decision: null
decision_answer: null
group: T-3656,T-3657,T-3658
---

Navigator accessibility: browser magnification and keyboard-safe picture dialogs.

**Acceptance:** Demonstrate Navigator reading and image viewing with browser magnification and keyboard alone at phone and desktop sizes: allow native mobile zoom, retain usable reading scroll and existing two-thumb world controls, distinguish visual viewport magnification from keyboard/orientation resizing, and make picture dialogs trap focus, isolate the background, close by Escape and restore focus. Verify zoom does not shrink the GPU canvas or lose reading controls. This is a bounded accessibility repair, not a claim of whole-app WCAG conformance.

## Owner scope and implementation plan

The owner asked to continue top-priority non-server items after the first classroom delivery and to checkpoint work to GitHub. This is a concrete first slice of list item 10. This work is delivered together with the classroom tools and photo hunt in combined PR #2197. Inspect viewport meta, Navigator touch-action ancestors, main.resize(), controls/touch.js visualViewport handling, and pictures.js modal lifecycle. Keep canvas/game gesture behavior explicit; test both reading and movement.

### Bounded keyboard continuation

Review of the remaining accessibility path reproduced a rail defect: opening Move or Jump,
which have no visible rail icon, leaves zero visible rail buttons in the Tab order. Extend
this ticket with exactly one visible rail Tab stop while preserving truthful selection and
manual arrow/Enter activation. Cover context disappearance, unregistering, async mounting,
and dock/reopen. Actual keyboard browser fixtures at both widths should exercise Tab and
Shift+Tab, not directly focus a rail button and thereby bypass the defect. This is part of
the same accessibility PR, not a claim of full WCAG conformance or a new feature service.

## Current recovery checkpoint — combined delivery, 19 November 2026

All three tickets now share **PR #2197**, branch
`steward/t3656-browser-classroom`, pushed head `edc7099032cd6d55d7a7e7f0d66d313b15960f10`,
tree `b9c9b74ecb9f98869ff6a46a4d56a1993db25dd8`. Its parents are normalized QA
`ddc78606998ea8aee589941c6ab6cae76a80440a` and folded DEV
`d47d9550bf914d33860a56b99fd11ad2f6f6018b`. This is one combined delivery
with one pending `T-3656.json` changelog entry; the shipped DEV changelog
is preserved and the duplicate `T-3657.json` entry is removed. PR #2199
is superseded and awaits coordinator closure; no PR has merged.

The existing magnification/dialog work, rail reachability and keyboard
ownership repair are included together. There is no remaining parent-first
integration step. The native ownership fixture's20 checks remain scoped to
the actual DOM/backend code at3131/597 and matching normalized runtime:
no world/WebGL, no granted pointer capture, and no physical-device or whole-app
WCAG certification. Those earlier reports keep their original provenance.

Frozen ddc source part7 exposed a stale inline-keyboard regex in
`tools/check_xr_mode.mjs`, after parts1–6 passed. Part8/preflight were not run.
The test-only repair `fd27937a007937189b573263eead231f2cca8c96` now checks the
actual extracted capture behavior and is integrated in edc. All20 focused XR
checks and keyboard regressions passed; official measurement reports no
in-tree writes. The quiet audit's zero-byte output is supported by an explicit
exit0 receipt, not inferred from silence. The combined nonquiet isolation
audit also passed after refreshing the incoming unique-ID validator measurement.

Published ddc desktop1–4 PASS320 and6–12 PASS111 remain historical c676-input
groups. Its desktop13–15 group completed308/2 with Space-inspect and
transfer-blob error failures; do not count it green. Final combined
source/preflight/moving/upload and fresh official13–15
at both widths are required for the changed d47 world/global inputs and feed.
The active part7 repair rerun has no claimed verdict here. No complete release
pass or merge is claimed.

Focused repair evidence: `/tmp/t3658-xr-capture-repair/`; combined provenance:
`/tmp/t3656-combined-d47-provenance.json`. T-3656 carries the combined delivery
status. Keep this ticket in review with #2197; earlier two-PR instructions in
previous recovery notes are superseded history.

## Previous recovery checkpoint — 18 November 2026

Combined work is pushed in dependent draft PR #2199 at
4a2ee67dcbc3067fd8e18fb432098822361f2476. Native published integration passed both widths
on feature commit 5674d33d, with real mobile pinch/pan and stable drawing-buffer dimensions,
actual photograph dialog keyboard/focus behavior, hunt travel and notebook/photo capture.
Focused fixtures also exercise magnified move/look regions, orientation/keyboard viewport
changes, Escape/Tab/ShiftTab, inert background, focus return and dialog reopen races.
Zero page/HTTP errors or overflow; expected request cancellations are recorded separately.
These are browser-emulated viewports, not physical-device or whole-app WCAG certification.

Preflight on current head passed source part 1/16 (89 checks), changelog and ticket-ID
metadata. Complete source/renderer gates and dependency cleanup remain before merge.
T-3657's recovery section records CI, evidence, branch and the exact rebase boundary.
Merge parent #2197 first, then rebase and validate #2199; the user authorized green DEV
merges and periodic GitHub checkpoints. No production promotion or server activation.
