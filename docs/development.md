# Development and verification

The text launch package must be combined with the actual application source. It is not a standalone Swift checkout and does not contain binaries or resources.

## Build

Use an Apple development toolchain whose SDK contains the macOS 26 glass APIs used by the current SwiftUI source. The Swift tools version is 5.9 and runtime deployment target is macOS 14; those values alone do not establish compatibility with an older SDK.

```sh
swift build -c release
bash run-tests.sh
```

TODO[BUILD_MATRIX]: Record the exact working Xcode/Command Line Tools, SDK, Swift, macOS, and architecture versions for the release checkout. The existing test runner compiles its own executables; `swift test` is not a documented substitute because the manifest has no test target.

## Existing test coverage

- `ActivityTests.swift`: gate persistence/sign-out, lifecycle matching, prose isolation, direct input waits, concurrent tasks, partial/truncated journals and expiry, old configuration, identifiers, malformed data.
- `UsageTests.swift`: multi-bucket and legacy responses, dynamic durations, missing versus zero, clamping, reset times, missing/returning Spark, plan-label handling.
- `UsagePanelLayoutTests.swift`: real hosted SwiftUI panel growth, height cap, shrinkage, and error layout.

The default run does not deliberately request live usage data. The layout executable hosts native views and needs a suitable macOS graphical environment. New CI must demonstrate that environment before claiming app tests pass there.

The compiled `UsageTests` supports `--live`, which queries the installed account. Treat that as a separate manual integration check; do not require contributor credentials in CI.

## Diagnostics and visual checks

From a built full checkout:

```sh
APP_BIN="$(swift build -c release --show-bin-path)/AgentBeacon"
"$APP_BIN" --diagnose
```

`--diagnose` requires the local app sign-in flag in the current implementation. Additional source-confirmed modes are `--render-preview PATH`, `--render-idle-preview PATH`, `--preview-usage PATH`, and `--show-usage`. Use absolute output paths. Usage preview reads live data and should be reviewed before sharing. It does not activate the normal monitoring UI's local access gate.

Test the bundled app, not only the bare executable, for resource loading, icon display, Launch at Login, permissions, and Dock behavior. Check a fresh user profile, permission denial, unavailable usage data, concurrent tasks, Command-Q with no menu open, smaller screens, and Reduce Motion.

## Documentation checks

```sh
python3 scripts/check-docs.py
python3 scripts/check-docs.py --release
```

The first checks text/package structure, JSON parsing, and local Markdown file links. The second also rejects unresolved `TODO[...]` markers. This launch draft intentionally fails release mode until its decisions are resolved. The included GitHub workflow runs only the documentation check; it does not certify the app build, sign it, upload data, or publish a release.

See [launch verification](../launch/VALIDATION.md) for checks actually run while creating this package.
