---
id: T-3439
title: Fix freezing in the Glessner courtyard; Settings to hide people and carriages and horses
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-06
closed: null
pr: 1815
claimed_by: run 11/6/2026, 10:44:01 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-07T04:44:02.791Z
decision: null
decision_answer: null
---

Fix freezing in the Glessner courtyard; Settings to hide people and carriages and horses.

Owner, 2026-11-07: "walking through the glessner courtyard i get some freezing, like the frame
freezes and then jumps forward, but when i leave the courtyard, its smooth ... maybe add a setting
to hide all people and hide all carriages and horses".

Cause (measured): Mattie Williamson (1904, the courtyard) let go of each distance level on a LOD
swap, so every crossing of her 8/20/45 m bands re-parsed her GLB, re-fitted her variation
(0.8-3.7 s of main thread per level in a container), regrew her hair, re-uploaded her 2048 px
pictures and recompiled 5-9 programs.

**Acceptance:**
- A swap back to a level drawn before reuses it: no parse, no build, no program link
  (tools/test_human_lod_park.mjs; a scripted courtyard walk in Chromium counts builds/links).
- Variation output is byte-identical and the first fit is several times faster.
- Settings > Show has People and Carriages and horses (Shown/Hidden), stored, honoured at boot;
  hidden = not drawn, advanced, fetched or picked, drivers included under People.
- Gate green; phone (light) unchanged in what it draws.
