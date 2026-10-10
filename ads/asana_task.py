"""Create (or re-position) the weekly "Review static ads batch" task in Asana.

The task goes at the TOP of the brand's Review column. The Asana connector can only add a task to
a section's bottom, so this script calls the Asana REST API with a personal access token instead.

    export ASANA_ACCESS_TOKEN=...      # Asana → My settings → Apps → Developer apps → Personal access token
    python ads/asana_task.py --week 2026-W44 --sheet-url <Drive sheet> --folder-url <Drive week folder>
    python ads/asana_task.py --move-to-top <task_gid>     # move an existing task to the top of Review

Project, Review section and assignee come from ads/brands/<brand>/brand.json → asana.
Prints the task URL.
"""

import argparse
import collections
import datetime as dt
import json
import os
import sys
from html import escape
from pathlib import Path

import requests
from dotenv import load_dotenv

ADS_DIR = Path(__file__).resolve().parent
API = "https://app.asana.com/api/1.0"
REPO_TREE = "https://github.com/imsamirr/claude_code_sam/tree/claude/clever-albattani-90x4ya"


def call(session, method, path, data):
    r = session.request(method, f"{API}{path}", json={"data": data}, timeout=60)
    if r.status_code >= 300:
        sys.exit(f"Asana {method} {path}: {r.status_code} {r.text[:400]}")
    return r.json()["data"]


def move_to_top(session, cfg, task_gid):
    # insert_after: null puts the task at the beginning of the section
    call(session, "POST", f"/tasks/{task_gid}/addProject",
         {"project": cfg["project_id"], "section": cfg["section_id"], "insert_after": None})


def batch_notes(bdir, week, sheet_url, folder_url):
    wdir = bdir / "weeks" / week
    concepts = json.loads((wdir / "concepts.json").read_text())["concepts"]
    groups = collections.Counter(c.get("group", "") for c in concepts)
    personas = collections.Counter(c["persona"] for c in concepts)
    spanish = sum(c.get("lang") == "es" for c in concepts)
    gifs = [c["id"].split("_")[1] for c in concepts if c.get("gif")]
    usage = wdir / "output" / "_usage.jsonl"
    cost = sum(json.loads(l)["cost_usd"] for l in usage.read_text().splitlines()) if usage.exists() else 0
    out = f"{REPO_TREE}/{wdir.relative_to(ADS_DIR.parent)}/output"
    links = [f'<li><strong>Concept sheet (review here):</strong> <a href="{escape(sheet_url)}">{week} concepts</a>. '
             "Fill in Verdict and Notes; the next Friday run logs them.</li>"] if sheet_url else []
    if folder_url:
        links.append(f'<li><strong>Weekly Drive folder:</strong> <a href="{escape(folder_url)}">{week}</a></li>')
    links.append(f'<li><strong>All creatives (images + preview sheets):</strong> <a href="{out}">GitHub: weeks/{week}/output</a></li>')
    facts = [
        f"<li>{len(concepts)} concepts, 1 static each (9:16 with content in the 4:5 safe area, plus a 4:5 crop)</li>",
        "<li>" + escape(", ".join(f"{n} {g or 'other'}" for g, n in groups.items())) + "</li>",
        "<li>Personas: " + escape(", ".join(f"{p} {n}" for p, n in personas.most_common())) + "</li>",
        f"<li>{spanish} in Spanish</li>",
        f"<li>GIF candidates (rendered after approval): {escape(', '.join(gifs)) or 'none'}</li>",
        f"<li>Image cost so far: ${cost:.2f}</li>",
    ]
    return (f"<body><h2>Static ads batch {week} is ready</h2><ul>{''.join(links)}</ul>"
            f"<h2>What's in it</h2><ul>{''.join(facts)}</ul></body>"), len(concepts)


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("--brand", default=os.getenv("ADS_BRAND", "comfortwear"))
    p.add_argument("--week")
    p.add_argument("--sheet-url", default="")
    p.add_argument("--folder-url", default="")
    p.add_argument("--move-to-top", metavar="TASK_GID")
    args = p.parse_args()

    token = os.getenv("ASANA_ACCESS_TOKEN")
    if not token:
        sys.exit("ASANA_ACCESS_TOKEN is not set; add it in the environment settings.")
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {token}"
    bdir = ADS_DIR / "brands" / args.brand
    cfg = json.loads((bdir / "brand.json").read_text())["asana"]

    if args.move_to_top:
        move_to_top(s, cfg, args.move_to_top)
        print(f"Moved {args.move_to_top} to the top of {cfg['section_name']}")
        return

    notes, n = batch_notes(bdir, args.week, args.sheet_url, args.folder_url)
    task = call(s, "POST", "/tasks", {
        "name": f"Review static ads batch {args.week} ({n} statics)",
        "projects": [cfg["project_id"]],
        "assignee": cfg["assignee_id"],
        "due_on": str(dt.date.today()),
        "html_notes": notes,
    })
    move_to_top(s, cfg, task["gid"])
    print(f"https://app.asana.com/0/{cfg['project_id']}/{task['gid']}")


if __name__ == "__main__":
    main()
