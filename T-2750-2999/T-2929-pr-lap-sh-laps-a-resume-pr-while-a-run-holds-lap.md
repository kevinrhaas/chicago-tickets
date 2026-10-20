---
id: T-2929
title: pr-lap.sh laps a resume PR while a run holds lap/pr-N: #1132's lock was taken at 13:00Z on 2026-10-20, the server lap pushed df6ae544a over it at 13:19Z and merge-ready merged it at 13:37Z, so the holding run's merge-dev, rederive (10 min), check.sh and smoke were all thrown away; the server lap and merge-ready should skip (or wait on) a PR whose lap lock a live run holds, the same compare-and-swap ticket.mjs lap uses
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-20
closed: null
pr: 1140
claimed_by: run 10/20/2026, 9:20:12 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-20T14:20:12.430Z
decision: null
decision_answer: null
---

pr-lap.sh laps a resume PR while a run holds lap/pr-N: #1132's lock was taken at 13:00Z on 2026-10-20, the server lap pushed df6ae544a over it at 13:19Z and merge-ready merged it at 13:37Z, so the holding run's merge-dev, rederive (10 min), check.sh and smoke were all thrown away; the server lap and merge-ready should skip (or wait on) a PR whose lap lock a live run holds, the same compare-and-swap ticket.mjs lap uses.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
