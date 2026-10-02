---
id: T-1215
title: Converge the reconstructed town: every person housed, every business roofed, every roof occupied or its use stated, the census's dwellings ratio met, the programme reconciled, the budgets re-measured and set — the completion report a visitor can open
state: split
epic: TOWN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-16
closed: 2026-10-02
pr: null
claimed_by: run 10/2/2026, 7:27:00 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-02T12:28:11.645Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37006354978
claimed_at: 2026-10-02T12:27:00.190Z
decision: null
decision_answer: null
---

The closeout of the whole reconstruction. The owner's stop condition, verbatim: *"you must
complete all businesses and all structures, and all residences so that every person in Chicago
has a place to live and a place to work … your goal here is to complete the entire city with
reconstruction based on evidence."*

**Acceptance:**

1. **The join is total.** `tools/audit_town_completion_1835.py --check` (in `check.sh`): every
   person's `lives_at[]` resolves to a standing structure, a vessel or a camp; every working
   person's `works_at[]` to a standing structure, a vessel, a camp or a stated `no_fixed_premises`;
   every business's primary location to a standing structure or a stated street-only/unplaceable
   limit (the T-1147 limits preserved and printed); every structure carries `occupants` or a
   stated use (`vacant_to_let` per L167, `outbuilding_of: <id>`, `civic`); zero dangling ids.
2. **The numbers.** The town census screen shows: roofs standing = programme target (or the
   headroom and why); dwellings vs the census's 398 within the bracket; residents / transients /
   garrison; households housed = households; the order book reads filled in every bucket; the
   roof programme reconciles; `docs/RESEARCH/1835_town_completion.md` prints every table by tier
   (attested / inferred / reconstructed) for persons, households, businesses, structures, streets.
3. **Fixed point.** Every generator and derived layer re-derives drift-zero; every LIBERTIES
   entry's `Scope:` agrees with the compiler; `substitute_reconstruction.py` covers structures
   (a new attested roof retires the reconstructed one on its lot).
4. **The budgets, honestly.** `measure_detail_ceilings.mjs` on the published tree at every stand;
   the ceilings and draw-call budget set consciously where they are defined, with the reasoning,
   `light` inside its floor; T-1154's finding reconciled (its trim landed, or the re-budget
   stated in its ticket); `smoke_renderer.mjs` green at both viewports on the published tree;
   the boot payload within `measure_boot_payload.mjs`'s budget or re-set with the reason.
5. **Visible.** The "Reconstructing the town" card reads complete; a walk from the fort to Wolf
   Point along South Water, Lake and Canal Street with a screenshot at each stand, committed under
   `docs/RESEARCH/shots/`; `docs/STATUS.md` states what remains unverified.
6. **The gate screen** says the town is complete to the reconstruction of 2026-09 and names the
   three tiers' shares.

**Stop condition:** a visitor can walk the whole town and open any door, and every door has a
name, a trade, a family and a reason behind it — or an honest empty.

**Links:** every ticket in this band · T-1179 · T-1190 · T-1154 · T-1156 ·
`data/town_census.json`.

## Two findings from T-1713, the South Division's outer books (2026-09-28)

Added here rather than filed, on QUEUE.md's own rule — *"add a finding to the ticket it was
found in"*, and the queue stands at its ceiling. Both are convergence items: each is a
ground or a record that closes wrongly and would close a district's books on a false
number if it were not written down. The measurements are in
`data/render/south_outer_close_out.json`.

**1. `harmon_log_cabin` is seated inside the plat and its position note describes somewhere
else.** The record stands on `blk_randolph_franklin#02` — plat lot 3, fronting Randolph, a
platted lot of the Original Town, and the lot ledger records that it bars another roof
there. Its own `position_note` says it "sits in the South Division outer band", which is
not where it is, and that Harmon's pre-empted ground is "two kilometres south of the
modelled ground". Measured: Sixteenth Street at Prairie — the line his record names as that
ground's north boundary — stands at local **N -2949.59** and the box's south wall is at
**N -3800.0**, so that line has been **850.4 m INSIDE** the modelled ground since T-0464
carried the wall to Twenty-Second Street. The cabin stands **2 677.6 m north** of it. The
same stale sentence is carried in three committed files:
`data/structures/harmon_log_cabin.json`, `data/sidecars/1835/harmon_log_cabin.json` and
`data/reconstruction/1835_inferred_household_programme.json`. **T-1713 deliberately did not
move the record**: nothing in this corpus states LAND south of Twelfth Street (`evidence_limit`
writes every vertex below N -2149.40 conjectural, and the terrain spec calls the 1650 m
below it frame and not reconstruction), so re-seating him there trades an invention on
modelled ground for an invention on conjectural ground. What is owed is either a re-seating
argued on that trade or a note that says what is true.

**2. The Michigan Street tract is named by T-1203's ground list and carried by none of its
four pieces.** T-1203's body lists "the Michigan Street tract's five seated blocks" first
among the four grounds of the South Division's outer band. The other three are the titles of
T-1707/T-1708, T-1709 and T-1710; this one is in no piece's title. And
`docs/RESEARCH/michigan_st_tract.md` is titled *"The Michigan St tract north of Kinzie
Street"* and reads it off Wright's 1834 survey immediately north of Kinzie and east of the
North Branch — the **North** Division. So either the parent's ground list names a tract that
is not in its district, or a ground of this district has fallen between two tickets. T-1713
recorded it and adjudicated neither.
