---
id: T-2636
title: Building fallback summary: a building with no summary record gets one templated from its sidecar, never raw fields, never ids, paths or snake_case
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-503
parent: null
opened: 2026-10-16
closed: null
pr: 918
claimed_by: run 10/16/2026, 4:42:14 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T21:42:14.765Z
decision: null
decision_answer: null
---

Building fallback summary: a building with no summary record gets one templated from its sidecar, never raw fields, never ids, paths or snake_case.

**Navigator Mk II — NAV-503.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2635 (NAV-502) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§12: structures without a record get a generated fallback built from the sidecar using templates,
never raw fields. Fixes the card opening with "(data/street_grid/1904.json)" and "parcel prairie_1800"
and the address three times (HIGH finding, `IMG_6942`).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-08: inspect a building with no summary file; the fallback renders with no ids, paths or snake_case, and gives the address once.
- [ ] A test runs the template over every 1904 and 1835 structure and finds no id, path or snake_case in the output.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.


## Finding (PR #918, 2026-10-16): 52 written accounts are not fit to print

The card leads with a building's own written account (`change_note`) word for word, but only when it passes the visitor-text lint. 52 accounts fail, so their cards show the templated lead instead: 35 in 1835, 17 in 1812, none in 1904. (PR #918's STATUS note says 35; that counted 1835 only.) The words are still in the sidecars and should be cleaned at the source; when an account passes the lint again it leads the card again, with no code change. Almost all fail on a ticket number written into the prose ("… (T-1776)"). A few fail on a file path, or on a field or record id quoted in the text (`documented_range`, `drawn_by`, `lake_house_finished`):

- 1812/burns_house_1812: ticket number `T-2487`
- 1812/coursoll_field_1812: ticket number `T-2513`
- 1812/forks_company_cornfield_1812: ticket number `T-2512`
- 1812/forks_house_clark_1812: ticket number `T-2512`
- 1812/forks_house_soldier_1812: ticket number `T-2512`
- 1812/lalime_house_1812: ticket number `T-2504`
- 1812/lee_house_1812: ticket number `T-2487`
- 1812/lees_place_cabin_1812: ticket number `T-2509`; ticket number `T-2503`; ticket number `T-2501`
- 1812/lees_place_field_fence_1812: ticket number `T-2509`; ticket number `T-2503`
- 1812/lees_place_haystack_1812_a: ticket number `T-2510`; ticket number `T-2503`; ticket number `T-2502`
- 1812/lees_place_haystack_1812_b: ticket number `T-2510`; ticket number `T-2503`; ticket number `T-2502`
- 1812/lees_place_haystack_1812_c: ticket number `T-2510`; ticket number `T-2503`; ticket number `T-2502`
- 1812/lees_place_haystack_1812_d: ticket number `T-2510`; ticket number `T-2503`; ticket number `T-2502`
- 1812/lemai_house_1812: ticket number `T-2504`
- 1812/potawatomi_camp_1812_middle: ticket number `T-2515`
- 1812/potawatomi_camp_1812_mouth: ticket number `T-2515`
- 1812/potawatomi_camp_1812_upper: ticket number `T-2515`
- 1835/agency_striker_log_house: ticket number `T-1714`
- 1835/caldwell_agency_log_house: ticket number `T-1714`
- 1835/chicago_lighthouse_keepers_quarters: ticket number `T-1716`
- 1835/emigrant_camp_shore: ticket number `T-1979`
- 1835/estray_pen: file path `data/enclosures/estray_pen.json.`; file path `docs/RESEARCH/civic_public_buildings_1835.md).`; id or snake_case word `drawn_by`
- 1835/exchange_coffee_house_stable: ticket number `T-1776`
- 1835/jb_beaubien_homestead: ticket number `T-0894`
- 1835/kelsey_boarding_house: ticket number `T-1717`
- 1835/kimberly_residence: ticket number `T-1717`
- 1835/lake_house_construction: file path `data/exclusions.json`; id or snake_case word `lake_house_finished`
- 1835/land_sale_camp_shore: ticket number `T-1804`
- 1835/landing_camp_west: ticket number `T-1803`; ticket number `T-1979`
- 1835/log_jail: file path `docs/RESEARCH/civic_public_buildings_1835.md).`; id or snake_case word `civic_public_buildings_1835`; ticket number `T-1687`
- 1835/mansion_house_stable: ticket number `T-1776`
- 1835/mckee_log_house: ticket number `T-1714`
- 1835/new_york_house_stable: ticket number `T-1776`
- 1835/newberry_dole_warehouse: ticket number `T-1717`; ticket number `T-2097`
- 1835/north_pier: id or snake_case word `documented_range`
- 1835/peck_store: file path `data/exclusions.json.`
- 1835/recon_1835_bank_freight_f3_001: ticket number `T-2022`
- 1835/recon_1835_branch_freight_f2_001: ticket number `T-2150`
- 1835/recon_1835_canal_trade_c3_001: ticket number `T-1766`
- 1835/recon_1835_canal_trade_c4_002: ticket number `T-1766`
- 1835/recon_1835_canal_trade_w1_003: ticket number `T-1766`
- 1835/recon_1835_canal_trade_w2_004: ticket number `T-1766`
- 1835/recon_1835_forks_freight_f2_001: ticket number `T-1773`
- 1835/recon_1835_south_branch_freight_f3_001: ticket number `T-2268`
- 1835/recon_1835_south_branch_freight_f3_002: ticket number `T-2268`
- 1835/recon_1835_south_branch_lumber_f4_001: ticket number `T-2269`
- 1835/sauganash_hotel_stable: ticket number `T-1776`
- 1835/south_pier: id or snake_case word `documented_range`
- 1835/steamboat_hotel_stable: ticket number `T-1776`
- 1835/tremont_house_1_stable: ticket number `T-1776`
- 1835/west_approach_wagon_camp: ticket number `T-1804`
- 1835/wolf_point_trading_camp: ticket number `T-1977`

Recompute with `visitorTextProblems` from `renderers/web/js/fallback-summary.js` over each sidecar's `change_note`.
