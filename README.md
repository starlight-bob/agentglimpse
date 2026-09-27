# AgentGlimpse

**Your agents’ status. Your Codex limits. One quiet glance.**

AgentGlimpse is a native macOS companion that brings AI agent activity into a small menu bar pill. See when an agent is working, waiting for you, or finished. Click to check Codex usage limits and reset countdowns in a softly translucent panel. When things go quiet, a tiny animated ginger cat keeps you company.

<img width="396" height="63" alt="Screenshot 2026-09-25 at 20 34 09" src="https://github.com/user-attachments/assets/8b473af1-0e48-4df8-940f-2b342fe70c51" />

<img width="428" height="613" alt="Screenshot 2026-09-25 at 20 34 23" src="https://github.com/user-attachments/assets/dd5dc241-85cd-49be-870b-cee042f20c23" />

Formerly **AgentBeacon**. AgentGlimpse is the selected public name.

> **Launch draft:** These materials describe the inspected AgentBeacon 1.4.9 source. This text-only package must be merged with the app source before build commands will work. The public release, license, and first-launch access policy are pending; see the [launch checklist](launch/CHECKLIST.md). Existing executable names and data paths still use AgentBeacon.

## At a glance

- **Activity you can recognize:** a blue working ring, amber input and limit indicators, a red error indicator, and a green completion check.
- **Separate agent identities:** light-blue Codex, soft-peach Claude, and teal ChatGPT badges, with custom PNG overrides.
- **Codex usage at a click:** reported quota percentages, reset countdowns, and the account plan when available. Refresh manually or let the app refresh every 60 seconds while monitoring is active.
- **Honest missing-data states:** unavailable percentages stay unavailable; failed refreshes label retained values as stale. A missing Spark section stays visible without invented numbers.
- **A native glass panel:** Liquid Glass on macOS 26+, with material fallbacks on earlier supported systems. Height follows the content; long usage lists scroll while controls remain visible.
- **A little personality:** a left-facing, full-body ginger cat with a swishing tail and blinking eyes in the idle pill. Animation respects the system Reduce Motion setting when animation state is evaluated.
- **Everyday controls:** Clear Done, Clear All, Launch at Login, a Dock presence, and standard Command-Q behavior.

## What it connects to

| Source | What the current implementation provides | Main limitation |
| --- | --- | --- |
| Local Codex session journals | Structured start, completion, abort, and certain direct input-request events; concurrent local task aggregation | Depends on the observed local journal format; not complete cloud-task or approval coverage |
| Codex account usage | Reported rate-limit windows through the installed Codex app-server | Requires a signed-in, compatible Codex installation and account response |
| Claude / ChatGPT / Codex desktop windows | Optional control-based activity detection | Requires Accessibility; app UI changes can affect detection |
| Desktop notifications | Optional completion and attention signals | Requires Full Disk Access; text classification is heuristic |
| State files and legacy hooks | Local JSON status, including connected-folder workflows | File producers and hook compatibility must be configured separately |

Read the [integration guide](docs/integrations.md) for coverage and setup. Usage reporting currently covers **Codex**, not Claude usage or every ChatGPT product limit. It displays **quota percentages**, not raw token totals, token costs, or per-task billing.

<img width="449" height="540" alt="Screenshot 2026-09-27 at 12 30 57" src="https://github.com/user-attachments/assets/2f6e545b-9334-4892-a5c4-c1db0a554e85" />

## Get started

The inspected package declares macOS 14 as its deployment minimum. Building the current glass UI requires an Apple SDK containing the macOS 26 APIs; the oldest working toolchain and supported hardware matrix still need release verification.

Once these files are merged into the complete source checkout:

```sh
bash run-tests.sh
bash install.sh
```

The current installer builds and ad-hoc signs `AgentBeacon.app`, preserves an existing app as a backup, and opens the installation. It does not install hooks. A private local sign-in gate remains in this source; public onboarding must be resolved before distributing a general-use build.

See [installation](docs/installation.md), [configuration](docs/configuration.md), and [troubleshooting](docs/troubleshooting.md).

## Privacy in plain language

The local Codex adapter reads journal files and interprets structured lifecycle events; it does not classify conversation prose. Optional window reading can access UI text. Optional notification and legacy hook integrations can store message excerpts in state files and logs. Logs may be written to the first configured extra state folder, which may itself be shared or synced.

Usage queries go through the installed Codex process and its existing account session. No separate credential store or analytics sender was found in the inspected app source, but this is not an offline-only product: Codex usage retrieval may use the network.

Read [privacy and data handling](docs/privacy.md) before enabling optional readers or sharing diagnostics.

## Learn more

- [Architecture](docs/architecture.md)
- [Development and verification](docs/development.md)
- [Known limitations](docs/known-limitations.md)
- [Uninstall and rollback](docs/uninstall.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md) and [security reporting](SECURITY.md)

## License and attribution

TODO[LICENSE_CHOICE]: Select the repository license and confirm the copyright holder. [LICENSE](LICENSE) records the unresolved status; a proposed MIT text is supplied separately for adoption. Third-party artwork requires its own review in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

This is an independent companion project. Product names identify the apps it integrates with; no affiliation or endorsement is claimed.

## Acknowledgments

Built by starlight-bob with assistance from ChatGPT and Codex for development, debugging, design iteration, and documentation.
