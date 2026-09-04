# FILESYSTEM ARCHITECTURE v1.0

Status: ACTIVE
Date: 2026-09-04

## Purpose

This document defines the long-term operating filesystem for CAPICAPI across the local/GitHub repository and the Google Drive CAPICAPI workspace.

## Git / Local Repository

Git is the source of truth for:

- code
- documentation
- schemas
- agent definitions
- prompts
- n8n workflow JSON
- integrations
- configuration templates
- tests
- automation logic
- lightweight structured metadata for MVP

Git must not contain:

- OAuth secrets
- tokens
- `.env`
- API keys
- raw video
- raw photo dumps
- STL/3MF production assets
- large generated media
- heavy analytics exports

## Google Drive Workspace

Drive is the operational workspace for heavy and human-operated assets:

- reference images
- raw photos
- raw videos
- printing timelapses
- 3D models
- slicer files
- test print media
- approved product assets
- generated media
- content pipeline assets
- analytics exports
- packaging assets
- agent outputs

Drive folder names help humans navigate, but structured metadata must not depend on Drive folder names alone.

## Lightweight Metadata Storage

Phase 0/MVP storage method:

- JSON files for canonical records
- CSV files where spreadsheet review is useful
- JSON Schema validation in `schemas/`
- Drive file/folder IDs stored in manifests when an asset needs stable external reference

No Postgres, Supabase, vector DB, Redis, or other database is introduced in Phase 0.

Recommended future escalation: introduce SQLite first if local query complexity grows; use a hosted database only when multi-user or automation concurrency requires it.

## Local Folder Purposes

| Path | Purpose |
|---|---|
| `docs/brand` | Capi identity, visual rules, naming, brand book. |
| `docs/product` | Physical product standards, print standards, packaging rules, rarity, Capi/series docs. |
| `docs/marketing` | Content strategy, virality framework, experiment standards, KPIs. |
| `docs/automation` | n8n, approval flow, integration map. |
| `docs/operations` | production workflow, inventory, QA, filesystem, lifecycle, source-of-truth. |
| `agents` | agent contracts, prompts, allowed tools. |
| `n8n` | future version-controlled n8n workflow definitions and fixtures. |
| `schemas` | JSON Schemas for metadata, workflows, and handoffs. |
| `integrations` | Google Drive, Telegram, social, and AI provider integration code/contracts. |
| `config` | non-secret manifests and environment examples. |
| `data/metadata` | MVP structured metadata records, not heavy assets. |
| `logs` | local non-secret logs and error/dead-letter contracts. |
| `tests` | validation tests for schemas and automation logic. |
| `archive` | superseded local docs and versioned artifacts. |

## Drive Folder Purposes

| Drive Path | Purpose |
|---|---|
| `00_ADMIN` | mirrored master docs, reports, and decisions. |
| `01_PRODUCT` | product development assets, Capi folders, models, slicer files, tests, approvals. |
| `02_PRINTING` | Bambu profiles, material/color/multicolor/waste tests, benchmarks. |
| `03_MEDIA_INBOX` | low-friction phone/raw media dump. |
| `04_CONTENT_PIPELINE` | content lifecycle from inbox through published/rejected. |
| `05_AI_ASSETS` | generated images, video, voice, music, temporary AI assets. |
| `06_SOCIAL` | platform-specific assets and analytics exports. |
| `07_MARKETING` | experiments, winners, failed tests, hooks, creative library. |
| `08_PACKAGING` | packaging artwork, dielines, renders, print files. |
| `09_INVENTORY` | inventory exports and operational inventory assets. |
| `10_ORDERS` | order exports and fulfillment operational files. |
| `11_AGENT_OUTPUTS` | heavy reports and artifacts produced by agents. |
| `99_ARCHIVE` | retired Drive assets and version history. |

## Folder Naming

Use uppercase Drive top-level operational folders with numeric prefixes for stable human ordering.

Use stable IDs for product/entity folders:

- `CAPI_001`
- `SERIES_01`
- `BATCH_20260904_0001`
- `CONTENT_2026_000001`

Do not rename ID folders after records exist. Use display names in metadata instead.

## File Naming

Use filenames for readability, not identity.

Recommended format:

```text
<stable-id>__<short-description>__v<major.minor>__<YYYYMMDD>.<ext>
```

Examples:

- `CAPI-S01-001-M001__front-render__v0.1__20260904.png`
- `PT-CAPI-S01-001-0001__slicer-export__v0.1__20260904.3mf`
- `CONTENT-2026-000001__approval-preview__v0.1__20260904.mp4`

## Versioning

Git-managed specs use semantic document versions. Drive assets use explicit file versions or revision IDs in metadata. Do not overwrite a production-approved asset without preserving the prior revision in archive or metadata history.

## Archive Policy

Archive when:

- an asset is superseded
- a test is obsolete but historically useful
- a content item is rejected permanently
- a production file is retired

Do not archive to hide failures. Failed tests remain part of the evidence base.

## Deviation From Approved Base

Earlier Phase 0 documents under `docs/experiments`, `docs/research`, and legacy agent specs are preserved as supplemental work. The approved architecture is now represented through root `AGENTS.md`, `docs/automation`, `n8n`, new schemas, and Drive folder manifests.
