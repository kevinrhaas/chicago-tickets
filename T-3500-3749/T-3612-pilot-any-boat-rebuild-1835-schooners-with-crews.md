---
id: T-3612
title: Pilot any boat; rebuild 1835 schooners with crews and circuits; 1812 trade boats; boats by season
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: 2026-11-16
pr: 2107
claimed_by: run 11/16/2026, 3:37:33 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-16T13:44:07Z
claimed_run: null
claimed_at: 2026-11-16T09:37:34.221Z
decision: null
decision_answer: null
---

Pilot any boat; rebuild 1835 schooners with crews and circuits; 1812 trade boats; boats by season.

Kevin, 2026-11-16 (thread "Pilot boats and rebuild 1835 schooners"), verbatim: "We have those boats in the river that we can ride and cross I would also like you to have the option to drive the boat on your own and pilot each boat down the river or in the lake. Also the schooners boats in 1835 we're not realistic they should phot match correct boats for 1835 with realistic wood and working crews on the boats, which some may be anchored but others move down and around the river up or down river making a circuit in and up or out to lake paths, there are 1835 boats but also I would think there could be some boats correct for 1812 too, of corkscrew handle scene logically with time of day and season on boats and jaunts if there are boats be reasonable and include them. Would be nice if I can board and pilot the schooners and all boats"

**Acceptance:**
- Every boat in 1812 and 1835 (crossing boats, skiffs, canoes, schooners, the new 1812 trade boats) can be boarded and piloted by the visitor on the river and out on the lake, with a way to step ashore.
- The 1835 schooners are rebuilt to match the period's pictures of Chicago's lake schooners (Andreas 1884 p.631 plate), with planked and painted wood, rigging and sails, and crews aboard.
- Some schooners lie moored or anchored; others sail circuits down the river, out through the harbour cut to the lake and back.
- 1812 gets period trade boats (Mackinaw boats, a bateau) and a lake vessel anchored off the bar when one would be there.
- Boats follow the hour and the season: laid up in winter, at anchor by night; jaunts at the water see them.

## Follow-up, 2026-11-21: water inside the boats you steer (PR #2286)

Kevin, 2026-11-21 (iPhone Chrome, dev preview, 1812 fort tour, stop 12 "Across the river"): "Water in the boat when I went for a ride".

- **Cause:** the boat at that stop is the garrison's scow (bateau). The trade boats and the 1835 rowboat/canoe in `vessel-model.js` laid their depth-only water lid 4 mm over the waterline, and `vessels.js ride()` heaves a piloted boat about ±2 cm in the river, so the lid went under and the river drew between the floorboards. It was not a T-3518 regression: the 12 crossing boats already lay their lid at the gunwale and stay dry.
- **Fix (PR #2286):** the lid now lies 3 cm under the sheer (`gunwaleLid`), and moored boats keep their berths clear of reeds (the scow lay in the reed bed). `test_vessels.mjs` checks the lid stays dry at the worst ride pose, which the old lid fails by 0.22 m.
- **Every 1812 boat a visitor or jaunt can ride:** the scow and the Kinzies' Mackinaw boat are fixed here; the 12 crossing boats (6 dugouts, 4 bark canoes, 2 skiffs) were already dry.

Garrison's scow at the helm, desktop and phone (before left, after right):

![desktop scow before and after](https://github.com/kevinrhaas/chicago-evidence/blob/0a223dbe8abe789058c669a737060d0d0862c6c5/evidence/1812-boats-dry-T-3612/desktop-garrison-before-after.jpg?raw=true)

![phone scow before and after](https://github.com/kevinrhaas/chicago-evidence/blob/0a223dbe8abe789058c669a737060d0d0862c6c5/evidence/1812-boats-dry-T-3612/mobile-garrison-before-after.jpg?raw=true)
