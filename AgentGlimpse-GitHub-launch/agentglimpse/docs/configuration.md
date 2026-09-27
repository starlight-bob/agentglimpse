# Configuration

The inspected application reads `~/.agent-beacon/config.json` when normal monitoring starts. Quit and reopen after editing. If the file cannot be decoded, the loader falls back to defaults and attempts to write them back; save a copy before changes.

| Key | Existing default | Effect |
| --- | --- | --- |
| `doneTTL` | `600` | Seconds completed states remain displayed |
| `staleTTL` | `14400` | Stale activity timeout; external and journal adapters apply it differently |
| `showIdleDot` | `true` | Legacy key name that now controls the idle cat pill |
| `animate` | `true` | Enables status/cat animation, subject to Reduce Motion |
| `extraStateDirs` | `["~/Documents/Claude Code/.agent-beacon"]` | Additional watched folders; first one is also the app log destination |
| `watchNotifications` | `true` | Starts the optional notification reader; needs Full Disk Access |
| `watchWindows` | `true` | Starts the optional desktop-window reader; needs Accessibility |
| `watchCodexSessions` | `true` | Starts local Codex journal detection |

See [current defaults](../examples/config.current-defaults.json) and a [narrower local-reader example](../examples/config.local-only.json). The latter uses no extra folder, disables window/notification readers, and leaves local Codex journal detection enabled. Both retain the app's account usage queries.

Use positive durations and paths to dedicated state folders. The decoder tolerates omitted keys by using defaults, but does not provide a comprehensive validation UI. Do not rely on arbitrary negative values or unexpected types.

Custom icons use `~/.agent-beacon/icons/<name>.png`, for example `codex.png`, `claude.png`, or `chatgpt.png`. Restart after replacing an icon because the renderer caches loaded images. Verify rights to any artwork you distribute.

Launch at Login is controlled through the app menu, using ServiceManagement, not a JSON field. No documented configuration key exists for disabling account usage refresh, changing its 60-second interval, switching accounts, or changing the journal root in the shipping app.

The planned AgentGlimpse app rename does not create a working `~/.agentglimpse` path. Continue using the current names until the migration in [RENAME.md](../launch/RENAME.md) is implemented.
