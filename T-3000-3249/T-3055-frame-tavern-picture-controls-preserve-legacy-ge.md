---
id: T-3055
title: Frame-tavern picture controls preserve legacy geometry
state: review
epic: TOWN
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: T-2376
opened: 2026-10-23
closed: null
pr: 1239
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
group: T-3055,T-3056
---

Frame-tavern picture controls preserve legacy geometry.

Proposed parent metadata: `parent: T-2376` (must be added explicitly after `new`;
`new --parent` is unsupported). Also serves T-2383 and T-2385.

Green Tree's seven-bay eaves facade, the Sauganash gable openings, and Tremont's
three-storey/shuttered/raised-entry form cannot be expressed faithfully by the
existing consumed parameter set. Add the missing opt-in controls in the shared
frame-tavern parameter/builder path, retaining every pre-existing default. This
is a generator prerequisite, not a declaration that any building matches all its
pictures. Source-shaped building refinements and their unresolved differences
remain owned by the original image-match cases.

Sources: `andreas_1884_green_tree_hotel_plate`,
`andreas_1884_sauganash_hotel_plate`, and `gifford_tremont_house_no_1`.
Use the actual images and their recorded source/rights/date limits; do not turn
monochrome tone or a retrospective view into attested dimensions. The Tremont
reference-use approval belongs to T-3053 and is not re-decided here.

**Acceptance:** existing default controls resolve identically and preserve their
geometry; opted-in fixtures exercise explicit bay counts, gable treatment and the
actual supplied picture features, with malformed values refused. Demonstrate
finite nondegenerate geometry, supported confidence channels, rebuilt freshness
for any affected committed assets, and desktop/mobile zero-error loading for the
resulting generator path. Document the exact input-hash/bake blast radius. No
assertion is weakened. Record the actual fixture/render evidence and its limits.

This ticket can close only for the finished shared tool capability. It does not
close or replace T-2376, T-2383 or T-2385, cannot claim their image verdicts are
matches, and must not be used to relabel unfinished building refinements as done.
If its real scope instead becomes drafting/refining those buildings, add their
Image gates and meet them before calling the ticket complete.


## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> Green Tree, Sauganash and Tremont picture work needs consumed bay, gable and corner-elevation controls with preserved defaults; this closes only the shared generator prerequisite, never the original image gates

**Released 2026-10-23** (claim of Codex frame generator and church source prerequisites; continuing own work 10/23/2026, 8:55:28 AM CT): Owner requested session wrap. Canonical work is pushed at 792598d88056dbc768bb5062258a803c6a62524b in draft resume PR https://github.com/kevinrhaas/chicago/pull/1239 . Exact corrected local1056PASS and source-tree/commit proof archived at https://github.com/kevinrhaas/chicago-evidence/blob/3575ef6/evidence/image-match-2026-10-22/final-parallel-recovery-20261023T1430/RECOVERY.md . Resume the existing PR after Hogan1229, merge current dev and finish final published desktop/mobile coverage before merging. This release does not mark prerequisite or original picture work done.
