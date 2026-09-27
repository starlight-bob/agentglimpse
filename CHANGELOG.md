# Changelog

This record distinguishes the planned public launch from versions found in local development history. It does not assert that historical builds were published on GitHub.

## Unreleased — AgentGlimpse launch preparation

- Prepared repository documentation, issue forms, a pull request template, documentation checks, and launch materials.
- Adopted AgentGlimpse as the public name throughout the launch materials; application identifiers, executable names, and data paths have not been renamed by this documentation package.
- Clarified quota percentages versus token counts, permission-dependent integrations, and local message retention.

TODO[RELEASE]: Set the public version, release date, source revision, and downloadable artifacts after release validation.

## AgentBeacon 1.4.9 — local development, 2026-09-18

- Made usage-panel height follow measured content, with scrolling when screen height is limited.
- Used the supplied Codex SVG in the panel header.
- Displayed the account plan from the usage response.

## AgentBeacon 1.4.8 — local development, 2026-09-18

- Kept the Spark section visible as Unavailable when a successful nonempty response omits it.
- Avoided substituting fabricated percentages or reset times for missing Spark measurements.

## AgentBeacon 1.4.7 — local development, 2026-09-17

- Added a standard application menu and made Command-Q available when the application is active without opening its controls menu.

## Earlier local development — 2026-09-13 to 2026-09-16

The available history records these changes, but does not map every one to a verified release tag:

- Structured local Codex activity tracking and concurrent-task aggregation.
- Refined light-blue Codex and peach Claude badges, working rings, and limit indicators.
- A local first-launch access gate and persistent Sign Out behavior.
- Codex usage windows, reset countdowns, and refresh controls.
- Native glass styling, rounded controls, and panel-edge fixes.
- An animated idle cat, later made smaller and left-facing with a shorter tail.
- Clear Done and Clear All controls in the usage panel.
- App-icon updates and installer icon-integrity checking.
- Regular Dock presence and Dock-click access to the usage panel.

History and source cross-checks are summarized in [research notes](launch/RESEARCH.md). Older assistant reports of successful tests are historical evidence, not a new validation of a public build.
