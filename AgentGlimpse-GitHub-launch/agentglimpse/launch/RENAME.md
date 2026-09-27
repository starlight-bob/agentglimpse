# AgentBeacon → AgentGlimpse migration plan

The project owner selected AgentGlimpse as the public name. This text package reflects that choice. It has not modified the source project, installed app, hooks, or existing user data.

## Recommended first step

Use AgentGlimpse as the display name while deliberately retaining existing storage and integration identifiers for an initial transition. This reduces migration work, but still needs source/resource changes and tests. Public docs must clearly explain the remaining AgentBeacon paths.

TODO[RENAME]: Decide between that transition and a complete technical rename. Avoid a global search-and-replace: compatibility paths, sign-in preference domains, and installer checks require explicit handling.

## Inventory

| Surface | Existing value or location | Work if changed |
| --- | --- | --- |
| Display strings | Agent Beacon / AgentBeacon in UI and accessibility labels | Update menus, gate, tooltips, panel controls, preview text and documentation |
| Swift product/target/executable | `AgentBeacon`; `Sources/AgentBeacon` | Coordinate Package.swift, test runner, preview/build commands and bundle assembly |
| Bundle | `AgentBeacon.app`, `com.starlightbob.agentbeacon` | Choose final identifier only with owner input; verify Dock, preferences, login items and permissions |
| State/config/icons | `~/.agent-beacon` | Retain compatibility or implement an explicit idempotent migration; do not silently drop state/config |
| Connected folder | `~/Documents/Claude Code/.agent-beacon` default | Preserve customized folders and update external writers/skills if changed |
| Helper | `agent-beacon`, `~/.agent-beacon/bin/agent-beacon` | Keep a compatibility alias or update installed hooks safely |
| Hook cleanup marker | `agent-beacon` substring | Remove only owned entries, preserve unrelated hooks and notify settings, keep backups |
| Usage client info | `agent_beacon` with an older embedded client version | Reconcile name/version with release metadata |
| Sign-in preference | `hasCompletedLocalSignIn` in the existing app domain | Resolve public onboarding; never ship a developer's completion flag or private verifier |
| Artwork | Named resources, runtime icon loader, Info.plist icon name | Update consistently; confirm asset rights |
| Installer icon check | Specific SHA-256 for `BeaconOrb-v1.icns` | Update checksum only alongside the intended final icon |
| Backups and install destination | Both user/system Applications paths; `AgentBeacon Backups` | Preserve rollback and avoid duplicate app identities |

## Migration acceptance checks

- Existing customized config is retained and old state producers still work or receive clear migration instructions.
- Existing optional permissions and login items are handled honestly; identifier/signature changes may require reauthorization.
- Fresh users can complete public onboarding without private credentials.
- Dock, Finder, Launchpad, About/Quit menu, usage panel, and accessibility labels identify the intended app.
- Command-Q and Dock reopen behavior work with no controls menu open.
- Installation, rollback and uninstall address both old and new names without deleting unrelated data.
- The final documentation uses only executable names and paths that actually work in the shipped version.

No automatic migration is implemented by this package.
