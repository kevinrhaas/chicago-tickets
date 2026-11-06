---
id: T-3402
title: Bring standing and walking people to life: breathing, weight shifts, gaze toward the visitor and street, natural blinks
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: 1743
claimed_by: run 11/5/2026, 10:54:09 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-06T04:54:10.522Z
decision: null
decision_answer: null
---

Bring standing and walking people to life: breathing, weight shifts, gaze toward the visitor and street, natural blinks.

Kevin, 2026-11-06: Hans "looks odd still ... too smooth and not real ... set us on a path for all humans to look photographic realistic", and "make progress on completing humans and making them fully available to interact with". Hans on his box got a life layer (driver-life.js, T-1790); the standing and walking figures of humans.js have only their clip and a fixed 4-second blink.

**Acceptance:**
- A new module, renderers/web/js/human-life.js (driver-life.js, driven-assembly-loader.js and fabric.js untouched), layered additively over the clip on every standing/talking/working and walking HumanActor within animation range.
- Standing: breathing in the chest and shoulders; a weight shift every several seconds (pelvis tips to the loaded hip, spine counters it, head stays level); looks around (eyes lead, head and neck follow, torso joins a wide look) at the street ahead, to each side and down, and turns to a visitor who comes within a few metres in front of them.
- Walking: quicker breathing, glances along the street and at a close visitor; the gait's own pelvis and legs untouched.
- Blinks at a natural irregular interval (2-6 s, an occasional double) in place of the fixed 4 s blink.
- `actor.life.attend(point, seconds)` for the interaction thread to call from the approach event.
- Bounded and deterministic: no accumulation through three's skip-unchanged track writes, seeded per person; a gate test on the real Otis export and the fixture (tools/test_human_life.mjs) in check.sh.
- No new assets or textures (1904 phone memory ceiling); the reconstructed motion recorded as a liberty.
