# GitHub launch checklist

This package is complete as a text draft. AgentGlimpse is the selected public name. The following checklist separates publishing decisions and app work from documentation preparation.

## Resolve before public release

- [x] Adopt AgentGlimpse as the public name throughout the launch materials.
- [ ] TODO[NAME_AVAILABILITY]: Check the intended repository/domain namespace for AgentGlimpse.
- [ ] TODO[OWNER]: Confirm repository owner, slug, and canonical URL.
- [ ] TODO[SOURCE_BASELINE]: Import the intended source snapshot and record its commit; reconcile it with the 1.4.9 baseline.
- [ ] TODO[ACCESS_GATE]: Make public onboarding usable and remove private access material from distributable source/resources/history.
- [ ] TODO[LICENSE_CHOICE] and TODO[COPYRIGHT]: Adopt the license and correct holder line; align contribution terms.
- [ ] TODO[ASSET_RIGHTS]: Complete asset provenance and notices, or replace/remove affected assets.
- [ ] TODO[RENAME]: Implement the chosen name migration and preserve compatibility.
- [ ] TODO[SECURITY_CONTACT]: Establish and test a private security-report route.
- [ ] TODO[BUILD_MATRIX]: Record tested OS/CPU/toolchain combinations.
- [ ] TODO[SIGNING]: Record the actual signing/notarization status and supported install flow.
- [ ] TODO[VALIDATION]: Run the app tests and manual release checks on the final revision.
- [ ] TODO[RELEASE]: Choose public version/date and produce artifact checksums and release notes.

## Repository preparation

- [ ] Merge this text package into the reviewed source; do not overwrite newer source-owned docs without reviewing differences.
- [ ] Review staged changes for credentials, local paths, private verifier material, raw chat histories, logs, and generated build output.
- [ ] Verify issue forms and pull request template in GitHub's UI.
- [ ] Keep the included workflow described as documentation checks only. Add app CI after proving the runner/toolchain/GUI requirements.
- [ ] Add reviewed screenshots/demo/hero if wanted, following the text-only asset brief.
- [ ] Fill metadata and final URLs in the launch copy.
- [ ] Resolve all TODO markers and remove stale draft language; run `python3 scripts/check-docs.py --release`.
- [ ] Publish the repository and release only after the remaining decisions and app work are complete.

## Manual release checks

- [ ] Fresh install and update from the previous private build; expected destination and backup.
- [ ] Public onboarding, quit, relaunch, sign-out policy, and Launch at Login.
- [ ] Correct Dock/Finder/Launchpad icon and standard Command-Q with no controls menu open.
- [ ] Start, direct input wait, resume, complete, abort, and concurrent local Codex activity.
- [ ] Permission denial and reauthorization for optional desktop adapters.
- [ ] Dedicated bridge folder: write, expiry, clear and helper cleanup.
- [ ] Usage success, missing windows, missing percentages, missing Spark, stale response, reset countdown, and unknown plan.
- [ ] Dynamic panel height, small-screen scrolling, glass fallback, Reduce Motion, and useful accessibility labels.
- [ ] Log locations and retained notification/hook content match privacy disclosures.
- [ ] Rollback and uninstall preserve unrelated files/configuration.

The name-selection item reflects the owner’s explicit choice in this task. App-validation items are not checked merely because a historical task reported success on an earlier local build.
