# RecallForge public visibility campaign

Owner direction: organic only; no LinkedIn; English; roughly 30 minutes daily for four weeks. Equal attention to learner usefulness and open-source visibility. The YouTube display name must be **RecallForge**. Preferred handles: `@RecallForge`, `@RecallForgeStudy`, then `@RecallForgeApp`, subject to availability.

Owner update: keep publishing and outreach in this chat; do not create unattended campaign runs. Hacker News is excluded. Existing YouTube release schedules remain part of this plan. Complete the owner's DEV Community profile using verified public information before publishing the engineering article.

## Product and positioning

Free, open-source browser practice and revision with original question packs, source-linked explanations, wrong/skipped-answer retesting, daily revision, and portable backups. No viewer account is required. Generation happens separately in a compatible AI agent, not inside the website. The three ten-question finance packs are independent introductory demonstrations, not official questions, full exam preparation, or evidence of exam readiness.

- App: https://dagerottdev.github.io/RecallForge/
- Repository: https://github.com/DagerottDev/RecallForge
- Questions and review: [source record](promotion/SOURCES.md)
- Narration, titles, scenes and upload timing: [video specification](promotion/videos.json)
- Ready-to-adapt community posts and outreach: [publication drafts](promotion/POSTS.md)
- Five individual educator invitations: [tailored drafts and verified contact routes](promotion/EDUCATOR_INVITATIONS.md)
- Actual outcomes and remaining gates: [publication log](promotion/PUBLICATION_LOG.md)

## YouTube channel package

Create a separate project channel under the owner's chosen Google account; do not rename or repurpose an existing channel. Use `output/promotion/assets/avatar.png` and `banner.png`, with the same RF brand as the app.

Description:

> RecallForge is a free, open-source study workspace for practice questions, explanations, wrong-answer retests, daily revision, and portable backups. Try original introductory demonstrations for investment fundamentals, technical analysis, financial risk, and Cell Biology. No account is required to use the browser viewer. Your questions, answers, and progress stay in your local workspace. These demonstrations are independent of CFA Institute, CMT Association, and GARP, and do not replace official curricula. Video narration is AI-generated; app demonstrations use disposable example data.

Profile links: **Try RecallForge** (live app), **Source code & generator** (repository). Playlists: **Getting Started**, **Finance Practice**, **Shorts**. Feature the quick tour as the channel trailer when available. Use the project identity, not credentials or claims about the owner's examination qualifications.

## Release sequence

Produce all eight videos before publishing. First publish the quick tour, then its Short two days later. Publish CFA, FRM, and CMT tutorials at weekly intervals after kickoff, each followed by a Short two days later. Prefer 09:00 Asia/Kolkata for future scheduled releases; the first video can publish immediately after verification. Anchor the schedule to the actual first-publication date, not the document's preparation date.

For each video: upload privately, verify processed playback and the correct narration/captions, upload English SRT captions, set the appropriate playlist and audience, check current AI-disclosure requirements, and then publish or schedule. Content is general adult education and **not made for kids**. Explain AI narration in descriptions. Do not use other people's cloned voices, copyrighted music, exam-provider content, fabricated usage claims, or pass-rate promises.

Descriptions start with the app and repository links. Then give the specific tutorial summary, original introductory-content boundary, AI narration disclosure, and disposable demo-data note. Shorts descriptions also include `#Shorts`; do not ask viewers to reconstruct a long URL from narration. Direct them to the clickable channel-profile app link.

## Distribution and daily work

- X: announce the channel and app demos after the first video is public; share each weekly tutorial and selected Shorts.
- 300Hours: ask permission before posting CFA/FRM resource discussions.
- Official CMT Discord: ask staff about an appropriate accessible channel. Candidate-only channels may require registration or membership; do not bypass that eligibility.
- r/CFA and r/FRM: send one relevant modmail permission request to each. Treat silence as no permission. Skip a declined promotional route and log the reason.
- DEV Community: complete the signed-in owner's profile, preserve existing valid information, and publish the engineering article. Use verified project links and avoid invented background or qualifications. Check for an existing article before creating a duplicate.
- Five educators/study-group organizers: individual, relevant invitations through published professional contact routes. One follow-up after seven days, then stop if declined or unanswered. Confirm promotional or group-sharing rules first.
- AnalystForum and Bionic Turtle are secondary prospects. Check current access and rules; do not post advertisements in their discussions.

Daily allocation: ten minutes responding to feedback, ten minutes contributing useful discussion, ten minutes reviewing results. Spend that time on actual helpful participation; do not manufacture activity or repetitive posts. No paid ads, mass messages, Product Hunt launch, or LinkedIn activity.

## Measurement

Public GitHub baseline on 2026-10-12: **0 stars**, verified through the repository API. Record the channel baseline once created and the consenting app baseline when its owner dashboard is available. Unavailable metrics remain unavailable, not zero.

Weekly review: public links and moderation status, YouTube views/watch time/subscribers, useful feedback, GitHub stars, consenting app activity, completed sessions, and returning learners. Existing analytics groups traffic broadly; no new tracking, raw URLs, query strings, or private study data will be added. YouTube views cannot be precisely attributed to app activity.

Month-one experiment targets: eight published videos, 500 combined video views, 20 subscribers, 20 consenting active learners, ten additional GitHub stars, and ten useful feedback responses. These are targets, not forecasts. After two weeks, allocate effort to channels that produce substantive feedback or learner activity.

## Reproducing media

The isolated Python environment is `output/promotion/.venv`, with its Python 3.12 runtime under `output/promotion/.python`; no media dependency is added to package.json. Use `output/promotion/.hf-cache` for downloaded public model files. Kokoro 0.9.4 with voice `af_heart` is used locally. Full environment versions are saved under `output/promotion/production-requirements.txt`.

```sh
HF_HOME=output/promotion/.hf-cache output/promotion/.venv/bin/python scripts/render-promotion.py
```

Use `--only <video-id>` to rerender one video. Actual browser captures live under `output/promotion/captures`. Final MP4, narration WAV, SRT, frame timing, and technical validation records are in each video's `output/promotion/<video-id>/` directory. Avatar, banner and distinct thumbnails are in `output/promotion/assets`. Do not delete those ignored media files until the uploads and retention record are verified.

Existing narration is reused from `output/promotion/speech`. A new uncached sentence may require the initial public model/voice download; set `HF_HUB_OFFLINE=1` only after that model cache is populated. Use `--artwork-only` to regenerate the channel artwork and thumbnails without changing narration or video exports.

## Acceptance

All thirty questions pass both validators. Numerical answers have independent arithmetic tests. Browser checks exercise all four samples from the disk distribution without external requests, source-linked feedback, keyboard navigation, reload preservation, and deduplication. Existing analytics, storage, workflow, backup/PDF and expiry regressions must remain green. Review diffs and verify Pages before linking a newly introduced feature publicly.

Media checks verify dimensions, frame timing, audio/subtitle streams, finite unclipped source audio, duration, and file hashes. Inspect representative rendered frames and processed uploads. A technical audio check is not a human listening review. Any unavailable account access, Google verification/terms acceptance, playback check, moderation permission or human review must remain explicit in the publication log.
