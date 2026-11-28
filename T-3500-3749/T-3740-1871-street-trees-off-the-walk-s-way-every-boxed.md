---
id: T-3740
title: 1871 street trees off the walk's way: every boxed tree clear of corner crossings, doorways, gates and stoops, and the planter refuses one that is not
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-23
closed: null
pr: null
claimed_by: Better Trees refinement 11/28/2026, 5:53:08 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-28T11:53:09.273Z
decision: null
decision_answer: null
group: T-3740,T-3833,T-3834,T-3835
---

1871 street trees off the walk's way: every boxed tree clear of corner crossings, doorways, gates and stoops, and the planter refuses one that is not.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. Audit the 1871 street-tree boxes against crossings, usable walk routes, door landings, gates and stoops, beginning at the Water Tower. Record actual affected ids and geometry/data locators; the planter refuses demonstrably obstructing boxes consistently in every detail tier.
2. Read the Water Tower reference images themselves. Distinguish the intended 1866–67 setting, the post-fire 1871 photograph and the later 1890 grounds; do not use post-fire absence as evidence of pre-fire absence or promote reconstructed planting to attested.
3. Show the resulting Water Tower and representative street clearances in fixed published desktop/phone views in all four seasons. Keep supported planting and historical cards/grades intact; explain each relocation or removal and its reconstruction bounds.
4. Full Native, appropriate published phone/desktop smoke, original performance policy and current-Dev preflight pass before a green Dev merge.

## Work available on a branch (loop, 2026-11-28)

A loop slice built this a minute before the "Better Trees refinement" claim landed, then stood down rather than race it. The work is on `steward/t3740-1871-trees-off-ways` (head e8be5df0b7, unmerged, no PR; liberties.json re-derived): https://github.com/kevinrhaas/chicago/compare/dev...steward/t3740-1871-trees-off-ways — take it or leave it.

- `tools/lay_1871_street_furniture.py` `house_ways` puts every house's way in on its walk (13,622 houses front a walk; `yard_m` is the front's setback to 5 cm): the stand-in's steps or porch at the front's middle (`city_context_emit.py` `entrance`, scaled as city-context.js scales the kit) and the detail's door or front-yard gate on the middle bay's line (city-fronts.js).
- The planter moves a box before a way in, on a board crossing or against a post or the kerb's dress to the nearest clear spot within 4.2 m: 807 of 6,693 moved, none dropped, the young share unchanged. `check_trees` refuses a planting that breaks any of it; `--self-test` proves five refusals (gate, steps, crossing, corner, lamp). `data/street_furniture/1871.json` is byte-identical.
- `--check` and `--self-test` pass locally; check.sh parts and the smoke were NOT run on it.


**Owner follow-up, 2026-11-28:** after the completed Better Trees merge, the owner approved the proposed placement, natural forms, close detail, all-season progression and motion/distance refinement with “Go for it”. This is a related four-ticket group under T-3740, not a repeat of the completed T-3747/T-3748/T-3760 work.
