---
id: T-3569
title: Replace 1904 music with Kevin's ten-track ragtime playlist on shuffle
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: 2026-11-12
pr: 1954
claimed_by: run 11/12/2026, 11:24:21 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-12T18:50:57Z
claimed_run: null
claimed_at: 2026-11-12T17:24:22.500Z
decision: null
decision_answer: null
---

Replace 1904 music with Kevin's ten-track ragtime playlist on shuffle.

Owner request, 2026-11-12: "i would like to replace the music in 1904 with this set of songs that you would pick and start randomly in the playlist, like on shuffle, maybe these should be compressed by you in order to push up there, i can upload to cloudflare whatever package is tiny and efficient and good for the app still good audio"

**Acceptance:**
- The ten owner-supplied MP3s (Brass Trolley, Main Street Trot, Nickel Stroll, Patent Leather, Pocket Change, Ragtime Avenue, Sidewalk Ticker, Sunday Best, Tin Pan Stroll, Trolley Hop) are the whole 1904 playlist; Salon Waltz and Elegant Waltz leave 1904 playback (originals kept).
- 1904 starts at a random track and plays a shuffled order; every track plays before any repeats, and a new shuffle never opens with the track that just ended. 1812/1835 keep their in-order repeat.
- Small web deliveries: Opus primary, AAC fallback for browsers without Ogg/Opus; matched loudness; one streamed track at a time (no decoded buffers, phone memory unchanged).
- Upload package (content-addressed, MIME/cache manifest) handed to Kevin for R2; verification receipt updated once uploaded. Tests and gate green before DEV merge.
