"""Minimal Kie.ai client: upload a local file, run a market model, wait for its result.

    from kie import upload, run
    url = upload("ref.png")
    urls = run("nano-banana-pro", {"prompt": "...", "image_input": [url], "aspect_ratio": "4:5"})

Needs KIE_AI (the API key) in the environment or .env. Uploaded files expire after 24 hours.
"""

import json
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
API = "https://api.kie.ai/api/v1"
UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"


def _headers():
    return {"Authorization": f"Bearer {os.environ['KIE_AI']}"}


def credits():
    return requests.get(f"{API}/chat/credit", headers=_headers(), timeout=30).json()["data"]


def upload(path, folder="ads"):
    path = Path(path)
    with open(path, "rb") as f:
        resp = requests.post(UPLOAD, headers=_headers(), timeout=300,
                             files={"file": (path.name, f)},
                             data={"uploadPath": folder, "fileName": path.name})
    body = resp.json()
    if not body.get("success", body.get("code") == 200):
        raise RuntimeError(f"upload failed: {body}")
    data = body["data"]
    return data.get("downloadUrl") or data.get("fileUrl") or data["url"]


def create(model, inp):
    body = requests.post(f"{API}/jobs/createTask", headers=_headers(), timeout=60,
                         json={"model": model, "input": inp}).json()
    if body.get("code") != 200:
        raise RuntimeError(f"{model}: {body}")
    return body["data"]["taskId"]


def wait(task_id, poll=5, timeout=1800):
    end = time.time() + timeout
    while time.time() < end:
        data = requests.get(f"{API}/jobs/recordInfo", headers=_headers(), timeout=60,
                            params={"taskId": task_id}).json().get("data") or {}
        if data.get("state") == "success":
            return json.loads(data["resultJson"])["resultUrls"]
        if data.get("state") == "fail":
            raise RuntimeError(f"task {task_id} failed: {data.get('failMsg') or data}")
        time.sleep(poll)
    raise TimeoutError(task_id)


def run(model, inp, **kw):
    return wait(create(model, inp), **kw)


def download(url, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=600)
    resp.raise_for_status()
    path.write_bytes(resp.content)
    return path
