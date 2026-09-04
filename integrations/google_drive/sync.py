"""Dry-run-first Google Drive mirror for CAPICAPI docs.

The local repository is canonical. This script mirrors selected Markdown files
from config/drive_manifest.json into a user-owned Google Drive only when called
with --apply and valid local credentials.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = REPO_ROOT / "config" / "drive_manifest.json"
MARKDOWN_MIME = "text/markdown"
GOOGLE_DOC_MIME = "application/vnd.google-apps.document"
FOLDER_MIME = "application/vnd.google-apps.folder"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]


class SyncError(RuntimeError):
    """Raised for expected sync failures with actionable messages."""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    if manifest.get("schema_version") != "1.0.0":
        raise SyncError("Unsupported manifest schema_version. Expected 1.0.0.")
    return manifest


def save_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def source_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def log_event(manifest: dict[str, Any], event: dict[str, Any]) -> None:
    log_path = REPO_ROOT / manifest["log_path"]
    log_path.parent.mkdir(parents=True, exist_ok=True)
    event = {"timestamp": utc_now(), **event}
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")


def require_google_client_libs() -> dict[str, Any]:
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
    except ImportError as exc:
        raise SyncError(
            "Google client libraries are not installed. Install them locally with "
            "`pip install google-api-python-client google-auth-httplib2 "
            "google-auth-oauthlib`."
        ) from exc

    return {
        "Request": Request,
        "Credentials": Credentials,
        "InstalledAppFlow": InstalledAppFlow,
        "build": build,
        "MediaFileUpload": MediaFileUpload,
    }


def authenticate(libs: dict[str, Any], open_browser: bool) -> Any:
    credentials_path = REPO_ROOT / os.getenv(
        "CAPICAPI_GOOGLE_CREDENTIALS",
        "integrations/google_drive/credentials.json",
    )
    token_path = REPO_ROOT / os.getenv(
        "CAPICAPI_GOOGLE_TOKEN",
        "integrations/google_drive/token.json",
    )

    if not credentials_path.exists():
        raise SyncError(
            f"Missing OAuth credentials at {credentials_path}. See DRIVE_SETUP.md."
        )

    creds = None
    Credentials = libs["Credentials"]
    Request = libs["Request"]
    InstalledAppFlow = libs["InstalledAppFlow"]

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_path),
                SCOPES,
            )
            creds = flow.run_local_server(
                port=0,
                open_browser=open_browser,
                authorization_prompt_message=(
                    "Open this Google authorization URL, approve Drive access, "
                    "then return here:\n{url}\n"
                ),
                success_message=(
                    "CAPICAPI Drive authorization complete. You can close this browser tab."
                ),
            )
        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(creds.to_json(), encoding="utf-8")

    return libs["build"]("drive", "v3", credentials=creds)


def q(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


def find_child(service: Any, parent_id: str | None, name: str, mime_type: str) -> str | None:
    clauses = [
        f"name = '{q(name)}'",
        f"mimeType = '{q(mime_type)}'",
        "trashed = false",
    ]
    if parent_id:
        clauses.append(f"'{q(parent_id)}' in parents")
    query = " and ".join(clauses)
    result = (
        service.files()
        .list(q=query, spaces="drive", fields="files(id, name)", pageSize=10)
        .execute()
    )
    files = result.get("files", [])
    return files[0]["id"] if files else None


def ensure_folder(service: Any, name: str, parent_id: str | None) -> str:
    existing_id = find_child(service, parent_id, name, FOLDER_MIME)
    if existing_id:
        return existing_id

    metadata: dict[str, Any] = {"name": name, "mimeType": FOLDER_MIME}
    if parent_id:
        metadata["parents"] = [parent_id]
    created = service.files().create(body=metadata, fields="id").execute()
    return created["id"]


def ensure_drive_path(service: Any, manifest: dict[str, Any], drive_path: str) -> tuple[str, str]:
    parts = [part for part in drive_path.split("/") if part]
    if len(parts) < 2:
        raise SyncError(f"Drive path must include root and filename: {drive_path}")

    root_name = manifest["root_folder_name"]
    if parts[0] != root_name:
        raise SyncError(f"Drive path must start with {root_name}: {drive_path}")

    parent_id = (
        os.getenv("CAPICAPI_DRIVE_ROOT_FOLDER_ID")
        or manifest.get("root_folder_id")
        or ensure_folder(service, root_name, None)
    )
    manifest["root_folder_id"] = parent_id

    for folder_name in parts[1:-1]:
        parent_id = ensure_folder(service, folder_name, parent_id)

    return parent_id, parts[-1]


def ensure_folder_path(service: Any, manifest: dict[str, Any], drive_path: str) -> str:
    parts = [part for part in drive_path.split("/") if part]
    if not parts:
        raise SyncError("Folder path cannot be empty.")

    root_name = manifest["root_folder_name"]
    if parts[0] != root_name:
        raise SyncError(f"Folder path must start with {root_name}: {drive_path}")

    parent_id = (
        os.getenv("CAPICAPI_DRIVE_ROOT_FOLDER_ID")
        or manifest.get("root_folder_id")
        or ensure_folder(service, root_name, None)
    )
    manifest["root_folder_id"] = parent_id

    for folder_name in parts[1:]:
        parent_id = ensure_folder(service, folder_name, parent_id)

    return parent_id


def update_or_create_doc(
    service: Any,
    libs: dict[str, Any],
    doc: dict[str, Any],
    repo_path: Path,
    parent_id: str,
    drive_name: str,
) -> str:
    MediaFileUpload = libs["MediaFileUpload"]
    media = MediaFileUpload(str(repo_path), mimetype=MARKDOWN_MIME, resumable=False)
    file_id = doc.get("drive_file_id")

    if not file_id:
        existing_id = find_child(service, parent_id, drive_name, GOOGLE_DOC_MIME)
        file_id = existing_id

    if file_id:
        service.files().update(
            fileId=file_id,
            media_body=media,
            fields="id",
        ).execute()
        return file_id

    metadata = {
        "name": drive_name,
        "parents": [parent_id],
        "mimeType": GOOGLE_DOC_MIME
        if doc["mirror_type"] == "google_doc"
        else MARKDOWN_MIME,
    }
    created = (
        service.files()
        .create(body=metadata, media_body=media, fields="id")
        .execute()
    )
    return created["id"]


def sync(manifest_path: Path, apply: bool, open_browser: bool = True) -> int:
    manifest = load_manifest(manifest_path)
    docs = manifest.get("documents", [])
    if not docs:
        raise SyncError("Manifest contains no documents.")

    planned: list[dict[str, Any]] = []
    for doc in docs:
        repo_path = REPO_ROOT / doc["repo_path"]
        if not repo_path.exists():
            raise SyncError(f"Missing source file: {doc['repo_path']}")
        digest = source_hash(repo_path)
        changed = digest != doc.get("source_hash")
        planned.append({"doc": doc, "repo_path": repo_path, "hash": digest, "changed": changed})

    if not apply:
        print("DRY RUN - no Google authentication attempted and no Drive writes performed.")
        for folder in manifest.get("folders", []):
            status = "known" if folder.get("drive_folder_id") else "needs-id"
            print(f"{status}: folder {folder['drive_path']}")
        for item in planned:
            doc = item["doc"]
            status = "changed" if item["changed"] else "unchanged"
            print(f"{status}: {doc['repo_path']} -> {doc['drive_path']}")
        return 0

    libs = require_google_client_libs()
    service = authenticate(libs, open_browser=open_browser)

    for folder in manifest.get("folders", []):
        folder_id = ensure_folder_path(service, manifest, folder["drive_path"])
        folder["drive_folder_id"] = folder_id
        log_event(
            manifest,
            {
                "event": "ensured_folder",
                "drive_path": folder["drive_path"],
                "drive_folder_id": folder_id,
            },
        )
        print(f"ensured folder: {folder['drive_path']}")

    for item in planned:
        doc = item["doc"]
        parent_id, drive_name = ensure_drive_path(service, manifest, doc["drive_path"])
        file_id = update_or_create_doc(service, libs, doc, item["repo_path"], parent_id, drive_name)
        doc["drive_file_id"] = file_id
        doc["source_hash"] = item["hash"]
        doc["last_synced_at"] = utc_now()
        log_event(
            manifest,
            {
                "event": "synced_document",
                "repo_path": doc["repo_path"],
                "drive_path": doc["drive_path"],
                "drive_file_id": file_id,
            },
        )
        print(f"synced: {doc['repo_path']} -> {doc['drive_path']}")

    save_manifest(manifest_path, manifest)
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mirror CAPICAPI docs to Google Drive.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview planned sync actions.")
    mode.add_argument("--apply", action="store_true", help="Write changes to Google Drive.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Path to drive manifest JSON.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Print the Google authorization URL instead of opening a browser automatically.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    apply = bool(args.apply)
    try:
        return sync(
            args.manifest.resolve(),
            apply=apply,
            open_browser=not args.no_browser,
        )
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
