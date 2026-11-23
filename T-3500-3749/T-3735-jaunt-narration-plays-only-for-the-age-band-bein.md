---
id: T-3735
title: Jaunt narration plays only for the age band being read; Narrated filter per band
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-23
closed: null
pr: null
claimed_by: run 11/23/2026, 6:45:32 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-23T12:45:34.168Z
decision: null
decision_answer: null
---

Jaunt narration plays only for the age band being read; Narrated filter per band.

Owner, 2026-11-23: "Narration should always match the age band of the story you are running ... if a person is on the say age 8-10 band then that narrating plays but if they are on 11-13 ... and you do not have narration for that then don't play that other wrong narration unless you have the correct one."

Cause: clips are looked up by the SHA-256 of the words alone, so a telling for another band that shares words with a voiced telling (the same title and opening, an unchanged stop) played that telling's recording. And the Jaunts menu's Narrated pill filtered before choosing the reader's telling, so it fell back to the base (another band's) telling.

**Acceptance:** a jaunt plays (and offers Listen for) a recording only when that telling itself is voiced (catalog `narrated`, from data/narration/voices.json); every other telling plays no narration, while its text and music run as before. With the Narrated pill on, the menu lists only tellings for the reader's picked ages that are themselves narrated, never another band's in their place. Tests cover both. Nothing new is voiced.
