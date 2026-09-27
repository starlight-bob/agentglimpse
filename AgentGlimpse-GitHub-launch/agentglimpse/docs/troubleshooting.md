# Troubleshooting

## No activity appears

Confirm the normal app has passed its local first-launch gate. Open **AgentBeacon controls** and inspect **Codex activity**. The journal adapter needs readable recent files at `~/.codex/sessions`. A cloud task without a local journal will not appear through that adapter.

For Claude or other desktop-window detection, check that `watchWindows` is enabled, the app has Accessibility permission, and the agent window exposes a recognized busy/stop/approval control. A closed window may prevent detection. For connected-folder signals, verify that the producer is writing fresh JSON to the configured directory.

After an ad-hoc rebuild, macOS may require removing and re-adding the app's optional permission entry. Use the currently installed app, not a backup copy.

## A state seems stuck or disappears unexpectedly

Check the producer timestamp and expiry settings. The default done display lasts ten minutes, and stale activity four hours; demo states last one minute. Local journal active-state expiry is based on file modification time. Conflicting adapters can change the newest visible state.

Clear Done and Clear All dismiss activity, but can delete bridge JSON in watched folders. They do not cancel agent tasks or reset quotas. A cleared local task reappears after a newer lifecycle event.

## Usage is unavailable

Confirm a compatible Codex installation is signed in and reachable. The app uses fixed executable candidates; a custom CLI location may not be discovered. Refresh from the panel. An account may return fewer windows than another account, or none at all.

Unavailable Spark rows mean the service did not supply Spark measurements. They are not 0% usage. An unavailable percentage is distinct from an actual zero. A stale label means a refresh failed and values from this run remain displayed. A countdown reaching zero does not guarantee the service has reset; refresh to check.

The local app sign-in gate and Codex account sign-in are separate. Completing one does not sign in to the other.

## Glass or panel sizing looks different

Native glass is conditional on macOS 26+. Earlier supported runtimes use materials. Panel height follows content and available screen space; long usage lists scroll. Screenshots may not faithfully reproduce the live translucent background.

If reporting a layout problem, include OS version, display scaling, available screen height, and a sanitized screenshot. Do not include private task content.

## The icon is wrong, or Command-Q does not work

Verify the launched bundle is the intended installation and not a copy in Downloads or a backup directory. The current installer validates a specific icon resource. If deliberately changing it, update the resource, app metadata, runtime loading, and installer checksum together.

Command-Q acts on the active app. The current source installs an application menu for that behavior. Clicking the Dock icon should activate the app and open usage or sign-in. See [rollback](uninstall.md) if the wrong version was installed.

## Build or hook setup fails

An older SDK can lack the glass APIs even though the runtime minimum says macOS 14. Record the toolchain version and follow [development setup](development.md). Legacy hook compatibility is host-dependent, and the helper must exist at the path expected by its installer. Restore a backup if configuration changes are wrong; do not repeatedly run the installer over malformed settings.

For reports, use the GitHub issue form and share only a minimal, reviewed diagnostic excerpt. [Privacy](privacy.md) explains which logs can contain message text.
