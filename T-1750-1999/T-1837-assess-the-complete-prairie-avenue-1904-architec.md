---
id: T-1837
title: Assess the complete Prairie Avenue 1904 architectural asset programme
state: split
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-01
closed: 2026-10-01
pr: null
claimed_by: interactive architectural study
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T02:02:34.100Z
claimed_run: null
claimed_at: 2026-10-02T01:41:36.141Z
decision: null
decision_answer: null
---

Owner request, 2026-10-01: assess all remaining Prairie Avenue structures and shared architectural elements for photographic-quality reconstruction matching Glessner; create a staged ticket programme. Infer missing detail from maps and photographs with declared reconstruction.

**Acceptance:** publish a source-pinned architectural study; reconcile all 62 named records and 91 map frontages; specify reusable components, per-building distinctive features, uncertain phases and rear structures; file bounded dependent implementation tickets with complete coverage and preserve the existing construction hold.

This is a planning and ticketing task. No renderer or model change is claimed. The existing T-0475/T-0476/T-0477 construction hold remains in force.

**Filing over budget:** the owner explicitly requested this multi-ticket architectural programme. Child work will be staged under the held Prairie programme without reordering unrelated work.

## Assessment delivered; implementation split into staged children

The [architectural study](../evidence/T-1837-prairie-1904-architectural-study/README.md) is complete. Its [ticket plan](../evidence/T-1837-prairie-1904-architectural-study/TICKET-PLAN.md) assigns **110 children, T-1840 through T-1949**: 3 sheet reconciliations, 16 shared component systems, 73 front-building packages, 7 rear/service packages, 4 adjacent-context packages, 4 streetscape packages and 3 block acceptance packages.

Coverage was verified against all **62 named records, 91 map-frontage rows and 92 viewer parcels**. These are distinct source enumerations, not 91 proven unique houses. Rear/service and additional visible background polygons have explicit census/build owners; their exact unique-building totals remain unresolved. Allerton/address aliases, Keith photograph attribution, altered mansions, Robbins completion date and the Rees shared coach house are called out individually.

The live viewer library and image data match the pinned code snapshot by SHA-256. The study includes specific architectural briefs, source/image handles, per-attribute inference rules, material/geometry/export requirements and Glessner comparison/whole-block browser acceptance.

`split` records that the requested planning result has been delivered and its future implementation belongs to these children. It does **not** claim that models were built or that a code PR merged. The existing construction hold and the owner's queue order are preserved. The user explicitly requested the many-ticket decomposition, authorizing this filing beyond normal incidental-ticket limits.

## Owner resumed and queued the programme — 2026-10-01

Owner: “Go”, then “Push the tickets to dev queue in one group below”. The inherited construction hold is lifted for all 110 implementation tickets, T-1840–T-1949. They are open in one contiguous, dependency-ordered group at the bottom of the dev queue. Existing unrelated queue rows retain their order. The legacy umbrella tickets remain scope references; execute the named child packages and their dependencies, not duplicate umbrella builds.
