---
id: T-3796
title: Public site: a small dismissable Preview marker on every page, saying the site is early and improving with early adopters' feedback; dismissal remembered
state: review
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2400
claimed_by: run 11/27/2026, 10:27:24 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T16:27:25.917Z
decision: null
decision_answer: null
---

Public site: a small dismissable Preview marker on every page, saying the site is early and improving with early adopters' feedback; dismissal remembered.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:** (a) Every page of the public site (`site/`, the pages that load `js/show.js`) shows a small "Preview" marker in the site's Control Room look, a few words at most. (b) One tap or click dismisses it and the dismissal is remembered on that browser. (c) Works at 390x780 and desktop, never covers the menu or the Enter button, hidden in print. (d) Before/after pictures in the PR and close note.

Owner, 2026-11-27: "make the production website mark it with a \"Preview\" indicator you can dismiss so that people know its early and we are contiuning to develop and improve with early adopters and feedback, do not be wordy make this preview marker very elegant and simple and clean and not verbose and annoying".

## Result (PR #2400)

A quiet pill in the corner of every public-site page: **● PREVIEW │ Feedback ×** ("Still improving" taken out at Kevin's word, 2026-11-27). Feedback goes to Contact; × hides it for good on that browser.

Desktop, before | after:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/bffb0e2a3395d16fb32d0cfcf4dbb782216f6c95/evidence/T-3796-preview-marker/desktop-before-after.jpg?raw=true" width="900">

Close-up:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/bffb0e2a3395d16fb32d0cfcf4dbb782216f6c95/evidence/T-3796-preview-marker/desktop-marker-close-up.png?raw=true" width="400">

Phone, before | after:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/bffb0e2a3395d16fb32d0cfcf4dbb782216f6c95/evidence/T-3796-preview-marker/phone-before-after.jpg?raw=true" width="640">

Phone after × and a reload:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/bffb0e2a3395d16fb32d0cfcf4dbb782216f6c95/evidence/T-3796-preview-marker/phone-after-dismiss.jpg?raw=true" width="320">
