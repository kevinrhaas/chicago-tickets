---
id: T-1214
title: Build the camps of the summer of 1835: a tent and wagon-camp archetype, the encampments on the grounds the transient ticket evidenced — the land-sale crowd south of the fort, the immigrants' wagons at the west approach, the pier gang at the river mouth — bounded, labelled, and empty of figures
state: split
epic: TOWN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-16
closed: 2026-10-01
pr: null
claimed_by: run 10/1/2026, 8:23:42 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-01T13:27:34.007Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36867717332
claimed_at: 2026-10-01T13:23:42.965Z
decision: null
decision_answer: null
---

No tent, encampment, wagon camp or lodge exists in any form: no record, no archetype
(`generators/archetypes/` has nine), no family, no exclusion, no liberty. T-1178 wrote
the people and the candidate grounds (`1835_camp_grounds.json`); this ticket gives them ground
and canvas. Native and Métis camps of families in town to trade or awaiting the annuity payment are IN
scope on the owner's 2026-09-17 ruling — sized and placed from T-1177's evidence, every such
record `review_required` + `touches_removal`, a lodge form added to the archetype only where a
source describes one; the August 1835 gathering is weeks after the scene date and is NOT
staged (AGENTS.md § Standing constraint, restated on every record).

**Acceptance:**

- A `camp` archetype (`generators/archetypes/camp.py` + `camp_params.py`): wall/wedge tents on
  poles, a covered wagon (the box and bows), a brush shelter, a cooking fire ring and a woodpile,
  parameters for count, arrangement (row, ring, scatter), canvas condition; `CONSUMED`,
  `GROUND_CONTACT`, `CONFIDENCE_VALUE` like its siblings; a family code added to the inventory
  (`X1 camp`) with a target from the transient bracket; the schema's `archetype` enum extended.
- Records placed on the camp grounds by T-1199's rows, tested for dry ground, outside
  every corridor and no-build region except where a region permits (`fort_dearborn_reservation`
  `permitted[]` — the lake shore south of the fort is a decision the record states), each with
  `occupants` = the transient party and the evidence sentence that put a camp there.
- Bake (`needs_bake: true`); `smoke_renderer.mjs` at both viewports; LIBERTIES entry with scope;
  L1 restated — no figure, no smoke-as-a-person, canvas and wagons only.
- **Visible:** a screenshot from the fort's south-west corner shows the camp on the shore.

**Stop condition:** every transient party has a camp to be counted at, and the camps read as
the summer of the land sale.

**Links:** T-1178 · T-1199 · `data/reconstruction/1835_no_build_ground.json` ·
AGENTS.md § Standing constraint · L1.

## Handed on from T-1808 (2026-10-02): what the boarding houses leave behind
T-1209's last books piece (T-1808, PR #256) closed the Washington-tier keeper seam: the lodgers
stage now reads a platted adoption under `lodging_near_the_landings` as the house's keeper, so
any house T-1950..T-1953 raise for a banded keeper is kept by that household with no keeper drawn.
The remaining H3 boarding houses are those four tickets'. Carried here for the camps' own frame
read: on the published tree at dev@d4fbc4a5 all three detail tiers read OVER their ceilings at
desktop (full 1,516,064 / 1,460,000 at Lake and Canal; balanced 1,330,437 / 1,280,000; light
885,296 / 825,000 at the forks — `docs/measurements/t-1808-detail-ceilings-desktop.json`).
Price the camps with `measure_detail_ceilings.mjs --price` before they deal.
