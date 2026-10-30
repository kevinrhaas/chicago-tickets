---
id: T-3253
title: 1904 Prairie Avenue households: every resident family and live-in staff on the house cards
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-29
closed: null
pr: 1469
claimed_by: run 10/29/2026, 9:27:44 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-30T02:27:45.251Z
decision: null
decision_answer: null
---

1904 Prairie Avenue households: every resident family and live-in staff on the house cards.

Owner, 2026-10-30 (project thread "Fill 1904 Prairie household people"): *"you don't have very many of the people on the people cards in 1904 for prairie I think you should research all of those and make sure you put the families there in the houses with all of the people in the house, including staff and servants where possible"*.

Today `data/residents_1904/households/` holds one card (the Glessners, two people).

**Acceptance:**
- Every standing 1904 Prairie Avenue house that a source puts a household in gets a card in `data/residents_1904/households/`, with every person a source names in it: the family, relatives and boarders, and live-in staff (coachmen, cooks, maids, nurses, governesses) where the sources name them.
- Sources read directly, not summarised: the Chicago Blue Book 1904 Prairie Avenue street list, the 1900 US census population schedules for the Prairie Avenue enumeration districts, and the Glessner House material already cited. Each person carries their own source ids; nobody is added without one.
- A person documented only before or after 1904 (e.g. a servant enumerated in 1900) carries that as a bound, never as a 1904 fact; their grade says so.
- Houses with no source for a household say so on the card instead of being filled.
- One PR into dev, merged on a green gate; `place-names.json` lines for any new family the jaunts need.
