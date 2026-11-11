---
id: T-3544
title: Recorded harness and wagon sounds follow moving teams
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-10
closed: null
pr: null
claimed_by: run 11/10/2026, 7:40:15 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-11T01:40:16.602Z
decision: null
decision_answer: null
---

Recorded harness and wagon sounds follow moving teams.

Owner request: everything that sounds nearby has its visible source; moving wagons grow louder as they approach. Recorded proxies are authorized. Continue audio work and merge to DEV when green, alongside concurrent merges.

**Acceptance:**
- The existing recorded harness and wooden-wagon deliveries follow the actual loaded moving assemblies. Harness serves the four dated teams; wagon rolling serves only the three wooden wagons, never the 1904 brougham.
- Sources follow world position and distance, use the Effects slider, and cease on stop, dwell, pause, reduced motion, hidden/cull, off-hours or disposal. Missing actors never emit.
- Default mute fetches no sound; opt-in playback is bounded to two nearby teams/four voices and two mono 48 kHz buffers within 8 MiB. Pending decodes cannot revive muted/disposed sources.
- Reuse verified R2 delivery hashes without new media upload; retain CC0 provenance and explicitly reconstructed placement. No claim of a historical Chicago recording or production listening approval.
- Meaningful motion/lifecycle, spatial mixer, browser and catalog/regeneration tests pass, followed by all four local gate parts, preflight and published smoke at both required sizes before DEV merge.
