"""Batch image generation on Kie.ai (Nano Banana Pro).

usage: python3 kie.py jobs.json OUTDIR
jobs.json: [{"name": "...", "prompt": "...", "aspect_ratio": "4:3", "refs": ["https://..."]}, ...]
Reads the API key from $KIE_AI. Submits every job, polls until each finishes, saves OUTDIR/<name>.<ext>.
"""
import json, os, sys, time, urllib.request

API = 'https://api.kie.ai/api/v1/jobs'
KEY = os.environ['KIE_AI']


def call(method, url, body=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={'Authorization': f'Bearer {KEY}', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    jobs = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    pending = {}
    for j in jobs:
        if any(f.startswith(j['name'] + '.') for f in os.listdir(out)):
            print('have', j['name'], flush=True)
            continue
        body = {'model': 'nano-banana-pro', 'input': {
            'prompt': j['prompt'], 'image_input': j.get('refs', []),
            'aspect_ratio': j.get('aspect_ratio', '1:1'), 'resolution': j.get('resolution', '2K'), 'output_format': 'png'}}
        r = call('POST', f'{API}/createTask', body)
        if r.get('code') != 200:
            print('submit failed', j['name'], r, flush=True)
            continue
        pending[r['data']['taskId']] = j['name']
        print('submitted', j['name'], flush=True)
    deadline = time.time() + 1800
    while pending and time.time() < deadline:
        time.sleep(10)
        for tid, name in list(pending.items()):
            try:
                d = call('GET', f'{API}/recordInfo?taskId={tid}')['data']
            except Exception as e:  # transient
                continue
            state = d.get('state')
            if state == 'success':
                urls = json.loads(d['resultJson'])['resultUrls']
                ext = urls[0].split('?')[0].rsplit('.', 1)[-1]
                urllib.request.urlretrieve(urls[0], os.path.join(out, f'{name}.{ext}'))
                print('done', name, flush=True)
                del pending[tid]
            elif state == 'fail':
                print('FAILED', name, d.get('failMsg'), flush=True)
                del pending[tid]
    for name in pending.values():
        print('TIMEOUT', name, flush=True)


if __name__ == '__main__':
    main()
