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
pr: 2199
claimed_by: run 11/18/2026, 1:41:34 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-18T19:41:36.836Z
decision: null
decision_answer: null
group: T-3657,T-3658
---

Navigator accessibility: browser magnification and keyboard-safe picture dialogs.

**Acceptance:** Demonstrate Navigator reading and image viewing with browser magnification and keyboard alone at phone and desktop sizes: allow native mobile zoom, retain usable reading scroll and existing two-thumb world controls, distinguish visual viewport magnification from keyboard/orientation resizing, and make picture dialogs trap focus, isolate the background, close by Escape and restore focus. Verify zoom does not shrink the GPU canvas or lose reading controls. This is a bounded accessibility repair, not a claim of whole-app WCAG conformance.

## Owner scope and implementation plan

The owner asked to continue top-priority non-server items after the first classroom delivery and to checkpoint work to GitHub. This is a concrete first slice of list item 10. Work is isolated from PR #2197 while its release gates finish, and merges after that PR together with the photo hunt if the group remains coherent. Inspect viewport meta, Navigator touch-action ancestors, main.resize(), controls/touch.js visualViewport handling, and pictures.js modal lifecycle. Keep canvas/game gesture behavior explicit; test both reading and movement.

### Bounded keyboard continuation

Review of the remaining accessibility path reproduced a rail defect: opening Move or Jump,
which have no visible rail icon, leaves zero visible rail buttons in the Tab order. Extend
this ticket with exactly one visible rail Tab stop while preserving truthful selection and
manual arrow/Enter activation. Cover context disappearance, unregistering, async mounting,
and dock/reopen. Actual keyboard browser fixtures at both widths should exercise Tab and
Shift+Tab, not directly focus a rail button and thereby bypass the defect. This is part of
the same accessibility PR, not a claim of full WCAG conformance or a new feature service.

## Current recovery checkpoint — keyboard ownership, 19 November 2026, 01:38 UTC

PR #2199 remains draft and in review at `6ee1a689`, dependent on #2197. The
keyboard ownership repair is backed up at
`597a7c392f7300eeafd069b2afe245c44c1bb7cf` on
`backup/t3658-keyboard-ownership` and included in normalized QA `ddc786069`.
It keeps reader/control keys with focused UI, clears held motion on entry,
preserves world controls and intended E-to-close behavior, and protects
native dialogs, text fields and picture dialogs. Existing isTyping semantics
remain intact.

The actual native browser fixture passed **20/20 checks** at 390×780 and
1280×800 with no page/HTTP/external-request errors. It exercises real capture,
backend, native activation, focus, dialogs and movement ownership. No world
or WebGL loaded; pointer-lock requests were counted without granting capture.
All seven tested runtime hashes match the backed-up and normalized code.
The new isolation row measured zero in-tree writes; its self-test passed.
The full audit console PASS was reported separately, and its empty log is
not treated as evidence. [Evidence46910da](https://github.com/kevinrhaas/chicago-evidence/tree/46910daedcd6f68a9b07f50d58328c21c16207a4/evidence/t3657-t3658-hunt-accessibility-2026-11-18/keyboard-ownership)
preserves the reports, screenshots, exact source hashes and limitations.

Published ddc desktop **1–4 passed 320/0** in 38m29s: 307 staged checks and
13 always-on checks once. Desktop 6–12, desktop 13–15 and mobile 1–15 groups
remain active. Local isolated source part 1/8 passed 175 steps; its final
CHECK PASS is complete but the original shell-exit receipt was lost, so no
exit code is claimed. Remaining source parts, preflight and final integrated
gates are required. T-3657 names the runs and source receipt.

Parent renderer coverage is complete under its retained/fresh proof and
moving/upload is green. As of this checkpoint, parent source attempt 2 has
only part 4 PASS174; parts 2/6/8 have runners, 1/3/5/7 are queued, and the
aggregate is pending. After
the parent squash/fold, follow T-3657's normalized b1-to-ddc method, preserve
the shipped changelog and T-3656 entry removal, and compare actual new DEV
inputs before evidence reuse. Neither PR has merged. This remains a bounded
accessibility repair, not physical-device or whole-app WCAG certification.

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
