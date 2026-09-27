# Product research and evidence

Prepared 2026-09-25. This file explains which claims are grounded in available history and source, which are historical reports, and which remain proposals.

## Coverage and access limits

The supplied cached preview of “Github launch materials” was available. The requested `read_thread` tool and a ChatGPT conversation search/history connector were not exposed in this session. The referenced ChatGPT conversation could not be fetched beyond that preview, and a full search of the user's ChatGPT account was not performed.

As a fallback, relevant local Codex task records were read in place, followed by the actual local application source. This recovered extensive product development discussions without claiming access to unavailable ChatGPT history. Only product-relevant records were used; raw transcripts, private credentials, personal screenshots, and unrelated account data are not included in this package.

Evidence sets:

- **H0 — supplied launch preview:** the user describes an agent-status and usage app with a liquid-glass appearance and asks for a GitHub launch package and new name.
- **H1 — local development task beginning 2026-09-13:** the user requests repairs to Codex/Claude detection, lighter icons, independent app behavior, a local access gate, sign-out, a usage panel, glass refinements, an animated cat, clear controls, icon updates, and Dock presence. User requests were compared with subsequent assistant completion reports and current source, rather than assumed shipped merely because requested.
- **H2 — local development task beginning 2026-09-17:** standard Command-Q/application-menu behavior; handling missing Spark data; adaptive panel height, supplied SVG, and actual account-plan label. Completion reports identify 1.4.7, 1.4.8, and 1.4.9.
- **H3 — local product-description message on 2026-09-18:** the user calls AgentBeacon a Dynamic Island-style indicator for usage and agent progress. This supports the intended positioning, not a numeric progress or token-count implementation.
- **H4 — name selection in this task:** the project owner selected AgentGlimpse and requested corresponding changes across the launch files.
- **S1 — local application source snapshot:** `Package.swift`, `Resources/Info.plist`, 15 Swift source files, existing tests, installers, helper, hooks, README, and usage-panel notes. Info.plist says 1.4.9 / build 19; the old README title still says 1.2.3. A file-hash inventory is supplied in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json).

The available source is the strongest evidence for current implementation behavior. Historical assistant statements about successful tests are recorded as reports, not re-executed validations. Source identity still needs to be reconciled with the eventual release commit and binary.

## Product understanding

The central job is reducing the need to reopen an agent window simply to check whether it is busy or needs attention. The product combines an ambient menu bar indicator with an on-demand usage panel. Its design is part of its value: small recognizable provider badges, a softly frosted surface, compact controls, and an idle cat that gives an otherwise utilitarian monitor personality.

Activity and usage are technically distinct. Activity comes from multiple local adapters with different coverage. Usage is a read of Codex account limits, not an estimate from task text. The product is a standalone native Mac app with a Dock icon and lifecycle controls; integrations can involve hooks or a skill, but calling the whole product just a plugin would be incomplete.

## Claim-to-evidence map

| Claim | Primary evidence | Assessment |
| --- | --- | --- |
| Native Mac app, Swift/AppKit/SwiftUI | S1 `Package.swift`, `main.swift`, `AppDelegate.swift`, `UsagePanel.swift` | Implemented |
| Menu bar pill with per-agent identity and status | H1; S1 `PillRenderer.swift`, `Model.swift` | Implemented |
| Animated left-facing ginger cat | H1; S1 `PillRenderer.swift` transform/drawing, `AppDelegate.swift` animation | Implemented |
| Conditional Liquid Glass and fallback materials | H1; S1 `UsagePanel.swift` availability checks | Implemented; full OS matrix unverified |
| Local Codex start/done/abort/input tracking | H1; S1 `CodexSessionWatcher.swift` and activity tests | Implemented for observed journal shape |
| Concurrent local task handling | H1; S1 `StateStore.aggregate`, per-file journal sessions | Implemented; external files differ |
| Claude/ChatGPT/Codex desktop readers | H1; S1 AX/notification watcher identifier maps | Implemented, permission- and format-dependent |
| Connected-folder state bridge | S1 `Model.swift`; installed legacy skill corroborates folder-writing model | Implemented; producer setup required |
| Codex percentages and reset times | H1/H2; S1 `UsageMonitor.swift` | Implemented; raw token counting absent |
| Account-plan header and dynamic height | H2; S1 panel/layout/monitor files | Implemented |
| Missing Spark displayed unavailable | H2; S1 `displayBuckets` and usage tests | Implemented presentation fallback |
| Dock and standard Command-Q | H1/H2; S1 `LSUIElement=false`, regular activation, application menu | Implemented; fresh release still needs manual validation |
| Local access gate, remembered completion, Sign Out | H1; S1 gate/window and lifecycle code | Implemented private-build behavior; public policy unresolved |
| No direct app analytics sender found | S1 inspected source | Bounded source-review observation, not network audit |
| Notification/hook message retention | S1 `NotificationWatcher.swift`, `Log.swift`, helper | Implemented; must be disclosed |
| AgentGlimpse name | H4 — owner selection in this task | Selected public name; app code migration remains pending |
| MIT candidate and GitHub templates | This package | New launch materials; license remains a proposal |

## Corrections to stale or overly broad claims

1. The old README's teal idle light has been replaced by the cat in current code.
2. The old README version heading is stale; Info.plist and the later task agree on 1.4.9.
3. “Token usage” is colloquial in the launch request. Current code shows rate-limit percentages and windows; no raw-token or spend calculation was found.
4. Usage refresh is active on a timer even with the panel closed. It is not only an on-open feature.
5. General “no content retained” language would be false: notification messages and legacy hook excerpts can reach state and logs; opt-in AX dumps can contain UI text.
6. Source runtime minimum macOS 14 does not mean a macOS 14 SDK can compile current macOS 26 glass calls, nor prove Intel support.
7. Expiry does not delete external files, but explicit Clear does. Both facts belong in public docs.
8. The app is now a regular Dock application, not strictly a hidden menu bar utility.
9. The access gate is a local preference/verifier mechanism, and usage preview is separate from that gate. It should not be sold as secure authentication.
10. Historical UI changes and test reports are not proof of a signed, notarized, publicly released artifact.

## Not established

No confirmed public repository owner, adopted software license, copyright identity, public access policy, downloadable AgentGlimpse binary, notarization record, full compatibility matrix, asset redistribution clearance, public security contact, or first public release tag was found. These are tracked in [OPEN_DECISIONS.md](OPEN_DECISIONS.md).

No evidence establishes Claude usage figures, token-price accounting, per-task numerical progress, notifications sent by AgentGlimpse itself, mobile apps, Windows/Linux support, cloud synchronization built by this project, an auto-updater, or agent orchestration. They are not advertised.
