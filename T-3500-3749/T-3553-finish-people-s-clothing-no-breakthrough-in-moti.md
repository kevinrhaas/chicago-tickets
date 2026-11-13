---
id: T-3553
title: Finish people's clothing: no breakthrough in motion, better collars and seats, the six-role wardrobe reviewed beside period photographs, coat tails that sway
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: null
claimed_by: run 11/13/2026, 3:10:40 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-11-13T21:10:41.458Z
decision: null
decision_answer: null
---

Finish people's clothing: no breakthrough in motion, better collars and seats, the six-role wardrobe reviewed beside period photographs, coat tails that sway.

## Why this ticket (owner, 2026-11-12)

Kevin, thread "Consolidate ticket queue": "the people human tickets, horses and carriages I think a lot has been done and there probably are only a few items left to do so those can be pulled out and consolidated into a limited number of tickets that will be faster to complete". This ticket is what is left of the clothing work. It replaces **T-1789** (modular human library), **T-3410** (first wardrobe catalogue) and **T-3421** (coat-tail sway), which are withdrawn into it. Their files keep their history; read them only for a detail this one does not carry.

## Already done on dev — reuse it, don't rebuild it

- The portable pipeline: T-1786 contract (#606), T-1787 exporter (#644), T-1788 browser actor (#669); 248 measured GLBs over four LODs on a shared 56-joint rig.
- The wardrobe kit T-3409 (#1746), face/body variation T-3412 (#1755), hair and eyes T-3414 (#1763), the female shared-rig base T-3423 (#1787), the paired reference rig T-3417 (#1754), the fabric shader (T-2804, #1733) and the coachman's livery (T-3398, #1739).
- The six catalogue roles: Glessner's day dress (#1822), Frances Glessner and the maid (#1823), the 1835 merchant and labourer and the 1812 private (#1824).
- The cloth finish and level hems (#1904), fine wool coats (#1928), the 1812 settler's looser linen seat (#1933).

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **No clothing breaks through in motion.** Check walking and turning poses, not only standing: the coachman's trousers through his coat, the women's aprons, the soldiers' stripes and trim on bending sleeves. Fix the garment or its weights, not the camera.
- [ ] **Collars** read as shirt collars at conversation distance: neckline and coat junction reshaped on the existing garments.
- [ ] **Seats**: no trousers tracing the buttock cleft on any figure in motion (the 1812 settlers are done by #1933; check the rest).
- [ ] **Coat tails sway** on people who walk in coats, as the drivers' spring tails already do (T-3409).
- [ ] **The six-role catalogue reviewed**: one paired still per role at 3 m and 10 m beside a dated period photograph or plate (the T-3417 rig), differences listed candidly.
- [ ] Desktop 1280×800 and phone 390×780 shots before and after, in the real scenes, in the ticket's evidence folder. Phone memory stays inside the T-3537 / T-3542 ceilings; no person, horse or carriage is dropped to fit.

Keep each person's identity, colours, style, provenance and adopted clips. Ship in as many PRs as it takes, each one a visible improvement; the ticket closes when the list above is ticked.

## Progress

- 2026-11-13 — **Breakthrough in motion, hanging cloth** (PR #1979). Kevin, following a coated man on 18th St in 1904 on his phone: "no one should have their legs break through their clothing like that". Every hanging garment (coat skirts, the coachman's livery, tails, 1812 capotes, shirt tails, blankets, breechcloths, girls' frocks, petticoats, aprons) now hangs from the waist over the legs (human-skirt.js `garmentKind`, COAT style for coats); tested on all 35 assets at every LOD, standing, posed and walking. Coat tails now sway with the walk. Left: the Potawatomi man's breechcloth flap corner (3.1 cm over a leg at the end of a stride, was 11.2) and his legging selvage through his shirt tail standing (asset as drawn); soldiers' stripes and trim on bending sleeves are not yet checked.
- 2026-11-13 — **Nobody stands in a stair** (PR #2014). Kevin, of a 1904 maid half inside the bottom steps of a front stoop: "she cannot stand where there are stairs like that, no one should be able to". Barriers now start at a riser (prairie_barriers KNEE_M 0.14, walks ≤0.124 m stay ground); back-yard stoops and 1835 street-front stoops/mounting blocks are barrier rows (derive_doors_scene stoop_rows); planDay `standClear` moves every played place off a stair, a chat's spots too; human-spacing steps a stander out. Gate: test_house_barriers.mjs §4-6.
