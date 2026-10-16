# T-2671 — grade colours gold / silver / bronze: captures

Playwright (headless Chromium, software GL), source tree served locally, `?year=1904`,
the `glessner_house` anchor, BY GRADE (the Confidence chip) on.

- `compare-bygrade-1440x900.jpg`, `compare-bygrade-390x844.jpg` — before (dev @ d53615dc)
  and after, side by side, at the Glessner front. After: the door and windows (Attested)
  gold, the granite and street (Inferred) silver, the dithered walk and trees
  (Reconstructed) bronze.
- `before-gallery-sheet.jpg`, `after-gallery-sheet.jpg` — every grade element (card dots,
  conf chips, people dots and chips, HUD chip dot, menu and legend swatches, census bar,
  reconstructed marks) in all four machine skins, dark row then light row.
- `after-cvd-dark.jpg`, `after-cvd-light.jpg` — the after gallery (Control Room) under
  simulated protanopia, deuteranopia and tritanopia (Machado 2009, severity 1.0).

Contrast and colour-vision distances are re-measured on every gate run by
`tools/check_grade_colors.mjs --print`.
