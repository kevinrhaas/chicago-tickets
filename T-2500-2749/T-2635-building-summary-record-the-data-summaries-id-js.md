---
id: T-2635
title: Building summary record: the data/summaries/<id>.json schema, its compiler into what the Inspect app reads, and a gate refusing a fact with no grade, an Attested fact with no source, a string over its length or an id or path in a string
state: review
epic: PIPELINE
requested_by: owner
seen: true
effort: M
legacy_id: NAV-502
parent: null
opened: 2026-10-16
closed: null
pr: 904
claimed_by: run 10/16/2026, 2:37:12 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T19:37:12.814Z
decision: null
decision_answer: null
---

Building summary record: the data/summaries/<id>.json schema, its compiler into what the Inspect app reads, and a gate refusing a fact with no grade, an Attested fact with no source, a string over its length or an id or path in a string.

**Navigator Mk II — NAV-502.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## What to build

§12 "Building summary record", "Impact score", "Linted". Invisible on its own; it is the gate that
blocks the Inspect app (NAV-501 (T-2638)) — visible-progress exemption 3, name it in the PR.

Schema (one authored file per notable structure, read by the Inspect app):
`id, scene, name, address, status{text,today,grade,sources}, built{year,grade}, use, summary (≤ 60 words,
≤ 3 sentences), key[{label,value,grade,sources}], residents[{person, role ≤ 12 words}],
lookFor[{text ≤ 8 words, feature, camera{yaw,pitch}, grade}], notable[{text ≤ 25 words,
about: person|structure, grade, sources}], style, story[{date,text,era}]`.

- Grades use the data's existing vocabulary: attested / inferred / reconstructed.
- Every source id resolves in `data/sources/`; every person id resolves in the people records.
- The compiler ranks `notable` for the front page by impact: surprising ×3, about a person ×2, visible
  from the street ×2, Attested ×1.5.
- Gate (in `check.sh`): grade on every fact, sources on every Attested fact, the length limits above,
  no ids, file paths or snake_case inside any string. Reading level is NAV-1004 (T-2669).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Schema and compiler committed; check.sh runs the gate and it fails on each planted fault (missing grade, unsourced Attested fact, over-length summary, a snake_case id in a string, an unresolved source id).
- [ ] A minimal valid record compiles to the published output the Inspect app will read.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
