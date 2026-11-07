---
id: T-3459
title: Jaunts take each stop's season from its date, from the first scene; the Battle of Fort Dearborn starts at the fort
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
closed: null
pr: 1835
claimed_by: run 11/7/2026, 10:04:20 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-07T16:04:21.272Z
decision: null
decision_answer: null
---

Jaunts take each stop's season from its date, from the first scene; the Battle of Fort Dearborn starts at the fort.

Kevin, 2026-11-07: "when i started the battle of fort dearboarn jaunt, it starts and its spring but it did not change to spring in the first scene. i had it set to winter before i jaunted and it stayed in winter" — and: "that jaunt starts the story begins with the fort, should we not start and have stop 1 as the fort?"

Cause: the three 1812 story jaunts carry no `ambience`; their stops carry dates (April 1812, August 1812) but a date only moved the sun, never the Season, so a visitor's own Winter stood through the whole outing.

**Acceptance:**
- A dated stop holds the season of its date (Mar-May spring, Jun-Aug summer, Sep-Nov fall, Dec-Feb winter), transiently, from the first scene (during the start flight), and changes when a later stop's date crosses into another season; an undated stop takes the jaunt's `ambience.season`; the visitor's own Season comes back at the end.
- Battle of Fort Dearborn: stop 1 is the fort (spring 1812), its story opening moved onto it, Lee's Place second; the jaunt's season label agrees with its stops (April = spring, August = summer: the battle was 15 August 1812).
- Every jaunt across 1812/1835/1904 checked: welcome/menu light line shows the right season.
- test_jaunts_reducer covers it; gate green; desktop + 390x780 screenshots.
