# Security policy

## Report a vulnerability privately

TODO[SECURITY_CONTACT]: Before public launch, enable GitHub private vulnerability reporting or publish a monitored security contact. Neither is confirmed by this draft.

If the repository offers **Security → Report a vulnerability**, use it. If it is unavailable and no private contact has been published, do not put exploit details, credentials, or personal logs in a public issue; ask the maintainer to establish a private route without disclosing the sensitive details.

Include the affected version, macOS version, relevant adapter, impact, minimal reproduction, and sanitized supporting information. Never send real account credentials, full session journals, notification databases, or a working private access-gate secret.

## Supported versions

TODO[RELEASE]: Publish the first public version and its security-support scope. The inspected local baseline is AgentBeacon 1.4.9 (build 19); this is not evidence of a public support commitment. No response-time or fix-time guarantee has been established.

## Boundaries that matter

- Activity badges are advisory UI, not proof of task success or an authorization decision. Aborted local tasks also become done.
- State JSON is trusted local input. A process able to write a watched folder can influence the displayed status. Use dedicated folders, not arbitrary shared directories.
- The optional window reader uses Accessibility. The optional notification reader uses Full Disk Access and an internal macOS database format.
- Notification and hook messages can be written to local files. A connected or synced directory can expose those files beyond this app.
- Usage retrieval invokes the installed Codex executable with the user's existing account session. Executable discovery, subprocess handling, and response parsing are relevant review areas.
- The existing local sign-in screen uses a bundled verifier and a saved preference. It is not an online identity service, encryption boundary, or tamper-resistant licensing system. The usage-preview command can query usage without unlocking the normal app UI.
- The supplied legacy hook installer modifies agent configuration and is not a transactional configuration editor. Review it and back up affected files before use.

See [privacy](docs/privacy.md) and [known limitations](docs/known-limitations.md) for current behavior. No security audit, notarization, sandbox certification, or vulnerability bounty is claimed.
