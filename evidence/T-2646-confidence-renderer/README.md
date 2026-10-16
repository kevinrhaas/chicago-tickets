# T-2646 — Confidence view renderer: captures and readings

Playwright, headless Chromium (software GL), source tree, 390×844, the Confidence view on.
Each sheet: the default BY GRADE look; X-RAY set from the test hook
(`__chicago4d.confidence.setGrade('inferred', {mode:'ghost', opacity:0.5})`,
`setGrade('reconstructed', {mode:'ghost', opacity:0.25})`); and a mixed set of looks.

- `looks-1904-390x844.jpg` — the Glessner front. Ghosted granite and trees are see-through;
  the Attested door and windows stay solid gold.
- `looks-1835-390x844.jpg` — the 1835 spawn.

Draws and triangles, read from `__chicago4d.stats()` after one `step()` (both passes counted):

| scene | look | draw calls | triangles | budget (calls / tris) |
|---|---|---|---|---|
| 1904 Glessner, 390×844 | BY GRADE | 124 | 3,815,074 | 360 / 4,600,000 |
| 1904 Glessner, 390×844 | X-RAY | 96 | 2,685,883 | 360 / 4,600,000 |
| 1835 spawn, 390×844 | BY GRADE | 196 | 1,841,730 | 330 / 3,400,000 |
| 1835 spawn, 390×844 | X-RAY | 135 | 1,674,719 | 330 / 3,400,000 |

X-RAY draws fewer because what holds only ghosted grades leaves the opaque pass and the
sun's shadow pass, and is drawn once, in the ghost pass.

Frame cost, `tools/measure_walk_frames.mjs --only mobile --tiers light --moves walk,turn [--xray]`
(390×780 touch, 4× CPU throttle, the mid-tier phone stand-in; the draw itself is skipped, as
the tool does on a GPU-less runner, so these are the frame's JavaScript), run back to back on
a shared 4-core box under load: scripted ms median / p95 — walk 6.0 / 11.1 plain, 7.1 / 11.8
X-RAY; turn 7.5 / 14.4 plain, 8.7 / 15.2 X-RAY. The p95 stays inside a 16.7 ms (60 fps) frame.
