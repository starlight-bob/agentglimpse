# Known limitations

- **Scope:** native macOS app; no Windows/Linux application or web dashboard is established.
- **Usage:** Codex quota percentages and reset times only. No confirmed raw token totals, dollar accounting, per-task usage attribution, Claude usage, or all-product ChatGPT quotas.
- **Availability:** account windows and plan information depend on what Codex returns. Spark placeholders do not prove access to that model or a particular entitlement.
- **Activity coverage:** local journal detection depends on an observed format. Cloud tasks, nested/asynchronous requests, and every approval/error/limit path are not covered.
- **Outcome semantics:** done can mean completed or aborted; it is not a success verdict. An idle cat means no current displayed state, not proof no agent is running anywhere.
- **Concurrency:** separate local Codex sessions are aggregated; external JSON is newest-per-agent and can lose simultaneous-task detail. Fresh adapter signals can supersede older ones.
- **Desktop adapters:** Accessibility depends on exposed controls. Notification text parsing and the internal macOS notification schema can change or produce false classifications.
- **Privacy:** optional adapters and legacy hooks can persist content excerpts. The default extra folder can be shared; defaults do not imply strict local isolation.
- **Clear actions:** can delete JSON in all watched directories. Display expiry alone does not delete old files.
- **Local gate:** existing private access screen must be resolved for public users. It is not a security boundary; usage preview is separate from normal sign-in gating.
- **Refresh:** account usage refresh runs even with the panel closed while normal monitoring is active. No configuration flag for disabling it was found.
- **Packaging:** source uses old names, an icon checksum guard, and ad-hoc signing. Renaming the README does not rename the installed app.
- **Compatibility:** macOS 14 is declared; Intel/universal artifacts, oldest working SDK, and a full OS test matrix are not verified here.
- **Accessibility:** source includes accessibility labels and Reduce Motion checks, but no complete accessibility audit is claimed.

See [troubleshooting](troubleshooting.md) for practical checks and [open decisions](../launch/OPEN_DECISIONS.md) for launch blockers.
