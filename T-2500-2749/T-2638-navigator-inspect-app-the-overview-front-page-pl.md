---
id: T-2638
title: Navigator Inspect app, the Overview front page: plate, address, name, status chips, summary, key facts, residents, Look for, Notable facts and the Confidence meter, replacing the floating building card
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-501
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Navigator Inspect app, the Overview front page: plate, address, name, status chips, summary, key facts, residents, Look for, Notable facts and the Confidence meter, replacing the floating building card.

**Navigator Mk II — NAV-501.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2635 (NAV-502) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2636 (NAV-503) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§08 "The building dossier", M7. The Inspect app replaces the floating card (`js/popup.js`, `css/card.css`).
Front page, top to bottom:

1. Plate: the best period photo through the CRT treatment (from the card's Images tab sources, T-2389);
   if none, a render from the "Show me" angle.
2. Address line, name, three status chips: Still standing / Gone (year), Built year, Use.
3. Summary: 3 sentences, ≤ 60 words, authored (NAV-502 (T-2635) record or NAV-503 (T-2636) fallback).
4. Key facts grid: Architect, Owner, Style, Today — each with a grade dot.
5. Who lives here (scene year): up to 3 people with a one-line role, then "+ N more".
6. Look for: 3 features with SHOW ME (the camera move is NAV-505 (T-2640)).
7. Notable facts: 1–3, swipeable.
8. Confidence meter: the Attested / Inferred / Reconstructed split; tap opens Sources.

Inspect prefetches the summary when a target tag appears (§14). Every line carries its grade dot.
People here are text records; drawn figures come from the portable-humans band (8C), which the owner
cleared on 2026-10-16 once they can be rendered.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Inspecting Glessner House shows the front page in the M7 order from its summary record; a building without a record shows the fallback.
- [ ] Every fact line carries a grade dot; the address appears once; works at 390x844 with text size 140 % (QA-18).
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
