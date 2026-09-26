---
id: T-1627
title: T-1622 re-dealt blk_south_water_franklin out from under the agencies smoke fixture: mobile part 3 asks recon_1835_blk_south_water_franklin_d5_01 for its REFUSED agency holding and 1835_agencies.json no longer names that roof at all
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-09-26
pr: 86
claimed_by: run 9/26/2026, 11:42:27 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-26T17:24:52Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36256256604
claimed_at: 2026-09-26T16:42:27.478Z
decision: null
decision_answer: null
---

T-1622 re-dealt blk_south_water_franklin out from under the agencies smoke fixture: mobile part 3 asks recon_1835_blk_south_water_franklin_d5_01 for its REFUSED agency holding and 1835_agencies.json no longer names that roof at all.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found by a lap of T-1611's PR #74, 2026-09-26, and it is dev's, not that branch's.**
`SMOKE_VIEWPORT=mobile SMOKE_STAGE=1-3` is 239/240 on the merge of origin/dev into
`steward/t-1611-block-redeal`, the one red being

    mobile 390x780: a refused holding is on the card of the house it was refused for

`smoke_renderer.mjs:7029` reads that card off `recon_1835_blk_south_water_franklin_d5_01`.
`1835_agencies.json` in dev today does not mention that structure id anywhere, so the
popup grows no agency section and `present` is false before `refused` is ever asked.

**Why it is dev's.** T-1622 (#79, merged into dev 2026-09-26) is the commit that touched
both `data/reconstruction/1835_agencies.json` and
`data/structures/recon_1835_blk_south_water_franklin_d5_01.json` — it raised two new roofs
on that block's last free front, and the refusal moved off the roof the fixture pins.
The lapping branch's own `1835_agencies.json` is byte-identical to dev's, and its platted
deal differs from dev's by exactly the six rear cottages of three other blocks
(`git diff origin/dev...HEAD` names no agency, register or franklin file). The last
recorded mobile 1-3 reading, 2026-09-26T12:23Z, is a PASS — taken before #79.

**Two ways to close it, and the choice is the point.** Either the refusal genuinely belongs
to a different roof now, in which case the fixture should be repointed at whichever roof
`1835_agencies.json` records it against and the smoke says why it moved; or the re-deal
dropped a refusal it should have carried, in which case the file is wrong and not the test.
Read `1835_agencies.json`'s own generator before picking — a fixture edited to make a suite
green is how a real regression gets buried.
