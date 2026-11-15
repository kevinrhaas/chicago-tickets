---
id: T-3553
title: Finish people's clothing: no breakthrough in motion, better collars and seats, the six-role wardrobe reviewed beside period photographs, coat tails that sway
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
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
- 2026-11-13 — **Find and Follow land outside** (PR #2020). Kevin, Find/Follow on Mrs. W. L. Grey in 1904: "its a inside 3d space that you cant see what is going on so when you find someone or start to follow them you should wait until they get outside for us to land". 2000 and 2010 Prairie's entrances had been derived on the footprint's front, inside the front block the frame house builds before it; they now open on their front blocks, answered at the foot of the porch steps (derive_doors_scene.py; every reconstructed entrance stands past what is built before its front). Find/Follow stands keep off porches and outside the house's drawn shape; Follow waits while someone is in their doorway and stops at their door going in (all years).
- 2026-11-14 — **People are solid** (PR #2044). Kevin, 1904 phone at Prairie and 18th, walking into a man and seeing the inside of his head: "you should not see inside people's heads and bodies". The walker is held 0.64 m off every drawn figure and slides round them (walker.js `clearOfBodies`, no tunnelling at a sprint); passers-by step round the visitor and a stander pressed on steps aside (human-spacing.js `body`); a figure whose body holds the eye is not drawn that frame (humans.js `hideAtEye`), for flights and landings. All years. Gate: test_walker_bodies.mjs.
- 2026-11-14 — **The first host stands at the door** (PR #2053). Kevin, iPhone, dev, Grades 3–5 Glessner Household: "I did not see John show even after he started speaking". A jaunt started from Home asked for John before human-days had run a frame, so he was taken as a dayless figure and his day (spring morning, away at the office) then put him indoors at his mark, undrawn. human-days `roster()` collects on demand in `host()`; jaunt-hosts retries, never hand-takes, a figure that has a day. Both grade versions were hit. Phone QA: John drawn at his mark facing the visitor.

  ![Before and after, phone, stop 1](https://github.com/kevinrhaas/chicago-evidence/blob/6dad334b78e8b4b95abb785be3b194195bf07d38/evidence/T3553-jaunt-host-door/phone-stop1-before-after.jpg?raw=true)
- 2026-11-14 — **The women's finery** (PR #2055). Kevin: "Give the women some variation in their clothing appearance" (Gilded Age fine dresses). Every Prairie Avenue lady of 1904 has her own summer, spring/fall and winter dress (silk afternoon, lingerie, walking suit, velvet, shirtwaist; half-mourning silk with jet for most women of 60+), trimmed with lace, ribbon and velvet bands, braid, tucks, flounces, jet or a woven figure, and a picture hat, sailor or toque with plumes, flowers or a bow; none alike. Maids, cooks (print and check), companions and girls varied; Sarah Grey keeps her portrait dress. 1812's calico, checks and stripes are drawn from the records' own words, mean colour kept. Shader uniforms only (fabric.js, human-finery.js), no textures; seasons follow Settings > Season. Liberty L-finery-3553; 11 Met CI sources. Gate: test_human_finery.mjs. Not yet: garment shapes (bodices, sleeves, trains), coats and furs, 1835 women.

  ![1904 ladies, before (top) and summer (bottom)](https://github.com/kevinrhaas/chicago-evidence/blob/0397b4796fc40788c7c7958b7f617202cb3b150f/evidence/finery-T-3553-2026-11-14/ladies_1904.png?raw=true)

  ![Four ladies in summer, spring/fall and winter](https://github.com/kevinrhaas/chicago-evidence/blob/0397b4796fc40788c7c7958b7f617202cb3b150f/evidence/finery-T-3553-2026-11-14/ladies_seasons.png?raw=true)

  ![1812 town women, before (top) and after](https://github.com/kevinrhaas/chicago-evidence/blob/0397b4796fc40788c7c7958b7f617202cb3b150f/evidence/finery-T-3553-2026-11-14/town_1812.png?raw=true)
- 2026-11-15 — **The 1812 jaunts played by their people** (PR #2063). Kevin: "place all the right people at the right scenes from history so we can witness the events"; ruling "Build-up and aftermath" (no blow, shot or blood; the fallen lie still; no child shown fallen). Every stop of *The Battle of Fort Dearborn* and *The Killing of Jean Lalime* carries a `stage` played by jaunt-stage.js: Lee's place and the flight, the order, the council, the gate, the whole evacuation party marching down the shore past the visitor, warriors lying and kneeling on the bank who rise as the column halts, Black Bird's handshake with the fallen beyond, the Lalime-Kinzie quarrel, the night crossing and the grave. Postures kneel/kneel2/crouch/sit/prone/lie; hands stay on a posed body. Casts generated by docs/RESEARCH/jaunt-stage-1812-3553; liberty L-1812-staged-jaunts-3553. Gate: test_jaunt_stage.mjs. Next: the column's wagons with the women and children riding, Mills and Moffett driving.
  Before / after (river mouth, the bank, the quarrel, the flight):
  ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/before-battle-of-fort-dearborn-08-river-mouth.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/after-battle-of-fort-dearborn-08-river-mouth.jpg?raw=true)
  ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/before-battle-of-fort-dearborn-09-the-bank.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/after-battle-of-fort-dearborn-09-the-bank.jpg?raw=true)
  ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/before-killing-of-jean-lalime-05-the-quarrel.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/after-killing-of-jean-lalime-05-the-quarrel.jpg?raw=true)
  ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/before-killing-of-jean-lalime-07-the-flight.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/after-killing-of-jean-lalime-07-the-flight.jpg?raw=true)
- 2026-11-15 — **The 1812 column brings its wagons** (PR #2068). Kevin: "I would think you have the full evacuation party for the evacuation." At the river mouth and the sand bank the town's two wagons leave their rounds and roll in the column, driven by Privates Mills and Moffett; Mrs. Burns, Mrs. Corbin, Mrs. Lee's daughter and the garrison children ride (Helm's narrative, Wau-Bun), the other women walk beside. A stage now takes town teams (`stage.teams`, `cast[].ride`; transport-loop staged mode). Also fixed the dev changelog fold, broken since #2063 (compile_jaunts checked a GLB the fold's sparse checkout leaves out; it now checks the dress recipe). Before (dev) and after, the river mouth at 76 s:
  ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/before-wagons-river-mouth.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/jaunt-stage-1812-3553/after-wagons-river-mouth.jpg?raw=true)
- 2026-11-15 — **18+ tellings of the 1812 battle and the Lalime killing** (PR #2083). Kevin: "this one is targeted at adults and shows everything incredibly graphically"; "Yes scalpings did occur so we want to be honest about it"; "That adults band you can call 18+". Two `version_of` jaunts (audience adults, content warning), hidden until Settings › 18+ jaunts, never in teacher handouts. Weapons in hand and strike/stab/aim/fire/struck motions (human-fight.js), gun flash and smoke; Lalime's pistol and the knife at the gate; Lee's Place shootings; the volley, the bayonet charge and hand-to-hand fighting on the beach; Wells's death; the dead scalped. No child struck; Wells's heart told, not shown. Blood and wounds follow in a second PR.
  ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/t3553-18plus-jaunts-2026-11-15/lalime-2-shot.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/t3553-18plus-jaunts-2026-11-15/lalime-4-after.jpg?raw=true) ![](https://github.com/kevinrhaas/chicago-evidence/blob/claude/project-thread-l2dj9e/evidence/t3553-18plus-jaunts-2026-11-15/bank-2-charge.jpg?raw=true)
