---
id: T-3575
title: Add a VR headset mode: Enter VR, head-tracked look, thumbstick walk and snap turn (WebXR)
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: 2026-11-12
pr: 1976
claimed_by: run 11/12/2026, 7:06:14 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-13T03:39:50Z
claimed_run: null
claimed_at: 2026-11-13T01:06:15.353Z
decision: null
decision_answer: null
---

Add a VR headset mode: Enter VR, head-tracked look, thumbstick walk and snap turn (WebXR).

The owner, 2026-11-13 (project thread "Add VR headset mode"): *"What would be the least expensive way to try to add VR style headset navigation to this and try a vr headset"*, then *"Sure"* to adding a WebXR "Enter VR" mode on dev, to try with a WebXR emulator extension and later a Meta Quest 3S browser.

**Acceptance:**
- A browser that reports `immersive-vr` support shows an Enter VR key in the town's HUD; every other browser (desktop and phone without a headset) shows nothing new and draws exactly as before.
- In the headset: head-tracked stereo view at the walker's eye; left stick walks (and flies) where you look, with collision and the step rule unchanged; right stick snaps the turn and, flying, rises and falls; A/X toggles fly; Exit VR (or the headset's own exit) returns to the page's controls.
- A standalone headset (Quest, Pico browsers) boots as a phone-class device: the phone's tier and memory diet, people, horses and carriages kept; the VR frame is drawn at a reduced framebuffer scale instead (`?vr-scale=` overrides).
- Gate green, smoke unchanged at 390x780 and 1280x800.
