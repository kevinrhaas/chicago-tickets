---
id: T-3153
title: The photo-ticket stopping rule: a within-tolerance status in the image gate, no run-filed photo follow-ups for a photo-gated house, a sign-off is never split, and a 25-ticket cap per house
state: claimed
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-25
closed: null
pr: null
claimed_by: run 10/25/2026, 8:24:49 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-25T13:24:50.185Z
decision: null
decision_answer: null
---

The photo-ticket stopping rule: a within-tolerance status in the image gate, no run-filed photo follow-ups for a photo-gated house, a sign-off is never split, and a 25-ticket cap per house.

Owner, 2026-10-25 (thread "Stop endless photo-match tickets"): *"I appreciate all the focus on Glessner but i feel like you keep going on with creating tickets in an almost never ending fashion ... you need to help me with not creating more and more tickets when there are probably some seriously diminishing returns"*. He then chose **"Full rule, close 5 now"** on the proposal (Glessner: 115 tickets since the gate, 110 differences fixed, 9 left, its sign-off re-filed five times).

**Acceptance:**
1. AGENTS.md rule 11 and `data/reference_views/README.md` state the good-enough bar (a difference is open only if a street visitor would notice it: over about 1 ft / 0.3 m, an element missing or the wrong shape, a wrong count, a wrong material or colour), the `within tolerance` status, no run-filed photo follow-ups, one unsplittable sign-off, and the 25-ticket cap.
2. `image_gate.mjs` accepts `within tolerance`, which does not block `matches`; its self-test proves it.
3. `ticket.mjs new` refuses a filing that is not `--by owner` for a photo-gated house, and for any house past 25 tickets since 2026-10-11; `split` refuses a sign-off and a gated house past the cap unless `--owner-asked "<his words>"`. A test proves each refusal and that an owner filing and a perf filing still go through.
4. The five closures (T-3141, T-3142, T-3138, T-3149, T-3075) and the T-3140 / T-3093 notes are done in the tickets repo (done 2026-10-25).
