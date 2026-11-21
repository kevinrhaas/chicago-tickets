---
id: T-3711
title: Filter jaunts by narration and music
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-20
closed: null
pr: 2271
claimed_by: run 11/20/2026, 5:33:43 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-20T23:33:44.373Z
decision: null
decision_answer: null
---

Filter jaunts by narration and music.

The owner, 2026-11-20: "for all the jaunts with music or narration allow that to be added as a filter so we can filter and include only those jaunts with narration".

**Acceptance:**
- The jaunt catalog says which jaunts are narrated (listed in data/narration/voices.json `jaunts`) and which carry music (a jaunt list the music work fills in; none yet).
- The Jaunts menu has a Listen row with a Narrated pill (and a With music pill once any jaunt has music); a picked pill lists only those jaunts, alongside the group, age and search filters; Clear filters lets it go.
- A narrated card says so on its tags row.
- A year with no narrated jaunt shows no Listen row.
- Desktop and phone (390x780) pictures in the PR.
