---
id: T-3793
title: Stage 2 streaming machine image: Ubuntu with the NVIDIA L4 driver, Chromium and the Selkies streamer, opening the town at the student's year, built by a script into the chicago-stream project
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
claimed_by: run 11/27/2026, 1:14:49 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T19:14:49.914Z
decision: null
decision_answer: null
---

Stage 2 streaming machine image: Ubuntu with the NVIDIA L4 driver, Chromium and the Selkies streamer, opening the town at the student's year, built by a script into the chicago-stream project.

**Acceptance:** (a) A script in the repo (`tools/stream/`) builds a machine image in chicago-stream: Ubuntu LTS, the NVIDIA driver for L4, Chromium with GPU rendering on, and the Selkies browser streamer (WebSockets), opening chicago.polecat.live/4d/ at the year and settings the starter passes. (b) A test machine from the image streams the 1904 town to a phone and to a low-end PC at 1080p, 30 fps or better at about 8 Mbps, sound included; measured frame rate, input delay and bytes per hour recorded in docs. (c) The machine signs nothing in itself: the player signs in inside the stream as on any device. (d) The test machine is deleted after the run; the image stays. Pictures at both widths.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 2. Owner, 2026-11-27, decision card "File the Stage 2 GPU streaming tickets now?": "File the 3 Stage 2 tickets". Google Cloud project `chicago-stream` (separate from Firebase chicago-61643, same billing account, so a spending stop never touches sign-in); one g2-standard-4 (one NVIDIA L4) in us-central1, Spot first (about $0.42/h plus egress, about $0.71/h all in; on demand about $1.00/h). GPU quota requested 2026-11-27 (GPUS_ALL_REGIONS 2, L4 in us-central1 2); Google may take up to a week or refuse. First test: Bill Tyre's Dell (Intel UHD 630). Credentials never committed: the deploy reads a repo secret.
