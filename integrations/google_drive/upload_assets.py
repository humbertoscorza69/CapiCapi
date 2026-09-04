"""Upload heavy CAPICAPI assets to Google Drive.

The local repository remains the canonical source for code and lightweight
metadata. This helper uploads generated or operational assets into the approved
Drive workspace using the same OAuth configuration as the document sync tool.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
from pathlib import Path
from typing import Any

import sync as drive_sync


def find_named_child(service: Any, parent_id: str, name: str) -> str | None:
    query = (
        f"name = '{drive_sync.q(name)}' and "
        f"'{drive_sync.q(parent_id)}' in parents and trashed = false"
    )
    response = (
        service.files()
        .list(q=query, spaces="drive", fields="files(id, name)", pageSize=1)
        .execute()
    )
    files = response.get("files", [])
    return files[0]["id"] if files else None


def upload_file(
    service: Any,
    libs: dict[str, Any],
    path: Path,
    parent_id: str,
    drive_name: str | None,
) -> str:
    if not path.exists() or not path.is_file():
        raise drive_sync.SyncError(f"Missing asset file: {path}")

    name = drive_name or path.name
    mime_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    media = libs["MediaFileUpload"](str(path), mimetype=mime_type, resumable=False)
    existing_id = find_named_child(service, parent_id, name)

    if existing_id:
        service.files().update(fileId=existing_id, media_body=media).execute()
        return existing_id

    metadata = {"name": name, "parents": [parent_id]}
    created = (
        service.files()
        .create(body=metadata, media_body=media, fields="id")
        .execute()
    )
    return created["id"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drive-folder", required=True)
    parser.add_argument("--summary-json", required=True)
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    libs = drive_sync.require_google_client_libs()
    manifest = drive_sync.load_manifest(drive_sync.DEFAULT_MANIFEST)
    service = drive_sync.authenticate(libs, open_browser=not args.no_browser)
    folder_id = drive_sync.ensure_folder_path(service, manifest, args.drive_folder)

    uploads = []
    for file_arg in args.files:
        path = Path(file_arg).resolve()
        file_id = upload_file(service, libs, path, folder_id, path.name)
        uploads.append(
            {
                "local_path": str(path),
                "drive_name": path.name,
                "drive_file_id": file_id,
                "drive_folder": args.drive_folder,
                "drive_folder_id": folder_id,
            }
        )
        print(f"uploaded: {path.name} -> {args.drive_folder}")

    summary_path = Path(args.summary_json)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps(
            {
                "drive_folder": args.drive_folder,
                "drive_folder_id": folder_id,
                "uploads": uploads,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"summary: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
