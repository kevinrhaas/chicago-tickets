---
id: T-0777
title: assets/manifest.web.json's $note is rewritten with escaped em-dashes, so its own generator does not reproduce what dev committed
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-05
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: dev's assets/manifest.web.json $note now matches what web_derivatives.sh writes."
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
---

assets/manifest.web.json's $note is rewritten with escaped em-dashes, so its own generator does not reproduce what dev committed.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

assets/manifest.web.json's $note is rewritten with escaped em-dashes, so its own generator does not reproduce what dev committed.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Found while shipping T-0686 (PR #882). `tools/web_derivatives.sh` writes
`assets/manifest.web.json` with `json.dump(..., ensure_ascii=True)` (or equivalent), so the
`$note` field's em-dashes come out as `\u2014` while the copy committed on `dev` carries them
literally. Any run that touches the file therefore produces a one-line diff that has nothing
to do with the hashes it is banking, and the file's own instruction — "the remedy for a
mismatch is `tools/web_derivatives.sh --only <name>`, never an edit of this file" — means
nobody can tidy it by hand without breaking that rule.

**Acceptance:** the tool's output for an unchanged tree is byte-identical to what is
committed; the fix is in the writer, not in the file. Same family as T-0687 (a generator that
no longer reproduces its own record).

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** dev's assets/manifest.web.json $note now matches what web_derivatives.sh writes.
