---
id: T-3622
title: Dev's desktop smoke part 5 is red: 'full' and 'light' are over their triangle ceilings at West prairie (3,513,901 of 3,495,000; 1,225,393 of 1,190,000)
state: claimed
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: null
pr: null
claimed_by: run 11/16/2026, 2:32:07 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43948981037
claimed_at: 2026-11-16T20:32:08.425Z
decision: pending
decision_answer: null
---

Dev's desktop smoke part 5 is red: 'full' and 'light' are over their triangle ceilings at West prairie (3,513,901 of 3,495,000; 1,225,393 of 1,190,000).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: smoke (desktop, 5) fails with identical readings on PR #2113's head 5571776b (job 133475434934) and PR #2102's head 8178526f (job 133504032739), two unrelated houses, so every open PR's leg 5 inherits it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Decision needed

**Question:** Desktop 1280x800 at the West prairie stand is now over all three scene-detail triangle ceilings, and that turns every PR's smoke part 5 red. Measured on dev c8649f3cd (published mirror, tools/measure_detail_ceilings.mjs, the gate's own instrument): full 3,552,275 of 3,495,000, balanced 2,710,157 of 2,675,000, light 1,251,432 of 1,190,000. The phone, 390x780, is inside all three (light 1,090,622). Two of today's owner parcels did it together: T-3612's schooners (the new vessels layer costs about 41,000 triangles at Light from that stand, and on its own it put Light at 1,225,393 on PR #2113 and PR #2102) and T-3605's Gifford street faces (about 26,000 more). Full and Balanced can move under the 2026-08-21 'just raise it' ruling. Light is the floor, and each raise of it so far (T-2015, T-2035, T-2339) was yours to authorize. Raise Light a fourth time, or hold it and trim?

- (a) Raise it: Light 1,190,000 -> 1,270,000 (1,251,432 plus T-0672's 15,791 headroom, rounded up to 5,000), with Full -> 3,575,000 and Balanced -> 2,730,000 on the same margins. Nothing in the scene changes, and dev's part 5 goes green in one PR.
- (b) Hold Light at 1,190,000 and trim at Light only: draw no vessel past about 600 m at Light (like the 350 m furniture reach), which recovers at most about 41,000, plus a second trim for the other ~20,000+ that is not found yet. Distant schooners disappear on Light, and dev's part 5 stays red until both trims land.

**Recommendation:** (a) Raise it: Light 1,190,000 -> 1,270,000 (1,251,432 plus T-0672's 15,791 headroom, rounded up to 5,000), with Full -> 3,575,000 and Balanced -> 2,730,000 on the same margins. Nothing in the scene changes, and dev's part 5 goes green in one PR. — Both parcels are ones you asked for, and the ruling is that the scene needing it is the justification. The phone is still well inside its floor, the breach is desktop-only, and coarse schooner hulls would save only about 5,000 (measured), so a trim means taking boats off Light. Option a unblocks every open PR's part 5 today.

**Asked:** 2026-11-16 by https://github.com/kevinrhaas/polecat-platform/actions/runs/43948981037. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.
