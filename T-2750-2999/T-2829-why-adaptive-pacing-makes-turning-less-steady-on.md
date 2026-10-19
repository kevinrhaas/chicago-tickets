---
id: T-2829
title: Why Adaptive pacing makes turning less steady on the owner's phone (turn sd 4.7 to 6.5 ms, max 44 to 73 ms in T-2733's reading), and whether Adaptive stays the default until it does not
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-18
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

Why Adaptive pacing makes turning less steady on the owner's phone (turn sd 4.7 to 6.5 ms, max 44 to 73 ms in T-2733's reading), and whether Adaptive stays the default until it does not.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 153 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2733's acceptance asks for exactly this follow-up to be filed with the reading attached: the cause of the turn regression and the default it bears on are a separate question from filing the reading

## The reading it starts from (T-2733, the owner's iPhone, 2026-10-19, 1835 scene, Light, 5 s a mode)

Filed verbatim in the code repo at `chicago/4d/docs/measurements/t-2733-owner-phone-1835.txt` (rows as JSON beside it):

```
move    mode      draws  mean    sd   med   p95   max  >33 >50
walk    fixed       163  30.8   6.0  29.0  43.0  59.0   34   3
walk    adaptive    161  31.3   5.0  30.0  41.0  46.0   47   0
turn    fixed       186  27.1   4.7  27.0  37.0  44.0   16   0
turn    adaptive    157  32.0   6.5  32.0  41.0  73.0   56   3
flight  fixed       162  31.0   3.9  31.0  38.0  45.0   42   0
flight  adaptive    161  31.2   5.0  30.0  41.0  49.0   48   0
```

Walk fell (sd 6.0 → 5.0, p95 43 → 41, max 59 → 46); turn rose (sd 4.7 → 6.5, +38 %; p95 37 → 41; max 44 → 73, three frames over 50 ms where Fixed had none); flight rose a little (sd 3.9 → 5.0, p95 38 → 41). The phone does not hold 60 at Light even on Fixed (medians 27–31 ms), so Adaptive is pacing to 30 there — and on a turn, Fixed's median (27 ms) was already faster than Adaptive's 30-fps pace (32 ms), so pacing may be holding frames back that would have come sooner. Adaptive is the default (`#s-governor`, first option).

T-2733 also made the readout print the scene, the Sharpness stop and the pixel ratio each drive drew at (min–max, so Adaptive's scale switching shows), and made 15 s a mode the default run. A repeat on that build is the first thing to ask for: one 5 s sample a mode is thin.

## What to find

- Read `js/frame-governor.js` against this: does the 30-fps pace (or the shadow halving, or the scale stepping between 0.67× and 1×) switch on and off during a turn, and is a switch what the 73 ms frame is? A turn re-draws the whole view each frame (new geometry in view, new texture uploads), unlike a walk, which changes it gradually.
- Whether a turn should pace at all when Fixed already beats the paced interval.
- Take a longer repeat from the owner with T-2733's readout (the drawn-ratio column says whether the scale moved).

**Acceptance:** (state it before working — the definition of done, never weakened to pass) — a cause for the turn regression named from the code and the readout's drawn-ratio column, a fix if one is in reach that the owner's repeat reading shows (turn sd and p95 no worse under Adaptive than Fixed), and if the answer is that Fixed should be the default until then, a decision card for the owner (`ticket.mjs ask`) rather than a default changed by a run.
