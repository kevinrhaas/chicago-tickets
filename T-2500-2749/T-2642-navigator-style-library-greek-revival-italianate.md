---
id: T-2642
title: Navigator style library: Greek Revival, Italianate, Second Empire, Queen Anne and Chicago School modules, each with four sourced 'how to spot it' cues and a credited reference plate
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-506b
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/18/2026, 7:28:42 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-19T00:28:42.581Z
decision: null
decision_answer: null
---

Navigator style library: Greek Revival, Italianate, Second Empire, Queen Anne and Chicago School modules, each with four sourced 'how to spot it' cues and a credited reference plate.

**Navigator Mk II — NAV-506b.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2641 (NAV-506) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§12 "Style library": shared modules, each with 4 "how to spot it" cues and a reference plate.
Plates come from images with a source record and rights (hard rule 6; `assets/LICENSES.md` for any
committed file); cues are plain, ≤ 8 words each, graded where they make a claim. Buildings link to a
module by their `style`.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Five modules committed and shown on buildings of those styles in 1835 and 1904; every plate credited and licensed.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
