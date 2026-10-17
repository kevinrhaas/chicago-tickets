---
id: T-2637
title: Glessner House summary record, the pilot: every line mapped to a graded fact in the Glessner research or a source record, fact-checked, and approved by the owner as the pattern for every other building
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: NAV-1005
parent: null
opened: 2026-10-16
closed: null
pr: 922
claimed_by: run 10/16/2026, 6:30:42 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T23:30:42.599Z
decision: answered
decision_answer: a
---

Glessner House summary record, the pilot: every line mapped to a graded fact in the Glessner research or a source record, fact-checked, and approved by the owner as the pattern for every other building.

**Navigator Mk II — NAV-1005.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2635 (NAV-502) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

NAV-1005 and the editorial note in §08. The mockup's Glessner copy (M7/M8) is illustrative.

- Author `data/summaries/glessner_house.json`. The doc names "glessner-dossier.json"; there is no
  such file — the research is `docs/RESEARCH/glessner_house_1904.md` plus the Glessner source records
  in `data/sources/` (e.g. the HABS record) and the Prairie Avenue 1904 library.
- Check in particular, as the note asks: the daughter Frances Glessner Lee's Nutshell Studies,
  Richardson's death before construction, and the 1966 rescue. All three are well known and none is in
  the 4D sources yet: add a real, checkable source record for each, or drop the line. Never invent a
  source (hard rule 1).
- People: John J. and Frances M. Glessner and the household in 1904, from the people records.
- Look for: three features with camera targets (the mockup's: granite street walls, the great arch on
  18th Street, the narrow north windows) — keep them only if the model shows them.
- Owner ruling 2026-10-16: the loop writes, the owner approves this pilot as the pattern. Open the PR,
  then `ticket.mjs ask` this ticket: (a) approve as the pattern (b) changes needed — and do not merge
  before the answer. Later records ship on the gate without a card each.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The record passes NAV-502 (T-2635)'s gate; every fact has a grade and every Attested fact a resolving source.
- [ ] The three editorial-note facts each have a real source record, or are absent.
- [x] The owner has answered the approval card with (a) before merge.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.

## Finding (PR #922, 2026-10-17): the pilot ships with no residents

The record's `residents` is empty, and the gate is right to refuse anything else: no 1904 people directory exists. The 1835 one (`data/sidecars/1835/people.json`) is compiled by `tools/compile_scene.py` from the 1835 household records in `data/residents/`, and only for a scene whose `layers` list residents. The 1904 scene lists none, and the smoke holds it to having no People section (T-1740). Making the Glessner household enter a 1904 directory honestly is a separate parcel: 1904 household records, a residents layer on the 1904 scene, the compile path, and re-ruling T-1740's "no People section in 1904" check. That should be its own ticket. Until it lands, the Glessners are named in the summary, the key facts (Owner) and the story.

The household facts are ready for that ticket. John J. and Frances M. Glessner lived at 1800 in 1904 (HABS data pages; the museum's family page). The grown children did not: the daughter married in February 1898 and "within a few years" moved one block north to 1700 S. Prairie Avenue, and the son married in June 1898 (`glessner_house_family_page`). No source read names the 1904 household staff.

## Decision needed

Answered 2026-10-17 by the owner in the coordinating session: (a) approve as the pattern.

**Question:** Approve the Glessner House summary record (draft PR #922, https://github.com/kevinrhaas/chicago/pull/922) as the pattern for every other building's front page? It has a 3-sentence summary, 5 key facts, 3 Look-for items, 6 notable facts and a 12-entry story, 28 facts, all Attested and sourced. The Nutshell Studies, Richardson's death before construction and the 1966 rescue each now cite a real source record. It has no residents, because 1904 has no people directory yet (finding on this ticket).

- (a) Approve as the pattern: merge it, and later records ship on the gate without a card each
- (b) Revise: say what to change (tone, length, which facts lead, or the empty residents) and the pilot is reworked before merge

**Recommendation:** (a) Approve as the pattern: merge it, and later records ship on the gate without a card each — every line is graded, sourced and fact-checked against what the sources say; the empty residents are a missing 1904 directory, not a flaw in the pattern

**Asked:** 2026-10-16. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.
