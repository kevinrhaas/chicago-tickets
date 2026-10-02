---
id: T-1978
title: The distant treeline wobbles and cuts down along Lake Street
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: null
pr: 287
claimed_by: run 10/2/2026, 10:17:20 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-02T15:17:20.018Z
decision: null
decision_answer: null
---

The distant treeline wobbles and cuts down along Lake Street.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 249 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The owner asked for this to be filed and worked now, from three screenshots on dev looking west down Lake Street toward Clark; T-0120 (the earlier treeline ticket) is done, so there is no open ticket to add it to.

**The owner, 2026-10-02, on dev at /4d/dev/1835/, on Lake Street approaching Clark, facing W 272°:**
*"at this angle the horizon tree line top is still wobbly up and down and there is a big cut down
and highly visible because its so wobbly in the distance, it probably should be much less wobble if
any at this distance, be more stable and lower, this happens all down lake, but please walk and horse
and wagon and fly the streets and common perspectives and correct this"*

His frame shows the horizon band (`trees.js` § 5, `horizon-timber`) behind the Lake Street houses
as a tall dark-green silhouette with crown-sized bumps and one deep notch — it reads as a range of
hills, not a far treeline.

**Acceptance:**
1. The band's crown/gap texture is anchored to the WORLD (the body's own path), not to
   bearing × distance from the eye, so walking, the wagon and fly do not re-randomise the
   silhouette between re-solves.
2. The texture's amplitude falls with distance: a body past about a kilometre draws a
   near-level top with no deep notches; the near treelines keep their gaps.
3. The far silhouette stands lower than on dev at the Lake & Clark stand facing west, measured
   in pixels from a before/after capture at the same pose.
4. Checked by capture walking Lake Street, on the wagon, and in fly, plus the common anchors;
   `check.sh` green and the smoke by parts green, mobile included.
