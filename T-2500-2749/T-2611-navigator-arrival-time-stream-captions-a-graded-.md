---
id: T-2611
title: Navigator arrival: time-stream captions, a graded and sourced deck of 8-12 landmark years per destination shown as the ticker passes each one (at most 3 on fast loads, 8 on slow)
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-102
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 4:41:56 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T21:41:56.346Z
decision: null
decision_answer: null
---

Navigator arrival: time-stream captions, a graded and sourced deck of 8-12 landmark years per destination shown as the ticker passes each one (at most 3 on fast loads, 8 on slow).

**Navigator Mk II — NAV-102.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2610 (NAV-101) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§05 "Time-stream captions". As the ticker passes a landmark year a one-line caption shows for about
2 s ("1966 · Chicagoans save the Glessner House from the wrecking ball.").

- One deck per destination (1904, 1835, 1812), 8–12 captions each, in a data file the arrival page
  reads (e.g. `data/timestream/<scene>.json`), each with `year`, `text` (≤ 70 characters), `grade`
  and `sources`.
- **Captions are graded content like any other fact.** Every source id resolves in `data/sources/`
  (hard rule 1). The doc's 1904 examples — 1966 house saved, 1933 Century of Progress, 1919 Black Sox,
  1909 Burnham Plan — are not all in the 4D sources yet: add a real, checkable source record, or drop
  the caption. Never invent one.
- These are facts about the years *between* now and the destination, shown in transit; they do not put
  anything in the scene (hard rule 3 is about the scene).
- On a fast connection show at most 3, picked by rank (an `importance` field); on a slow one up to 8.
- Owner ruling 2026-10-16: the loop writes the decks; they ship on the gate (sources, length, and the
  reading-level check once NAV-1004 (T-2669) lands).
- Voice (§03): plain, specific, ≤ 20 words, a little funny, never mocking people of the past.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Three decks committed, 8-12 captions each, every caption graded, every source id resolving; a check refuses a caption with no source or over 70 characters.
- [ ] QA-03: under Slow 3G, 8 or fewer captions show; on a fast load 3 or fewer.
- [ ] Captions appear only as the ticker passes their year, each for about 2 s, and are announced politely to screen readers at most once each.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
