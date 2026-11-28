---
id: T-3795
title: Stage 2 spending stop: a $100 monthly budget on chicago-stream whose alerts stop every streaming machine, plus an hours counter the starter checks before it starts one
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: 2026-11-27
pr: 2395
claimed_by: run 11/27/2026, 1:14:54 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-28T02:52:55Z
claimed_run: null
claimed_at: 2026-11-27T19:14:55.689Z
decision: null
decision_answer: null
---

Stage 2 spending stop: a $100 monthly budget on chicago-stream whose alerts stop every streaming machine, plus an hours counter the starter checks before it starts one.

**Acceptance:** (a) A $100 monthly budget on chicago-stream with alerts at 50, 90 and 100% to the owner. (b) The budget's Pub/Sub alert runs a small function that stops every streaming machine at 100% and turns the starter off until the next month or until the owner turns it back on. (c) The starter keeps its own count of machine-hours this month and refuses to start one past the hours $100 buys (the hard cap, since budget alerts can lag by hours). (d) Tested by a fake alert: machines stop, starter refuses, owner sees why. (e) Nothing here can touch chicago-61643 (sign-in, Firestore).

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 2. Owner, 2026-11-27, decision card "File the Stage 2 GPU streaming tickets now?": "File the 3 Stage 2 tickets". Google Cloud project `chicago-stream` (separate from Firebase chicago-61643, same billing account, so a spending stop never touches sign-in); one g2-standard-4 (one NVIDIA L4) in us-central1, Spot first (about $0.42/h plus egress, about $0.71/h all in; on demand about $1.00/h). GPU quota requested 2026-11-27 (GPUS_ALL_REGIONS 2, L4 in us-central1 2); Google may take up to a week or refuse. First test: Bill Tyre's Dell (Intel UHD 630). Credentials never committed: the deploy reads a repo secret.
