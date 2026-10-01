---
id: T-1213
title: Signboards for every business that would have hung one: the reconstructed firms' names and trades in period lettering and forms, the attested signs untouched, the signless trades left signless by rule
state: open
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-09-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
---

`data/signage/town_business_signboards.json` (`generate_business_signboards.py`, T-0039/T-0066/
T-0130, L130) holds 33 signs and REFUSES a sign on a `recon_*` roof because no business was
named there. After T-1190 every roof's business is named, so the refusal's condition is
gone for the reconstructed firms — and the owner ruled in August that signs are fine as
reconstructions. Drawn at load — no bake.

**Acceptance:**

- The signboard rule extended: a reconstructed firm of a `public_trades` type gets a sign whose
  text is its period firm style (T-1184's style guide), `sign_text_confidence:
  reconstructed`, in one of the period forms the layer already models (board over the door,
  bracket sign, sapling pole at a tavern, a painted panel) chosen by trade and by the archetype's
  sign socket; `works_trades` get the trade word only or none, per the existing rule; taverns get
  the device the record names or a reconstructed one from the period's vocabulary (the wolf at
  Wolf Point is attested; invented devices are named as invented).
- Attested signs unchanged (self-test); `generate_business_signboards.py --check` green;
  `opening_fit` honoured so no sign covers a door or window.
- **Visible:** South Water and Lake Street read as a business street from the walker's eye; a
  sign tap opens the business card (T-1181).

## Photographic-quality benchmark — owner, 2026-09-30

The owner sets **photographic quality** as the standard: the successful Glessner
House v4 rendering in the 1904 scene is the minimum visual benchmark to live up
to and surpass. Complete and consume **T-1769's preparation package before closing
this ticket**. Reuse its proven methods and shared assets where appropriate;
adapt them to July 1835 materials, construction, age and use.

Acceptance also requires inspection of the **actual published browser output** at
390×780 and 1280×800: fixed walker's-eye views, closeups and a wider context view,
with before/after captures, reference comparisons and a written visual critique.
Compare against the promoted Glessner v4 baseline and record which techniques
were reused, adapted or rejected, why, and which qualities match or improve on it.
Review physical scale, relief/silhouette, joinery, surface response, variation,
contact/depth shadows, tiling and shimmer. A green validator, a texture contact
sheet or an offline beauty render alone cannot establish photographic quality;
visible shortcomings must be corrected before closure.

Preserve historical tiers and attested/inferred facts. Photograph-like appearance
does not make reconstructed detail attested. Measure town-wide costs before and
after at the relevant worst stands and all detail tiers; retain the Light floor,
shared-material batching and deliberate, measured re-budgeting under AGENTS.md.
Glessner's local Full allowance is not a town-wide budget.

**Sign-specific acceptance:** lettering is period-appropriate painted work on
wood, with credible board thickness, grain, paint coverage, edge wear and attachment.
Brackets, straps and poles use shared timber/iron materials; shadows and mounting
depth must read correctly. Text stays legible at the walker's intended viewing
distance without looking like a modern glowing overlay. Review a store board,
bracket sign and tavern device, including oblique and mobile views. Wear cannot erase
the business name or change attested wording, and no sign obscures an opening.

**Stop condition:** every firm that would have hung a sign has one, and every sign says what it
is.

**Links:** T-0039 · T-0066 · T-0130 · L130 · T-1184 · T-1181.
