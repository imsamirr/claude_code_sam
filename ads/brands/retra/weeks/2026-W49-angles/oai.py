"""OpenAI gpt-image-2 renders (Kie is out of credits). python3 oai.py <out.png> <WxH> <quality> <prompt-file> [ref.jpg ...]"""
import base64, json, os, sys, time
from pathlib import Path
import requests
from PIL import Image
out, size, quality, pfile, *refs = sys.argv[1:]
prompt = Path(pfile).read_text()
files = [("image[]", (Path(r).name, open(r, "rb"), "image/jpeg" if r.endswith("jpg") else "image/png")) for r in refs]
key = os.getenv("OPENAI_API_KEY")
url = "https://api.openai.com/v1/images/edits" if refs else "https://api.openai.com/v1/images/generations"
for attempt in range(3):
    if refs:
        r = requests.post(url, headers={"Authorization": f"Bearer {key}"}, files=files, timeout=900,
                          data={"model": "gpt-image-2", "prompt": prompt, "quality": quality, "n": "1", "size": size})
    else:
        r = requests.post(url, headers={"Authorization": f"Bearer {key}"}, timeout=900,
                          json={"model": "gpt-image-2", "prompt": prompt, "quality": quality, "n": 1, "size": size})
    if r.ok: break
    print("err", r.status_code, r.text[:300], flush=True); time.sleep(8)
    for f in files: f[1][1].seek(0)
body = r.json()
Path(out).write_bytes(base64.b64decode(body["data"][0]["b64_json"]))
with open(Path(out).parent / "_usage.jsonl", "a") as f:
    f.write(json.dumps({"out": Path(out).name, "size": size, "quality": quality, "usage": body.get("usage"), "refs": [Path(x).name for x in refs]}) + "\n")
print(out, Image.open(out).size, body.get("usage"))
