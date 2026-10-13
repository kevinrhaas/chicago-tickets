---
id: T-2490
title: 1812: build the Potawatomi lodges at their documented camping place on the south bank by the later State Street bridge, and date the camp of the 12-16 August gathering from Wau-Bun
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

1812: build the Potawatomi lodges at their documented camping place on the south bank by the later State Street bridge, and date the camp of the 12-16 August gathering from Wau-Bun.

## The owner's ruling (2026-10-13, project thread "1812 structures")

> You can include native lodges as documented

This extends his 2026-09-17 ruling (AGENTS.md, standing constraint: Native and Métis people are reconstructed, evidence-bounded) to the 1812 built environment: Potawatomi lodges stand in the 1812 scene where and when a source puts them. The PR adds this ruling, verbatim, to AGENTS.md's standing-constraint section. Unchanged: no human figure is drawn (L1), no invented ceremony, dialogue or depiction, every lodge record carries `review_required` and `touches_removal` with its own sentence, and the 1812 scene stays unreleased until the review by Native scholars or community organisations (T-0472).

## What the sources document

- **The habitual camping place.** Currey 1912, ch. II, p. 68: the Potawatomi near the fort "lived in their wigwams near the river", "their favorite camping place being at a point on the south bank near the present State Street bridge. A swale or gully opened into the river there, reaching back as far as the present line of Randolph Street"; p. 63: other tribes came as "occasional parties camping in their wigwams on the banks of the river near the fort". (Currey is tier 4 and needs a source record; see the shared section.)
- **The camp of the August gathering.** Wau-Bun ch. XVIII: after Winnemeg brought Hull's order on 7 August, "the Indians being assembled from the neighboring villages, a council was held with them on the afternoon of the 12th". Ch. XIX, Mrs. Helm's narrative of 15 August: "back towards the Chicago River, along the southern bank of which was the Pottowattamie encampment", "one of the wigwams", "a stream that flowed near" (footnote 36: "Along the present State Street"); and "the Indian camp, near the fort, where had been left their squaws and children" (`kinzie_waubun_1856`). The two sources agree on the place: the south bank at the stream or swale by the later State Street.
- **The ground.** The swale is on the 1812 ground; check `data/terrain/epochs/e1830_natural/` for it and draw the camp on its banks, not in it. Position is a stated reading of "near the present State Street bridge" against this project's State Street line, never a pin.

## The date, and the default this ticket takes

The scene is dated 1 August 1812 (T-2050). The large camp is documented only from the gathering (assembled by the 12th) to the burning of the 16th, so it is dated `1812-08-12..1812-08-16` in the data and does NOT stand on 1 August (AGENTS.md rule 3). On 1 August the scene shows the habitual camping place with a few lodges, graded `inferred` from Currey's "favorite camping place" (the note says the occupation on that day is not attested). The number of lodges in either state is a liberty. Whether the scene's date should move to the gathering is the owner's call (asked on the thread's decision card); if he moves it, this ticket follows the new date.

## How the lodges are built

Form from the sources, not from a generic tipi: read what the corpus says about Potawatomi summer lodges and wigwams (bark or rush-mat covering on a bent-pole frame; Wau-Bun describes the mats the women made "of which the squaws manufacture the coarse matting used in covering their wigwams"). Moses and Kirkland's buffalo-hide "teepees" (v1 p. 32, lines 5120-5125) are the 1895 author imagining 1803, and are not used. Every dimension and covering is a liberty with its reasoning. A new archetype, if one is needed, is engine-neutral and generated from data like every other structure (AGENTS.md rules 4 and 5). Cards say what the lodges are, whose camp it was by the sources' own words, and what is reconstructed, and they carry the review flag.

No picture of the 1812 camp is known. If the run finds one (the Kirkland 1893 and Currey 1912 plates are the places to look), it is image-gated.

**Acceptance:** on 1 August a few lodges stand at the camping place by the State Street swale, graded inferred, and the gathering's camp records exist dated 12-16 August; every lodge record has `review_required` and `touches_removal` with its sentence (`tools/measure_review_constraint.py` passes); AGENTS.md carries the ruling; no human figure anywhere; desktop and 390x780 shots; the scene stays unreleased.
