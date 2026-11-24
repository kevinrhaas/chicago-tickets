---
id: T-3728
title: 1904 freezes for 15 s while loading on the owner's weak test PC: between-track tufts ask every segment of every track
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-11-22
closed: 2026-11-24
pr: 2337
claimed_by: run 11/22/2026, 5:40:41 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-24T11:57:20Z
claimed_run: null
claimed_at: 2026-11-22T23:40:42.113Z
decision: null
decision_answer: null
---

1904 freezes for 15 s while loading on the owner's weak test PC: between-track tufts ask every segment of every track.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- On the owner's test PC (i5-10400, UHD 630, Bill's class), a CPU profile of 1904's boot showed one main-thread task of 15-18 s, 14.8 s of it in railway.js `nearTrack`: every tuft scattered between the tracks tested every segment of every one of 39 tracks (7,948 points).
- Done when that lookup no longer walks every segment, the longest boot task on that PC falls to about 2 s, and the tufts placed are exactly the same: same count, same places, same random draws after them.
