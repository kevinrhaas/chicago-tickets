---
id: T-1743
title: The Beaubien homestead reads as three identical log houses by the fort, and two of them stand on the fort road
state: done
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-10-03
pr: 357
claimed_by: run 10/3/2026, 11:08:02 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-03T20:31:54Z
claimed_run: null
claimed_at: 2026-10-03T16:08:02.670Z
decision: answered
decision_answer: b
---

The Beaubien homestead reads as three identical log houses by the fort, and two of them stand on the fort road.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 143 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-filed from a screenshot of the live scene; T-1712, the ticket that built these, is closed, so there is no open ticket to fold it into.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What the owner saw

Col. Jean Baptiste Beaubien has three near-identical log houses right by the fort, and some of them block the road. The owner's reading is that there should be **one** house for him, unless there is evidence for a complex like that.

## What the records say (measured 2026-09-28 on dev)

**The group has four records, and three of them are the same `log_dwelling` archetype.** The fourth, the barn, is an `outbuilding` but is deliberately drawn as a 20 x 16 ft cabin:

| record | archetype | placement (local E, N) | footprint | position |
|---|---|---|---|---|
| `jb_beaubien_homestead` | log_dwelling | 1127.1, 174.8 | 12.19 x 6.10 m | inferred |
| `beaubien_new_residence` | log_dwelling | 1145.0, 174.8 | 9.75 x 6.10 m | reconstructed, by eye (T-1712) |
| `beaubien_trading_post` | log_dwelling | 1145.0, 158.5 | 6.10 x 4.88 m | reconstructed, by eye (T-1712) |
| `beaubien_barn` | outbuilding | 1127.1, 158.5 | 6.10 x 4.88 m | reconstructed, by eye |

**Two of them stand on the road itself.** The `fort_road` centreline (`data/streets/1835.json`) runs north at about E 1146–1148 between N 120 and N 188. It passes **through** the footprints of `beaubien_new_residence` (E 1145–1154.75) and `beaubien_trading_post` (E 1145–1151.1), so the distance from the centreline to each is 0.0 m. The homestead clears it by 8.2 m and the barn by 13.8 m. The corridor half-width is 6.0 m and the track half-width is 2.8 m. So the two buildings T-1712 added by eye were placed on top of a road that `fort_road` had already drawn. Nothing checks structures against the street corridors; if something did, it would have refused both.

## The evidence for a complex, and against it

- **For.** Andreas lists what the homestead held: the factory building, a **new residence**, a **small trading post**, and an **old cabin used as a barn** (scan p. 185; p. 183 has "He used the old cabin after this for a barn"). Wentworth's account of the June 1839 sale names "Beaubien's house, out-buildings, and garden" on lots 6–10. So a group of buildings is attested, and this is not an invented complex. See `docs/RESEARCH/jb_beaubien_homestead.md` §§ 1, 4 and 6a.
- **Against how it is drawn.**
  - Nothing locates, sizes or describes any of the three that are not the homestead.
  - Andreas's "new residence" may well be the building the homestead record *is*. Dossier § 6a says Wentworth's "traditional residence" at the corner is most likely the new residence, so the group may be double-counting one house.
  - Andreas's p. 183 barn sentence sits in the Dean-house paragraph (the house at the lake shore), so "the old cabin" may be a Dean-house cabin rather than one on this ground.
  - What the scene shows now is three indistinguishable dwellings in a grid by eye, and two of them are on the road.

## The fix, depending on the owner's answer

- **(a) One house.** Keep `jb_beaubien_homestead` and take the other three out of the scene. Record the attestations in the dossier as unplaced, next to the Factor's House.
- **(b) Keep a reduced group, sited honestly.**
  - Fold `beaubien_new_residence` into the homestead, since it is the likelier identity per § 6a.
  - Keep the trading post and the barn as clearly smaller outbuildings, not dwellings: a store or shed form, and the barn as a barn.
  - Re-site everything off the `fort_road` corridor, behind (west of) the frontage.
  - Add a gate step that refuses any structure footprint inside a street corridor.

**Acceptance:**
- No Beaubien footprint intersects the `fort_road` corridor (or any street corridor).
- At most one Beaubien building reads as a dwelling.
- The dossier § 4 and `docs/LIBERTIES.md` L283 are updated to match.
- The scene walk at 390x780 and at desktop shows the fort road clear past the fort.

## Decision needed

**Question:** Col. J. B. Beaubien currently has four buildings by the fort, three of them identical log houses, and two of them sit on the fort road. Andreas does attest a group: the factory building, a new residence, a small trading post, and an old cabin used as a barn. But nothing places or sizes the extra three, and the 'new residence' is probably the house we already model. Which should the scene show?

- (a) One house only: keep the homestead and remove the new residence, the trading post and the barn from the scene (kept as unplaced attestations in the dossier)
- (b) The homestead plus two small outbuildings: fold the new residence into the homestead, draw the trading post and the barn as a shed and a barn rather than houses, and move everything off the road

**Recommendation:** (b) The homestead plus two small outbuildings: fold the new residence into the homestead, draw the trading post and the barn as a shed and a barn rather than houses, and move everything off the road — Andreas and Wentworth ('house, out-buildings, and garden') both attest more than one building, so removing them all under-reads the sources. The duplication and the road are both faults of how T-1712 drew the group, not of the evidence. (b) shows one dwelling, which is what you expected, and still honours the out-buildings.

**Asked:** 2026-09-28. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

## Owner answer, 2026-09-28: (b)

*"go with b for beaubien"*

So the scene shows **one dwelling for Col. Beaubien**, the homestead, with two small outbuildings. That replaces the either-or in "The fix" above:

- Fold `beaubien_new_residence` into `jb_beaubien_homestead`, taking it out of the scene. Record in dossier § 4 that Andreas's "new residence" is read as the house the homestead record already models (§ 6a).
- Keep `beaubien_trading_post` and `beaubien_barn` as **outbuildings, not dwellings**: the trading post as a small store/shed form, and the barn as a barn. Neither may use the `log_dwelling` archetype.
- Re-site both off the `fort_road` corridor, behind (west of) the frontage.
- Add the gate step that refuses any structure footprint inside a street corridor.
- Update L283 in `docs/LIBERTIES.md` to match.
