---
id: T-1807
title: The two H1 boarding houses sized from their beds: frame_dwelling learns stovepipes, north_h1_007 and west_006 baked
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1780
opened: 2026-10-01
closed: 2026-10-01
pr: 233
claimed_by: run 10/1/2026, 11:25:26 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-01T17:42:06Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36874944140
claimed_at: 2026-10-01T16:25:26.729Z
decision: null
decision_answer: null
---

The two H1 boarding houses sized from their beds: frame_dwelling learns stovepipes, north_h1_007 and west_006 baked.

Piece 2 of 3 of **T-1780 — The smaller houses and the books: H1/H2 fenestration and chimneys from capacity once T-1293/T-1196 rule what they are, the frame budget read, a boarding-house row screenshot, T-1214 handed on**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The two H1 small boarding houses (`recon_1835_north_h1_007`, `recon_1835_west_006`) stand
on `frame_dwelling`, which has no stovepipe parameter; its five-bay centre-passage front is
the H1 crosswalk's stated "5 bays" and is not resized. `frame_dwelling` gains an off-by-default
`stovepipes` count (every committed dwelling rebuilds byte-identical), and the two houses
carry a `capacity` block and stovepipes sized from their beds by T-1806's rule, baked.
