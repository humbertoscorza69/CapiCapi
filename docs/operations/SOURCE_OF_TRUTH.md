# SOURCE OF TRUTH v1.0

Status: ACTIVE
Date: 2026-09-04

## Policy

The local Git repository is the canonical technical source of truth for CAPICAPI.

Google Drive is a published/collaboration mirror for selected documents and the operational workspace for heavy assets. It must not become the only copy of important documents or structured metadata.

## Canonical Artifacts

Canonical artifacts include:

- Markdown specifications
- decision logs
- JSON Schemas
- non-secret manifests
- source code
- experiment protocols
- production records
- measured data files

## Drive-Owned Operational Assets

Drive owns heavy operational assets:

- raw photos and videos
- printing timelapses
- 3D production model files
- slicer files
- test print media
- generated media
- analytics exports
- packaging assets
- agent output artifacts

Structured metadata for those assets starts in Git under `data/metadata` for Phase 0/MVP. Drive file and folder IDs may be referenced in metadata, but folder names are not the database.

## Mirror Rules

Drive sync must be:

- explicit
- dry-run capable
- logged
- based on stable file IDs where possible
- duplicate-resistant
- one-way from local repo to Drive unless a future decision changes this

## Forbidden

- uncontrolled bidirectional sync
- credentials committed to Git
- Drive-only source documents
- silent rewrites of major rules
- manual edits in Drive that are treated as canonical without being pulled back into Git deliberately
