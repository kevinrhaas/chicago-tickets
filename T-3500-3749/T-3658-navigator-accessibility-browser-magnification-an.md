---
id: T-3658
title: Navigator accessibility: browser magnification and keyboard-safe picture dialogs
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: null
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
