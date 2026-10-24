---
id: T-3088
title: Refine the horse anatomy and near silhouette against cleared views
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-2800
opened: 2026-10-23
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

Refine the horse anatomy and near silhouette against cleared views.

Piece 3 of 4 of **T-2800 — Build the first anatomically grounded photographic horse master**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2800 was split (2026-10-23T23:58:39.740Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1.2h ago, Codex resumed horse photographic refinement after own merged PR1244 10/23/2026, 5:45:48 PM CT — held by the run that split it
- branch `steward/t2794-t2800-photographic-refinement-20261023-2245` — the splitter's own
- branch `steward/t2800-planted-standing-v16-dev-20261023`
- branch `steward/t2800-standing-idle-dev-20261022`

The run that split it (by hand) may be working one of the pieces now.

## Scope and acceptance

Finish one horse's source-bounded anatomical near master, retaining T-2800's
unmet anatomy/topology and source-comparison requirements. No fleet/breed variants.

- Use cleared anatomical and dated period references to define scale, body
  proportions, head/eyes/ears/muzzle, neck/shoulder, limbs/joints/hooves, mane and
  tail. Keep this a generic working animal, not an identified horse or claimed breed.
- Resolve actual near silhouette/anatomy discrepancies at matched front, profile,
  quarter and detail views. Inspect the actual images and maintain a discrepancy
  register; do not treat the eye-only child as acceptance of the whole head/body.
- Provide a source-bounded canonical master with clean supported topology for
  T-2803. Test metre scale/axes, connected joints and weight-bearing hoof contact;
  every changed geometry/skin must have fresh protected-source and exported proof.
- Retain rights/modern attribution, per-attribute confidence and liberties for
  coat, grooming, unknown dimensions and unpictured features. Do not derive from
  rights-pending references or invent Chicago ownership.
- Use the supported canonical build path, without installing Blender on the
  improve runner. Hand exact accepted master hashes to the surface/LOD sibling.
