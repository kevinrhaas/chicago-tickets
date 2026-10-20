---
id: T-2898
title: The owner's 15 s Read frame pacing repeat on the T-2829 build (/4d/dev/1835/, iPhone, Settings, Performance, Read frame pacing): the turn row's Adaptive sd and p95 at or under Fixed's, at most one ratio switch, and whether any frame over 50 ms came on a switch; filed verbatim, and Adaptive stays the default only if it passes
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2829
opened: 2026-10-19
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

The owner's 15 s Read frame pacing repeat on the T-2829 build (/4d/dev/1835/, iPhone, Settings, Performance, Read frame pacing): the turn row's Adaptive sd and p95 at or under Fixed's, at most one ratio switch, and whether any frame over 50 ms came on a switch; filed verbatim, and Adaptive stays the default only if it passes.

Piece 2 of 2 of **T-2829 — Why Adaptive pacing makes turning less steady on the owner's phone (turn sd 4.7 to 6.5 ms, max 44 to 73 ms in T-2733's reading), and whether Adaptive stays the default until it does not**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2829 was split (2026-10-20T01:32:25.989Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 35m ago, run 10/19/2026, 7:57:42 PM CT — held by the run that split it
- PR #1112 on claude/loop-optimization-tickets-mmvcns — T-2829, T-2606, T-2774, T-2824, T-2723: performance and GPU batch — phone pacing, boot GL errors, flora and gaze-pick stalls — held by the run that split it

The run that split it (by hand) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## 2026-10-20 — the owner's repeat on the T-2829 build, filed verbatim

```
Read frame pacing (T-2733) — 2026-10-20T12:59:36.587Z
375x636 (screen 375x812) at ratio 3, detail light, 15 s a mode
scene 1835, sharpness Low (1), drawn at 1 at rest
Mozilla/5.0 (iPhone; CPU iPhone OS 27_0_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/155.0.8059.37 Mobile/15E148 Safari/604.1
build 0.1.0

move    mode      draws  mean    sd   med   p95   max  >33 >50  drawn at
walk    fixed       522  28.8   7.4  27.0  47.0  67.0   58  16  1
walk    adaptive    552  27.3   6.4  26.0  43.0  71.0   48   9  0.72-1, 3 switches (1 of the >50 on one)
  FELL: sd 7.4 → 6.4 ms, p95 47.0 → 43.0 ms
turn    fixed       538  27.9   7.1  27.0  44.0  63.0   69  15  1
turn    adaptive    556  27.0   6.2  26.0  39.0  62.0   69   4  0.72-1, 2 switches (0 of the >50 on one), paced 9 %
  FELL: sd 7.1 → 6.2 ms, p95 44.0 → 39.0 ms
flight  fixed       386  39.0   5.6  37.0  54.0  64.0  374  26  1
flight  adaptive    408  36.9   5.2  35.0  48.0  69.0  343  20  0.85-1, 1 switch (0 of the >50 on one)
  FELL: sd 5.6 → 5.2 ms, p95 54.0 → 48.0 ms
```

Against the acceptance in this ticket's title:
- **Turn row, Adaptive sd and p95 at or under Fixed's: MET.** sd 6.2 against 7.1, p95 39 against 44; frames over 50 ms 4 against 15. That reverses T-2733's reading (Adaptive turn sd 6.5 / p95 41 / max 73 against Fixed 4.7 / 37 / 44). Walk and flight fell too, on every column but max.
- **At most one ratio switch: NOT MET.** The turn switched twice (0.72–1), the walk three times, and the flight once. T-2829's ladder fix was meant to stop at a step that buys nothing; these steps did buy something (median and p95 down on every move), so the ladder is stepping on purpose. The criterion was a prediction from T-2829's model, not a requirement the owner set.
- **Frames over 50 ms on a switch:** turn 0, walk 1 of 9, flight 0. The 1904 reading (T-2719, same session) had 2 of the >50 on a switch on its walk and its flight. So a resize is sometimes a hitch on this phone, and on 1835 it is rare.
- **Paced 9 % on the turn**, where T-2829's model predicted about 0 %.
- **Default: Adaptive stays.** It beats Fixed on sd and p95 in every move in 1835, and the switch count is a cost it is paying for that.
- Note: Fixed itself read rougher than on 2026-10-19 (turn sd 7.1 against 4.7, now over 15 s a mode against 5 s), so a like-for-like comparison is today's two rows, not yesterday's.
