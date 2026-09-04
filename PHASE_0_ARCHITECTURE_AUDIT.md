# Phase 0 Filesystem / Architecture Audit

Date: 2026-09-04
Status: COMPLETE

## 1. Local Structure Created

Created or expanded local/GitHub structure for root operating docs, approved docs areas, approved agent homes, n8n, integrations, config, metadata, logs, tests, schemas, and archive/versioning.

Preserved supplemental docs under `docs/experiments` and `docs/research`, plus detailed first-pass agent specs.

## 2. Drive Structure Created

Created the approved operational hierarchy under the existing `CAPICAPI` Drive root:

- `00_ADMIN`
- `01_PRODUCT`
- `01_PRODUCT/BASE_CAPI`
- `01_PRODUCT/SERIES_01`
- `01_PRODUCT/SERIES_01/CAPI_001`
- `01_PRODUCT/FUTURE_SERIES`
- `02_PRINTING`
- `03_MEDIA_INBOX`
- `04_CONTENT_PIPELINE`
- `05_AI_ASSETS`
- `06_SOCIAL`
- `07_MARKETING`
- `08_PACKAGING`
- `09_INVENTORY`
- `10_ORDERS`
- `11_AGENT_OUTPUTS`
- `99_ARCHIVE`

Template scope intentionally stops at `BASE_CAPI`, `SERIES_01`, and `CAPI_001`. No mass Capi folder generation was performed.

## 3. Source Of Truth Matrix

| Data class | Source of truth | Heavy asset home |
|---|---|---|
| Code/integrations | Git | Not applicable |
| Docs/specs | Git | Mirrored selectively to Drive |
| Schemas | Git | Not applicable |
| Agent definitions/prompts | Git | Agent artifacts in Drive |
| n8n workflow JSON | Git | Runtime logs/exports in Drive if heavy |
| Capi/product metadata | Git JSON/CSV under `data/metadata` | `CAPICAPI/01_PRODUCT` |
| Series metadata | Git JSON/CSV under `data/metadata` | `CAPICAPI/01_PRODUCT` |
| 3D model files | Metadata in Git | `CAPICAPI/01_PRODUCT/**/MODELS` |
| Slicer/3MF files | Metadata in Git | `CAPICAPI/01_PRODUCT/**/SLICER`, `CAPICAPI/02_PRINTING/PROFILES` |
| Print test measurements | Git structured metadata | Drive photos/videos/timelapses under test folders |
| Raw photos/videos | Drive | `CAPICAPI/03_MEDIA_INBOX` |
| AI-generated media | Metadata in Git when promoted | `CAPICAPI/05_AI_ASSETS` |
| Content records | Git structured metadata | `CAPICAPI/04_CONTENT_PIPELINE` |
| Publications | Git structured metadata | `CAPICAPI/06_SOCIAL` |
| Analytics exports | Metadata/summaries in Git | `CAPICAPI/06_SOCIAL/ANALYTICS_EXPORTS` |
| Packaging assets | Rules in Git | `CAPICAPI/08_PACKAGING` |
| Inventory/orders | Structured metadata in Git for MVP | `CAPICAPI/09_INVENTORY`, `CAPICAPI/10_ORDERS` |
| Agent logs | Non-secret structured records in Git when useful | Heavy outputs in `CAPICAPI/11_AGENT_OUTPUTS` |

## 4. Schemas Created

- `schemas/capi.schema.json`
- `schemas/series.schema.json`
- `schemas/model_revision.schema.json`
- `schemas/print_test.schema.json`
- `schemas/production_batch.schema.json`
- `schemas/content_item.schema.json`
- `schemas/experiment.schema.json`
- `schemas/publication.schema.json`
- `schemas/agent_event.schema.json`
- updated `schemas/drive_manifest.v1.schema.json` for Drive folders

## 5. Unresolved TBDs

- physical product size
- layer height
- support-free geometry limits
- minimum printable feature sizes
- filament brands/SKUs
- material cost
- purge/waste behavior
- print time
- packaging design
- inventory/SKU implementation
- social platform credentials
- n8n runtime deployment
- Telegram approval implementation
- content KPI formulas

All manufacturing values remain `TBD — REQUIRES PHYSICAL TEST`.

## 6. Security Concerns

- `credentials.json`, `token.json`, `.env`, sync logs, heavy media, and 3D production assets are ignored by Git.
- OAuth token exists locally after authorization and must not be copied into docs, logs, or Drive.
- Future n8n exports must be reviewed to ensure credentials are not embedded.
- Logs must never contain plaintext secrets or OAuth refresh tokens.

## 7. Missing Before Phase 0 Complete

No blocking filesystem/data-architecture items remain for Phase 0.

Still intentionally not started:

- Capi v0 modeling
- filament/color selection
- physical print testing
- social publishing automation
- live n8n workflows
- database infrastructure

## 8. Idempotency Evidence

The Drive hierarchy is managed by `config/drive_manifest.json`. The sync script finds existing folders by parent/name and stores stable Drive folder IDs, so repeat runs do not create duplicate folders.

Final idempotency test status: PASS. A second Drive apply completed against the same managed folder paths after initial creation without creating a separate hierarchy.

## 9. Deviations From Approved Base

- Preserved `docs/experiments` and `docs/research` from earlier Phase 0 work because they contain useful policy and source records.
- Preserved detailed legacy agent specs alongside the approved agent homes instead of deleting them.
- Kept the existing document mirror paths stable to avoid breaking previously created Drive Docs. The new Drive operational hierarchy was added alongside the mirror.
