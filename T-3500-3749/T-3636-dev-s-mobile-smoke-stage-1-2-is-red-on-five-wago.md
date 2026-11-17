---
id: T-3636
title: Dev's mobile smoke stage 1-2 is red on five wagon and yard checks since the T-3558 wagon change (yard goods, Green Tree yard wagons, town wagon spread, type mix, dealt slew)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-17
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Dev's mobile smoke stage 1-2 is red on five wagon and yard checks since the T-3558 wagon change (yard goods, Green Tree yard wagons, town wagon spread, type mix, dealt slew).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (loop, 2026-11-17)

`SMOKE_VIEWPORT=mobile SMOKE_STAGE=1-2 node tools/smoke_renderer.mjs --published` on bare
`origin/dev` at 285b22502: 192 passed, 5 failed, the same five as on PR #2147's branch (and on
CI's `smoke (mobile, 1-2)` for #2147 at 8a5fef6c1, run 44086546268):

- the yard layer stands the record's goods (110 frontage(s) refused, 0 sheds)
- the Green Tree's yard wagons stand clear, square to its rear wall (0 wagons)
- the town's wagons are spread across its streets, not at two doors
- the town's wagons vary in type (6 farm_box, 39 cart, 2 covered)
- the town's wagons stand at the slew the rule dealt them

Dev's record read PASS on this leg at 04:35Z; T-3558 ("the 1835 town's standing wagons are the
photographic farm box, and fewer", 2f7fca6fa) landed on dev after it. Likely the smoke's wagon
and yard expectations were not moved with the change. Filed in `tools/dev-smoke-state.json` by #2147.
