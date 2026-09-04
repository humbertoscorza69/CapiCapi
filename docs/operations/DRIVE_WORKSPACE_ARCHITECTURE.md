# GOOGLE DRIVE WORKSPACE ARCHITECTURE v1.0

Status: ACTIVE
Date: 2026-09-04

## Purpose

The CAPICAPI Drive workspace stores heavy and operational assets that do not belong in Git.

## Created Root

Drive root:

```text
CAPICAPI/
```

## Approved Folder Hierarchy

The operational hierarchy is managed through `config/drive_manifest.json` and created by `integrations/google_drive/sync.py --apply`.

Initial template scope:

- `BASE_CAPI`
- `SERIES_01`
- `SERIES_01/CAPI_001`

Future Capi folders must be generated programmatically from the `CAPI_001` template pattern.

## Low-Friction Media Inbox

The human operator should dump phone/raw assets into:

```text
CAPICAPI/03_MEDIA_INBOX/
```

Broad subfolders:

- `PHOTOS`
- `VIDEOS`
- `TIMELAPSES`
- `PRINTING`
- `PACKAGING`
- `OTHER`

The operator does not need to rename files, assign IDs, classify platform use, or move files into campaign folders. Future automation will ingest, classify, tag, and route assets.

## Drive Is Not The Database

Drive paths are operational. Structured metadata records live in Git for MVP under `data/metadata` and follow JSON Schemas in `schemas/`.

When Drive assets become part of a product, print test, content item, or publication record, metadata should store:

- Drive file ID
- Drive folder ID where useful
- stable CAPICAPI entity ID
- lifecycle status
- source relationship
- hash if practical

## Existing Documentation Mirror

The previous document mirror remains active and is not broken. The operational asset hierarchy is added alongside it. Documentation may later be mirrored into `00_ADMIN/MASTER_DOCS`, but the existing mirror paths remain stable until a deliberate migration decision is made.
