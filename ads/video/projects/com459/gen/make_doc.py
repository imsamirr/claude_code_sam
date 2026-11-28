"""AI podiatrist lines for COM459 (placement from StefanBrain), cut from the final VO takes, lip-synced with Kie kling/ai-avatar-pro."""
import json, os, re, subprocess, sys, requests
E = "../edit/vo3"; K = os.environ["KIE_AI"]
norm = lambda x: re.sub(r"[^a-z0-9']", "", x.lower())
LINES = {  # name: (take, section, first words, last word)
 "D_H1": ("H1", "H1", "I know", "design."),
 "D_H2": ("H2", "H2", "take them out", "now."),
 "D_H3": ("H3", "H3", "You think you", "shoe,"),
 "D_P1": ("body", "P1", "Three things people", "home."),
 "D_P2": ("body", "P2", "does not tell", "story."),
 "D_P3": ("body", "P3", "and putting strain", "knees."),
 "D_P4": ("body", "P4", "that friction leads", "pain."),
}
TONE = {"D_H1": "talking naturally with a slight knowing smile", "D_H2": "giving a firm, friendly warning", "D_H3": "empathetic, nodding knowingly",
        "D_P1": "counting to three on her fingers, warm expert tone", "D_P2": "shaking her head gently with a knowing smile",
        "D_P3": "explaining with concern, small hand gesture", "D_P4": "explaining with concern, open-palm gesture"}
img = requests.post("https://kieai.redpandaai.co/api/file-stream-upload", headers={"Authorization": f"Bearer {K}"},
                    files={"file": open("doc1.jpg", "rb")}, data={"uploadPath": "comfortwear/com459", "fileName": "doc1.jpg"}, timeout=120).json()["data"]["downloadUrl"]
out = {}
for name, (take, sec, first, last) in LINES.items():
    if sys.argv[1:] and name not in sys.argv[1:]: continue
    ws = json.load(open(f"{E}/{take}_final.json"))["sections"][sec]; toks = [norm(t) for t in first.split()]
    i = next(k for k in range(len(ws)) if [norm(w["w"]) for w in ws[k:k + len(toks)]] == toks)
    e = next(k for k in range(i, len(ws)) if ws[k]["w"] == last)
    s0, s1 = ws[i]["s"] - 0.08, ws[e]["e"] + 0.25
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s0:.3f}", "-to", f"{s1:.3f}", "-i", f"{E}/{take}_final.wav", "-af", "afade=t=out:st=%.3f:d=0.12" % (s1 - s0 - 0.12), "-ar", "44100", f"{name}.wav"], check=True)
    au = requests.post("https://kieai.redpandaai.co/api/file-stream-upload", headers={"Authorization": f"Bearer {K}"},
                       files={"file": open(f"{name}.wav", "rb")}, data={"uploadPath": "comfortwear/com459", "fileName": f"{name}.wav"}, timeout=120).json()["data"]["downloadUrl"]
    prompt = f"Female podiatrist in white lab coat, seated in her clinic, {TONE[name]} to camera; natural blinking; static camera, clinic background unchanged."
    t = requests.post("https://api.kie.ai/api/v1/jobs/createTask", headers={"Authorization": f"Bearer {K}"},
                      json={"model": "kling/ai-avatar-pro", "input": {"image_url": img, "audio_url": au, "prompt": prompt}}, timeout=60).json()
    print(name, f"{s1 - s0:.2f}s", t.get("code"), t.get("msg")); open("tasks.txt", "a").write(f"{name} {t['data']['taskId']}\n")
    out[name] = [take, sec, first, last, round(s0, 3), round(s1, 3)]
old = json.load(open("doctor_lines.json")) if os.path.exists("doctor_lines.json") else {}
old.update(out); json.dump(old, open("doctor_lines.json", "w"), indent=1)
