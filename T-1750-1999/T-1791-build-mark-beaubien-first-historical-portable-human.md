---
id: T-1791
title: Build Mark Beaubien as Chicago 4D's first historical portable human, from Blender master to interactive browser actor
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: L
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: null
blocked_on: T-1790
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Use **Mark Beaubien** as the first end-to-end named historical person. He already exists
in the project's resident/household/business evidence; this ticket gives that existing
identity a researched visual/animated representation rather than creating another person
record. Implementation target: `kevinrhaas/chicago` **dev**.

**Read first:** `data/residents/households/hh_beaubien_mark.json`,
`data/businesses/authored/biz_beaubien_mark_tavern_keeper.json`,
`data/sources/encyclopedia_chicago_mark_beaubien.json`,
`docs/RESEARCH/sauganash_hotel.md`, `docs/RESEARCH/exchange_coffee_house.md`,
the T-0462 resident-research row for `beaubien_mark`, and any stronger portrait/image
evidence found and committed during this ticket.

**Acceptance:**

- Build a dated visual-evidence sheet before modelling: contemporary/near-contemporary
  portrait or likeness evidence if available; later portraits clearly dated; documented
  age/role/body clues; period clothing references appropriate to his role and Chicago in
  the scene year. Separate attested likeness, period analogy and reconstruction. Do not
  turn a late-life portrait into an undocumented exact 1835 face.
- Assemble/refine Mark from the T-1789 Blender library on the shared skeleton. Custom face,
  hair, clothing or accessories are allowed where the evidence or a clearly stated
  reconstruction warrants them; reusable improvements go back into the library.
- Produce inspected Blender renders (front/three-quarter/profile, neutral lighting and
  period-clothed full body) and export LODs through T-1787. Preserve the Blender master,
  texture sources, rights/provenance, recipes and evidence links.
- Bind the browser actor to the existing `beaubien_mark` person ID and appropriate
  authored location/state; do not alter historical placement merely to make the demo easy.
  The actor idles, walks when driven, can perform a greeting/talk gesture, can be selected/
  approached, and opens or hands off to the existing person information.
- Render and inspect Mark in the **real 1835 browser scene** at desktop and mobile, close,
  conversation and street distances. Check terrain contact, scale against doors/people,
  shadows, hair/clothing artifacts, animation foot slide, LOD popping, textures and
  historical read. A Blender beauty render alone does not close the ticket.
- Record actual shipped size, triangles per LOD, materials/draw calls, texture memory,
  animation cost and frame impact. Correct visible/performance defects rather than
  weakening the scene budget to admit the first person.

**Stop condition:** a visitor to Chicago 4D can encounter a credible, explicitly sourced/
reconstructed Mark Beaubien in the browser, and the complete path remains portable to a
future Unreal import from the same Blender source.
