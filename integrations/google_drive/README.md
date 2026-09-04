# Google Drive Integration

Status: PREPARED, NOT AUTHENTICATED
Date: 2026-09-04

## Purpose

Mirror selected canonical repository documents into Google Drive for human-readable collaboration.

The local Git repository remains the source of truth.

## Files

- `sync.py` - dry-run-first sync tool
- `sync_log.jsonl` - generated local sync log, ignored by Git
- `../../config/drive_manifest.json` - non-secret mapping of repository paths to Drive paths and stable file IDs
- `../../DRIVE_SETUP.md` - user setup instructions

## Authentication

Preferred:

- OAuth 2.0 desktop app credentials for a user-owned Drive

Alternative:

- service account only if explicitly configured and the target Drive folder is shared with it

Never commit credentials or tokens.

## Current Behavior

Dry run:

```powershell
python integrations/google_drive/sync.py --dry-run
```

Apply:

```powershell
python integrations/google_drive/sync.py --apply
```

The script does not attempt authentication in dry-run mode. Apply mode requires Google client libraries and local credentials.

## Supported Sync Goals

- create or find the CAPICAPI Drive root folder
- create subfolders from the manifest path
- upload missing mirrored documents
- update existing mirrored documents by stable Drive file ID
- discover existing files to reduce duplicates
- update the manifest with Drive file IDs, source hashes, and sync timestamps
- write a local sync log

## Non-Goals

- uncontrolled bidirectional sync
- Drive-only canonical documents
- auto-publishing
- credential storage in Git
