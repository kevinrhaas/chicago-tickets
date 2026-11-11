---
id: T-3544
title: Recorded harness and wagon sounds follow moving teams
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-10
closed: 2026-11-11
pr: 1931
claimed_by: run 11/10/2026, 10:16:01 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-11T13:15:09Z
claimed_run: null
claimed_at: 2026-11-11T04:16:02.500Z
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

**Owner steering, 2026-11-11:** “For the music it should keep Playing like on repeat it played a song and ended in 1835.” Add continuous era-playlist repeat to this audio increment. Remove the intentional between-track silence, reuse the streaming element across natural track endings, and verify both 1835 tracks wrap to the first without another click. Muting, Music off, scene changes, hidden tabs and disposal must still stop playback; stale ended callbacks must not restart it. Keep the era libraries separate and load only the active track.

**Owner listening steering, 2026-11-11:** wind sounds too strong in town, particularly 1904; more exposure near the 1812 shore is reasonable. River audio in 1835 sounds moving/babbling although the scene shows nearly still, slow water. “The bugs were nice.” Preserve insect recordings, scheduling and levels; lower town wind with restrained lake proximity and hold the busy river proxy from scene playback until a calmer lapping source is qualified.

**Owner UI/travel steering, 2026-11-11:** replace the large Sound on/off text button with a compact speaker icon showing mute/on; retain an accessible touch target. Explain Ambience versus Effects in Settings with examples. Clarified music scope: “Only time-travel/arrival; keep period music in town.” Music must stay silent through the time stream, landing and arrival choices, then repeat in town; ambience/effects remain independent. A separate travel track is future owner-supplied work.

**Owner spacing follow-up:** sound descriptions sat too low and looked attached to the next setting. Group each label, slider and description together; use a small gap after its own slider and a larger gap before the next control.

**Owner text follow-up:** remove the unnecessary Music behavior paragraph and general Sound disclaimer shown below the sliders. Keep just the Ambience and Effects examples. Both removed; catalogue provenance and credits remain available through the existing library link.

**Owner river selection and upload, 2026-11-11:** “Light water on rocks.” The uploaded selected TRP575244 loop passed full public hash, CORS, MIME and range verification. Include it in this same increment while the concurrent DEV integration is undergoing fresh validation. Preserve exact accepted bytes/crop, keep prior TRP577323 held as river-held, retain river/lake/slough geography and insects, and qualify the 12,672,000-byte three-buffer environmental cache at high output rates. Current hold-only proof is superseded by these selected-river checks; no earlier gate is claimed as the final combined verdict.
