---
id: T-1729
title: Build the Glessner House at 1800 Prairie as it stood in 1904: the first researched version, from the HABS drawings, the Sanborn 1911 sheet and the Prairie library's dossier
state: split
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-09-28
pr: null
claimed_by: null
blocked_on: T-0474
needs_bake: false
closed_at: 2026-09-28T14:57:22.325Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Build the Glessner House at 1800 Prairie as it stood in 1904: the first researched version, from the HABS drawings, the Sanborn 1911 sheet and the Prairie library's dossier.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked for the 1904 Prairie Avenue / Glessner House render path, 2026-09-28

Source library: **`chicago/prairie_1904_v1/`**, viewable at https://chicago.polecat.live/prairie-1904/viewer/. Read its README and `docs/research-gaps.md` first; cite library rows and dossier entries by id.

**Why (owner, 2026-09-28):** the Glessner House is the view a visitor lands on in 1904 (T-1252's
spawn) and the first structure the owner will compare versions of (T-1730). This ticket builds the
**default version**. Carved out of T-0475, which keeps the rest of the landmark core.

**Acceptance:** (one demonstration, never weakened to pass)

1. A structure record `glessner_house` at **1800 Prairie**, the SW corner of E. 18th Street, on the
   T-0474 parcel. Its footprint follows the **HABS IL-1015** measured drawings (the six acquired
   sheets in the library's `glessner-dossier.json`; the 4D project already holds
   `data/sources/habs_glessner_house_il_1015.json`), checked against **Sanborn 1911 sheet 28**
   (stone, courtyard plan, coach house).
2. **Phase discipline**, from the dossier's own sequence: the 1885 Richardson sketch is **design
   intent**, not as-built. The 1888 *Inland Architect* plate and the circa-1888 porte-cochère
   photograph date the exterior. The 1892 changes are interior. Build the house **as it stood in
   1904** and cite, attribute by attribute, which dated source each value rests on. Modern
   restoration finishes count only where tied to a historic photograph.
3. Exterior massing, roof forms, the granite courtyard walls, the coach house and the service wing,
   each attribute tiered. The interior is **not** in scope.
4. Seen from the T-1252 landing pose, the house is recognisable against the 1888 plate and HABS
   photographs; screenshots at both viewports go in the PR.
5. Baked, `validate.py --stale` green, frame budget measured.

Blocked on **T-0474** (the parcel). It also needs T-1252's ground to stand on.
