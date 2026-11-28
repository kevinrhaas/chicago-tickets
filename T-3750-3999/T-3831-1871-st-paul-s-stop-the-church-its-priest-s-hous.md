---
id: T-3831
title: 1871 St. Paul's stop: the church, its priest's house and school, and Bateham's mills and kindling yard drawn as they were, not a brick block
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2439
claimed_by: run 11/28/2026, 1:19:52 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/46118910918
claimed_at: 2026-11-28T07:19:53.735Z
decision: null
decision_answer: null
---

1871 St. Paul's stop: the church, its priest's house and school, and Bateham's mills and kindling yard drawn as they were, not a brick block.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Kevin, 2026-11-28 (thread "Bring 1871 fire-night crowds and scenes to life"), of the T-3814 picture of the St. Paul's stop: *"Did st pauls really look like that? I think you have a brick square building on fire that and it seems odd to me"*

**What is drawn now:** no church. The burning building in the stop's view is a generic three-storey brick commercial block from the 1871 background fill (`data/context/1871.json` `context1871_core_0177_014_n_02`, kit `commercial_3`, district `river_industry`, about 19 × 32 m, at E -223, N -1499). The stop's words (*"The church is down. Behind it William B. Bateham's mills, with a thousand cords of kindling wood in the yard, are going too"*) describe something else.

**What the sources say (checked in the OCR texts):**
- Andreas, *History of Chicago* vol. II (1885), p. 406: "St. Paul's Church was established in 1868, at the corner of Mather and Clinton streets ... The church-edifice cost $15,000, the priest's residence $3,000, and the parish school $5,000". So there were three buildings.
- Sheahan and Upton, *The Great Conflagration* (1871), Catholic losses: "St. Paul's Church, 100 by 40 feet, valued at $15,000, with A $3,000 residence", and "St. Paul's Parish School, $5,000". At $15,000 against St. Michael's $200,000, it was a plain, cheap church, most likely frame (inferred, to be confirmed).
- Riley (Andreas II pp. 715-716, already the stop's `riley` claim): the brand lit "on the cupola of the German Catholic Church, on the northeast corner of Mather and Clinton streets. The entire building was almost instantaneously enveloped in flames." So it had a cupola.
- Bateham: Andreas II pp. 717-718, "a thousand cords of fire-kindling wood, in piles twenty-five feet high"; Goodspeed (1871) "the match factory, lumber yard, and shingle mills of W. B. Bateham"; on Canal Street south of Harrison.

**What:**
- Remove the generic brick block (and any other context fill) from the church's lot at the NE corner of Mather and Clinton. Build St. Paul's: a frame church about 100 × 40 ft with a cupola, the priest's house and the parish school, on the period kits. Look for a picture (Andreas plates, Sheahan and Upton, the Chicago History Museum's ruins photographs, the 1868-71 Catholic directories). If there is none, it is reconstructed, recorded as a liberty.
- At 22:30 the church is "down": draw it as burning ruins at the stop's hour (the fire map's `burning_by`), standing before the brand at 21:45 or so, as T-3751 does for its other stops.
- Behind it, Bateham's planing and shingle mills, the match factory and the yard's 25-ft kindling piles on Canal south of Harrison, all burning at 22:30.
- Check the other West Side stops (O'Leary barn, Parmelee's) for the same generic brick fill. The district was mostly wooden cottages, barns, mills and lumber yards.

**Acceptance:** the St. Paul's stop shows the church's ruins burning with Bateham's mills and yard going behind; no generic brick block on the church's lot; liberty recorded for whatever is reconstructed; before/after pictures, desktop and phone.

## Completion pictures (PR 2439)

St. Paul's before the fire, before and after:
<img src="//github.com/kevinrhaas/chicago-evidence/blob/a0650dc952ee59e7ce50af3ed3b8984b78ac89d7/evidence/1871-streets/T-3831/T-3831-St-Pauls-before-the-fire-desktop.jpg?raw=true" width="900">

Parmelee's stable before the fire, before and after:
<img src="//github.com/kevinrhaas/chicago-evidence/blob/a0650dc952ee59e7ce50af3ed3b8984b78ac89d7/evidence/1871-streets/T-3831/T-3831-Parmelee-before-the-fire-desktop.jpg?raw=true" width="900">
