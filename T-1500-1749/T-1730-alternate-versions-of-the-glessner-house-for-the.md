---
id: T-1730
title: Alternate versions of the Glessner House for the owner's side-by-side comparison: each an independent build from the same sources, registered as a structure version
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-09-30
pr: 202
claimed_by: steward/glessner-v4-default
blocked_on: null
needs_bake: true
closed_at: 2026-09-30T13:26:47Z
claimed_run: null
claimed_at: 2026-09-29T21:10:00Z
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


## Owner-directed v4, 2026-09-29 — in progress

The owner explicitly asks to use the default as v4's reference; this supersedes the earlier independent-geometry requirement for this version. Keep default/v2/v3 available. Claim: steward/glessner-v4.

Implement and visually verify intersecting east/west gables, west-wing south and courtyard windows, garden-level openings on north/east/west courtyard faces, the continuous northeast copper roof and north-wing return, variable-height rock-faced granite street elevations, brick courtyard walls with stone window surrounds, and east-wing chimneys against HABS. References: HABS/source library plus six owner-supplied images (Pasted Graphic 14–19). Modern imagery informs visible form only; textures are original or licensed, and differences inferred for 1904 are declared.

Acceptance: selectable baked v4, reference-matched views of every exterior/courtyard face and overhead, materially improved stone/brick/roof/window rendering, desktop/mobile evidence, project gates green, and an honest assessment against the owner's near-photographic target. Parallel evidence, geometry and materials work feeds one integrated version. Do not mark complete merely because data or tests pass.

## Owner selection, 2026-09-29

Owner selected v4 as the default in dev and explicitly requested promotion of dev to main production. PR #201 is merged with 712 gate steps and both complete viewport smokes green. Finish the package-aware default promotion in steward/glessner-v4-default, preserve the prior default as pre-v4 and v2/v3, verify the new default at both detail profiles, then use the production workflow after the dev gate passes. Browser workflow dispatch authorized by the owner.

Owner rights ruling, 2026-09-29: “Yes, leave them with rights unresolved.” Retain the courtyard-photo cross-checks in canonical form.detail_profile and form.v4_detail as a documented project-policy exception. Source habs_glessner_photo_05_court_c1923 remains check_required; no license clearance is claimed and no photographic pixels are used as textures. The two new canonical references are recorded through measure_rights_derivation.py --update, with no added unresolved sources.
