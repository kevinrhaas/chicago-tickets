---
id: T-1727
title: Structure versions by URL: ?structure=<id>&version=<label> loads one committed alternate of one structure, so competing builds of the same house can be compared side by side on dev
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: null
claimed_by: run 9/28/2026, 9:56:42 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-28T14:56:42.415Z
decision: null
decision_answer: null
---

Structure versions by URL: ?structure=<id>&version=<label> loads one committed alternate of one structure, so competing builds of the same house can be compared side by side on dev.

**Why (owner, 2026-09-28).** The owner wants several builds of the same house, starting with the
Glessner House, each on dev at once. He'll open them side by side, pick one, and then only that
one goes to dev's default and later to main. Separate branch deploys are not needed: *"parameters
so if its like structure=glessner_house&version=… that is fine"*. `main.js` already reserves this:
*"Other state (a structure to open, a camera) belongs in further query parameters beside `year`,
never in more path segments."*

**Acceptance:** (one demonstration, never weakened to pass)

1. **Storage.** An alternate lives beside its structure as a committed record plus mesh, for example
   `data/structures/versions/<structure_id>/<label>.json` with its baked asset. The canonical
   record stays where it is and remains the default. A version carries every provenance field a
   structure does (sources, tiers, liberties), so an alternate is never less honest than the
   default.
2. **Selection.** `?structure=<id>&version=<label>`, alongside `?year=` and `?anchor=`, swaps exactly
   that one structure for that version. Nothing else in the scene moves. An unknown id or label
   falls back to the default and says so in the HUD. It never fails silently or blanks the scene.
3. **Visible label.** While a version is active, the HUD and the structure's card name the version,
   so two screenshots can't be confused.
4. **Validation.** `validate.py` and `validate.py --stale` cover versions exactly as they cover
   structures. A version with no mesh, or a stale mesh, is a red gate. The publish step copies the
   versions to the mirror, and the boot payload does **not** grow: versions load lazily, only when
   asked for.
5. **Labels.** Labels are short neutral strings (`v1`, `v2`, `b`, `hall-plan`, and so on). **Never a
   model identifier**, which the repo forbids in any artifact. The owner keeps his own mapping from
   label to run.
6. **Proof.** A smoke assertion loads the default and one fixture version at 390×780 and 1280×800
   and checks that the swap happened and nothing else did. Until T-1729 exists the fixture can be
   any 1835 structure.
7. **Promotion.** A documented one-command path to make a version the new default:
   `tools/promote_version.mjs <id> <label>` moves the files, keeps the old default as a version, and
   re-bakes if needed. The owner's final call becomes one reviewable PR.

**Not blocked by terrain.** This needs no 1904 ground, so a lane can take it now while T-1250–T-1252
proceed.
