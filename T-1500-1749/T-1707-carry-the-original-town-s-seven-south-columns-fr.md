---
id: T-1707
title: Carry the Original Town's seven south columns from their terrain clip at N -400 to Madison Street, the plat's own south boundary, and emit the plat's last tier: street control on ground T-0219 already modelled, which is the one thing south_plat_beyond_committed_control's 104 roofs still wait on
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1203
opened: 2026-09-27
closed: null
pr: 154
claimed_by: run 9/28/2026, 1:49:48 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36387998473
claimed_at: 2026-09-28T06:49:48.818Z
decision: null
decision_answer: null
---

Carry the Original Town's seven south columns from their terrain clip at N -400 to Madison Street, the plat's own south boundary, and emit the plat's last tier: street control on ground T-0219 already modelled, which is the one thing south_plat_beyond_committed_control's 104 roofs still wait on.

Piece 1 of 4 of **T-1203 — Build the South Division's outer ground to its seats: the Fort Dearborn Addition and Michigan Street tract dwellings, the Clark–State cottages south of Washington where the ground allows, the packing and slaughter yards on the South Branch, the country places outside the plat**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Found by a later run (2026-09-28, while landing PR #144)

The split that made this ticket left the reconstruction order book naming its
parent, and `check.sh` is red on dev and on every branch because of it:

```
== the 1835 reconstruction order book re-derives, no bucket is overfilled, and every work order names a live ticket
FAIL: the book orders work from tickets nobody can claim — sweep the owner tables
onto the live successors (T-1420): structures/ordinary_dwellings/south has 67 left
and is ordered by T-1203, which is split
```

Measured 03:50Z on a clean checkout of `steward/t-1587-street-readings`, whose
diff does not touch `data/reconstruction/1835_reconstruction_order_book.json` —
so the red is dev's, dated to `T-1203: split` (tickets `b14284b`, 03:04:48Z), not
that branch's. 678 of 679 gate steps pass; this is the one.

This is the same failure T-1575 recorded and closed for `T-1556`: the order
book's owner tables have to be swept onto the live pieces when a ticket they
name is split. Whoever finishes this piece owns the sweep —
`structures/ordinary_dwellings/south`'s 67 remaining roofs want ordering by
whichever of T-1707-T-1710 actually builds them, and until they are, no branch
in the repository can get a green `check.sh`.
