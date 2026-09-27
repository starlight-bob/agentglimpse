# Installation

These instructions describe the inspected AgentBeacon 1.4.9 source. AgentGlimpse is the selected public name. The launch text package does not contain the app, source, images, or release downloads.

## Requirements

| Requirement | What is established |
| --- | --- |
| Runtime | Package.swift and Info.plist declare macOS 14+ |
| Native glass | The UI calls macOS 26 glass APIs conditionally; earlier systems use material fallbacks |
| Build environment | Swift tools manifest 5.9; current source needs an Apple SDK with the referenced macOS 26 APIs |
| Usage data | Compatible installed Codex desktop/CLI executable, signed in to an account that returns usage windows |
| Optional hooks | Bash helper; Python 3 for the legacy hook installer |
| Hardware | Local build artifacts show Apple silicon; Intel and universal distribution are not established |

TODO[BUILD_MATRIX]: Verify the minimum build toolchain and actual macOS/hardware support before publishing compatibility claims. A deployment target is not evidence of tests on every supported OS.

## Build and install from the complete source

Merge these documentation files into a complete, reviewed source checkout. It must contain `Package.swift`, `Sources/AgentBeacon`, `Resources`, the shell installers, and the existing tests.

From that checkout:

```sh
bash run-tests.sh
bash install.sh
```

`install.sh` builds the release executable with Swift Package Manager, assembles the app and resources, ad-hoc signs the bundle, and invokes `install-prebuilt.sh`.

The current destination is `~/Applications/AgentBeacon.app`, unless `/Applications/AgentBeacon.app` already exists, in which case the system Applications copy is replaced. Writing there may require appropriate filesystem permissions. The installer keeps the previous app in an `AgentBeacon Backups` folder beside the installation, verifies the staged signature and expected icon checksum, and opens the installed app. It preserves existing settings and does not install hooks.

TODO[SIGNING]: No Developer ID signing/notarization status has been verified. Do not advertise a notarized download or instruct users to disable macOS security protections. Document the actual release signing and supported opening procedure after testing.

## First launch

The inspected source contains a private offline username/class/password gate. Completing it saves a local completion flag; Sign Out clears that flag and stops the normal monitoring interface. These are not Codex account credentials.

TODO[ACCESS_GATE]: Decide whether the public build removes the gate or replaces it with documented onboarding. No private credentials or verifier value are included in this package. A general user cannot be assumed to have access to this existing build.

After access is enabled, the menu bar pill shows activity. Click it to open usage. The app also appears in the Dock; clicking its Dock icon opens the panel or the sign-in window. Command-Q quits while the app is active.

## Optional permissions and integrations

Local Codex journal detection does not require Accessibility or Full Disk Access. The window and notification readers are enabled in the existing default configuration, but need their respective macOS permissions to work. Use [configuration](configuration.md) to disable them if unwanted.

- Enable Accessibility for the app only if using the desktop-window reader.
- Enable Full Disk Access only if using the notification reader; relaunch afterward.
- Configure state-file producers and hooks separately using [integrations](integrations.md).

Ad-hoc rebuilds may need permission reauthorization. Enable **Launch at Login** through **AgentBeacon controls** if desired.

## Prebuilt release

TODO[RELEASE]: Publish a verified version, download URL, architecture list, checksum, and release notes. This draft intentionally has no invented download link or package-manager command.

For updates and removal, see [uninstall and rollback](uninstall.md).
