---
id: T-3745
title: Jaunt background music starts straight away: take the clipped main-theme intro off the jaunt beds and openings
state: open
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-24
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

Jaunt background music starts straight away: take the clipped main-theme intro off the jaunt beds and openings.

Kevin, 2026-11-24 (thread "Make the website more cinematic"): much of the jaunt music begins with a clipped part of the main title theme, which sounds incomplete and awkward. Jaunt background music should start immediately, not be preceded by the theme. Filed now; not built in that thread.

**What was measured (2026-11-24, spectral match of each score-v1 file's first 10 s against THEME-FINAL-portage-main-title.mp3):**
- `30-jaunt-opening-1812.mp3` and `30-jaunt-opening-1904.mp3` match the theme from 1.2 s (similarity 0.79): they are the clipped theme. `recorded-audio.js § scoreCueFor` plays this `opening` cue in the flight to stop 1, then the bed, so every scored jaunt starts with the clipped theme.
- `10-overture-1812/1835/1871/1904.mp3` open on the theme (0.91).
- Beds (40-52) and battle cues (42-45) do not open on the theme (0.10-0.51).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- No jaunt plays a partial main theme. Its music starts on its own bed (or stop cue) from the first second of the flight.
- The main title theme is only ever heard complete (THEME-FINAL), where it is used at all.
- `data/music/jaunts.json` and the catalog updated (`tools/build_jaunt_music.py`, `prepare_audio.py --score-only`, `compile_jaunts.py`), with `test_jaunt_score_browser.mjs` passing.
- Kevin listens to two jaunts (one 1812, one 1904) before it merges.
