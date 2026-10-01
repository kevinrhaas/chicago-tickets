---
id: T-1806
title: The five H2 boarding houses raised to their beds: upper windows and stovepipes sized from capacity, north and west, baked
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1780
opened: 2026-10-01
closed: 2026-10-01
pr: 232
claimed_by: run 10/1/2026, 9:33:28 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-01T16:19:43Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36867729968
claimed_at: 2026-10-01T14:33:28.264Z
decision: null
decision_answer: null
---

The five H2 boarding houses raised to their beds: upper windows and stovepipes sized from capacity, north and west, baked.

Piece 1 of 3 of **T-1780 — The smaller houses and the books: H1/H2 fenestration and chimneys from capacity once T-1293/T-1196 rule what they are, the frame budget read, a boarding-house row screenshot, T-1214 handed on**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The five standing H2 houses the lodging model counts as boarding houses
(`recon_1835_north_h2_022/028/030/045`, `recon_1835_west_035`, all `frame_tavern`,
`medium_boarding_house`) each carry `form.upper_windows` and `form.stovepipes` sized from a
`reconstruction.capacity` block that names the lodging-model row it read and the rule that
turned beds into the count, the way T-1778 sized the H3. The rule is written into their
generators (`generate_north_infill.py`, `generate_west_infill.py`), so `--check` re-derives
them; the five are rebaked with `bake.sh --only`; LIBERTIES records the H2 window band.
Visible: from the street, each house's upper storey shows its chamber rhythm instead of the
tavern's five bays, and stovepipes stand through the roof beside the two stacks.
The H2 *merchant* houses (`frame_dwelling`, `merchant_or_professional_house`) are not
boarding houses in the model and do not move.
