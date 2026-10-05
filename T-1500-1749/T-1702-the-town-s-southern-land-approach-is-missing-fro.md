---
id: T-1702
title: The town's southern land approach is missing from the street layer: the located State road from Vincennes over Hubbard's Trail reaches the modelled ground and no corridor carries it
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 10/4/2026, 7:03:59 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37245756008
claimed_at: 2026-10-05T00:03:59.736Z
decision: null
decision_answer: null
---

The town's southern land approach is missing from the street layer: the located State road from Vincennes over Hubbard's Trail reaches the modelled ground and no corridor carries it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. The three Hubbard readings T-1587 ruled `aggregate_only` — `hubbard_autobiography_1911#bk_hub_011`,
   `#bk_hub_082` and `#bk_hub_083` — are re-read with the committed ground in front of them, and the
   located State road either gets a record in `data/streets/1835.json` reaching the modelled box's
   south edge, or the absence is refused in writing with the reason.
2. Whatever is committed states which line it stands on and at what tier. A trail is not a platted
   corridor: if the approach is drawn it is drawn as a travelled line with `opened`/`worn` and a
   geometry grade that says honestly how the alignment was arrived at, and any invention is recorded
   in `docs/LIBERTIES.md`.
3. `tools/check.sh` is green and the PR states what moved.

## Why this ticket exists

T-1587 spent the 18 unasserted `street` readings and three of them turned out to be about the same
absence rather than about each other. Hubbard's Trail was, in his own words, 'the only well-defined
road between Chicago and the Wabash country'; in the winter of 1833-34 the General Assembly ordered a
State road located from Vincennes to Chicago with mile-stones on it, and from Danville north the
Commissioners adopted the trail for most of the way. So on 1 July 1835 the town's principal land
connection to the south-east was a LOCATED STATE ROAD and had been for about eighteen months.

`data/streets/1835.json` holds no southern land approach at all. `state` is drawn from local N -400
to +20 and stops; the four named School Section tiers are `platted, unopened, unworn` with a zero
track; nothing anywhere in the file carries a trail, a State road, or any travelled line entering the
modelled ground from the south. Three readings therefore reach the ground and find nothing on it to
reach — which is a finding about the street layer, not a gap in the readings, and T-1587 refused to
invent an alignment to give them an end.

It is filed rather than absorbed because the answer might well be the refusal: this project does not
rule a line across ground nobody has read, and the ground between the platted town and the section
line south of it is the same Washington-to-Madison tier T-0858 has open and unread.
