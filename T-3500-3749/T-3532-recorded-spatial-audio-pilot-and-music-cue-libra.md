---
id: T-3532
title: Recorded spatial audio pilot and music cue library
state: blocked-tech
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-09
closed: null
pr: null
claimed_by: run 11/9/2026, 8:20:16 PM CT
blocked_on: Local audio pilot is implemented and focused audio/browser checks pass. Integration is blocked by published storage: about 466 MiB versus the 432 MiB site limit; versioned audio hosting or a measured storage change is needed. Work remains uncommitted on audio/recorded-soundscape in the shared workspace. No PR or production promotion; remaining full gate and 3D smoke are outstanding. See docs/AUDIO.md and docs/STATUS.md.
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-10T02:20:18.819Z
decision: null
decision_answer: null
---

Recorded spatial audio pilot and music cue library.

**Acceptance:**
- Replace synthetic destination atmosphere with recorded water and wind, selected by the live terrain and season; opt-in sound remains silent and fetch-free by default.
- Integrate the seven owner-supplied music cues: Frontier=1812, Border=1835, Waltzes=1904. Stream only the selected era and support independent music volume. Owner confirmed usage/distribution rights in chat on 2026-11-10; generated-music provenance is explicit.
- Catalog source/license/derivative metadata; retain originals outside the published payload and show credits in the app.
- Verify lifecycle, mute, hidden-tab, scene changes, browser decoding and payload size. Report unverified listening quality and deferred moving-source/voice work honestly.
- No production promotion.
