---
id: T-2642
title: Navigator style library: Greek Revival, Italianate, Second Empire, Queen Anne and Chicago School modules, each with four sourced 'how to spot it' cues and a credited reference plate
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-506b
parent: null
opened: 2026-10-16
closed: 2026-10-19
pr: 1065
claimed_by: run 10/18/2026, 7:28:42 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-19T06:21:49Z
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

**2026-10-19.** Part 1 is PR #1065 (branch claude/t2642-style-library-v2): Second Empire and Italianate, four sourced cues and a public-domain plate each, on 1900, 2115 and 1834 Prairie. Left out for want of a source: Greek Revival (only the 1853 courthouse and the 1836 Clarke House, which is excluded from 1835, are named in it); Queen Anne (Chicagology calls 1919 Prairie Queen Anne, which conflicts with the district marker); Chicago School (no such building in either scene). A research pass on those three is under way, and the owner decides the rest.

## Owner's ruling (2026-10-19): three styles, acceptance amended
"Ship 3, drop the rest." T-2642 ships Second Empire and Italianate (PR #1065), beside the
Richardsonian Romanesque module already on dev (T-2641). The first acceptance line now reads:
**three modules (Richardsonian Romanesque, Second Empire, Italianate) committed and shown on
buildings of those styles in 1904; every plate credited and licensed.** Greek Revival, Queen
Anne and Chicago School are dropped for these scenes, for want of a source:
- Greek Revival: the only buildings a source names in it are the Clarke House (1836; outside
  1835 by data/exclusions.json, and at 4526 S. Wabash in 1904, outside the Prairie scene) and
  the 1853 courthouse. The Sauganash Hotel's "Greek Revival trim" is an uncited Wikipedia
  sentence, which docs/research/03-structures-north.md already marks as a modern gloss, and the
  repo's own rule is that Chicago's earliest Greek Revival house is Clarke, 1836. DESIGN.md's
  "Big in 1835" is contradicted by the records.
- Queen Anne: the one claim (1919 Prairie) is an uncredited Chicagology caption. The district
  marker names no style, and the 1973 Commission report quotes Meeker saying the house "has been
  rebuilt so often it's impossible to say any longer what it was originally trying to be."
- Chicago School: by the 1972 National Register district nomination's own definition, a
  steel-frame commercial style. Neither scene holds such a building; the nomination calls
  Glessner House a precursor.
The ruling also adds two source records: the 1973 Commission on Chicago Historical and
Architectural Landmarks report "Prairie Avenue: Chicago's First Gold Coast" and the 1972 NRHP
Prairie Avenue District nomination.
