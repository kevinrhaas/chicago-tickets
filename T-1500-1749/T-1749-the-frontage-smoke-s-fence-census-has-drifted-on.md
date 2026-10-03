---
id: T-1749
title: The frontage smoke's fence census has drifted on dev: 28 fence runs where the clause holds 31, and the two checks that read it are red on dev and on every branch
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: T-1752 (#201) restated the fence census with its cause (32); the checks are green on dev."
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The frontage smoke's fence census has drifted on dev: 28 fence runs where the clause holds 31, and the two checks that read it are red on dev and on every branch.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 140 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> It is a red on dev's own tree, measured on both sides this run with byte-identical census figures, so it is nobody's branch to fix in passing: every slice that runs desktop part 2 pays to re-derive it and then steps over it. It belongs to the frontage census clause, not to any build ticket in the queue.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. The two checks below are green at desktop part 2, **or** the clause in
   `tools/smoke_renderer.mjs` is restated to the measured figure with the cause
   written into it in the shape every other entry in that comment block has —
   which ticket moved the fence count, from what to what, and what did NOT move
   with it. Never the number alone.
2. Whichever way it goes, `data/liberties.json` and the other places that hold a
   fence population are restated from the measured file, not from this ticket.

## THE MEASUREMENT, SO NOBODY PAYS FOR IT AGAIN

Taken 2026-09-29 on the steward runner, `--published`, desktop part 2, twice:
once on `steward/t-1547-green-tree-frontage` and once on a clean `origin/dev`
worktree at `9aee39d0`. **Both are 86 passed / 2 failed, and the census figures
are byte-identical:**

```
5 record(s) [green_tree_frontage, sauganash_frontage, river_walk_frontage,
             lasalle_crossing_frontage, town_street_edge],
47 walk(s), 39 crossing(s), 18 post(s), 28 fence run(s),
835710 vertices, 120 wall(s) refused, problems [none]
… town_street_edge: 36 block face(s), 3224.7 m of walk, 28 fence run(s),
  255 walking deck(s) registered
```

The two reds:

- `the frontage layer lays all five records' walks and stands their posts`
- `the street edge is generated from the plat, not placed on one block`

**Walks, crossings and posts all match the clause** — 47 / 39 / 18, exactly what
`smoke_renderer.mjs` holds after T-1630. The fence count does not: the clause
expects **31** and the town lays **28**. The refusal count is 120 against a
clause comment whose last stated figure is in the nineties, so that one has
drifted too and the two almost certainly moved together — the fence rule and the
street-fence refusal are the same clause read from opposite sides, and every
prior entry in that comment block records them moving in a pair (T-1053: fences
32 → 31 and refusals 85 → 86, "the two move together and only together").

So this is most likely a ledger of lot-class changes that was never written down,
not a renderer fault: three platted lots stopped taking a street fence. Find
which three and why before touching the number.

`tools/dev-smoke-state.mjs` had desktop part 2 recorded PASS at
2026-09-28T18:06:58Z (stage 2-3), so the drift arrived on dev after that.

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** T-1752 (#201) restated the fence census with its cause (32); the checks are green on dev.
