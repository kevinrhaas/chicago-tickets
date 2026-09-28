---
id: T-1730
title: Alternate versions of the Glessner House for the owner's side-by-side comparison: each an independent build from the same sources, registered as a structure version
state: open
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: null
claimed_by: null
blocked_on: T-1732
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Alternate versions of the Glessner House for the owner's side-by-side comparison: each an independent build from the same sources, registered as a structure version.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 142 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked for the 1904 Prairie Avenue / Glessner House render path, 2026-09-28

Source library: **`chicago/prairie_1904_v1/`**, viewable at https://chicago.polecat.live/prairie-1904/viewer/. Read its README and `docs/research-gaps.md` first; cite library rows and dossier entries by id.

**Why (owner, 2026-09-28):** *"do different renders of the glessner house and test them out … see a
version of the glessner house … and then … a different one from a different model run and then
make a final call and push one of those … to dev and then to main."*

**How it works:** each run takes this ticket and builds **one independent version** of the Glessner
House from the same sources as T-1729, without copying T-1729's geometry. It registers the version
through **T-1727**'s mechanism under a neutral label (`v2`, `v3`, …; **never a model identifier**),
merges to **dev**, and posts its compare URL in the PR:

    https://chicago.polecat.live/4d/dev/1904/?anchor=glessner_house&structure=glessner_house&version=<label>

The default (T-1729's build) is the same URL without `&version=`.

**Acceptance per version:** (one demonstration, never weakened to pass)

1. Built from the T-1729 source set, each attribute tiered and cited. Where it reads a source
   differently from the default, the PR names the difference and the source, since that is what
   the owner is comparing.
2. Registered as a version, baked, `validate.py --stale` green. The default is untouched.
3. Screenshots from the `glessner_house` anchor at both viewports, next to the default's, go in the
   PR.
4. **This ticket stays open while the owner is still comparing.** Each run adds a version and moves
   this ticket back to `open`. The owner closes the round by choosing a label. That becomes one PR
   running `tools/promote_version.mjs glessner_house <label>` (T-1727) into dev, and then main on
   his dispatch of the promote workflow.

Blocked on **T-1729** (the default to compare against) and **T-1727** (the version mechanism).

**Repointed 2026-09-28:** T-1729 was split into T-1731 (the exterior specification) and T-1732
(place and bake the default version). The default this ticket compares against is **T-1732**'s
build, so `blocked_on` now names T-1732; each alternate version may read T-1731's spec as part of
the shared source set but must not copy T-1732's geometry.

