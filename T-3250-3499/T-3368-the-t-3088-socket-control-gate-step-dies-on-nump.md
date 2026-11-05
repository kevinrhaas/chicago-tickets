---
id: T-3368
title: The T-3088 socket control gate step dies on NumPy 2.5's removed 2-D np.cross, so check.sh part 2 is red on every steward runner
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-03
closed: null
pr: 1706
claimed_by: run 11/4/2026, 10:58:27 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41969777905
claimed_at: 2026-11-05T04:58:28.067Z
decision: null
decision_answer: null
---

`tools/check.sh --part 2/4` is RED on the steward runner, and has nothing to do with
whatever ticket the run is carrying. The step is

> Selected upper-lid source preserves925/eyeUV/hoof ownership and qualifies the fixed socket interface (T-3088)

and it dies inside dev's own transport code:

```
tools/transport/horse_socket_interface_v1/socket_controls.py:17, in orient
    def orient(a,b,c):return float(np.cross(b-a,c-a))
ValueError: Both input arrays must be (arrays of) 3-dimensional vectors,
            but they are 2 and 2 dimensional instead.
```

`orient()` is a 2-D signed-area test written as a cross product of two 2-vectors.
NumPy supported that with a `DeprecationWarning` and has now removed it. Measured
both ways on 2026-11-04:

| numpy | `np.cross([1,0],[0,1])` |
|---|---|
| 2.3.5 | `1.0`, with a `DeprecationWarning` |
| 2.5.4 | raises `ValueError` |

So which side of the line a machine falls on is decided by the Python it resolves
against, and the two environments disagree:

* `chicago-4d-check.yml` pins **Python 3.11**, where `pip install numpy` resolves
  **2.3.x** — the hosted `gate` was green on #1649's head `a6207b49` with this code.
* the steward runner has **Python 3.14**, where it resolves **2.5.4** — red.

That is the whole fault. It is not a regression in anyone's building work, but every
run that gates locally on this runner image meets it, and a run that reads it as its
own red can lose its budget chasing it. (T-2388's run on 2026-11-04 did diagnose it
correctly and re-ran part 2/4 green under `numpy<2.4`, at the cost of the detour.)

The fix is a one-line arithmetic change in `socket_controls.py` — the 2-D signed area
written out, e.g. `(b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])`, or a `cross2`
helper — not a numpy pin. The same call should be looked for elsewhere in
`tools/transport/`. It is deliberately NOT being done inside a building PR:
`socket_controls.py` is T-3088's source and T-3088 is live.

Worth deciding at the same time whether the gate workflow should pin numpy, so CI and
the runners cannot drift apart again on an API that is being removed underneath both.

**Acceptance:** `tools/check.sh --part 2/4` passes on a machine with numpy >= 2.5
with no numpy pin and no env override, the step keeps every assertion it has today,
and the hosted eight-part `gate` stays green. No 2-D `np.cross` call is left in
`tools/transport/`.
