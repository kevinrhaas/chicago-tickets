---
id: T-1790
title: Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: parallel people motion 10/18/2026, 10:06:49 PM CT
blocked_on: T-1789
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T03:06:49.232Z
decision: null
decision_answer: null
---

Give the shared Blender rig a small reusable animation vocabulary before multiplying
historical people. Implementation target: `kevinrhaas/chicago` **dev**.

**Acceptance:**

- Author or legally source and retarget a bounded first library on the T-1786 skeleton:
  neutral idle, alternate idle, walk, conversational/talk loop, greeting/point gesture,
  carry/hold and one simple period-neutral work motion. Root-motion policy is explicit.
- Clips loop cleanly where intended, keep feet planted, preserve plausible human scale and
  avoid modern-character mannerisms that visibly fight the 1835 scene. Historical-specific
  gestures are not asserted without evidence.
- Export all clips through T-1787 and prove they play through T-1788. One actor can change
  idle -> walk -> idle -> gesture without reload or skeleton replacement.
- Define lightweight facial behavior using the portable morph set where present: blink,
  jaw/open-close and a small expression set. Keep lip-sync hooks possible without making
  audio, an AI service or Unreal facial tooling a dependency.
- Include animation metadata for duration, looping, root motion, compatible LODs and tags
  so behavior can select clips by meaning rather than filename hacks.
- Measure CPU/frame impact for one animated close actor and a small group; record which
  features may be disabled at lower LODs.

**Stop condition:** named people can share one animation library in Blender and the browser
instead of embedding bespoke actions in every character file.

## Parallel checkpoint — 2026-10-19

Named-person source motion/CI authoring parcel is being archived; actual BPy/export, loaded contact and scene acceptance remain pending T1789. No anonymous replacement. See evidence/period-transport-2026-10-18/parallel-refinement-2026-10-19/ and CHECKPOINT.md. PR1041 remains draft; conditional dev merge awaits green final-head gates.
