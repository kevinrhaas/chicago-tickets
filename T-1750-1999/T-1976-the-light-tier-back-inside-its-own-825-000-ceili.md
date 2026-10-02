---
id: T-1976
title: The light tier back inside its own 825,000 ceiling and 90-call floor at every stand at both viewports by a trim, smoke part 5 green at both viewports
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1974
opened: 2026-10-02
closed: null
pr: 284
claimed_by: run 10/2/2026, 10:14:07 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37025200780
claimed_at: 2026-10-02T15:14:07.218Z
decision: null
decision_answer: null
---

The light tier back inside its own 825,000 ceiling and 90-call floor at every stand at both viewports by a trim, smoke part 5 green at both viewports.

Piece 2 of 2 of **T-1974 — The detail ceilings and the draw-call budget re-measured at every stand and set where they are defined, T-1154 reconciled, smoke green at both viewports**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## The reading this piece starts from (T-1975's run, 2026-10-02)

`node tools/measure_detail_ceilings.mjs` on the published mirror of dev @ 652ca8ea (the reading is
committed by T-1975 as `docs/measurements/t-1975-detail-ceilings-{desktop,mobile}.json`):

| viewport | `light` worst | against 825,000 | worst calls at `light` | against the 90-call floor |
| --- | --- | --- | --- | --- |
| desktop 1280x800 | 944,550 (the forks) | +119,550 | 102 (Lake and Market) | +12 |
| mobile 390x780 | 845,385 (Lake at Canal) | +20,385 | 93 (Lake and Market) | +3 |

Every desktop stand but the Sauganash is over: the forks 944,550, Lake at Canal 942,469, the open
aerial 932,220, Lake and Market 818,341 (inside by 6,659 but 102 calls).

What fills `light` at the forks, desktop (`tools/measure_stand_budget.mjs --stand the_forks --tiers
light`): structures 249,774 · terrain 222,772 · trees 146,608 · frontage 121,484 · streets 106,891 ·
yard 22,248 · yard-ground 21,346 · enclosures 18,644 · working_bank 13,650 · flora 11,857 · signage
6,284. The sun's pass is only 30,486 of it (3.2 %), so a shadow trim cannot carry this; the
furniture reach (350 m) still leaves frontage at 121,484 here, which is the first place to look.
The growth is spread over the ~60 owner-requested parcels merged 2026-09-26..10-02 (light read
772,025 worst on 2026-09-26), so there is no single change to bisect back out.

AGENTS.md: "`light` is the floor and stays the floor … keep it inside its own ceiling and spend new
headroom at the tiers above it." So this is a trim, not a raise — unless the owner rules otherwise
in as many words, as he did once on 2026-09-03 ("raise all 3"), and T-0672 then still owes the
return of that raise.
