# Uninstall and rollback

These paths describe the inspected AgentBeacon implementation. No AgentGlimpse path migration has been performed.

## Stop and remove the app

1. Turn off **Launch at Login** in AgentBeacon controls before quitting. If the app cannot open, remove/disable its entry in macOS Login Items settings.
2. Quit AgentBeacon using its menu or Command-Q while it is active.
3. Stop any independent state writers, connected-folder status skill, or hooks that still emit AgentBeacon files.
4. Remove the installed `AgentBeacon.app` from `~/Applications` or `/Applications`, whichever is in use. Check that you are removing the intended copy.
5. Remove its optional Accessibility and Full Disk Access entries in macOS settings if no longer needed.

Removing the app does not remove its state, logs, preferences, backups, or host hooks.

## Remove legacy hooks

If hooks were installed using the legacy script, back up current agent settings, inspect the script, and run from the complete source checkout:

```sh
python3 hooks/install-hooks.py --uninstall
```

It removes commands containing the `agent-beacon` marker from Claude/Codex hook JSON and removes its matching Codex notify line. It is not a full rollback: it can leave `hooks = true` and does not restore earlier configuration contents. Review the resulting files and remove an unused feature flag only if no other integration needs it. Remove manually installed hooks separately. Do not delete entire agent settings files.

## Remove retained data

After stopping writers, review and remove the project's files you no longer need:

- `~/.agent-beacon/`, including configuration, state, icons, the helper, and hook logs.
- Project-owned state files, `beacon.log`, and `ax-dump-*.txt` in each configured extra directory. The existing default is `~/Documents/Claude Code/.agent-beacon`.
- Old bundles under `AgentBeacon Backups` beside the app installation.
- The app's macOS preferences. For the current bundle identifier, this command removes its preference domain after quitting:

```sh
defaults delete com.starlightbob.agentbeacon
```

Do not delete the parent `Claude Code` folder or files belonging to another integration. If bridge files were synced or exposed to remote sessions, manage remote copies and backups through those tools separately. An app rename may change preference handling, so verify the release instructions first.

## Restore a prior app

Quit the current app and preserve it if needed. Locate the timestamped backup beside the installation, copy the backed-up bundle back to the intended installation as `AgentBeacon.app`, and open it. Verify the version, icon, and optional permissions. The backup suffix may be `.app.backup`; restore the normal `.app` name.

The installer preserves app bundles, not a complete configuration snapshot. Restoring an app does not undo later settings or hook changes; use the separate configuration backups you made.
