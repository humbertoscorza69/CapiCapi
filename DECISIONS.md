# Decisions

Meaningful project decisions are recorded here. Do not silently rewrite major project rules; create a new decision or versioned amendment.

## Decision D-0001

Date: 2026-09-04

Decision: The local Git repository is the canonical technical source of truth.

Reason: CAPICAPI requires versioned documents, schemas, decisions, and repeatable integration behavior.

Evidence: Project brief requires local repo canonical source and Google Drive as a controlled mirror.

Alternatives considered: Google Drive as primary source; uncontrolled bidirectional sync.

Consequences: Important documents originate in Git. Drive sync must be explicit, logged, and ID-stable.

Reversible? YES

## Decision D-0002

Date: 2026-09-04

Decision: Google Drive integration is prepared but not authenticated or run automatically.

Reason: Credentials are not available and secrets must not be committed.

Evidence: Project brief requires OAuth 2.0 or explicitly configured service account and no hardcoded credentials.

Alternatives considered: Manual uploads; hardcoded credentials; automatic cloud setup.

Consequences: User must configure credentials before Drive mirroring can run.

Reversible? YES

## Decision D-0003

Date: 2026-09-04

Decision: Standard Capi production targets zero supports, zero manual assembly, zero sanding, zero painting, and zero post-processing.

Reason: Manual labor per unit is treated as a scaling defect.

Evidence: Project brief establishes the hard manufacturing philosophy.

Alternatives considered: Higher-detail models with supports; painted details; multi-part assembly.

Consequences: Product design must fail or escalate when it cannot meet support-free and assembly-free constraints.

Reversible? YES, only with documented manufacturing evidence.

## Decision D-0004

Date: 2026-09-04

Decision: Capi v0 must precede Capi Master approval and Series 01.

Reason: Capi v0 is the engineering test asset that discovers size, quality, purge behavior, and production constraints.

Evidence: Project brief explicitly forbids beginning Series 01 before Capi v0 validation.

Alternatives considered: Designing sellable characters immediately.

Consequences: Series planning remains blocked until Capi v0 digital and physical validation.

Reversible? NO

## Decision D-0005

Date: 2026-09-04

Decision: Standard Capi variants are constrained to a maximum of 4 automatic colors, with 3 colors preferred.

Reason: Initial production hardware is Bambu Lab A1 with AMS Lite.

Evidence: Project brief and official Bambu A1 FAQ indicate A1 supports one AMS Lite, limiting automatic printing to 4 colors.

Alternatives considered: Manual filament swaps; painting; multi-part color assembly.

Consequences: Color-Z audits are required because color count alone is insufficient.

Reversible? YES, if manufacturing hardware or process changes.

## Decision D-0006

Date: 2026-09-04

Decision: Rarity probabilities and edition counts are not finalized in Phase 0.

Reason: Scarcity claims must be truthful and manufacturing economics are unmeasured.

Evidence: Project brief requires no fake precision and truthful scarcity.

Alternatives considered: Creating launch probabilities now.

Consequences: Rarity system defines tiers and controls, not production odds.

Reversible? YES

## Decision D-0007

Date: 2026-09-04

Decision: The Google Drive mirror is activated through the Desktop OAuth client in the current CapiCapi Google Cloud project.

Reason: The project needs a separate human-readable Drive mirror while preserving the local Git repository as canonical source of truth.

Evidence: Google Cloud Console showed project `CapiCapi`, OAuth client `Desktop client 1`, type `Escritorio`, and a client ID matching the local credentials file. The Google Auth Platform audience is External users, Testing status, with `humbertoscorza69@gmail.com` registered as a test user. The sync completed and a follow-up dry run reported all configured documents unchanged.

Alternatives considered: Publishing the app; creating fake homepage/privacy-policy URLs; using a service account.

Consequences: `config/drive_manifest.json` now stores stable Drive folder/file IDs. Local `credentials.json`, `token.json`, and sync log artifacts remain ignored by Git.

Reversible? YES
