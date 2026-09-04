# N8N ARCHITECTURE v1.0

Status: RESERVED, NOT IMPLEMENTED
Date: 2026-09-04

## Purpose

Reserve version-controlled homes and contracts for future n8n workflows without building live automation during Phase 1A.

## Future Workflows

- `MEDIA_INGEST`
- `MEDIA_CLASSIFY`
- `CONTENT_IDEA_GENERATION`
- `CONTENT_GENERATION`
- `CONTENT_REVIEW`
- `TELEGRAM_APPROVAL`
- `CONTENT_SCHEDULING`
- `CONTENT_PUBLISH`
- `METRICS_INGEST`
- `CONTENT_ANALYSIS`
- `EXPERIMENT_ANALYSIS`
- `PRINT_TEST_INGEST`
- `PRODUCTION_UPDATE`

## Local Homes

- workflow JSON: `n8n/workflows`
- reusable subflows: `n8n/subworkflows`
- templates: `n8n/templates`
- workflow schemas: `n8n/schemas`
- prompts: `n8n/prompts`
- fixtures: `n8n/fixtures`

## Rules

- n8n consumes Git-managed schemas and metadata.
- n8n may read/write Drive operational assets only through configured integrations.
- n8n logs must not contain plaintext secrets.
- n8n must not publish content until human approval is recorded.
- n8n does not become the source of truth.
