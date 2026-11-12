"""Upload large files (the 40-70 MB scrolling videos) to Google Drive with the Drive API, no size cap.

Credentials (OAuth for the Drive owner's own account, scope drive.file), as environment variables:
    GDRIVE_CLIENT_ID, GDRIVE_CLIENT_SECRET, GDRIVE_REFRESH_TOKEN

With the drive.file scope the app can only see files and folders it created itself, so by default the
videos go into a folder this script creates and reuses: "<Brand> Long-Form Videos (auto)" in My Drive.
It can be moved or shared freely in Drive afterwards; the app keeps access to it.

    python ads/drive_upload.py --brand dentalpulse ads/brands/dentalpulse/output/scroll_videos/DV13.mp4 ...
    python ads/drive_upload.py --brand dentalpulse --check          # verify the credentials only

Prints one line per file: "<local path>\t<Drive view link>". Re-uploading the same file name replaces nothing;
it adds a new file, so name versions clearly (e.g. DV01_voice.mp4).
"""

import argparse
import json
import os
import sys
from pathlib import Path

import requests

TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://www.googleapis.com/drive/v3"
UPLOAD = "https://www.googleapis.com/upload/drive/v3/files"
CHUNK = 8 * 1024 * 1024  # resumable upload chunk (multiple of 256 KiB)


def access_token():
    need = ["GDRIVE_CLIENT_ID", "GDRIVE_CLIENT_SECRET", "GDRIVE_REFRESH_TOKEN"]
    missing = [k for k in need if not os.getenv(k)]
    if missing:
        sys.exit(f"missing environment variables: {', '.join(missing)}")
    r = requests.post(TOKEN_URL, timeout=60, data={
        "client_id": os.environ["GDRIVE_CLIENT_ID"], "client_secret": os.environ["GDRIVE_CLIENT_SECRET"],
        "refresh_token": os.environ["GDRIVE_REFRESH_TOKEN"], "grant_type": "refresh_token"})
    if r.status_code != 200:
        sys.exit(f"token refresh failed ({r.status_code}): {r.text[:300]}")
    return r.json()["access_token"]


def folder_id(tok, name, parent=None):
    """Find (or create) a folder this app created, by name."""
    h = {"Authorization": f"Bearer {tok}"}
    q = f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    if parent:
        q += f" and '{parent}' in parents"
    r = requests.get(f"{API}/files", headers=h, params={"q": q, "fields": "files(id,name)"}, timeout=60).json()
    if r.get("files"):
        return r["files"][0]["id"]
    body = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    if parent:
        body["parents"] = [parent]
    return requests.post(f"{API}/files", headers=h, json=body, params={"fields": "id"}, timeout=60).json()["id"]


def upload(tok, path, parent, mime="video/mp4", name=None):
    size = path.stat().st_size
    h = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json; charset=UTF-8",
         "X-Upload-Content-Type": mime, "X-Upload-Content-Length": str(size)}
    r = requests.post(f"{UPLOAD}?uploadType=resumable&fields=id,webViewLink", headers=h, timeout=60,
                      data=json.dumps({"name": name or path.name, "parents": [parent]}))
    r.raise_for_status()
    session = r.headers["Location"]
    with open(path, "rb") as f:
        start = 0
        while start < size:
            chunk = f.read(CHUNK)
            end = start + len(chunk) - 1
            r = requests.put(session, timeout=300, data=chunk,
                             headers={"Content-Length": str(len(chunk)), "Content-Range": f"bytes {start}-{end}/{size}"})
            if r.status_code in (200, 201):
                return r.json()["webViewLink"]
            if r.status_code != 308:
                raise RuntimeError(f"upload failed ({r.status_code}): {r.text[:300]}")
            rng = r.headers.get("Range")
            start = int(rng.split("-")[1]) + 1 if rng else 0
            f.seek(start)
    raise RuntimeError("upload ended without a final response")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--brand", required=True)
    p.add_argument("--folder", help="folder name (default: '<Brand> Long-Form Videos (auto)')")
    p.add_argument("--subfolder", help="optional subfolder, e.g. the batch date 2026-11-19")
    p.add_argument("--check", action="store_true", help="only verify the credentials and the folder")
    p.add_argument("--folder-id", help="upload into this existing Drive folder (needs the full drive scope)")
    p.add_argument("--names", help="JSON file mapping local path -> Drive file name")
    p.add_argument("files", nargs="*")
    a = p.parse_args()
    tok = access_token()
    root = a.folder_id or folder_id(tok, a.folder or f"{a.brand.capitalize()} Long-Form Videos (auto)")
    parent = folder_id(tok, a.subfolder, root) if a.subfolder else root
    names = json.loads(Path(a.names).read_text()) if a.names else {}
    if a.check:
        print(f"ok: credentials work; folder https://drive.google.com/drive/folders/{parent}")
        return
    for f in a.files:
        link = upload(tok, Path(f), parent, name=names.get(f))
        print(f"{f}\t{link}", flush=True)


if __name__ == "__main__":
    main()
