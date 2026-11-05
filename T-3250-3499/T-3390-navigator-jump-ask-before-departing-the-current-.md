---
id: T-3390
title: Navigator Jump: ask before departing the current year (DEPART / CANCEL prompt)
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: null
claimed_by: run 11/5/2026, 1:48:48 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-05T19:48:49.584Z
decision: null
decision_answer: null
---

The owner, 2026-11-05: *"on the navigator there is an option to jump to the other years, you should ask before jumping and confirm that they are departing the current period etc, you can click on that and leave too easily"*.

The Navigator's Jump app (js/apps/jump-view.js) runs the transfer ring and leaves the year on one plain click of an era card. Recall already asks first (T-2735, js/recall.js); the jump to another year does not.

**Acceptance:**
- A plain click/tap on another year's card in Jump opens a confirm prompt in the machine's voice (eyebrow, `1904 › 1835` code, "Depart 1904 for 1835?", CANCEL / DEPART) and does nothing else; the ring runs only after DEPART.
- CANCEL, Esc, or a tap outside the card leaves the scene and the Navigator exactly as they were, with no transfer stamp written.
- Tab stays on the prompt's two keys; focus starts on CANCEL (the safe answer).
- Dressed by all four appearances (Control Room, Precision Brass, Retro Future, Deep Space) as the recall prompt is; fits 390×780 with 44 px keys.
- A modified click still opens the page as a link does (unchanged).
- test_nav_jump.mjs / test_recall.mjs cover it; the smoke's Jump checks (T-2655 part and part 15's real jump) confirm through the prompt.
