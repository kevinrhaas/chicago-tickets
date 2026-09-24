---
id: T-1549
title: The West Division spacing compares five lines at five different traced extents: mean_east is an unweighted vertex mean, so extending or truncating any trace moves that line's measured position
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: null
pr: 30
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The West Division spacing compares five lines at five different traced extents: mean_east is an unweighted vertex mean, so extending or truncating any trace moves that line's measured position.

`tools/measure_west_division_spacing.py` positions each north-south line by
`mean_east()`, an UNWEIGHTED mean of that line's traced vertices:

    def mean_east(street):
        pts = [(float(e), float(n)) for e, n in street["path_local_enu_m"]]
        return sum(p[0] for p in pts) / len(pts)

It is not arc-length weighted, and nothing bounds the northing range it averages
over. The five lines it compares are traced to five different extents, measured
2026-09-24 on the T-1490 branch:

| line | pts | northing range (local m) |
| --- | ---: | --- |
| `jefferson` | 2 | -400.0 .. +381.9 |
| `canal` | 4 | -400.0 .. +400.0 |
| `clinton` | 2 | -400.0 .. +80.0 |
| `des_plaines` | 2 | -400.0 .. +80.0 |
| `west_water` | 10 | -404.0 .. -86.6 |

For a two-point line the mean IS the midpoint of its two endpoints, so the line's
measured position is decided by where somebody stopped tracing. That makes the
spacing comparison sensitive to trace EXTENT, which is not a fact about the town.

**MEASURED, TWICE, IN ONE DAY.** Both open branches perturbed it without touching a
street's position:

- T-1490 carried `jefferson` north from +80 to +381.887 on its own surviving
  control, deliberately NOT refitting the bearing. Modern Jefferson jogs 9.1 m west
  between Fulton and Kinzie (T-1490 measured that jog itself), so averaging the
  longer line pulled its mean 3.62 m west: -396.89 -> -400.51.
- T-0141 cut `west_water` 22.53 m shorter under T-0768's rule, and its mean moved
  the other way, -13.15 -> -11.24.

The T-1490 shift is not cosmetic. `jefferson -> des_plaines` went from short by
~51.7 ft (~15.76 m, INSIDE the ~17.5 m datum residual) to short by 63.6 ft
(19.39 m, beyond it) — and with it the LAST short interval that sat inside the
residual. T-1540's own self-test then fires, correctly:

    FAIL at least one short interval must sit INSIDE the residual, or the
         measurement is not discriminating and every interval could be called
         a defect

That assertion is right and must not be weakened. What it caught is that the
measurement lost its ability to tell a real shortfall from pinning noise — because
a trace got longer, not because the grid changed.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. Each line's position is derived over a COMMON, STATED northing band — the band
   where the lines actually run beside each other — or by a method that does not
   move when a trace is extended or truncated at one end. Whichever is chosen is
   argued in the module's own docstring against the two movements above.
2. Re-deriving with the fix, `jefferson` and `west_water` do not move merely because
   T-1490 and T-0141 changed their extents; any residual movement is stated and
   attributed.
3. `--self-test` passes on its own terms, with the discrimination assertion intact
   and NOT relaxed. If no short interval genuinely sits inside the residual after
   the fix, that is a finding about the grid and is written up as one rather than
   asserted away.
4. The `inside_the_datum_residual` flags and the `short_by_ft` figures are restated
   wherever they are quoted — T-1540's changelog entry and any liberty that reasons
   from them.
5. Blocks T-1490 (#28) and T-0141 (#16), both of which currently trip this.
