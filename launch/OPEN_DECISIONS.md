# Open decisions

Every unresolved marker uses the `TODO[...]` convention. These are explicit gaps, not hidden assumptions. Source-verified behavior is documented without a placeholder.

| Marker | Needed decision or evidence | Where it matters |
| --- | --- | --- |
| TODO[NAME_AVAILABILITY] | Verify the intended repository/domain namespace for the selected AgentGlimpse name | Naming and metadata |
| TODO[OWNER] | Public GitHub owner and canonical URL for `agentglimpse` | Metadata and announcement link |
| TODO[LICENSE_CHOICE] | Copyright-holder choice of software and contribution license | LICENSE, README, CONTRIBUTING |
| TODO[COPYRIGHT] | Correct copyright year(s) and public holder name | MIT candidate / adopted LICENSE |
| TODO[ACCESS_GATE] | Remove or replace private-build gate; define usable public onboarding | Code and installation |
| TODO[SOURCE_BASELINE] | Confirm exact reviewed source commit and matching binary | Source import, release reproducibility |
| TODO[RENAME] | Choose display-only transition or full technical migration; implement and test | App, helpers, paths, settings |
| TODO[BUILD_MATRIX] | Minimum working toolchain/SDK; tested OS and CPU architectures | Compatibility claims |
| TODO[SIGNING] | Actual Developer ID/notarization/distribution choice and evidence | Installation and release |
| TODO[SECURITY_CONTACT] | Enable/test private reports or provide a monitored private route | Security/privacy reporting |
| TODO[ASSET_RIGHTS] | Clear or replace third-party artwork; fill required notices | Resources and visuals |
| TODO[RELEASE] | Version, date, artifact names, checksums, download URL, support scope | Changelog and release notes |
| TODO[VALIDATION] | Run app/release checks on the final public source and record results | Launch validation |

The MIT file is a complete license candidate, not an adopted license. The root LICENSE intentionally records the pending decision. No answer to an optional license question is treated as consent to a license.

After resolving decisions, remove or rewrite the relevant draft markers and checklist entries. Run the release check again. A passing documentation check alone cannot approve rights, signing, or functionality.
