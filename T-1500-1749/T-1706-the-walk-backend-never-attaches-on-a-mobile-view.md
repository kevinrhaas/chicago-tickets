---
id: T-1706
title: The walk backend never attaches on a mobile viewport: dev is red on five of part 4's checks — walk intent moves the camera 0.00 m with 'backend none', touch activates nothing, the thumbstick writes forward 0, and a right-half drag turns 180 degrees
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: All five walk checks pass: mobile parts 1-6 297/0 on 2026-10-01, which includes part 4."
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The walk backend never attaches on a mobile viewport: dev is red on five of part 4's checks — walk intent moves the camera 0.00 m with 'backend none', touch activates nothing, the thumbstick writes forward 0, and a right-half drag turns 180 degrees.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured, and where

Measured 2026-09-28 by the run that shipped T-1588, which ran `SMOKE_STAGE=3-4` at mobile
and found part 4 red. The five checks:

    FAIL  mobile 390x780: walk intent moves the camera — moved 0.00 m in 2.2 s (backend none)
    FAIL  mobile 390x780: the walker is pushed out of a building footprint — dropped at
                          (106.36000000000001, -126.6), ended at (106.36, -126.60)
    FAIL  mobile 390x780: touch activates the touch backend — none
    FAIL  mobile 390x780: thumbstick writes forward intent — intent.forward = 0
    FAIL  mobile 390x780: right-half drag turns the view — turned 180.0°

**It is dev's red and not that branch's.** The same part was run against a clean
`origin/dev` worktree (06129a65) published on its own, and produced the identical five
failures — filed in `tools/dev-smoke-state.json` as `mobile stage 4 FAIL` on
sha256:9a26e3709b090c2d. `renderers/` on the T-1588 branch differs from dev in
`residents.js` and `changelog.js` only, neither of which the walk backend reads.

`backend none` says the controls never attached at all, so this is not a tuning
regression: nothing is driving the camera. The welcome overlay landed recently and
deliberately holds the pointer until a visitor chooses to look around (v1187, "Your mouse
stays free until you choose to look around"), which is the first place to look — whether
the smoke's entry into the scene still reaches the state where the backend binds.

**Mobile is a release gate.** Until this is answered, no run can take a clean mobile part 4
reading, and a run whose diff touches the walk has no way to tell its own red from this one.

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** All five walk checks pass: mobile parts 1-6 297/0 on 2026-10-01, which includes part 4.
