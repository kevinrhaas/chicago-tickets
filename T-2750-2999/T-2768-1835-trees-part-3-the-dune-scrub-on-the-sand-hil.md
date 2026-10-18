---
id: T-2768
title: 1835 trees, part 3: the dune scrub on the sand hills from about 12th-16th to 25th Street, low red cedar, ground pine and sand cherry (needs a red cedar model and leaf tile in the T-2743 tree models)
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: T-2744
opened: 2026-10-18
closed: null
pr: 1032
claimed_by: run 10/18/2026, 11:30:37 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T16:30:37.016Z
decision: null
decision_answer: null
---

1835 trees, part 3: the dune scrub on the sand hills from about 12th-16th to 25th Street, low red cedar, ground pine and sand cherry (needs a red cedar model and leaf tile in the T-2743 tree models).

Piece 3 of 3 of **T-2744 — 1835 trees from the research: the 16th-18th Street shore cottonwood grove, cedar and sand-cherry dune scrub, North Side woods at their recorded density with the Rush Street path, Kinzie cottonwoods, fort fruit trees and Harmon's orchard**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2744 was split (2026-10-18T10:50:34.470Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/18/2026, 5:49:27 AM CT — held by the run that split it

The run that split it (by hand) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Added 2026-10-18: the North Side sand hills, the swales, and the cottonwood trunk

Kevin asked (thread "1812/1835 tree cover", 2026-10-18) for plants beyond the documented groves, from the land, water and climate. The ecology analysis is `/mnt/project-files/trees-1812-1835/ecology-analysis.md` §2.1-2.3; this ticket takes the dune habitats so the conifer templates are built once and used on both shores:

- **North of the river too**, between the Kinzie house and the lake: "a vast range of sand-hills, covered with stunted cedars, pines, and dwarf-willow trees" (Wau-Bun 1856; Chicago Magazine 1857). Red cedar, common and creeping juniper ("ground pine"), a few low pines (species unstated, graded inferred), dune willows, bearberry. Shot `eco-shots/shore-north-of-river.png` shows it bare today: the biggest empty area in the scene.
- **Interdunal swales**: the wet hollows between sand ridges, found from the heightfield. Rushes, sedges, willow and red-osier dogwood clumps, cottonwood seedlings (Cowles 1899).
- **Foredune woody plants**: sand cherry mats, dune willows, dune cottonwoods singly or in twos and threes.
- **Cottonwood trunk check**: the T-2766 grove trunks look slender for the 60-100 cm dbh the species record gives (likely the two-stem fork splitting the radius). Check against the record and period photographs and fix in tree-model.js.

Rendering: conifer and shrub templates in the T-2743 instanced system (near / mid / far, dithered level change), clumped placement. Positions are reconstructed under one liberty; species are attested (cedar, pine, willow, sand cherry) or inferred (juniper, bearberry). Hold every tier's detail ceiling, 1835 memory and the town_backyard frame.
