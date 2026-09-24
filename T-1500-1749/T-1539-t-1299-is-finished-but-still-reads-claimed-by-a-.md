---
id: T-1539
title: T-1299 is finished but still reads claimed by a run that died on 2026-09-21: close it, or say what is left. Its acceptance 1-4 and 6 are demonstrably in dev, and T-1515 fixed the acceptance-5 root it was held on
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: null
pr: null
claimed_by: run 9/24/2026, 8:16:58 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36004171336
claimed_at: 2026-09-24T13:16:58.285Z
decision: null
decision_answer: null
---

T-1299 is finished but still reads claimed by a run that died on 2026-09-21: close it, or say what is left. Its acceptance 1-4 and 6 are demonstrably in dev, and T-1515 fixed the acceptance-5 root it was held on.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured on `origin/dev` at ce2d616, 2026-09-24**, while T-1530's slice was picking:
T-1299 sits at row 4 of `list --workable` under a claim from `run 9/21/2026, 3:47:17 AM
CT` — three days old, so `claim` would steal it — and a run that steals it finds the work
already done. Every clause it is still open for is in `dev`:

- **1, 2, 3.** The ten press cards carry their trade in the singular `occupation` field,
  written by `tools/derive_resident_roles.py`, each with a `promoted_from_roles` block
  naming `ticket: T-1299` and carrying the ROWS' citations rather than the block's own —
  which is what T-0837's write gate needed to pass on the evidence. Checked on
  `curtiss_l_g` (attorney), `king_tuthill` (clothier), `sherman_silas_w` (sheriff),
  `mulford_james_h` (jeweller/silversmith/watchmaker), `jones_william`,
  `hubbard_elijah_kent`, `taylor_william_h`.
- **4.** The census count's ruling is on the cards.
- **6.** `tools/measure_layer_reads.py` declares both banked fields as READS with the
  expression that renders them — `persons[].roles[].place` and
  `persons[].roles[].employer_or_body`, with the `!== 'not_stated'` guard.
- **5 — the clause the PR was held on — was fixed by somebody else.** The six cards that
  lost their Fergus 1839 row all hold it again (`hubbard_elijah_kent` "banker, 47-",
  `jones_william` "justice of the peace", `king_tuthill` "New York clothing store",
  `mulford_james_h` "& Edward", `sherman_silas_w` "ex-sheriff", `taylor_william_h`
  "(Dan. Taylor)"). The cards' own notes say why: **T-1515** reads the 1839 directory off
  its own crosswalk whatever the 1835 field holds, which is exactly the fix T-1299's
  hand-on paragraph said "looks right" and sized as possibly needing a `split`.

So the unit is spent. What is left is a state, not work: either `done` it against the PR
that actually carried it, or say in the ticket which clause a reader should still
disbelieve. Note the held PR it names, **#1617, is a `kevinrhaas/custom` number** from
before the 2026-09-23 split, so the tickets repo's settle workflow can never resolve it
and no branch in `kevinrhaas/chicago` carries the work — it reached `dev` by another
route. That is the part a person has to decide.
