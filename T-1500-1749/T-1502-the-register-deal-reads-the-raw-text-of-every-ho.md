---
id: T-1502
title: The register deal reads the raw text of every household card as a name pool, so any pass writing a proper name onto one can silently retire a documented man from it
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-21
closed: null
pr: null
claimed_by: run 9/23/2026, 10:18:39 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-24T03:18:39.537Z
decision: null
decision_answer: null
---

The register deal reads the raw text of every household card as a name pool, so any pass writing a proper name onto one can silently retire a documented man from it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Written 2026-09-24 before work. Of the ticket's three routes, this takes the second and the
third together, and NOT the first: reading only `name` fields would drop the prose the
guard's own docstring says it reads on purpose, and would re-deal roofs today.

1. **The harvest reads declared key paths, not raw text.** `town_surnames()` walks the
   JSON values of the same three sources and reads a capitalised word only under a key
   path declared `read` in a committed list, per record kind (structures, households,
   exclusions). Measured 2026-09-24: the value walk reproduces the raw-text pool exactly
   (3,127 words, none from a JSON key), under 275 paths. Every one is declared `read`, so
   **no seat and no refusal changes** — `--report` is identical before and after.
2. **An undeclared path carrying a proper name is a red gate, not a silent refusal.**
   `--check` fails if any string under a key path the list does not declare carries a
   capitalised word, naming the record kind, the path, a file and the word. That is
   T-1489's `persons[].employment.business_name` caught at the writer's own PR.
3. **Every `already named in the town` refusal names its cause**: the file and key path the
   word was read from (and how many other places say it), in `--report` and in `--check`'s
   drift output when a settled seat is lost — so a collision is never again one
   unexplained DRIFT line.
4. **A `--self-test`** proves each assertion fires when broken: an undeclared path, a word
   under an `ignored` path kept out of the pool, a refusal naming its file and key, a lost
   seat printing its refusal, and the declaration still reproducing today's raw pool.
   Registered in check.sh as a self-test step.
5. **Nothing is re-ruled.** Whether any declared path (e.g. `persons[].workplaces[].business_name`,
   the same shape as the one that retired Eels) SHOULD be read is reported, with the
   refusals that rest on it alone, and left for a later ruling.

**Found by T-1489, 2026-09-21, as a red gate rather than as a reading.**
`tools/replace_invented_residents.py` decides which documented men of the register may
head an anonymous roof. One of its refusals is `town_surnames()`: every
`\b[A-Z][a-z]{2,}\b` word in the RAW TEXT of every structure record and every
non-`hh_inf_` household card — prose, notes and all — is read as a name the town has
already said something about, and a candidate whose surname is in that set is refused.

The guard already knows it can poison itself: its own docstring says the `hh_inf_`
households are excluded precisely because reading back a name this pass wrote would
refuse that man on the next run. The hole is that the exclusion is by DIRECTORY
PREFIX, and nothing stops a different pass writing a proper name into one of the cards
that IS read.

T-1489 did exactly that by accident. Its `persons[].employment` block carried the house's
`business_name` beside its id, so 33 cards in `households/` gained the word `Eels` —
and the deal stopped seating the documented tailor **Thomas S. Eels** on
`hh_inf_tailor_north_02`, reporting "already named in the town (eels)". One gate step
caught it; nothing else would have. T-1489 answered for itself by dropping the name
(the id resolves to it in one lookup) and asserting in its own `--self-test` that no
value in that block may carry a capitalised word.

**What is still owed.** That assertion guards ONE writer. Any future pass that puts a
proper name into a household card — a landlord, an employer, a witness, a vessel's
master — retires a documented man from this deal silently, and the failure surfaces as
one unexplained DRIFT line in a step about something else. The answer is probably one
of: read the harvest from declared NAME FIELDS rather than from raw text; or keep a
declared list of the keys the harvest may read and gate it; or have the harvest state,
per refused candidate, WHICH file and which key the word came out of, so a collision
names its own cause. That is a decision about the guard, not a bug fix, which is why
this is a ticket and not a patch.
