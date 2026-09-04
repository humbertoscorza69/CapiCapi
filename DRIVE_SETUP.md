# Google Drive Setup

The repository is the canonical source. Google Drive is only a controlled mirror for selected operational documents.

## Required User Steps

1. Create or select a Google Cloud project.
2. Enable the Google Drive API for that project.
3. Configure an OAuth consent screen for a user-owned Drive.
4. Create OAuth 2.0 Client ID credentials for a desktop application.
5. Download the client secret JSON.
6. Save it locally as `integrations/google_drive/credentials.json`.
7. Copy `.env.example` to `.env`.
8. Confirm `.env` points to the credential and token paths.
9. Review `config/drive_manifest.json`.
10. Run a dry run:

```powershell
python integrations/google_drive/sync.py --dry-run
```

11. When the dry run looks correct, run:

```powershell
python integrations/google_drive/sync.py --apply
```

## Service Account Alternative

Use a service account only if explicitly configured and the target Drive folder is shared with the service account email. OAuth is preferred because this is a user-owned business Drive.

## Never Commit

- `.env`
- `credentials.json`
- `token.json`
- client secrets
- service account private keys
- API keys

These are covered by `.gitignore`, but the operator is still responsible for reviewing `git status` before every commit.

## Current Status

Drive integration status: PREPARED, NOT AUTHENTICATED.

No credentials are present, no Drive folders have been created, and no documents have been uploaded.
