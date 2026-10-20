---
id: T-2894
title: The near ring's mid cards on the GPU's deal (fringe, inner handover and census), so a near pass no longer walks the mid ring on the CPU; read with measure_walk_frames.mjs's near re-deal line and the CPU profile at the throttled phone profile, with the near re-deal line's pass count fixed to agree with the near rebuild count first
state: done
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2774
opened: 2026-10-19
closed: 2026-10-20
pr: 1135
claimed_by: run 10/20/2026, 4:14:34 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-20T13:37:58Z
claimed_run: null
claimed_at: 2026-10-20T09:14:34.941Z
decision: null
decision_answer: null
---

The near ring's mid cards on the GPU's deal (fringe, inner handover and census), so a near pass no longer walks the mid ring on the CPU; read with measure_walk_frames.mjs's near re-deal line and the CPU profile at the throttled phone profile, with the near re-deal line's pass count fixed to agree with the near rebuild count first.

Piece 2 of 4 of **T-2774 — The near ring's remaining sets on the GPU, so the near re-deal reaches zero: the heads hung from the GPU's deal and the CPU near walk retired (T-2717 read it unchanged at 2.6-3.4 ms a pass, because it still deals every near slot for the heads), then mid, forbs and far shrubs, each read with measure_walk_frames.mjs's near re-deal line at the throttled phone profile**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2774 was split (2026-10-20T01:31:29.358Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 34m ago, run 10/19/2026, 7:57:39 PM CT — held by the run that split it
- PR #1112 on claude/loop-optimization-tickets-mmvcns — T-2829, T-2606, T-2774, T-2824, T-2723: performance and GPU batch — phone pacing, boot GL errors, flora and gaze-pick stalls — held by the run that split it

The run that split it (by hand) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
