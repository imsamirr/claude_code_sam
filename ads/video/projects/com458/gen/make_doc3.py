"""Re-lip-sync the AI podiatrist to the new (Sarah, v3) read. Cuts each doctor line from vo3/*_final.wav,
uploads to Kie and starts kling/ai-avatar-pro tasks -> tasks3.txt"""
import json, os, re, subprocess, requests
E = "../edit/vo3"; K = os.environ["KIE_AI"]
norm = lambda x: re.sub(r"[^a-z0-9']", "", x.lower())
LINES = {"D3_H1": ("H1", "H1", "I know"), "D3_H2": ("H2", "H2", "Those plush"),
         "D3_P1": ("body", "P1", "Three things people"), "D3_P3": ("body", "P3", "That is where")}
PROMPT = {"D3_H1": "Friendly female podiatrist in white lab coat talking naturally to camera, slight knowing smile, small hand gestures; natural blinking; static camera, clinic background unchanged.",
          "D3_H2": "Female podiatrist in white lab coat explaining to camera with a gentle warning tone, open-palm hand gestures, slight head shake; natural blinking; static camera, clinic background unchanged.",
          "D3_P1": "Female podiatrist in white lab coat counting to three on her fingers while explaining to camera, warm expert tone; natural blinking; static camera, clinic background unchanged.",
          "D3_P3": "Female podiatrist in white lab coat making a confident point to camera, calm reassuring tone, small hand gesture; natural blinking; static camera, clinic background unchanged."}
out = {}
import sys
for name, (take, sec, phrase) in LINES.items():
    if sys.argv[1:] and name not in sys.argv[1:]: continue
    j = json.load(open(f"{E}/{take}_final.json"))["sections"]; ws = j[sec]; toks = phrase.lower().split()
    i = next(k for k in range(len(ws)) if [norm(w["w"]) for w in ws[k:k + len(toks)]] == [norm(t) for t in toks])
    e = len(ws) - 1 if sec.startswith("H") else next(k for k in range(i, len(ws)) if ws[k]["w"].endswith(".") and k > i + 3)
    s0, s1 = ws[i]["s"] - 0.08, ws[e]["e"] + 0.25
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s0:.3f}", "-to", f"{s1:.3f}", "-i", f"{E}/{take}_final.wav", "-af", "afade=t=out:st=%.3f:d=0.12" % (s1 - s0 - 0.12), "-ar", "44100", f"{name}.wav"], check=True)
    out[name] = [take, sec, phrase, round(s0, 3), round(s1, 3)]
    up = requests.post("https://kieai.redpandaai.co/api/file-stream-upload", headers={"Authorization": f"Bearer {K}"},
                       files={"file": open(f"{name}.wav", "rb")}, data={"uploadPath": "comfortwear/com458", "fileName": f"{name}.wav"}, timeout=120).json()
    au = up["data"]["downloadUrl"]
    t = requests.post("https://api.kie.ai/api/v1/jobs/createTask", headers={"Authorization": f"Bearer {K}"},
                      json={"model": "kling/ai-avatar-pro", "input": {"image_url": "https://tempfile.redpandaai.co/kieai/12239740/comfortwear/com458/doc1.jpg", "audio_url": au, "prompt": PROMPT[name]}}, timeout=60).json()
    print(name, f"{s1 - s0:.2f}s", t); open("tasks3.txt", "a").write(f"{name} {t['data']['taskId']}\n")
old = json.load(open("doctor_lines3.json")) if os.path.exists("doctor_lines3.json") else {}
old.update(out); json.dump(old, open("doctor_lines3.json", "w"), indent=1)
