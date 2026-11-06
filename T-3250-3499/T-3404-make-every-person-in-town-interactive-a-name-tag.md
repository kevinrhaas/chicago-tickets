---
id: T-3404
title: Make every person in town interactive: a name tag when you look at them, Find for anyone standing, Follow, and a turned look as you come near
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: 1753
claimed_by: run 11/5/2026, 11:22:26 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-06T05:22:27.321Z
decision: null
decision_answer: null
---

Make every person in town interactive: a name tag when you look at them, Find for anyone standing, Follow, and a turned look as you come near.

Kevin, 2026-11-06: "make progress on completing humans and making them fully available to interact with". Today two people are placed in town, both drivers: Hans Johnson on the 1904 brougham and Otis Bardwell on the 1835 wagon. A click or tap opens their card and Find this person goes to them, but looking at a person names nothing, a standing figure (humans.js, the on-foot thread T-3402) has no Find, nobody can be followed, and nothing turns to a visitor who walks up.

**Acceptance:**
- Every placed person, drivers and standing/walking figures alike, is clickable/tappable and opens their own card (1904 person card; 1835 drawer card), already true for drivers and kept.
- Looking at a person: the target tag names them ("Hans Johnson · 30 ft") after the usual dwell, and the tag and the Inspect key open their card. Buildings behind them keep their own tag otherwise; the shared building probe and Inspect's target are unchanged.
- Find this person / Go to reaches anyone placed in town: a driver (kept), or a standing/walking figure, beside whom the visitor is set down on a clear stand.
- Follow: from the person's card and the Interact key, the visitor walks alongside a moving person (a driver's carriage) a few metres off, on clear ground, looking at them, until they move, press Stop following, or the person is gone. Works on a phone (390x780) and desktop.
- A standing/walking figure turns to look at a visitor who comes within its interaction radius (human-life.js `attend`, T-3402), and drivers keep driver-life's own look.
- No new assets or textures; gate test tools/test_person_interaction.mjs in check.sh; smoke stays green on the touched parts.
