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

## Current recovery checkpoint — keyboard ownership, 19 November 2026

The rail repair is in draft PR #2199 at6ee1a689. Further review reproduced a real capture/
backend conflict: ArrowDown on a Navigator button requested pointer lock and moved the
walker; Space inspected instead of activating the native button. The repair is backed up
at597a7c392f7300eeafd069b2afe245c44c1bb7cf on backup/t3658-keyboard-ownership and included
in normalized candidate ddc786069 on qa/t3657-t3658-current-dev-keyboard. It keeps reader/
control keys with their focused UI, clears held motion when focus enters it, preserves
world-focused controls and intended E-to-close card behavior, and excludes native dialogs,
text fields and picture dialogs from that E exception. Existing isTyping semantics stay.

Actual capture/backend regressions, existing Navigator/Settings tests and independent
review pass. Native browser fixture passed20/20 checks at390x780 and1280x800, zero page/
HTTP/external-request errors: real Space activation, rail Arrow focus, role-less dialogs,
held-W then Tab into UI, world keys, prevented keys, popup/Inspect E and text entry. No world
or WebGL was loaded; pointer-lock requests were counted without granting mouse capture.
Official isolation measurement recorded zero in-tree writes for the new gate; tool SHA256
d8f2163a1b9f38ebcaf83f68ff1660cf6485bd731b89f7e2e58707c9b853b21d. Audit/self-test passed;
the full audit console result was reported but its empty log is not used as evidence.
Native report: /tmp/t3658-keyboard-ownership-browser/report.json. Evidence checkpoint
dae64772938ce55ec15cb4bb9dbc0f1c9c6d4ae2 retains source hashes, screenshots and receipts.

T3657's current recovery note has the normalized integration method and pending full
renderer run IDs. Merge parent first, preserve its folded changelog, then finish the final
follow-up gates and merge DEV when green. This remains a bounded accessibility repair,
not physical-device testing or whole-app WCAG certification. No PR has merged yet.

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
