---
id: T-2823
title: Anonymous adult fallback role identities: period-qualified profiles and actor selection without invented residents
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: null
pr: 1041
claimed_by: resident-fallback 10/18/2026, 4:38:54 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T21:38:54.211Z
decision: null
decision_answer: null
---

Anonymous adult role identities: period-qualified profiles and actor selection without invented residents.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 159 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner explicitly requested generic adult drivers, riders, standing and walking figures on 2026-10-18, independent of Mark Beaubien; this additive identity contract must precede modular population work in band 8C.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Owner steering and scope (2026-10-18)

Prefer existing attested, inferred or reconstructed people as reference/model; generic adults are only a documented fallback when no suitable person is available. This additive path does not replace named residents or require Mark Beaubien to be the first technical benchmark. Implementation target: kevinrhaas/chicago dev.

## Acceptance

- Add mutually exclusive canonical person and anonymous adult role-profile identity paths; anonymous use never creates a person record/card or asserts an attested likeness.
- Fallback instances state why no suitable existing person serves, and list considered person IDs that resolve in the scene. Profiles are explicitly fallback-only.
- Enforce profile role/date and accepted asset/wardrobe date separately; initial 1812/1835/1904 profiles have no accepted assets. No production instances or placements.
- Preserve named review metadata and existing resident-card selection. Anonymous selection emits an explicit reconstructed role card with personId null and instance-specific identity.
- Refuse wrong dates/wardrobes, fake resident-card requests, unreasoned fallback, nonexistent candidate people and duplicate instance IDs; permit separate instances sharing one profile.
- Validate contract/schema and actual browser selection at mobile/desktop. Mechanical test qualification is unpublished and never marks a model production-ready.

## Work started

Contract/runtime/profile validation and refusal tests implemented; production asset acceptance and scene placement remain outside this ticket. No photographic quality, wardrobe acceptance or completed population budget is claimed.


Combined source checkpoint: work now lives in PR1041 at9cc7b9ac8 (full local998/0 and postcommit checksPASS). PR1046 is a preserved authoring source checkpoint; canonical resident qualification remains pending, and this retarget does not close production acceptance.
