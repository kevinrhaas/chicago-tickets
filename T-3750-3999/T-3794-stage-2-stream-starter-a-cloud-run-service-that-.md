---
id: T-3794
title: Stage 2 stream starter: a Cloud Run service that starts a Spot L4 machine for a signed-in, allow-listed player, hands back the stream link, and stops it after 10 idle minutes or 2 hours, two machines at most
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2395
claimed_by: run 11/27/2026, 1:14:52 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T19:14:52.802Z
decision: null
decision_answer: null
---

Stage 2 stream starter: a Cloud Run service that starts a Spot L4 machine for a signed-in, allow-listed player, hands back the stream link, and stops it after 10 idle minutes or 2 hours, two machines at most.

**Acceptance:** (a) A Cloud Run service in chicago-stream checks the player's Firebase ID token and an allow-list (owner, Bill Tyre, named testers), starts a Spot machine from T-3793's image (on-demand only if Spot is refused, and only for the owner), and hands back the stream link; the link works for that player only. (b) At most two machines at once; a third player is told the wait plainly. (c) A machine stops after 10 minutes with no input and after 2 hours in any case, and the player is warned a minute before. (d) The app shows *Play from the cloud* in Settings › Graphics only to allow-listed players, with the cost of an hour in plain words for the owner. (e) Deployed from GitHub with the repo secret GCP_STREAM_SA; no key in the repo. Measured: time from click to first picture.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 2. Owner, 2026-11-27, decision card "File the Stage 2 GPU streaming tickets now?": "File the 3 Stage 2 tickets". Google Cloud project `chicago-stream` (separate from Firebase chicago-61643, same billing account, so a spending stop never touches sign-in); one g2-standard-4 (one NVIDIA L4) in us-central1, Spot first (about $0.42/h plus egress, about $0.71/h all in; on demand about $1.00/h). GPU quota requested 2026-11-27 (GPUS_ALL_REGIONS 2, L4 in us-central1 2); Google may take up to a week or refuse. First test: Bill Tyre's Dell (Intel UHD 630). Credentials never committed: the deploy reads a repo secret.
