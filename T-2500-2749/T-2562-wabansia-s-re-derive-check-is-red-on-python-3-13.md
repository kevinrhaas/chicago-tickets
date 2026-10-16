---
id: T-2562
title: Wabansia's re-derive check is red on Python 3.13: an embedded docstring's indentation differs by interpreter
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: null
claimed_by: run 10/16/2026, 8:03:40 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38904221258
claimed_at: 2026-10-16T13:03:40.839Z
decision: null
decision_answer: null
---

Wabansia's re-derive check is red on Python 3.13: an embedded docstring's indentation differs by interpreter.

Found by T-2552 (2026-10-16), at the owner's request to ticket any consistent red: `check.sh`'s step "Wabansia's streets re-derive from the readings and the committed Kinzie line" (`python3 tools/seat_wabansia_streets.py --check`) fails on a clean `origin/dev` checkout with `RED wabansia_seating.json § tract_polygon_local_enu_m does not re-derive from the readings`.

## Cause

Not the data. `_trace_doc` stores `_tract.__doc__` verbatim as `tract_polygon_local_enu_m.sides` (tools/seat_wabansia_streets.py:572), and the check compares the committed JSON byte for byte. **Python 3.13 strips the common leading indentation from docstrings at compile time**; 3.11 does not. The committed file was written on 3.11 (CI pins `python-version: '3.11'`), so the step is green in CI and red on every 3.13 interpreter: this cloud sandbox runs 3.13.16. Running `--write` on 3.13 changes exactly one line of `data/traces/wabansia_seating.json`: the `sides` string, de-indented. Nothing else moves.

## Fix

Pass embedded docstrings through `inspect.cleandoc()` when writing AND when comparing, so the text is the same on every interpreter. Re-write the trace once (one line changes) and check that it stays green on 3.11 and 3.13. Grep the other tools that put a `__doc__` into a committed file (296 tools reference `__doc__`; most only print it as usage) for the same hazard.

## Acceptance

- `seat_wabansia_streets.py --check` is green on Python 3.11 and 3.13 against the same committed file.
- Any other committed file that embeds a docstring is normalised the same way, or named here as not affected.
