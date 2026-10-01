---
id: T-1816
title: The fabric-by-household rule: finish, paint, roof condition and age dealt to every reconstructed roof from the household class its type houses and, where the record names a keeper, that household's own trade and arrival year — written by the generators with a fabric_basis, the rule in the placement policy and materials.md, the card's Built line naming the fabric and whose house it is, the changed roofs rebaked
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1210
opened: 2026-10-01
closed: 2026-10-01
pr: 239
claimed_by: run 10/1/2026, 1:44:26 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-01T21:42:11Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36907211976
claimed_at: 2026-10-01T18:44:26.852Z
decision: null
decision_answer: null
---

The fabric-by-household rule: finish, paint, roof condition and age dealt to every reconstructed roof from the household class its type houses and, where the record names a keeper, that household's own trade and arrival year — written by the generators with a fabric_basis, the rule in the placement policy and materials.md, the card's Built line naming the fabric and whose house it is, the changed roofs rebaked.

Piece 1 of 3 of **T-1210 — Deal building fabric, finish and weathering by who lived and worked there: a physician's or forwarder's house painted and glazed, a tradesman's cottage weathered clapboard, a labourer's cabin unpainted and patched — the rule set on the material sheet, applied to every dwelling and business, no attested finish moved**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

Stated by the run that took it (2026-10-01), before working:

- **One rule, one module.** `tools/fabric_rule_1835.py` deals `finish_key`, `paint`,
  `roof_condition` and `age_state` for a reconstructed roof from (a) the household class
  its family houses — the reconstruction spec's own labels: an older log cabin or a shanty
  is a labourer's, a frame cottage a tradesman's, a merchant's or professional house a
  merchant's, a boarding house a keeper's, a store or works the trade's; a yard building
  follows the principal roof on its lot — and (b) where the record names an ASSIGNED
  keeper (`resident_assignment.status: assigned`), that household's own trade
  (`seat_known_1835.TRADE_CLAUSE`) and arrival year. Letter-list households refused a
  roof by T-0379 are never read.
- **All five generators deal through it** (block, inferred, west, north, west freight),
  replacing the `seq % 4` age/roof cycle; every record carries a `fabric_basis` naming the
  rule, the class and whose house it is. Generator `--check`s stay byte-exact.
- `white_paint` stays the Sauganash's alone; no attested or inferred value moves (self-test
  in `fabric_rule_1835.py --check`). The rule is written into the placement policy and
  materials.md with its evidence and the liberty it extends.
- **Visible:** the building card's "Built" line names the fabric and its basis; the changed
  roofs are rebaked and the town's wealth gradient (whitewashed and painted better houses,
  silvered and patched cabins) is readable in the browser at 390x780 and 1280x800.
- `check.sh` green; the `--for-diff` smoke legs green.
