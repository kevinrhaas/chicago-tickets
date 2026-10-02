---
id: T-1984
title: Storefronts on the walk: nothing stands in a doorway, no sign covers a door or window, no door merges with a window, and the ground at every entrance is trodden
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: 2026-10-02
pr: 291
claimed_by: run 10/2/2026, 11:19:55 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-02T20:21:47Z
claimed_run: null
claimed_at: 2026-10-02T16:19:55.232Z
decision: null
decision_answer: null
---

Storefronts on the walk: nothing stands in a doorway, no sign covers a door or window, no door merges with a window, and the ground at every entrance is trodden.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 251 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-reported from walking dev on 2026-10-02 with five screenshots; one ticket for the four faults of one report rather than four lines, under the queue ceiling

## The owner's report (2026-10-02, walking Lake Street on dev, five screenshots)

> when i walk the town, often i will see goods or furntiture in front of doors, or signs in front of doors or windows (not ones that might be hanging in front of windows but ones where the sign is on the face of the building and it covers a window or door, you should resize the sign and put it above or move it to an open space on the face of the structure and there are many case like these ones where the door and windows are merged? and also in and around in front of buildings there is prairie grass, that would be worn down and not be wild prairie right in front of the entrance to buildings

## Causes found (before any fix)

1. **Merged openings.** `frame_storefront_params.front_window_rects` sets out the ground-storey windows of a store with NO shopfront by bay count alone, and `plain_door_rect` centres the door on the same front without either asking the other — so on 11 plain stores (`inf_bakery_lake`, `inf_barber_shop`, `inf_butcher_market`, …) a window overlaps the door and the two holes draw as one notched opening. Four `single_pen` cottages (`inf_artisan_dwelling_west_a/b`, `inf_packer_dwelling`, `inf_sawyer_dwelling_a`) have two windows clamped 3 cm apart by `frame_dwelling._snap`.
2. **Signs over doors.** `tools/generate_business_signboards.py::_fit_flat`'s last move was "shrink it onto the door" — 12 flat boards are fixed to the door leaf (W. G. Blanchard among them) because the move and reshape found no full-size blank face.
3. **Steps not at the door.** `generate_frontage_works.FIT_DOOR_ALONG = 0.5` — "the door is not on any record: the middle of the front" — but the door IS on the record since T-0459/T-0520 (`facade_openings`); on a shopfront the door is off-centre, so the stoop lands in front of the show window.
4. **Prairie at the door.** Nothing asks where a door is before planting the sward; only fenced yards, streets and the strip suppress it.

**Acceptance:** (1) no two holes on any read front overlap or stand under 0.15 m apart, held by a gate; the affected stores and cottages rebaked. (2) No flat-mounted sign overlaps a door or window: a board that cannot stand clear at full size is lettered on the shop's fascia or shrunk onto clear face, never the leaf; held by the generator's own check. (3) Every door the town's readers know is listed once with its world position; the stoop stands at the door, and no fitting, good, planting or prop stands in a door's approach, held by a sweep. (4) A trodden-earth apron at every listed entrance suppresses the sward. Checked by walking Lake and South Water with screenshots.
