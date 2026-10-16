---
id: T-2594
title: T-2582's roof and 1904 street KTX2s are written top row first, so they land mirrored along v against their WebPs and the normal_gl relief is lit inverted across the course: rewrite them bottom row first as T-2589's FLIP_V does, and check the shingle relief against the WebP path
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

T-2582's roof and 1904 street KTX2s are written top row first, so they land mirrored along v against their WebPs and the normal_gl relief is lit inverted across the course: rewrite them bottom row first as T-2589's FLIP_V does, and check the shingle relief against the WebP path.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (T-2589, 2026-10-16)

- `ktx create` (KTX-Software 4.3.2) has no flip option and writes rows top first; three uploads a `CompressedTexture` with `flipY` false, so the file's top row lands at v = 0, where the WebP path (flipY true) puts it at v = 1.
- Measured on the frontage: with its three sheets written bottom row first, the KTX2 captures match the image path at 57-76 dB PSNR, the residual only compression noise on the timber (`/tmp` shots on the T-2589 PR). Top-first files would mirror every board's figure.
- For `normal_gl`, a v-mirror without negating green inverts the relief along v. `roof-relief.js` derives its UV in the shader; check which way its frame runs before deciding whether the roofs read it.
- Effort: S. Re-run `tools/ktx2_sheets.py` with the roof and street sheets in `FLIP_V` (or flip every sheet, and drop the set), then compare captures on and off `?ktx2=0`.
