# Privacy and data handling

This describes the source inspected on 2026-09-25, identified by its Info.plist as AgentBeacon 1.4.9, build 19. It is a source-based disclosure, not a traffic capture or independent security audit. Public build behavior must be rechecked if code changes.

## What is read and retained

| Feature | Data read | Data retained or written |
| --- | --- | --- |
| Local Codex activity | Recent files under `~/.codex/sessions`, including full JSON records encountered while tailing | In-memory file cursors and structured status; ordinary status logs. No conversation archive is created by this adapter |
| State bridge | Agent, status, reason, message, timestamp, session from watched JSON files | Producers leave state JSON on disk; explicit Clear can remove it |
| Optional Accessibility reader | Window accessibility trees, including short values/titles/descriptions; recognized controls determine state | Derived state files and diagnostic logs; opt-in dumps can contain UI text |
| Optional notification reader | New notification titles, subtitles, bodies, and source identifiers for the targeted apps | Combined notification text in state JSON and in `beacon.log` |
| Legacy hooks | Host payload fields, including messages and sometimes the last assistant message | State JSON can include excerpts; `hooks.log` records a message prefix |
| Codex usage panel | Account plan, bucket names, percentages, window durations, reset timestamps via installed Codex | Values and stale state held in memory for the current run; no usage-history file was found |
| Local app gate | Entered username, class, and password | A Boolean completion flag in macOS preferences; entered strings are not saved by the gate |

**Does it read prompts or conversation content?** The journal reader must read file bytes and parse records that can contain conversation content, but only structured lifecycle/tool fields drive its state. Optional Accessibility traversal can encounter conversation UI text; explicit text dumps retain some of it. Notification and hook payloads may also contain task or message content and can be retained. A blanket claim that the app never reads or stores content would be inaccurate.

## Network and credentials

No direct analytics sender, crash-report uploader, telemetry backend, or separate API-key store was found in the inspected app source. The local access gate does not send its inputs to a server.

Usage retrieval launches the installed Codex app-server using the user's existing Codex account session. That process may contact OpenAI services and use credentials managed by Codex. The app itself does not directly read Codex credential files in this code path. Do not interpret this as a promise that no authenticated process or network request is involved.

No source path was found that uploads the monitored conversation/state data to a AgentGlimpse service. A connected or synced state/log directory may nevertheless be available to another application, a cloud sync provider, or a remote agent session under that tool's own access rules.

## Files and retention

| Location in the current implementation | Contents and retention |
| --- | --- |
| `~/.agent-beacon/config.json` | Settings; persists until changed or removed |
| `~/.agent-beacon/state/*.json` | Latest writer states; display expiry does not itself delete files |
| `~/.agent-beacon/icons/` | Optional user-supplied PNG overrides |
| First configured extra state directory | Additional state JSON; also receives `beacon.log` when an extra directory exists |
| `~/Documents/Claude Code/.agent-beacon` | Existing default extra directory; may be a connected folder |
| `~/.agent-beacon/beacon.log` | Log destination when no extra state directory exists |
| `beacon.log` at the selected destination | Diagnostic and notification-derived text; the logger removes/recreates it when size exceeds about 1 MB, not on a time-based schedule |
| `~/.agent-beacon/hooks.log` | Legacy hook log; no rotation was found in the helper |
| `ax-dump-<agent>.txt` beside `beacon.log` | Explicitly requested UI-text dump; remains until removed or overwritten |
| App preferences under current bundle ID `com.starlightbob.agentbeacon` | Saved local sign-in completion flag |
| `AgentBeacon Backups` beside the installed app | Prior app bundles retained by the installer |

Notification and Accessibility adapters write derived states to the primary state directory. The journal adapter's per-session state stays in memory. The default 10-minute done and four-hour stale settings control display, not a data-deletion promise. Sign Out stops the normal UI's monitoring but does not erase existing files or disable independently installed hooks. The standalone usage-preview path may still query Codex.

## Permissions and controls

The local Codex journal adapter does not require Accessibility or Full Disk Access. Window and notification readers do. In the inspected defaults, both optional reader flags are true, although macOS permission still gates access.

To narrow monitoring, set `watchWindows` and `watchNotifications` to false and use an empty `extraStateDirs` array in the existing configuration, then restart. See the supplied [local-only configuration example](../examples/config.local-only.json). This example narrows local readers and folders; it does **not** disable the Codex usage network query. The current configuration has no usage-refresh disable flag.

Do not use a shared folder containing unrelated JSON as a state directory. Clear All may delete its JSON files, and other writers can influence displayed state.

## Sharing diagnostics and removing data

Before sharing a log or screenshot, inspect it for notification text, task names, message excerpts, account details, UI text, usernames, and personal paths. Never publish credential files, full agent journals, notification databases, or private access-gate material.

Use [uninstall instructions](uninstall.md) to stop hooks, remove the app, and locate retained data. If a folder was synced or connected elsewhere, removing a local file does not establish deletion of remote copies or backups.

TODO[SECURITY_CONTACT]: Publish a monitored private contact before launch for privacy or security reports.
