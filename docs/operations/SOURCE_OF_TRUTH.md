# SOURCE OF TRUTH v1.0

Status: ACTIVE
Date: 2026-09-04

## Policy

The local Git repository is the canonical technical source of truth for CAPICAPI.

Google Drive is a published/collaboration mirror. It must not become the only copy of important documents.

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
