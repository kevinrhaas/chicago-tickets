---
id: T-2454
title: settle: a chained ticket whose predecessor lost its queue line opens at the head of the band below band 9, not at the foot of the file
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: run 10/13/2026, 2:15:17 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-13T07:15:17.673Z
decision: null
decision_answer: null
---

settle: a chained ticket whose predecessor lost its queue line opens at the head of the band below band 9, not at the foot of the file.

**The owner, 2026-10-13:** "Are Glessner tickets being consistently worked? Like I see 2213 I think at the end of the queue and I would think at any given time there would be at least one Glessner ticket being claimed and work at all times".

**What happened:** T-2212 was re-blocked on T-2416 by hand on 2026-10-12 while a run was already working it, so its band-7 line moved to 8b. The run's `done --pr 743` then dropped the 8b line and left T-2212 in review with no queue line. When #743 merged (2026-10-13 04:56 UTC), `settle` reopened T-2213 but had no line to hand it, so `unblockSuccessors` appended it at the foot of the file (line 206 of 206), below every Prairie and image-match ticket. T-2213 was moved back by hand the same day.

**Acceptance:**
- When the merged ticket has no queue line, its chained successor opens at the head of the first numbered band below band 9 (the head of the ranked programme, band 7 today), and settle says so; with no band 9 it still appends.
- `tools/test_ticket_repo_mode.mjs` covers it.
