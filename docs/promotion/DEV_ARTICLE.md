# Building RecallForge: an offline study workspace with source-linked practice

I built [RecallForge](https://dagerottdev.github.io/RecallForge/) to make the loop between practice, mistake review and revision easier to repeat. It is free and open source. You can try the browser viewer without an account, and its working study data stays in your local browser.

The new introductory samples cover investment fundamentals, technical analysis and financial risk, alongside the original Cell Biology sample. Each finance pack contains ten original questions with explanations and public reference links. These are demonstrations of the workspace, not official exam questions or complete preparation courses.

## A small runtime with a complete study loop

The viewer uses JavaScript, HTML and CSS. IndexedDB stores packs, sources, attempts, unfinished sessions and revision data. The built distribution is a single HTML file containing its runtime, fonts, PDF worker and samples, so the viewer can also be opened offline. Building it uses npm dependencies; running the existing distribution does not require a backend, account service or AI API key.

A learner can import a validated JSON pack, study with immediate feedback, or run an exam using that pack's timing and scoring settings. Results include explanations and source references. Wrong and skipped questions can feed a focused retest, while daily revision schedules another pass over saved questions.

## Reproducibility where it helps

Seeded shuffling and topic-balanced custom mocks make question selection reproducible. The engine validates pack structure, answer definitions, timing and total marks before use. It preserves the distinction between single-answer and exact-set multiple-answer questions.

Overall exam timing uses an absolute deadline: closing the page does not grant a new exam period. Saved per-question time likewise does not reset simply because a learner navigates away and returns. Those details matter if a saved session is supposed to mean the same thing after reopening.

## Sources stay connected to the question

A question can link to a public reference or a local source file/page/excerpt. Local text, image and PDF sources can be opened from the workspace. A pack export contains its metadata and links; the full workspace backup is the route for carrying local source files to another device.

The finance demonstrations use original wording and numeric scenarios. References support the concepts, and deterministic tests independently calculate the numerical answers. Their difficulty is inferred rather than calibrated to official examination papers, and there has been no independent human subject-matter review.

## Local storage needs an escape route

Browser-local storage makes the app usable without an account service, but the data belongs to that browser profile and site address. Clearing browser data or changing devices can lose access to it. Portable backups make that boundary explicit.

Backups support plain JSON or optional password encryption, previewed merge or replace, and one restore recovery snapshot. Encryption protects the exported file; it does not encrypt the working IndexedDB database. A forgotten backup password cannot be recovered.

## Honest progress signals

The app saves detailed attempts, timing and confidence, and can compare matching questions between an original attempt and a retest. These are study signals. Mixed-pack scores are not directly comparable, and small topic samples cannot establish mastery. The interface carries those limits rather than treating every percentage as a certification of understanding.

## Generation is separate from practice

The included source-grounded MCQ generator skill is open source under the same MIT license. It runs in a compatible AI-agent environment with reference material, rather than inside the website. The learner's AI tool can have its own provider costs. Manually authored schema-valid packs work too.

## Verification and privacy

The current local checks cover deterministic controller/core behavior, both pack validators, four embedded samples from disk, native browser storage, workspace workflows, consent-gated analytics, and offline backup/PDF/expiry behavior. Chromium is the tested browser; this does not establish Safari, Firefox or physical touch-device coverage.

Optional production analytics requires explicit consent and sends only fixed allowlisted events. It excludes questions, answers, scores, notes, source files and backups. Local copies do not send those events. The campaign reuses that contract and does not add campaign tracking or recordings.

[Try RecallForge](https://dagerottdev.github.io/RecallForge/) or [inspect the source](https://github.com/DagerottDev/RecallForge). The RecallForge YouTube walkthrough will be linked here once its public URL is verified. I'd value feedback on the practice-to-revision loop and the tradeoffs of a browser-local workspace.
