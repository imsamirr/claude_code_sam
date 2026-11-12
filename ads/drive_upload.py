"""Upload large files (scroll videos) to Google Drive with the Drive API, resumable, in chunks.

Credentials come from the environment (the user's own OAuth app + refresh token, set 2026-11-12):
    GDRIVE_CLIENT_ID, GDRIVE_CLIENT_SECRET, GDRIVE_REFRESH_TOKEN

    python ads/drive_upload.py --folder <folderId> file1.mp4 file2.mp4 ...   # prints JSON lines: name, id, link
    python ads/drive_upload.py --folder <folderId> --check                     # verify access to the folder

Re-uploading a name that already exists in the folder updates that file in place (same link), so links on
Notion cards stay valid.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://www.googleapis.com/drive/v3"
UPLOAD = "https://www.googleapis.com/upload/drive/v3/files"
CHUNK = 32 * 1024 * 1024  # multiple of 256 KiB


def access_token():
    r = requests.post(TOKEN_URL, timeout=60, data={
        "client_id": os.environ["GDRIVE_CLIENT_ID"], "client_secret": os.environ["GDRIVE_CLIENT_SECRET"],
        "refresh_token": os.environ["GDRIVE_REFRESH_TOKEN"], "grant_type": "refresh_token"})
    if not r.ok:
        sys.exit(f"token refresh failed: {r.status_code} {r.text[:300]}")
    return r.json()["access_token"]


def find(tok, folder, name):
    q = f"'{folder}' in parents and name = '{name}' and trashed = false"
    r = requests.get(f"{API}/files", headers={"Authorization": f"Bearer {tok}"}, timeout=60,
                     params={"q": q, "fields": "files(id,name)", "supportsAllDrives": "true", "includeItemsFromAllDrives": "true"})
    r.raise_for_status()
    files = r.json().get("files", [])
    return files[0]["id"] if files else None


def upload(tok, folder, path, mime="video/mp4"):
    path = Path(path)
    size = path.stat().st_size
    existing = find(tok, folder, path.name)
    h = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json; charset=UTF-8",
         "X-Upload-Content-Type": mime, "X-Upload-Content-Length": str(size)}
    if existing:
        r = requests.patch(f"{UPLOAD}/{existing}?uploadType=resumable&supportsAllDrives=true", headers=h, json={}, timeout=60)
    else:
        r = requests.post(f"{UPLOAD}?uploadType=resumable&supportsAllDrives=true", headers=h,
                          json={"name": path.name, "parents": [folder]}, timeout=60)
    r.raise_for_status()
    session = r.headers["Location"]
    pos = 0
    with open(path, "rb") as f:
        while pos < size:
            f.seek(pos)
            data = f.read(CHUNK)
            end = pos + len(data) - 1
            for attempt in range(5):
                try:
                    r = requests.put(session, data=data, timeout=600,
                                     headers={"Content-Length": str(len(data)), "Content-Range": f"bytes {pos}-{end}/{size}"})
                    break
                except requests.RequestException:
                    time.sleep(2 ** attempt)
            else:
                raise RuntimeError(f"{path.name}: chunk at {pos} failed 5 times")
            if r.status_code in (200, 201):
                pos = size
                fid = r.json()["id"]
            elif r.status_code == 308:
                rng = r.headers.get("Range")
                pos = int(rng.split("-")[1]) + 1 if rng else 0
            else:
                raise RuntimeError(f"{path.name}: upload failed {r.status_code} {r.text[:300]}")
    meta = requests.get(f"{API}/files/{fid}", headers={"Authorization": f"Bearer {tok}"}, timeout=60,
                        params={"fields": "id,name,size,webViewLink", "supportsAllDrives": "true"}).json()
    return {"name": meta["name"], "id": fid, "size_mb": round(int(meta.get("size", size)) / 1e6),
            "link": meta.get("webViewLink", f"https://drive.google.com/file/d/{fid}/view"),
            "download": f"https://drive.google.com/uc?export=download&id={fid}"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--folder", required=True)
    p.add_argument("--check", action="store_true")
    p.add_argument("files", nargs="*")
    a = p.parse_args()
    tok = access_token()
    if a.check:
        r = requests.get(f"{API}/files/{a.folder}", headers={"Authorization": f"Bearer {tok}"}, timeout=60,
                         params={"fields": "id,name,capabilities(canAddChildren)", "supportsAllDrives": "true"})
        print(r.status_code, r.text[:300])
        return
    for f in a.files:
        t0 = time.time()
        res = upload(access_token(), a.folder, f)  # fresh token per file (access tokens last 1 hour)
        res["secs"] = round(time.time() - t0)
        print(json.dumps(res), flush=True)


if __name__ == "__main__":
    main()
