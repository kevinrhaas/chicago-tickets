---
id: T-0672
title: The three ceilings were raised for one parcel on 2026-09-03 and light's floor was spent: re-measure once #432 lands and take every tier back down
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-03
closed: null
pr: null
claimed_by: run 10/4/2026, 6:06:47 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37242356570
claimed_at: 2026-10-04T23:06:47.802Z
decision: null
decision_answer: null
---

**THIS TICKET EXISTS TO TAKE THEM BACK DOWN.** It is the retirement the owner's ruling
required — *"raise with stated headroom and a named retirement"* — and it is named in the
block comment at the definition in `renderers/web/js/main.js`.

## What was raised, and on whose word

The sixth re-basing of the scene-detail ceilings, 2026-09-03, on the owner's explicit
ruling. Told that landing PR #432 would require touching `light` as well as the two tiers
above it, he answered in as many words: **"raise all 3"**.

| tier | from | to | clear at the measured worst, with #432 in |
|---|---|---|---|
| `full` | 1,400,000 | **1,460,000** | 18,059 (1.24 %) |
| `balanced` | 1,225,000 | **1,280,000** | 16,806 (1.31 %) |
| `light` | 785,000 | **825,000** | 15,791 (1.91 %) |

Each tier keeps at least the ABSOLUTE headroom it carried on dev before the raise
(14,075 / 13,014 / 15,621), rounded up to the nearest 5,000, so the ladder keeps its shape.

## Why this one is written to be un-blockable

**T-0229 was the last retirement ticket and it never fell due.** Its expiry was gated behind
a flora ticket, and T-0231 exists solely to record that the raised ceilings "would never have
come down". A retirement that depends on somebody else's work is not a retirement.

So this one depends on nothing. Its trigger is a measurement, and the measurement can be
taken by any run at any time:

1. `PW_EXECUTABLE=… node tools/measure_detail_ceilings.mjs --only desktop`
2. For each tier, set the ceiling to **the measured worst stand plus the headroom recorded
   above** (18,059 / 16,806 / 15,791), rounded to the nearest 5,000.
3. If a tier reads lower than the raise assumed, it comes DOWN to what was measured. Lowering
   is free and needs no argument — it can only make the gate stricter. That is the same shape
   `tools/measure_research_spend.py --tighten` takes one layer over.

## `light` FIRST

`light` is the tier a weak machine boots into, and every previous re-budget of this table
spared it deliberately — *"the floor a weak machine boots into is not spent here, which is
the standing constraint on every re-budget this table has taken."* This raise broke that
constraint for the first time, knowingly and on a specific answer. **Whoever works this
ticket takes `light` back before either tier above it.** A weak machine currently boots into
a tier drawing 809,209 where it drew 769,379.

## The unverified number this ticket also settles

The raise was sized from a measured 2026-08-28 parcel delta applied to today's dev, **not
from a reading of the merged tree**. PR #432 has been conflicted since 2026-08-28 and its
re-derive needs Blender, which the session that took the ruling did not have. So:

- **The moment #432 is green, re-measure the merged tree.** If it reads under these ceilings,
  they come down to it immediately — that is not a favour, it is the condition the raise was
  granted on.
- If #432 is instead withdrawn or overtaken, **the raise has no parcel to carry and every
  tier returns to 1,400,000 / 1,225,000 / 785,000.** A ceiling raised for a record that never
  lands is the worst case this table has, and it is what the "five raises and one return"
  count is there to prevent becoming six and none.

**Done when** every tier sits at its measured worst plus the recorded headroom, `light` is at
or under 785,000 again, and the block comment records the return so the count reads "six
raises and two returns" rather than six and one.

## Finding, 2026-10-02 (T-1959's run, PR #272): dev is over every tier and the call budget at Lake at Canal

Measured on the published mirror of dev at 729de887, desktop, `full`, at Lake Street at Canal (part 5's
worst stand), with T-1959's woodpile record refused at the network so the reading is dev's alone:
**1,654,816 triangles against the 1,460,000 ceiling (+194,816) and 221 draw calls against 215.** Smoke
part 5 on the T-1959 branch failed all three tiers there (full 1,611,977, balanced 1,413,832, light
931,682 before #266/#271 landed). T-1959 adds +70,928 triangles and +2 calls at that stand on top. So
every PR that touches the frame is red on part 5 until this is cut or re-budgeted under AGENTS.md's
three constraints; `tools/woodpile_shots.mjs --anchor lake_at_canal` takes the before/after reading.

## `light` is over on dev again — read 2026-10-03 (T-0192)

Read with `tools/measure_detail_ceilings.mjs`, published mirror of dev @ d8b7748d, T-0135's five
stands, desktop 1280x800: `light` worst **851,431 at the forks** against 825,000 (over by 26,431),
open aerial 813,093, Lake at Canal 801,916. T-1976 had trimmed it to 803,067 at the forks on
2026-10-02, so about 48,000 came back in a day of parcels; not bisected. Desktop smoke part 5 is
red on `light` alone. T-0192 (#331) hid its cross-street walks at `light`
(`light.crossStreetWalks: false`) and still reads 856,275 there (+4,844, inferred from the walks'
planting keep-outs, which apply at every tier). `full`/`balanced` were re-set to 2,140,000 /
1,820,000 in the same PR. The floor is this ticket's, or a trim's, to win back.
