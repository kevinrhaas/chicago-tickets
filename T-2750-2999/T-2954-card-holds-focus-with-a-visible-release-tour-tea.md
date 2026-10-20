---
id: T-2954
title: Card holds focus with a visible release; tour teaches select and release, menus and settings, not Confidence
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-20
closed: null
pr: null
claimed_by: run 10/20/2026, 1:06:09 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-20T18:06:09.796Z
decision: null
decision_answer: null
---

Card holds focus with a visible release; tour teaches select and release, menus and settings, not Confidence.

The owner, 2026-10-20 (project thread "Tour basics and release button"): *"on the tour you need to be clearer about how to click on something and unselect using the esc key ... after you click glessner its hard and/or put something in the interface that acts like the escape key as a release"*; *"you say show confidence on and off on the tour and its kind of hard to turn that on and off and find it so i think maybe that is not something that we want in the tour, show basic getting around and navigation and the menus and whats there, and what they can do as options/settings top level"*; and *"when i click on a building and the card comes up, the focus should be on the card until i either close the card or click on the main display"*.

What happens today (desktop): a click under the crosshair opens the card while the pointer stays locked, so the mouse keeps turning the view, W A S D keeps walking, and the card cannot be clicked. Esc once frees the mouse (the browser's own release), Esc again closes the card. The card's only close is a bare × that scrolls away with the card.

**Acceptance:**
- Opening a building's card frees the pointer, stops walking and looking from the keyboard, and puts keyboard focus on the card (arrows scroll it). Released by Esc (one press), the card's Close, or a click / tap on the scene, which goes back to walking.
- The card carries a visible release that stays in view while the card scrolls: `Close` with an `Esc` keycap on a keyboard device, a 44 px `Close` on touch.
- The Field Check drops the Confidence view and Go deeper steps. Steps: the Navigator, look, walk, select a building (click / tap), release it, open Move, open Settings, ready. Bubbles say click on a mouse device and tap on touch, 14 words or fewer.
- Teacher handout, tests and smoke follow the new steps. Phone 390x780 and desktop, all four appearances.
