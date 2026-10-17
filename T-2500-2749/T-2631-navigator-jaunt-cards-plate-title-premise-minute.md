---
id: T-2631
title: Navigator Jaunt cards: plate, title, premise, minutes, stops and keepsake state for each route, with a Jaunt in progress pinned on top with Continue that survives a reload
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-402
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: 962
claimed_by: run 10/17/2026, 3:55:27 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T11:11:56Z
claimed_run: null
claimed_at: 2026-10-17T08:55:27.909Z
decision: null
decision_answer: null
---

Navigator Jaunt cards: plate, title, premise, minutes, stops and keepsake state for each route, with a Jaunt in progress pinned on top with Continue that survives a reload.

**Navigator Mk II — NAV-402.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2630 (NAV-401) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07 "Jaunts". A card per route (`data/jaunts/`, 28 routes; `js/jaunt-cards.js`) with a photo plate,
title, one-line premise, minutes and stops, and a keepsake badge once earned (keepsakes live in this
app — doc suggestion). A Jaunt in progress sits on top: "CONTINUE · STOP 2 OF 2 … Next: …".
Plates come from credited images already in the project (Prairie library / `data/sources/`), never
from the design doc's unsourced mockup plates.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-13: start a Jaunt, reload mid-way; Home and the Jaunts app both show Continue at the right stop.
- [ ] Every route has a card with minutes and stops; earned keepsakes show on their cards.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
