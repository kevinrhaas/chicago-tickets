---
id: T-1732
title: Place and bake the Glessner House on the T-0474 parcel and T-1252 ground as the default version, from the T-1729 exterior specification
state: done
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1729
opened: 2026-09-28
closed: 2026-09-28
pr: 188
claimed_by: run 9/28/2026, 9:22:42 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-29T04:50:35Z
claimed_run: null
claimed_at: 2026-09-29T02:22:42.973Z
decision: null
decision_answer: null
---

Place and bake the Glessner House on the T-0474 parcel and T-1252 ground as the default version, from the T-1729 exterior specification.

Piece 2 of 2 of **T-1729 — Build the Glessner House at 1800 Prairie as it stood in 1904: the first researched version, from the HABS drawings, the Sanborn 1911 sheet and the Prairie library's dossier**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The parent's acceptance items 1, 3 (as scene geometry), 4 and 5, built FROM T-1731's specification
(`docs/RESEARCH/glessner_house_1904.md`, `data/research/glessner_house_1904_spec.json`):

1. A structure record `glessner_house` at 1800 Prairie on the T-0474 parcel, standing on T-1252's
   ground, its footprint and heights taken from the T-1731 spec with the spec's per-attribute tiers
   and sources carried onto the record; any reconstructed value that becomes a scene claim gets its
   `docs/LIBERTIES.md` entry.
2. Seen from the T-1252 landing pose, recognisable against the 1888 plate and HABS photographs;
   screenshots at both viewports in the PR.
3. Baked, `validate.py --stale` green, frame budget measured.

Blocked on **T-0474** (the parcel) and needs **T-1252**'s ground. This is the DEFAULT version that
T-1730 compares against.

