---
id: T-2719
title: T-2598's Prairie walk moving p95 at phone profile on a real GPU (SwiftShader draws a frame in seconds, so the steward runner cannot read it)
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2602
opened: 2026-10-17
closed: 2026-10-20
pr: 1137
claimed_by: run 10/20/2026, 8:47:57 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-20T15:00:51Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39432047918
claimed_at: 2026-10-20T13:47:57.434Z
decision: null
decision_answer: null
---

T-2598's Prairie walk moving p95 at phone profile on a real GPU (SwiftShader draws a frame in seconds, so the steward runner cannot read it).

Piece 2 of 3 of **T-2602 — T-2598's remaining readings: captures at glessner-aloft-ne and the three street-eye stands (measure_memory --walk prairie --captures), the moving p95 at phone profile on a GPU, and the 1904 memory ceilings re-read with residency**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2602 was split (2026-10-17T16:59:35.730Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/17/2026, 11:59:01 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39051423277) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39051423277) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## 2026-10-19 — the owner's first 1904 attempt crashed

The owner tried the 1904 reading on his iPhone with T-2732's Read frame pacing; the tab died at the Glessner front (T-2828). Take this reading only after T-2733 (the tool's 1904 poses, scene and ratio printed, a longer run) and T-2828 (the crash) have merged; then ask the owner for a 1904 reading and file it here.

## 2026-10-20 — the owner's 1904 reading (iPhone, Chrome iOS), filed verbatim

The tab did not die: T-2828's fix holds on his phone. The build carries T-2829's governor change (the readout's "switches (n of the >50 on one)" column is T-2829's).

```
Read frame pacing (T-2733) — 2026-10-20T12:54:42.421Z
375x636 (screen 375x812) at ratio 3, detail light, 15 s a mode
scene 1904, sharpness Low (1), drawn at 1 at rest
Mozilla/5.0 (iPhone; CPU iPhone OS 27_0_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/155.0.8059.37 Mobile/15E148 Safari/604.1
build 0.1.0

move    mode      draws  mean    sd   med   p95   max  >33 >50  drawn at
walk    fixed       346  43.5   3.6  43.0  50.0  54.0  345  14  1
walk    adaptive    378  39.8   4.8  40.0  48.0  55.0  339  10  0.72-1, 2 switches (2 of the >50 on one)
  DID NOT FALL: sd 3.6 → 4.8 ms, p95 50.0 → 48.0 ms
turn    fixed       430  34.9  10.0  32.0  53.0  57.0  199  57  1
turn    adaptive    499  30.1  10.3  26.0  51.0  58.0  166  26  0.67-1, 3 switches (0 of the >50 on one)
  DID NOT FALL: sd 10.0 → 10.3 ms, p95 53.0 → 51.0 ms
flight  fixed       194  77.8   6.6  80.0  85.0  86.0  193 193  1
flight  adaptive    202  74.5   8.1  73.0  90.0  98.0  201 201  0.85-1, 1 switch (2 of the >50 on one)
  DID NOT FALL: sd 6.6 → 8.1 ms, p95 85.0 → 90.0 ms
```

**The reading this ticket asked for — T-2598's Prairie walk moving p95 at phone profile on a real GPU: walk p95 50 ms Fixed / 48 ms Adaptive (median 43 / 40 ms, about 23–25 fps).** The phone does not hold 30 fps walking Prairie Avenue at Light: 345 of 346 Fixed walk frames are over 33 ms.

What else it says:
- **Flight is the worst move by far**: median 73–80 ms (about 13 fps), every frame over 50 ms in both modes. That is the 1904 aerial at phone profile, and it is the largest cost this reading names.
- **Turn is uneven, not slow**: median 26–32 ms but sd 10 ms and 26–57 frames over 50 ms.
- **Adaptive buys throughput on 1904, not steadiness**: more draws in every move (walk 346 → 378, turn 430 → 499), medians down (walk 43 → 40, turn 32 → 26, flight 80 → 73), p95 down on walk and turn — but sd up on every move and flight's p95 up 85 → 90. It stepped the scale 2–3 times a move (to 0.67–0.72); on walk and flight two of the >50 ms frames came on a switch, so a resize is a hitch on this phone (the question T-2829 left open — answered: yes, sometimes).
