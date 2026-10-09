---
id: T-2259
title: compile_scene.py derives the resident rows' lives_at/works_at and the building sidecar's lived/worked-here links from associated_with rows instead of the singular pair (people.js, destinations.js and residents.js read the compiled rows)
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-1274
opened: 2026-10-09
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

compile_scene.py derives the resident rows' lives_at/works_at and the building sidecar's lived/worked-here links from associated_with rows instead of the singular pair (people.js, destinations.js and residents.js read the compiled rows).

Piece 2 of 4 of **T-1274 — Move the renderers and tools off the singular lives_at/works_at once the plural rows carry every claim, and retire the pair**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
