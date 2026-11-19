---
id: T-3671
title: Accessibility pass toward WCAG 2.1 AA: menus, cards, text size, colour-safe confidence, narration transcripts
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: null
pr: null
claimed_by: run 11/19/2026, 8:59:58 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T15:00:03.841Z
decision: null
decision_answer: null
---

Accessibility pass toward WCAG 2.1 AA: menus, cards, text size, colour-safe confidence, narration transcripts.

**Acceptance:** (stated 2026-11-19 before work; the owner asked for "the full accessibility pass")
- Keyboard: every rail app, Navigator screen, Settings tab, jaunt menu/panel and card is reachable and operable with Tab, Shift-Tab, Enter, Space, arrows in tab strips, and Esc; no trap; opening moves focus in, closing returns it (2.1.1, 2.1.2, 2.4.3).
- Focus is visible everywhere, at least 3:1, in all four appearances and both themes (2.4.7, 1.4.11).
- Screen readers: tabs, dialogs, toggles and icon-only keys have roles, names and states; headings are headings; arrivals and stop changes are announced; pictures have text alternatives; the page names its year (4.1.2, 1.3.1, 4.1.3, 1.1.1, 2.4.2).
- Text: the Text size setting reaches 200 % across all interface text, and 200 % browser zoom, 320 px reflow and user text spacing lose nothing (1.4.4, 1.4.10, 1.4.12). Text contrast at least 4.5:1 (1.4.3).
- Grades (attested / inferred / reconstructed) never rely on colour alone, and their colours stay distinct under protan, deutan and tritan simulation (1.4.1).
- Narration: every narrated piece shows its words while it plays, and narration can be paused or stopped (1.2.1, 1.4.2).
- Motion: one Motion setting (System / Reduce / Full) that removes head-bob, fly-in travel and UI animation; no UI moves for more than 5 s without a way to stop it; nothing flashes more than three times a second (2.2.2, 2.3.1).
- docs/ACCESSIBILITY.md states what conforms and names what does not (the 3-D canvas itself has text alternatives through cards, it is not itself screen-readable). Browser tests assert each item above.
