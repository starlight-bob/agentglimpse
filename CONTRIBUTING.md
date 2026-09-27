# Contributing to AgentGlimpse

Useful contributions include reproducible detection bugs, compatibility reports, accessible UI improvements, privacy fixes, and clearer setup instructions.

This repository package is a launch draft. TODO[LICENSE_CHOICE]: Establish the project and contribution licensing terms before accepting external code contributions. No contributor agreement or contribution relicensing policy has been adopted here.

## Report a problem

Use the bug report form for crashes, incorrect activity, usage failures, or display issues. Include the app version, macOS version, hardware architecture, agent app version, integration used, expected behavior, and a short reproduction. Missing usage data should be reported as missing, not converted to zero.

Use the feature form to explain a workflow and the outcome you want. For a new integration, include the documented event source, required permissions, and a sanitized example. Do not attach full conversation journals, account files, notification databases, or unreviewed logs. See [privacy](docs/privacy.md).

Report suspected vulnerabilities through [SECURITY.md](SECURITY.md), not a public issue containing exploit details or personal data.

## Work on the code

Follow [development setup](docs/development.md). Keep changes focused and explain the observable before/after behavior. Preserve existing configuration compatibility unless a migration is supplied.

For changes to detection, test lifecycle transitions, concurrent tasks, partial or malformed records, expired data, and permissions being unavailable. For usage changes, test missing versus zero, stale responses, variable windows, and unavailable Spark data. For UI changes, include a sanitized before/after image and check small screens and Reduce Motion. Add regression tests where they protect meaningful behavior.

Run the existing `bash run-tests.sh` suite for changes that touch its coverage. Build the complete app for source changes. A successful automated run does not replace a real desktop check for Dock behavior, permissions, glass rendering, or login items. State what was not tested.

## Pull requests

Use the included pull request template. Update the affected documentation and add an Unreleased changelog entry for user-visible changes. Do not add generated builds, credentials, personal sign-in verifiers, or copied third-party artwork without confirmed rights.

Keep discussion respectful and specific. Discuss the work, explain disagreements, and avoid harassment or disclosure of personal information. A private moderation contact has not been established; TODO[SECURITY_CONTACT] also needs a maintainer contact decision.
