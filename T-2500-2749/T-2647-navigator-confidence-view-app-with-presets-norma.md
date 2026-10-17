---
id: T-2647
title: Navigator Confidence view app with presets NORMAL, BY GRADE, ATTESTED ONLY and X-RAY, replacing the HUD chip, caret and checkbox menu, with the C hotkey still toggling BY GRADE
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-601
parent: null
opened: 2026-10-16
closed: null
pr: 974
claimed_by: run 10/17/2026, 2:29:36 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T07:29:36.862Z
decision: null
decision_answer: null
---

Navigator Confidence view app with presets NORMAL, BY GRADE, ATTESTED ONLY and X-RAY, replacing the HUD chip, caret and checkbox menu, with the C hotkey still toggling BY GRADE.

**Navigator Mk II — NAV-601.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2646 (NAV-603) — do not claim this ticket until it has merged; take the next workable ticket instead.

## Found by the loop (2026-10-17): X-RAY is over the draw budget on dev

Desktop smoke part 2's T-2646 check `X-RAY ghosts two grades in a pass drawn last, inside the
draw budget` is RED on dev: 335 calls against a budget of 330. Read with a probe at the smoke's
own frame (`frame('sauganash_hotel', 26)`, 1280x800, animation held, Inferred ghost 50 %,
Reconstructed ghost 25 %), identically on dev 0182d2fc7 (before T-2700) and c8cfb30e6 (after):
plain 222 · BY GRADE 222 · X-RAY 335 = opaque 187 + ghost pass 148 (661 targets, 4728 opaque
instances left out, 13 ghost instances left out), zero page errors. Mobile part 2 passes it.
#921's own desktop 2-3 leg (head 0538fa6a) passed this check, so something that landed on dev
around it moved the count. This preset puts X-RAY one tap away, so the frame should be inside
its budget before it ships: bring the ghost pass's calls down (not the budget up), quoting BY
GRADE and X-RAY calls at desktop and mobile before and after. (Not filed as its own line: the
queue is over its ceiling.)

## What to build

§09, M9. NORMAL: everything shown, no color (default). BY GRADE: today's Confidence chip. ATTESTED
ONLY: only the parts somebody wrote down. X-RAY: Attested solid, Inferred at 50 %, Reconstructed ghosted
at 25 %. The Confidence icon glows while the view is on. Footer readout: GRADE MASK, MESHES, FRAME CLK.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [x] QA-12: ATTESTED ONLY gives the same scene as hiding Inferred and Reconstructed by hand.
- [x] C toggles BY GRADE; each preset is one tap; the #confidence-menu HUD controls are gone.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [x] Works in all four machine skins and with reduced motion.
- [x] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [x] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [x] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [x] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
