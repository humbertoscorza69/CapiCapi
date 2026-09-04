# ID STANDARD v1.0

Status: ACTIVE
Date: 2026-09-04

## Purpose

Stable IDs allow CAPICAPI to connect Drive assets, Git metadata, n8n workflows, content, print tests, and agent logs without relying on filenames.

## ID Conventions

| Entity | Format | Example |
|---|---|---|
| Series | `SNN` | `S01` |
| Capi/Product | `CAPI-SNN-NNN` | `CAPI-S01-001` |
| Model revision | `CAPI-SNN-NNN-MNNN` | `CAPI-S01-001-M001` |
| Print test | `PT-CAPI-SNN-NNN-NNNN` | `PT-CAPI-S01-001-0001` |
| Production batch | `BATCH-YYYYMMDD-NNNN` | `BATCH-20260904-0001` |
| Content item | `CONTENT-YYYY-NNNNNN` | `CONTENT-2026-000001` |
| Marketing experiment | `EXP-YYYY-NNNN` | `EXP-2026-0001` |
| Social publication | `PUB-YYYY-NNNNNN` | `PUB-2026-000001` |
| Agent run | `RUN-YYYYMMDD-AGENT-NNNN` | `RUN-20260904-ORCHESTRATOR-0001` |

## Rules

- IDs are unique.
- IDs are stable after creation.
- IDs are human-readable.
- IDs are machine-readable.
- IDs are independent of filenames and folder names.
- Public display names may change without changing IDs.

## Allocation

Phase 0 allocation is manual but must be recorded in structured metadata.

Future automation may allocate IDs through a single n8n subworkflow or local script. That allocator must check existing metadata records before issuing a new ID.
