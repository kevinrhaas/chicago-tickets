---
id: T-1595
title: The light tier's 90-call floor is breached on dev at 99 calls at the open aerial, and it was 94 six days ago
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: 76
claimed_by: run 9/26/2026, 5:45:32 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36236599918
claimed_at: 2026-09-26T10:45:32.128Z
decision: null
decision_answer: null
---

The light tier's 90-call floor is breached on dev at 99 calls at the open aerial, and it was 94 six days ago.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The measurement (2026-09-26, found while landing T-1580 / #54)

`SMOKE_VIEWPORT=desktop SMOKE_STAGE=5 node tools/smoke_renderer.mjs --published`,
steward-runner, published mirror, on T-1580's branch at 3m 40s:

```
FAIL desktop 1280x800: the light tier draws inside its 90-call floor at the worst
     stand — 99 calls at light, worst stand the open aerial — floor 90, set by the
     owner 2026-08-28 against a measured 85 at Lake and Market
```

**It is inherited, not T-1580's.** `tools/dev-smoke-state.json` already carried this
same check failing on dev at **94 calls, same stand**, on 2026-09-20T18:24Z. The
worst stand is `from_above`, which T-1580's diff does not touch — it added a scene
anchor, and an anchor is a camera in a menu rather than geometry.

**So the floor is eroding again, and nobody owns it.** 94 → 99 in six days, against
a floor of 90. The three tickets that reported the last erosion — T-0247, T-0248,
T-0249, all on the *80*-call floor in 2026-08 — are `withdrawn`, because the owner
answered them by raising the floor to 90 on 2026-08-28 rather than by cutting calls.
The ruling is recorded at the definition site in `tools/smoke_renderer.mjs` and on
T-0247.

**Placed under T-0135** because T-0135 owns the neighbouring question — the
draw-call ceiling is checked at one camera and it is not the worst one — and
whatever answers this should answer that at the same time.

**Acceptance:** the check is green on dev at both viewports, by one of two routes,
and the PR says which and why: the light tier draws inside 90 calls at every stand
in `STANDS`, or the floor is a number the owner has moved again with the measurement
in front of him (`ticket.mjs ask`, since a budget he set on the record is his to
re-set). The floor may not be raised silently, and the check may not be narrowed to
a stand that passes.
