# Google Drive Setup

The repository is the canonical source. Google Drive is only a controlled mirror for selected operational documents.

## Required User Steps

1. Create or select a Google Cloud project.
2. Enable the Google Drive API for that project.
3. Configure an OAuth consent screen for a user-owned Drive.
4. Create OAuth 2.0 Client ID credentials for a desktop application.
5. Download the client secret JSON.
6. Save it locally as `integrations/google_drive/credentials.json`.
7. If the OAuth app is in Testing mode, add the owner Google account as a test user in Google Cloud Console.
8. Copy `.env.example` to `.env`.
9. Confirm `.env` points to the credential and token paths.
10. Review `config/drive_manifest.json`.
11. Run a dry run:

```powershell
python integrations/google_drive/sync.py --dry-run
```

12. When the dry run looks correct, run:

```powershell
python integrations/google_drive/sync.py --apply
```

If the browser authorization prompt does not appear clearly, run:

```powershell
python integrations/google_drive/sync.py --apply --no-browser
```

Then open the printed Google authorization URL manually.

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

Drive integration status: AUTHENTICATED AND SYNCED.

The local OAuth client secret is present at `integrations/google_drive/credentials.json`, which is ignored by Git. The local OAuth token is present at `integrations/google_drive/token.json`, which is also ignored by Git. The configured documents have been mirrored to a separate `CAPICAPI` folder in Google Drive.

## Known OAuth Blocker

If Google shows `Access blocked: Capi Capi has not completed the Google verification process` with `Error 403: access_denied`, the OAuth app is still in Testing mode and the signed-in account is not allowed as a tester.

Fix in Google Cloud Console:

1. Open the Google Cloud project that owns the OAuth client.
2. Go to APIs & Services > OAuth consent screen.
3. Add the Google account that will authorize Drive access under Test users.
4. Save the change.
5. Run `python integrations/google_drive/sync.py --apply --no-browser` again.

This project is intended to stay in External + Testing mode during development. Do not publish the app or create fake homepage/privacy-policy URLs just to support local development.
