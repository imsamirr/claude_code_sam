"""Upload files of any size to a Google Drive folder (shared drives included) with the Drive API.

The Drive connector caps each call at ~3 MB, so finished videos go up through here instead.
Credentials come from the environment (never printed): GDRIVE_CLIENT_ID, GDRIVE_CLIENT_SECRET,
GDRIVE_REFRESH_TOKEN (an OAuth refresh token with a Drive scope).

Usage:
    python ads/video/drive_upload.py <folderId> file1.mp4 [file2.mp4 ...]   # upload into folder
    python ads/video/drive_upload.py <folderId> --mkdir "2026-W46"           # make a subfolder, print id
Files already in the folder with the same name are skipped (re-run safe); --replace overwrites.
"""

import json
import os
import sys
from pathlib import Path

import requests

TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://www.googleapis.com/drive/v3/files"
UPLOAD = "https://www.googleapis.com/upload/drive/v3/files"
CHUNK = 16 * 1024 * 1024
MIME = {".mp4": "video/mp4", ".mov": "video/quicktime", ".png": "image/png", ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg", ".gif": "image/gif", ".csv": "text/csv", ".json": "application/json"}


def token():
    r = requests.post(TOKEN_URL, data={"client_id": os.environ["GDRIVE_CLIENT_ID"],
                                       "client_secret": os.environ["GDRIVE_CLIENT_SECRET"],
                                       "refresh_token": os.environ["GDRIVE_REFRESH_TOKEN"],
                                       "grant_type": "refresh_token"}, timeout=30)
    if r.status_code != 200:
        raise SystemExit(f"token refresh failed: HTTP {r.status_code} {r.json().get('error', '')}")
    return r.json()["access_token"]


def existing(h, folder):
    q = f"'{folder}' in parents and trashed = false"
    r = requests.get(API, headers=h, params={"q": q, "fields": "files(id,name,size)", "pageSize": 1000,
                                             "supportsAllDrives": "true", "includeItemsFromAllDrives": "true"},
                     timeout=60)
    r.raise_for_status()
    return {f["name"]: f for f in r.json().get("files", [])}


def mkdir(h, folder, name):
    have = existing(h, folder)
    if name in have:
        return have[name]["id"]
    r = requests.post(API, headers=h, params={"supportsAllDrives": "true", "fields": "id"},
                      json={"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [folder]},
                      timeout=60)
    r.raise_for_status()
    return r.json()["id"]


def upload(h, folder, path, replace_id=None):
    size = path.stat().st_size
    mime = MIME.get(path.suffix.lower(), "application/octet-stream")
    meta = {} if replace_id else {"name": path.name, "parents": [folder]}
    url = f"{UPLOAD}/{replace_id}" if replace_id else UPLOAD
    method = requests.patch if replace_id else requests.post
    r = method(url, headers={**h, "X-Upload-Content-Type": mime, "X-Upload-Content-Length": str(size)},
               params={"uploadType": "resumable", "supportsAllDrives": "true"}, json=meta, timeout=60)
    r.raise_for_status()
    session = r.headers["Location"]
    sent = 0
    with path.open("rb") as f:
        while sent < size:
            chunk = f.read(CHUNK)
            end = sent + len(chunk) - 1
            r = requests.put(session, data=chunk, timeout=600,
                             headers={"Content-Length": str(len(chunk)), "Content-Range": f"bytes {sent}-{end}/{size}"})
            if r.status_code not in (200, 201, 308):
                raise SystemExit(f"{path.name}: upload failed at byte {sent}: HTTP {r.status_code} {r.text[:200]}")
            sent = end + 1
    return r.json()["id"]


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        raise SystemExit(__doc__)
    folder, rest = args[0], args[1:]
    h = {"Authorization": f"Bearer {token()}"}
    if rest[0] == "--mkdir":
        print(mkdir(h, folder, rest[1]))
        return
    replace = "--replace" in rest
    files = [Path(p) for p in rest if p != "--replace"]
    have = existing(h, folder)
    for p in files:
        if p.name in have and not replace:
            print(f"skip  {p.name} (already in folder)")
            continue
        fid = upload(h, folder, p, have[p.name]["id"] if p.name in have else None)
        print(f"ok    {p.name}  {p.stat().st_size / 1e6:.1f} MB  https://drive.google.com/file/d/{fid}/view")


if __name__ == "__main__":
    main()
