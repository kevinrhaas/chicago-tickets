---
id: T-1953
title: The West's three H3 boarding houses the book orders, on the platted ground T-1414 seats, each with its stable and privy, keepers and lodgers seated
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1810
opened: 2026-10-01
closed: null
pr: null
claimed_by: run 10/9/2026, 11:31:52 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38024189090
claimed_at: 2026-10-10T04:31:52.274Z
decision: null
decision_answer: null
---

The West's three H3 boarding houses the book orders, on the platted ground T-1414 seats, each with its stable and privy, keepers and lodgers seated.

Piece 4 of 4 of **T-1810 — Raise the H3 boarding houses the book still orders beyond the two Washington-tier seats — the South's remaining eight and the West's and North's, whose placement no banded keeper has claimed yet — each with its stable and privy, keepers and lodgers seated**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Queue cleanup 2026-10-10 (owner: "are there any other held tickets that can be cleared")

Unblocked: **T-1414 is done** (PR #341, closed 2026-10-03), so the ground it owed is seated. Read on `dev` at b281f6d9 before anything else:

- In `data/reconstruction/1835_665_roof_programme.json` the `west_division_beyond_committed_control` unit is `complete` with 0 roofs and **28 roofs of surplus headroom** on named West blocks. Open West blocks with room: `blk_washington_clinton` (39 capacity, 20 standing), `blk_west_washington_des_plaines` and `blk_west_washington_jefferson` (6 each, 0 standing).
- **But the programme's `remaining.by_district.west` is 0 and `by_district_family.west` is empty.** The West's last owed H3 left the remainder at c0d76927 (T-2148, 2026-10-06). The only H3 still owed anywhere is one in the South.

So the first step is a reading, not a build: does the book still order the West's three H3s? If it does, raise them on the open West blocks above. That also seats T-2023's 7 West adults, who are still `ordered_with_no_bed`. If it does not, say so here and withdraw this ticket, and re-point T-2023 at whatever now owes the West a lodging roof.

## READ 2026-10-10 (slice 7/7): the book no longer orders the West's boarding houses. Withdrawn.

Read on `dev` at b281f6d9b, which is the reading the cleanup above asked for before any build.

- **The book's cell is filled.** `structures/larger_boarding_houses/west` in
  `data/reconstruction/1835_reconstruction_order_book.json` reads target 6, standing 6,
  to_build 0. It read 2 standing and 4 to build at 70f606b8b (T-1816, 2026-10-01). T-2148
  (7bab8f204, 2026-10-06) raised the difference when it dealt `blk_washington_clinton`'s 13
  roofs: `recon_1835_blk_washington_clinton_h3_02` (an H3 boarding house, 11 ordinary beds),
  `_h1_05` and `_h2_01`. The roof programme agrees: `remaining.by_district.west` is 0 and
  `by_district_family.west` is empty. No family in the West is left to build, H3 or otherwise.
- **The 7 West adults are no longer owed by the live book either.** The "7 ordered with no
  bed" in `1835_lodgers_seated.json` → `quota_basis.top_up.what_is_left` is the top-up's FROZEN
  room (male 20-29 ×2, 30-39 ×2, 40-49, 50+, female 40-49), read when T-1538 recorded it. Every
  one of those cells in the live book now reads `filled` equal to `to_reconstruct`
  (male 20-29 8/8, 30-39 5/5, 40-49 1/1, 50+ 1/1; female 40-49 1/1), and `re_cut_since` records
  the book cutting male 20-29 West from 12 to 8. A West roof raised now would mint seven people
  the book no longer asks for.
- So there is nothing for this ticket to raise. The book cell keeps `owning_ticket: T-1953`;
  the work-order gate (`every_work_order_names_a_live_ticket`) only reads owners of cells with
  work left, and this one has none, so withdrawing it strands nothing. T-2023, which was
  `blocked-tech` on this ticket, is re-pointed below and unblocked.
