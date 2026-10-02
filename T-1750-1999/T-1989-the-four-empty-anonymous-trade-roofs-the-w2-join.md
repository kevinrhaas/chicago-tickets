---
id: T-1989
title: The four empty anonymous trade roofs (the W2 joiner's shop on Randolph, the F2 warehouse at the forks, the W5 work shop on Wolcott the off-plat deal adopted for the Miller and Hall tannery household but never spent, the C3 store on Lake) each seated by a deal or shown unseatable: the order book has an occupant class for each and the policy accepts it where it stands, so a stated use would break 1835_stated_uses' rule (b)
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1986
opened: 2026-10-02
closed: null
pr: null
claimed_by: run 10/2/2026, 12:56:49 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37043683812
claimed_at: 2026-10-02T17:56:49.148Z
decision: null
decision_answer: null
---

The four empty anonymous trade roofs (the W2 joiner's shop on Randolph, the F2 warehouse at the forks, the W5 work shop on Wolcott the off-plat deal adopted for the Miller and Hall tannery household but never spent, the C3 store on Lake) each seated by a deal or shown unseatable: the order book has an occupant class for each and the policy accepts it where it stands, so a stated use would break 1835_stated_uses' rule (b).

Piece 2 of 2 of **T-1986 — The anonymous programme roofs left empty (stables, barns, sheds, a privy and four trade buildings) each tied to the dwelling or establishment it serves by T-1980's part_of, or given a stated use, the audit's empty count at zero**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (stated before working)

`python3 tools/audit_town_completion_1835.py` lists none of these five in `occupied.empty`: recon_1835_blk_west_randolph_des_plaines_w2_01, recon_1835_forks_freight_f2_001, recon_1835_north_w5_040, recon_1835_south_c3_015, recon_1835_west_013; `empty_owing_somebody.house_of_trade` and `.dwelling` fall by the four's share, and `outbuilding_naming_no_yard` reaches 0 once T-1988's nine land.

- The four trade roofs are offered by a new deal, `tools/seat_trade_roofs_1835.py`, to the keepers the employment ledger owes a house of their own (`keeps_their_own_house`) whose card names no workplace, in the roof's own division, matched by the trade the premises rulings give the roof's family (W2 carpenter/joiner by the crosswalk label; F2 the forwarding store; C3 the store and grocery signage; W5 the heavy-trade signage the heavy_and_noxious clause names), nearest to the keeper's own roof, seeded. A seat reaches the roof's card as "worked here" through compile_scene, the way the housing deal's seats do; it writes no card and no structure record.
- A roof the deal cannot seat says why on its card (`stated_use`, the T-1985 surface) and in the audit, with the count that proves it — never by inventing a keeper.
- recon_1835_west_013 is refamilied A5 → D2 by `tools/execute_roof_redeal.py --apply --only` (the redeal's own standing verdict), rebaked with `bake.sh --only`, and the housing deal (`house_the_present_1835.py --build`) re-run so a household waiting on a roof can take it.
- No confidence is upgraded; every generator `--check` and check.sh green; liberty recorded.

## Also owned here: recon_1835_west_013 (found by T-1988)

A fifth anonymous roof belongs with these four for the same reason: a household could be seated in it. `recon_1835_west_013`, the A5 small utility building west of Canal and Lake, stands on a principal street, where the placement policy's ancillary_behind_its_own_roof clause will not put a yard building. So `tools/redeal_anonymous_roofs.py` already rules it a **refamily A5 → D2**: a rough plank dwelling, wanted where it stands. T-1988 drafted a stated use for it (the yard building of recon_1835_west_004, after the West recipe's `yard_group`). Rebuilding the redeal then showed the stated use turning the verdict into "kept over a policy breach because it is seated". That keeps a roof from one of the 523 households waiting on a roof, which `1835_stated_uses.json` rule (b) forbids. The row was withdrawn. The remedy is to carry out the refamily and seat a household, which is a seating answer like the four above, and it takes the audit's `outbuilding_naming_no_yard` count from 1 to 0.
