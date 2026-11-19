---
id: T-3694
title: Jaunts open without a second load: the list's data and code fetched quietly after the town is ready
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: null
pr: 2225
claimed_by: run 11/19/2026, 11:00:49 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T17:00:51.360Z
decision: null
decision_answer: null
---

Jaunts open without a second load: the list's data and code fetched quietly after the town is ready.

**Acceptance:** after the town is ready, Take a Jaunt shows the list without a second load screen, on desktop and phone (390×780), in every year; opening the list adds no large memory (no route grid built just to show it); nothing extra loads while the visitor walks.

## Done (PR #2225)

Opening the list built the whole 1 m route grid (11.9 M cells in 1835, 250-450 MB) to time the cards, then planned every leg of up to 30 cards before showing any. Cards are now timed building to building, and the list's code and files are read ahead at Home in idle time (0.1-0.2 MB, never while walking).

| | wait, tap to list | memory taken by opening the list |
|---|---|---|
| 1835 desktop | 18.6 s → 0.04 s | 251 MB → 0 |
| 1835 phone | 21.3 s → 0.05 s | 271 MB → 8 MB |
| 1812 desktop | 7.3 s → 0.04 s | 425 MB → 1 MB |
| 1812 phone | 7.2 s → 1.8 s | 445 MB → 33 MB |

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/812088f9fe2c6f0bf0f2502ff612fbd4e0a6727f/evidence/jaunts-open-T-3694/before-after-timings.png?raw=true" width="900">

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/812088f9fe2c6f0bf0f2502ff612fbd4e0a6727f/evidence/jaunts-open-T-3694/after-1835-desktop-list.png?raw=true" width="640"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/812088f9fe2c6f0bf0f2502ff612fbd4e0a6727f/evidence/jaunts-open-T-3694/after-1835-phone-list.png?raw=true" width="260">

Trade-off: Across Wolf Point's card reads 3 min, not 11 (a straight line across the river); the outing times its routed walk once started.
