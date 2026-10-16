---
id: T-2671
title: Grade colors gold, silver and bronze: Attested gold, Inferred silver and Reconstructed a clearly browner bronze, everywhere a grade shows: card and dossier dots, people chips, the HUD and the Confidence view's scene tint, in both themes
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-S04
parent: null
opened: 2026-10-16
closed: null
pr: 906
claimed_by: run 10/16/2026, 2:37:22 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T19:37:22.315Z
decision: null
decision_answer: null
---

Grade colors gold, silver and bronze: Attested gold, Inferred silver and Reconstructed a clearly browner bronze, everywhere a grade shows: card and dossier dots, people chips, the HUD and the Confidence view's scene tint, in both themes.

**Navigator Mk II — NAV-S04.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## What to build

Owner, 2026-10-16: *"for the default colors of attested inferred and reconstructed, they look too
similar attested and reconstructed maybe you could do it as gold silver bronze and bronze is obviously
browner than gold. Gold being attested of course."*

Today: `--doc` / `--inf` / `--con` in the stylesheets with light-theme overrides in `css/card.css`
(`.fact-*`), `css/people.css` (`.grade-*`), `css/walk.css` (`.conf-*`), and the scene tint in
`js/confidence.js` (its `0x…` grade constants and the shader factors noted beside them).

- Attested = **gold**, Inferred = **silver**, Reconstructed = **bronze**. Bronze must read as brown,
  not as a darker gold: separate it from gold in hue and in lightness (a starting point: gold about
  #D4AF37, silver about #B8C0C8, bronze about #8C5A2B; tune per theme).
- One set of tokens drives every place a grade shows (dots, chips, legend, scene tint); light and dark
  themes each get values that hold 3:1 against their panel for dots and 4.5:1 where grade text is read.
- The three must stay distinguishable for the common color-vision deficiencies (simulate deuteranopia,
  protanopia, tritanopia; lightness steps carry the difference). NAV-602 (T-2648)'s color-blind-safe swatch set
  is an extra option, not a replacement.
- The Navigator's Confidence view (NAV-603 (T-2646), NAV-602 (T-2648)) uses these as its defaults.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [x] Every grade dot, chip, legend and the BY GRADE scene tint shows gold / silver / bronze, in light and dark themes, from one set of tokens.
- [x] A side-by-side capture at the Glessner front with BY GRADE on shows bronze clearly browner than gold; the color-vision simulations keep all three distinct.
- [x] Contrast: dots 3:1 and grade text 4.5:1 against their panels in both themes.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [x] Works in all four machine skins and with reduced motion.
- [x] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [x] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [x] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [x] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
