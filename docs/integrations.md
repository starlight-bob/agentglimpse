# Integrations

This is an account of the current local source, not a guarantee that every current or future agent version uses the same formats. Activity detection and account usage are separate integrations.

## Local Codex activity

`CodexSessionWatcher.swift` tails `~/.codex/sessions/**/*.jsonl`. It interprets `task_started`, `task_complete`, `turn_aborted`, and `task_aborted`, along with recognized direct synchronous `request_user_input` calls and matching outputs. It polls every second and rediscovers recent files every five seconds.

The adapter keeps task state in memory and combines concurrent local sessions so one completed task cannot hide another unfinished one. It reads journal records, but does not classify chat prose or persist a conversation copy. The source format is an observed local format, not a compatibility promise.

Cloud tasks without local journals, nested tool calls, asynchronous input requests, and all possible approval/error/limit events are not fully covered. Aborted tasks map to done, so a green check means the tracked turn stopped; it does not certify success. Check **Codex activity** in the controls menu for adapter health.

## Codex usage limits

The app finds an installed Codex executable using application discovery and fixed candidate paths, including the desktop app's `Contents/Resources/codex`, `/opt/homebrew/bin/codex`, and `/usr/local/bin/codex`. It starts `codex app-server`, initializes the connection, and requests `account/rateLimits/read`. It does not create a task or request a quota reset.

It reads usage buckets, window durations, percentages used, reset timestamps, and plan information when supplied. There is no confirmed raw-token counter, token-cost calculator, Claude usage adapter, account switcher, or universal ChatGPT quota dashboard.

Monitoring starts an initial usage query and a 60-second timer, including while the panel is closed. Opening the panel also refreshes. Closing it does not stop that timer; signing out of the normal app stops monitoring. The standalone usage-preview command is a separate path and can fetch live account usage without completing the local app gate.

Missing windows are omitted. A missing percentage is shown as unavailable, not zero. If a successful nonempty response lacks Spark, presentation adds unavailable 5-hour and weekly Spark rows. Those rows contain no measured figures or reset dates. Failed refreshes retain current-run data with a stale label.

## Desktop window reader

The optional Accessibility reader targets these bundle identifiers from the source:

| Identifier | Internal agent label |
| --- | --- |
| `com.openai.codex` | `codex` |
| `com.openai.chat` | `chatgpt` |
| `com.anthropic.claudefordesktop` | `claude` |

Every two seconds it scans accessible windows for busy indicators and recognized Stop/Approve buttons. It may inspect other UI text while traversing the tree, but ordinary conversation prose is not used as a status trigger. Coverage depends on the app's accessible controls and labels, and is not a general localization guarantee. Closed or inaccessible windows can prevent reliable transition detection.

## Notification reader

This optional adapter reads macOS's notification database with `sqlite3 -readonly`. It reacts to new notifications from the identifiers above. Keyword matching assigns input, error, and limit states; other notifications are treated as done. It requires Full Disk Access and depends on an internal database schema. It can retain notification text in state files and logs; see [privacy](privacy.md).

## Local JSON bridge

The app watches `~/.agent-beacon/state` and folders in `extraStateDirs`, using filesystem events plus a two-second fallback poll. A state has:

| Key | Meaning |
| --- | --- |
| `agent` | Agent identifier, such as `claude`, `codex`, or a custom identifier |
| `status` | `working`, `attention`, or `done` |
| `reason` | Optional: `none`, `input`, `error`, or `limit` |
| `message` | Optional brief description; may be persisted by the writer |
| `ts` | Required Unix timestamp in seconds, freshly generated for each update |
| `session` | Optional source/session identifier; `demo` expires after 60 seconds |

Use the existing helper from the complete source checkout for a simple local test:

```sh
bash bin/agent-beacon set example working none "Demo task"
bash bin/agent-beacon set example attention input "Waiting for input"
bash bin/agent-beacon set example done none "Finished"
bash bin/agent-beacon clear example
```

For external writers, atomically replace a dedicated `<agent>.json` using a temporary file. Generate a fresh `ts`; copying a fixed timestamp will create an expired state. Use simple identifiers with letters, digits, underscores, or hyphens; the legacy helper is not a hardened parser for arbitrary untrusted identifiers.

External files are reduced to the newest state per agent across watched directories before aggregation. They do not provide the same per-task concurrency tracking as local Codex journals. Fresh local states can suppress older file states. Explicit Clear actions can delete JSON files in **all** watched folders; keep each bridge folder dedicated to this purpose.

For connected-folder/Cowork workflows, the remote session must be able to write a configured folder, with instructions or a skill to emit status. The app does not automatically make every remote task observable. The existing default extra folder is `~/Documents/Claude Code/.agent-beacon`; choose the actual folder connected on the user's machine.

## Legacy hooks — optional, review before use

The source includes `bin/agent-beacon` and `hooks/install-hooks.py`. The helper maps host lifecycle notifications into files; the installer edits `~/.claude/settings.json`, `~/.codex/hooks.json`, and `~/.codex/config.toml`.

Before running it, back up those files and inspect compatibility with the installed host versions. The script expects the helper at `~/.agent-beacon/bin/agent-beacon`, but does not copy it there itself. In a reviewed complete checkout, the setup sequence is:

```sh
mkdir -p "$HOME/.agent-beacon/bin"
cp bin/agent-beacon "$HOME/.agent-beacon/bin/agent-beacon"
chmod +x "$HOME/.agent-beacon/bin/agent-beacon"
python3 hooks/install-hooks.py
```

This is a legacy opt-in path, not the default installation. The script can replace malformed JSON with a new object, has no built-in transactional backup, and its TOML editing is regex-based. It removes commands matching `agent-beacon` and leaves an unrelated existing notify setting in place. The uninstall mode does not fully restore prior configuration or remove every feature flag. See [uninstall](uninstall.md).

Source-confirmed hooks include session start/end, prompt submission, pre/post tool use, permission requests, notifications, and stop. Host-side availability must be tested; the adapter's event names alone do not prove current host support.
