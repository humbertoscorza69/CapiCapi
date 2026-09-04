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

Amendment: Refined by D-0009. This means Capi v0 must precede Capi Master v1.0 production lock and Series 01, not that Capi v0 defines CAPICAPI's visual identity.

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

## Decision D-0008

Date: 2026-09-04

Decision: CAPICAPI uses a two-tier operating filesystem: Git/GitHub for code, docs, schemas, agent definitions, prompts, n8n workflows, integrations, tests, and lightweight metadata; Google Drive for heavy operational assets.

Reason: The business needs both version-controlled technical truth and a low-friction human asset workspace for raw media, 3D files, slicer files, test print media, generated media, approvals, exports, and agent outputs.

Evidence: The approved Phase 0 filesystem architecture requires separate responsibilities between local/GitHub and Drive and a low-friction media inbox for phone/raw asset dumps. The Drive hierarchy was created through the authenticated Google Drive integration and the manifest now stores stable folder IDs.

Alternatives considered: Keeping heavy assets in Git; treating Drive folder names as the database; introducing a database before real workflow volume exists.

Consequences: Heavy/operational assets stay out of Git. Structured metadata starts as JSON/CSV under `data/metadata` and validates against schemas. Future n8n workflows must use IDs and metadata, not filenames alone.

Reversible? YES

## Decision D-0009

Date: 2026-09-04

Decision: Phase 1 is split into Phase 1A visual direction exploration, Phase 1B provisional visual master/reference pack, and Phase 1C provisional 3D master adapted for DFM before Phase 2 Capi v0 engineering validation.

Reason: CAPICAPI needs proprietary, repeatable visual IP before engineering the first physical prototype, but the final production master must not be locked before physical FDM evidence shows what survives manufacturing.

Evidence: Phase 1A identified that `CAPI_MASTER_SPEC.md` and `VISUAL_LANGUAGE.md` were structurally sound but too broad to define stable character recognition, reference-package requirements, or 3D modeling handoff rules.

Alternatives considered: Treating `CAPI_V0_BRIEF.md` as the visual identity source; locking a consumer character before physical testing; beginning final 3D modeling before human visual approval.

Consequences: `docs/product/CAPI_V0_BRIEF.md` is reclassified as a future engineering prototype brief. The active Phase 1A identity source is `docs/brand/CAPI_VISUAL_DNA.md`. Capi v0 still precedes Capi Master v1.0 production lock and Series 01, but it no longer defines CAPICAPI's visual identity.

Reversible? YES, with owner approval and a recorded replacement phase decision.

## Decision D-0010

Date: 2026-09-04

Decision: Phase 1A visual exploration uses four materially different lanes: Grounded Loaf Collectible, Designer Toy Mascot, Expressive Stylized / Anime-adjacent, and Sculptural Art Toy.

Reason: The three-lane model did not sufficiently test the expressive/stylized end of the character design space. CAPICAPI needs to compare base character DNA before costumes, props, expression tricks, or material styling influence the decision.

Evidence: Owner approved Phase 1A architecture with a required amendment adding an expressive stylized lane, a mandatory base character round, expression tests, role stress tests, a structured scorecard, and an external visual reference policy.

Alternatives considered: Keeping three directions; allowing role/costume concepts before base comparison; treating scorecard ranking as automatic approval.

Consequences: No visual generation begins until the four base-character prompts are reviewed. Scores are advisory only; human judgment remains authoritative.

Reversible? YES, with owner approval and a recorded replacement exploration decision.
