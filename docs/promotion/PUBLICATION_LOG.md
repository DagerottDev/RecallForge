# RecallForge campaign publication log

Prepared 2026-10-12; updated 2026-10-14. This log is evidence, not a list of assumed publications. Dated checkpoints below are historical; the tables describe current verified status.

| Item | Status | Evidence / remaining action |
|---|---|---|
| Three finance demos | Deployed and validated | Ten original questions each; source and arithmetic review in SOURCES.md |
| Sample chooser and offline embedding | Local browser checks passed | Four samples, feedback, source links, navigation, saved history and deduplication |
| App regression | Passed | 41 Node tests, 8 Python checks; analytics acceptance; 9 storage, 15 workflow checks; offline backup/PDF/expiry |
| GitHub baseline | Verified 2026-10-12 | 0 stars through public repository API |
| Live finance-demo deployment | Verified | Commit `9b424ee30609eb235e5cda50288f7a92d55d9f6c`; [CI and Pages passed](https://github.com/DagerottDev/RecallForge/actions/runs/38239212491); live HTML matched built artifact |
| Kokoro narration | Eight exports generated | Local af_heart voice, speed 1.10; isolated environment, no paid provider |
| Eight video exports | Complete | Four 1080p landscape videos and four vertical Shorts; MP4/SRT/technical validation and distinct artwork under output/promotion |
| Channel creation | Verified 2026-10-13 | [RecallForge @RecallForgeStudy](https://www.youtube.com/@RecallForgeStudy); owner completed terms acceptance and phone verification; existing personal channel preserved |
| Channel branding/profile/playlists | Approved logo published | Folded-R avatar, banner and public quick-tour thumbnail visually verified on 2026-10-14; app/GitHub links, description and three playlists exist |
| First quick-tour upload/publication | Public 2026-10-13 | [Quick tour](https://www.youtube.com/watch?v=ipCjNABrAQA); processed 1080p playback, English SRT, custom thumbnail, AI label; copyright checks clear |
| Other seven releases | Five scheduled; two private | Videos 02–06 have authored English captions, disclosure, matching thumbnails and processed private playback checks. See release table; no future release is counted as public |
| X channel announcement | Public 2026-10-14 | [Creator-disclosed announcement](https://x.com/Rajveer761SM/status/2110279973424783794), approved logo graphic with alt text, tour/app/source links |
| 300Hours permission | Pending | Send focused administrator request |
| CMT Discord permission | Pending | Accessible channel, current staff rules |
| r/CFA permission | Submitted; delivery not independently verified | Creator-disclosed permission request submitted through compose form; form cleared. Current rule prohibits unauthorized promotion and non-approved prep providers. No public post |
| r/FRM permission | Submitted; delivery not independently verified | Permission request submitted; form cleared. Current rule prohibits blatant advertising. No public post |
| DEV article | Draft ready; owner sign-in needed | Public tour link added; DEV sign-in includes terms agreement, left to owner |
| Show HN | Draft ready; owner sign-in needed | Login required; check prior submissions after owner sign-in |
| Five educator invitations | Draft template ready | Verify relevant recipients and published contact routes |
| Weekly measurements | Pending | Record actual metrics; unavailable is not zero |

## Releases

| Video ID | Playlist | Relative day | Public URL | Actual status |
|---|---|---:|---|---|
| 01-quick-tour | Getting Started | 0 | https://www.youtube.com/watch?v=ipCjNABrAQA | Public; verified |
| 02-quick-question-short | Shorts | 2 | — | `AKjDQeO2Aoc` scheduled for 2026-10-15 09:00 IST / 03:30 UTC; not public |
| 03-cfa-fundamentals | Finance Practice | 7 | — | `c1SQbuKnK4s` scheduled for 2026-10-20 09:00 IST / 03:30 UTC; not public |
| 04-cfa-mistake-short | Shorts | 9 | — | `Hs-05OQUqR8` scheduled for 2026-10-22 09:00 IST / 03:30 UTC; not public |
| 05-frm-risk | Finance Practice | 14 | — | `0pQF4cxGxtA` scheduled for 2026-10-27 09:00 IST / 03:30 UTC; not public |
| 06-risk-revision-short | Shorts | 16 | — | `LGH_NET_A6U` scheduled for 2026-10-29 09:00 IST / 03:30 UTC; not public |
| 07-cmt-analysis | Finance Practice | 21 | — | `JDFkoisGfJw` Private; captions/metadata and 1080p playback checked; custom thumbnail and 2026-11-03 schedule pending |
| 08-moving-average-short | Shorts | 23 | — | `ntNsjZtBzjM` Private; captions/metadata and vertical 1080p playback checked; custom thumbnail and 2026-11-05 schedule pending |

Record public permalinks only after verifying their actual content and visibility. Record scheduled dates in Asia/Kolkata and UTC. Never interpret a private or scheduled upload as publicly published.

## Logo approval checkpoint — 2026-10-13

The owner requested a new logo and explicit final-design approval before publication. Candidate master is `src/assets/branding/recallforge-mark.png`; local approval board is `output/branding/review.html`. App header, offline favicon and README changes are prepared locally. No new logo was pushed, deployed or uploaded to YouTube. Existing public quick tour keeps its original RF branding pending approval. Seven later videos remain private drafts; no release schedules were submitted.

Known remaining gates: approve logo; prepare matching channel/video artwork; finish seven video metadata/captions and processed playback checks; schedule releases; verify Reddit permission-request delivery/replies; send remaining administrator and educator requests; publish X, DEV and Show HN through verified owner accounts; begin weekly measurements.

## Usage reserve checkpoint — 2026-10-13

Native Codex five-hour usage reached 83% used / 17% remaining; pause under the owner standing reserve instruction. No goal completion is claimed.

New logo remains unpublished. Automatic approval review rejected the banner upload because explicit final-design approval was missing; an approval question is pending in the chat. App icon was exported at 256px while preserving the original master; the offline build is 5,110,098 bytes and build freshness/diff checks pass. The media renderer now uses the candidate logo and supports `--artwork-only`; avatar, banner and all eight thumbnails have validated export dimensions. All files are local and uncommitted.

First Short `AKjDQeO2Aoc` was saved as Private after its metadata/captions setup. Remaining six later uploads still need metadata/captions. Verify current Studio state before continuing. After explicit logo approval and usage reset or owner override: publish app/README/channel branding; update thumbnails; finish seven private processed playback checks and scheduling; resume community permission checks and broader distribution. Keep the public quick-tour URL unchanged: https://www.youtube.com/watch?v=ipCjNABrAQA .

## Explicit design approval — 2026-10-13

The owner explicitly approved the displayed folded-R logo: “go ahead with the logo”. Publishing the app/README/channel branding and thumbnails is now authorized. Usage allowance reset to 0% used before resumption. Earlier rejection and reserve checkpoints above are historical.

## Verified logo release and first schedule — 2026-10-13

Commit `9ff409599e218a15c4548ee2ecb387b1c22364d7` is pushed. [CI and Pages](https://github.com/DagerottDev/RecallForge/actions/runs/38390057108) passed deterministic, Python, storage/workflow/offline checks and deployment. The live app header loads the embedded 256px logo; README references the same logo. YouTube publicly displays the approved R and new banner. The original quick-tour video URL remains public and unchanged.

YouTube now requires advanced-feature verification for additional daily custom thumbnails. The owner has a pending verification handoff in Studio; automatic review rejected an agent attempt to advance it because the plan reserves Google verification to the owner. No verification bypass was attempted. CFA upload `c1SQbuKnK4s` is Private with correct title/description/audience, Finance Practice playlist, AI disclosure and authored English SRT. Processed playback was checked at 1920×1080. Thumbnail upload is gated by advanced-feature verification; scheduling remains pending.

## Second reserve checkpoint — 2026-10-13

Native Codex usage reached 82% used / 18% remaining. Pause under the owner standing reserve instruction; the full campaign remains incomplete.

Verified progress: approved logo is deployed in the app and README (CI/Pages run 38390057108 passed); YouTube avatar/banner published; Getting Started, Shorts and Finance Practice playlists created; first Short AKjDQeO2Aoc privately checked at 1080×1920 and scheduled 2026-10-15 09:00 IST; CFA c1SQbuKnK4s has its authored English SRT, AI disclosure, correct metadata and Finance Practice assignment, saved Private and played at 1920×1080. The owner approval for the logo is explicit and must not be requested again.

Current gate: YouTube requires owner advanced-feature verification for further daily custom thumbnails. Studio tab 8 preserves the owner handoff; tab 17 is the auxiliary content editor. Owner question is pending; do not advance verification. No new community posts or educator messages were sent during this run.

Next actions after reset or reserve override: verify owner advanced-feature status; finish CFA thumbnail/schedule and the other five draft setups; check processed private playback and schedules; recheck public thumbnail/avatar propagation; update campaign assets ZIP; commit current renderer avatar-background fix and log; continue X, DEV, Show HN, community permissions, educator invitations and weekly measurement. Preserve existing published video URLs and no-LinkedIn constraint.

## Branding and release continuation — 2026-10-14

Native usage reserve checked before resumption: 17% used / 83% remaining. Public channel avatar, banner and quick-tour thumbnail now visibly show the approved folded-R logo. Live app loads the embedded 256×256 logo; GitHub README loads the same committed PNG. Offline build freshness passed. The opaque navy avatar avoids white corners after YouTube's circular crop; avatar/banner/eight-thumbnail dimensions passed.

Normal custom-thumbnail uploads worked today for CFA, CFA Short, FRM and risk Short. No advanced verification action was taken, and owner verification completion is not inferred. CFA and CFA Short scheduled for 20 and 22 October; FRM scheduled for 27 October, all at 09:00 IST / 03:30 UTC. Short 04 played at 1080×1920, FRM at 1920×1080, with authored English tracks. Risk Short 06 (`LGH_NET_A6U`) played at 1080×1920 but Studio reported a transient save error; its final visibility is pending verification.

The isolated media environment's Python symlink points to a temporary runtime that is no longer available. Existing media exports remain intact. Artwork assertions used the bundled Python runtime; narration reruns require restoring the isolated interpreter. Existing MP4s retain the earlier RF overlays; channel/page artwork uses the approved logo.

Risk Short schedule independently verified in the regular editor: 29 October 2026, 09:00 IST. The stale draft window was closed after server-saved status verification. CMT thumbnail upload did not open a file chooser; a stalled Get advanced features dialog appeared. No verification action was taken. Two CMT thumbnails remain pending.

Both CMT uploads are finalized as Private, with authored English captions, English language, AI disclosure, no paid promotion, audience selection and correct playlists. Main CMT playback checked at 1920×1080; moving-average Short at 1080×1920. Their two custom thumbnails and planned 3/5 November release schedules remain pending; no public publication is claimed.

The launch ZIP was refreshed with approved branding and current records: 59 files, 29,938,020 bytes, eight MP4s, no pending-logo-approval folder, CRC checks passed. Commit `1d10fe365b4fd3b5e4c674cd4b44331c7ca27008` is remote-verified and CI/Pages run 38529499108 succeeded.

Proposed daily unattended campaign automation was rejected by automatic approval review because persistent publishing and outreach were not explicitly approved. No automation was created. A specific owner choice is pending; authorized interactive campaign work continues.

A tailored FinTree invitation is prepared in output/promotion/fintree-invitation.txt, using its published educator contact route. Gmail standalone composer did not expose an editable message body; one reload failed to load the site. No Send action was taken, and no educator invitation is counted as delivered. The owner private account address is intentionally omitted from this public log.
