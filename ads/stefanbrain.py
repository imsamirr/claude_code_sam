"""StefanBrain from the ad pipeline: brand knowledge uploads and copy for static batches.

Talks to the StefanBrain MCP endpoint over plain HTTP (JSON-RPC), so it works in scheduled runs whether
or not the session loaded `.mcp.json`, and MCP asks bill the StefanBrain plan, not the API wallet.

Auth: `STEFANBRAIN_API_KEY` (stefan_sk_...) when set. In cloud sessions the key is a network secret on
the environment and the proxy injects it, so the placeholder below is replaced in flight. Never print or
commit the key.

    python ads/stefanbrain.py status
    python ads/stefanbrain.py call <tool> '<json args>'
    python ads/stefanbrain.py upload --brand <brand> <files...>     # stage + attach to the brand's product
    python ads/stefanbrain.py history --brand <brand>               # research/static_copy_history.md
    python ads/stefanbrain.py digest --brand <brand>                # research/ad_account_digest.md (no Atria calls)
    python ads/stefanbrain.py market --brand <brand>                # research/atria_market_pack.md (no Atria calls)
    python ads/stefanbrain.py copy --brand <brand> --week <folder> [--ids ...] [--chunk 10]
    python ads/stefanbrain.py revise --brand <brand> --week <folder> --id <concept id> "<what to fix>"

Per-brand ids live in brand.json → `stefanbrain` {product_id, project_id, session_prefix}.
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

import requests

HOST = "https://stefanbrain.com"
MCP = f"{HOST}/api/developers/v1/mcp"
ROOT = Path(__file__).resolve().parent
POLL_S = 15
MAX_WAIT_S = 50 * 60


def _headers():
    key = os.getenv("STEFANBRAIN_API_KEY") or "proxy-injected"
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream"}


def call(tool, args, timeout=600):
    """One MCP tools/call. Returns (structuredContent or {}, text, is_error)."""
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool, "arguments": args}}
    for attempt in range(5):
        try:
            r = requests.post(MCP, headers=_headers(), json=body, timeout=timeout)
        except requests.RequestException as e:
            if attempt == 4:
                raise
            time.sleep(5 * 2 ** attempt)
            continue
        if r.status_code in (429, 502, 503, 504):
            time.sleep(int(r.headers.get("Retry-After", 5 * 2 ** attempt)))
            continue
        if r.status_code in (401, 403):
            sys.exit(f"StefanBrain {r.status_code}: key missing or rejected (set STEFANBRAIN_API_KEY or the "
                     f"stefanbrain.com network secret on this environment).")
        r.raise_for_status()
        break
    text = r.text
    if "text/event-stream" in r.headers.get("Content-Type", ""):
        text = "\n".join(l[6:] for l in r.text.splitlines() if l.startswith("data: "))
    msg = json.loads(text)
    if "error" in msg:
        raise RuntimeError(f"{tool}: {msg['error']}")
    res = msg["result"]
    out = "\n".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text")
    return res.get("structuredContent") or {}, out, bool(res.get("isError"))


def ask(message, project=None, session=None, schema=None, file_ids=None, chat=None, key=None):
    """ask_stefanbrain, then poll until done. Returns the final structured content (with output /
    structured_output when the run finished) plus the chat id."""
    args = {"message": message}
    for k, v in (("project", project), ("session", session), ("file_ids", file_ids), ("chat", chat),
                 ("idempotency_key", key)):
        if v:
            args[k] = v
    if schema:
        args["output_config"] = {"format": {"type": "json_schema", "schema": schema}}
    sc, text, err = call("ask_stefanbrain", args)
    if err:
        raise RuntimeError(text)
    run_id, chat_id = sc.get("run_id"), sc.get("chat")
    start = time.time()
    while sc.get("status") in ("running", "queued", "pending") and run_id:
        if time.time() - start > MAX_WAIT_S:
            raise TimeoutError(f"StefanBrain run {run_id} still running after {MAX_WAIT_S // 60} min "
                               f"({sc.get('app_url')})")
        time.sleep(POLL_S)
        poll = {"family": "mcp_ask", "run_id": run_id}
        if project:
            poll["project"] = project
        if session:
            poll["session"] = session
        sc, text, err = call("get_job_result", poll)
        if err and "running" not in text.lower():
            raise RuntimeError(text)
    sc.setdefault("chat", chat_id)
    sc["_text"] = text
    return sc


def structured(sc):
    """Pull the JSON answer out of a finished ask, wherever the server put it."""
    for k in ("structured_output", "structuredOutput"):
        if isinstance(sc.get(k), dict):
            return sc[k]
    for k in ("output", "answer", "_text"):
        v = sc.get(k)
        if isinstance(v, str) and "{" in v:
            try:
                return json.loads(v[v.index("{"): v.rindex("}") + 1])
            except ValueError:
                pass
    raise RuntimeError("StefanBrain finished without JSON: " + str(sc.get("_text", ""))[:800])


def stage(paths):
    """POST /files (multipart, <=10 per request). Returns {path: upload_id}."""
    hdr = {"Authorization": _headers()["Authorization"]}
    ids = {}
    for i in range(0, len(paths), 10):
        batch = paths[i:i + 10]
        files = []
        for p in batch:
            ctype = "text/markdown" if p.suffix == ".md" else "text/csv" if p.suffix == ".csv" else \
                "application/json" if p.suffix == ".json" else None
            files.append(("files", (p.name, open(p, "rb"), ctype) if ctype else (p.name, open(p, "rb"))))
        r = requests.post(f"{HOST}/api/developers/v1/files", headers=hdr, files=files, timeout=600)
        r.raise_for_status()
        for p, f in zip(batch, r.json()["files"]):
            ids[str(p)] = f["id"]
    return ids


def brand_cfg(brand):
    bdir = ROOT / "brands" / brand
    cfg = json.loads((bdir / "brand.json").read_text())
    sb = cfg.get("stefanbrain") or {}
    if not sb.get("project_id"):
        sys.exit(f"brand.json → stefanbrain.project_id missing for {brand}")
    return bdir, cfg, sb


# ---------- copy for a static batch ----------

COPY_SCHEMA = {
    "type": "object",
    "properties": {"concepts": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "headline": {"type": "string"},
            "on_image_text": {"type": "array", "items": {"type": "string"}},
            "primary_text": {"type": "string"},
            "fb_headline": {"type": "string"},
            "fb_description": {"type": ["string", "null"]},
            "angle": {"type": "string"},
            "why": {"type": "string"},
        },
        "required": ["id", "headline", "on_image_text", "primary_text", "fb_headline", "fb_description",
                     "angle", "why"],
        "additionalProperties": False}}},
    "required": ["concepts"],
    "additionalProperties": False,
}

SLOT_KEYS = ("id", "group", "persona", "appliance", "colorway", "lang", "format", "funnel", "offer", "rival",
             "angle_gap", "angle", "based_on", "benchmark", "background", "copy_slots", "copy_notes")


def brief(cfg, folder, concepts):
    """The ask: the batch facts StefanBrain can't see, then one block per concept slot. No framework,
    tone or sample-copy instructions (StefanBrain's own method writes the copy)."""
    rules = {k: cfg[k] for k in ("product", "price", "audience", "approved_claims", "claims_to_avoid",
                                 "claims_note", "offers", "old_methods", "copy_rules", "naming_rule") if cfg.get(k)}
    if (cfg.get("program") or {}).get("offer"):
        rules["current_offer_rule"] = cfg["program"]["offer"]
    lines = [
        f"Write the copy for this {cfg['name']} Meta static ad batch ({folder}, {len(concepts)} ads).",
        "",
        "Where it runs: single-image Meta ads (feed 4:5). Each ad needs:",
        "- headline: the main line printed on the image (women 60+ / busy adults read it in under 2 seconds;"
        " the batch rule is 15 words or fewer on the whole image).",
        "- on_image_text: any other short lines the layout prints (callouts, labels, review text, offer pills),"
        " in reading order; [] if the layout has only the headline. Respect copy_slots when given.",
        "- primary_text: the Meta primary text above the image.",
        "- fb_headline: the Meta headline under the image (40 characters max). fb_description: optional, 30 max.",
        "- angle: one line naming the angle you used. why: one line on the proof/pattern it comes from"
        " (a winning ad, script or customer phrase in the project files).",
        "",
        "Ground every ad in the brand's own data in the project and product files: the ad-account export"
        " (what spent and converted), past scripts, winning briefs, customer voice. Iterations keep their"
        " source ad's audience, pain and core promise; net-new concepts take a new angle for the slot's"
        " persona. Each ad in the batch must read differently from the others.",
        "",
        "Brand facts and rules (hard limits, not style):",
        json.dumps(rules, ensure_ascii=False, indent=1),
        "",
        "Concept slots (id, audience, layout and source are fixed; the words are yours):",
    ]
    for c in concepts:
        lines.append(json.dumps({k: c[k] for k in SLOT_KEYS if c.get(k) not in (None, "", [])},
                                ensure_ascii=False))
    lines += ["", "Return every id exactly once."]
    msg = "\n".join(lines)
    if len(msg) > 31000:  # ask_stefanbrain caps the message at 32,000 characters
        raise SystemExit(f"Brief is {len(msg)} chars: lower --chunk or trim based_on/copy_notes.")
    return msg


def copy_cmd(args):
    bdir, cfg, sb = brand_cfg(args.brand)
    wdir = bdir / "weeks" / args.week
    cpath = wdir / "concepts.json"
    data = json.loads(cpath.read_text())
    concepts = data if isinstance(data, list) else data.get("concepts", data)
    todo = [c for c in concepts if (not args.ids or c["id"] in args.ids)
            and (args.force or c.get("copy_source") != "stefanbrain")]
    if not todo:
        print("Nothing to write (all concepts already have StefanBrain copy; --force to redo).")
        return
    chunks = [todo[i:i + args.chunk] for i in range(0, len(todo), args.chunk)]
    prefix = sb.get("session_prefix", args.brand)

    def run(ix_chunk):
        ix, chunk = ix_chunk
        session = f"{prefix}-statics-{args.week}-{ix + 1}"
        msg = brief(cfg, args.week, chunk)
        sc = ask(msg, project=sb["project_id"], session=session, schema=COPY_SCHEMA,
                 key=f"{args.brand}-{args.week}-{ix + 1}-{len(chunk)}")
        return session, sc.get("chat"), sc.get("app_url"), structured(sc)

    out_path = wdir / "stefanbrain_copy.json"
    log = json.loads(out_path.read_text()) if out_path.exists() else {"runs": []}
    by_id = {c["id"]: c for c in concepts}
    missing = {c["id"] for c in todo}
    with cf.ThreadPoolExecutor(max_workers=min(4, len(chunks))) as ex:
        for session, chat, url, res in ex.map(run, enumerate(chunks)):
            log["runs"].append({"at": dt.datetime.now().isoformat(timespec="seconds"), "session": session,
                                "chat": chat, "url": url, "concepts": res["concepts"]})
            for r in res["concepts"]:
                c = by_id.get(r["id"])
                if not c:
                    print(f"  unknown id from StefanBrain: {r['id']}")
                    continue
                c.update({"headline": r["headline"].strip(), "on_image_text": r["on_image_text"],
                          "primary_text": r["primary_text"].strip(), "fb_headline": r["fb_headline"].strip(),
                          "fb_description": r.get("fb_description") or "", "copy_angle": r["angle"],
                          "copy_why": r["why"], "copy_source": "stefanbrain", "stefanbrain_chat": chat})
                missing.discard(r["id"])
            print(f"{session}: {len(res['concepts'])} concepts · {url}")
    out_path.write_text(json.dumps(log, ensure_ascii=False, indent=1))
    cpath.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    if missing:
        print(f"MISSING from StefanBrain (write a follow-up or fall back): {sorted(missing)}")
        sys.exit(2)
    print(f"Wrote copy for {len(todo)} concepts into {cpath}")


def revise_cmd(args):
    """Follow-up in the same chat that wrote a concept (QA failures, claim fixes, length)."""
    bdir, cfg, sb = brand_cfg(args.brand)
    cpath = bdir / "weeks" / args.week / "concepts.json"
    data = json.loads(cpath.read_text())
    concepts = data if isinstance(data, list) else data.get("concepts", data)
    c = next(c for c in concepts if c["id"] == args.id)
    schema = {**COPY_SCHEMA}
    msg = (f"Revise {args.id}: {args.note}\nCurrent copy: " + json.dumps(
        {k: c.get(k) for k in ("headline", "on_image_text", "primary_text", "fb_headline")}, ensure_ascii=False)
        + "\nReturn just this id.")
    sc = ask(msg, project=sb["project_id"], chat=c.get("stefanbrain_chat"), schema=schema)
    r = structured(sc)["concepts"][0]
    c.update({"headline": r["headline"].strip(), "on_image_text": r["on_image_text"],
              "primary_text": r["primary_text"].strip(), "fb_headline": r["fb_headline"].strip(),
              "fb_description": r.get("fb_description") or "", "copy_angle": r["angle"], "copy_why": r["why"]})
    cpath.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    print(json.dumps(r, ensure_ascii=False, indent=1))


def product_files(product_id):
    sc, _, _ = call("manage_products", {"request": {"action": "get", "product": product_id, "section": "files"}})
    files, offset = list(sc.get("files") or []), len(sc.get("files") or [])
    while sc.get("next_file_offset") or sc.get("has_more"):
        sc, _, _ = call("manage_products", {"request": {"action": "get", "product": product_id, "section": "files",
                                                        "file_offset": sc.get("next_file_offset", offset)}})
        if not sc.get("files"):
            break
        files += sc["files"]
        offset += len(sc["files"])
    return files


def upload_cmd(args):
    """Stage files and attach them to the brand's StefanBrain product. A file whose name is already on the
    product replaces the old copy (the old one is hidden), so weekly refreshes don't pile up."""
    bdir, cfg, sb = brand_cfg(args.brand)
    paths = [Path(p) for p in args.files]
    names = {p.name for p in paths}
    old = [f["file_id"] for f in product_files(sb["product_id"]) if f.get("name") in names]
    ids = stage(paths)
    vals = list(ids.values())
    for i in range(0, len(vals), 20):
        sc, text, err = call("manage_products", {"request": {"action": "update", "product": sb["product_id"],
                                                             "files": {"add": vals[i:i + 20]}}})
        print(text[:600])
        if err:
            sys.exit(1)
    for i in range(0, len(old), 20):
        sc, text, err = call("manage_products", {"request": {"action": "update", "product": sb["product_id"],
                                                             "files": {"remove": old[i:i + 20]}}})
        print(f"Replaced {len(old[i:i + 20])} older copies: {text[:200]}")


def history_cmd(args):
    """Every static we've made (headline, angle, source, verdict + reason) as one file for StefanBrain, so it
    doesn't repeat headlines and learns from the user's approvals and rejections."""
    bdir = ROOT / "brands" / args.brand
    fb_path = bdir / "feedback.json"
    fb = json.loads(fb_path.read_text()) if fb_path.exists() else []
    fb = fb if isinstance(fb, list) else fb.get("feedback", [])
    verdict = {}
    for f in fb:
        verdict[f.get("concept") or f.get("image", "").rsplit("_v", 1)[0]] = f
    out = [f"# Static ads we've made ({args.brand})", "",
           "Every concept from weeks/*/concepts.json, newest first: headline, angle, source and the user's verdict "
           "where logged. Don't reuse these headlines; learn from the rejection reasons.", ""]
    for w in sorted((bdir / "weeks").glob("*/concepts.json"), reverse=True):
        data = json.loads(w.read_text())
        cs = data if isinstance(data, list) else data.get("concepts", [])
        out += [f"## {w.parent.name} ({len(cs)})", ""]
        for c in cs:
            v = verdict.get(c.get("id"), {})
            line = f"- {c.get('id')} · {c.get('persona', '')} · {c.get('headline', '')!r} · angle: {c.get('angle', '')}"
            if v:
                line += f" · VERDICT {v.get('verdict')}: {v.get('notes', '')}"
            if c.get("copy_source"):
                line += f" · copy: {c['copy_source']}"
            out.append(line)
        out.append("")
    path = bdir / "research" / "static_copy_history.md"
    path.write_text("\n".join(out))
    print(f"Wrote {path} ({path.stat().st_size // 1024} KB)")


def digest_cmd(args):
    """Our ad account as StefanBrain reads it, built only from the CSVs the routine's Atria pulls already
    wrote (no extra Atria calls: Atria charges credits per API call). Each ad: name, format, spend, ROAS,
    purchases, headline and primary text; seasonal rows add transcripts."""
    import csv
    data = ROOT / "brands" / args.brand / "research" / "data"
    cfg = json.loads((ROOT / "brands" / args.brand / "brand.json").read_text())

    def rows(name):
        path = data / name
        if not path.exists():
            return []
        with open(path, newline="") as f:
            return list(csv.DictReader(f))

    def num(x):
        try:
            return float(str(x).replace(",", "").replace("$", ""))
        except ValueError:
            return 0.0

    def block(r, transcript=False):
        spend = num(r.get("spend") or r.get("total_spend_cad") or r.get("spend_cad"))
        roas = r.get("roas") or r.get("blended_roas") or ""
        head = (f"### {r.get('ad_name') or r.get('example_ad_name') or r.get('platform_ad_id')}\n"
                f"{r.get('format', '')} · {r.get('audience', '')} · {r.get('status', '')} · spend {spend:,.0f} · "
                f"ROAS {roas} · purchases {r.get('purchases', '')}".replace(" ·  · ", " · "))
        out = [head]
        if r.get("headline"):
            out.append(f"**Headline:** {r['headline'].strip()}")
        if r.get("primary_text"):
            out.append("**Primary text:** " + r["primary_text"].strip())
        if transcript and r.get("transcript"):
            out.append("**Transcript:** " + r["transcript"].strip())
        return "\n\n".join(out) + "\n"

    sections = [
        ("Top spenders, last 7 days", "top7_spenders.csv", False, 40),
        ("New winners, launched in the last 7 days", "new7_winners.csv", False, 40),
        ("Current winners, last 30 days (spend $300+, ROAS 1.8+)", "current_winners.csv", False, 80),
        ("Rising: launched in the last 30 days and already winning", "rising_winners.csv", False, 40),
    ]
    note = (cfg.get("program") or {}).get("roas_note", "")
    out = [f"# {cfg['name']} ad account digest", "",
           f"Built {dt.date.today()} from our Meta ad account (Atria pulls in research/data). Currency CAD. "
           "Spend shows what scaled; ROAS is Meta-reported. " + (f"Note: {note}" if note else ""), ""]
    seen = set()
    for title, name, tr, cap in sections:
        rs = rows(name)
        if rs:
            out += [f"## {title} ({min(len(rs), cap)})", ""] + [block(r, tr) for r in rs[:cap]]
            seen |= {r.get("platform_ad_id") for r in rs[:cap]}
    win = rows("winning_statics_raw.csv") or rows("winning_statics.csv")
    win.sort(key=lambda r: -num(r.get("spend") or r.get("total_spend_cad")))
    uniq, keys = [], set()
    for r in win:
        k = ((r.get("headline") or "").strip().lower(), (r.get("primary_text") or "")[:200].strip().lower())
        if k in keys or r.get("platform_ad_id") in seen:
            continue
        keys.add(k)
        uniq.append(r)
    if uniq:
        out += [f"## Lifetime winning statics ($5k+ spend since 2024, unique copy, top {min(len(uniq), 150)})", ""]
        out += [block(r) for r in uniq[:150]]
    seas = {}
    for p in sorted(data.glob("seasonal_*.csv")):
        for r in rows(p.name):
            seas.setdefault(r.get("platform_ad_id"), {**r, "_week": p.stem.split("_", 1)[1]})
    if seas:
        out += ["## Seasonal: what won this time last year (by target week)", ""]
        for r in sorted(seas.values(), key=lambda r: (r["_week"], -num(r.get("spend")))):
            out.append(f"(target week {r['_week']})")
            out.append(block(r, True))
    los = rows("losing_statics.csv") or rows("losing_statics_raw.csv")
    if los:
        out += ["## Statics that failed (paused at under $200 spend)", ""]
        out += [f"- {r.get('ad_name')} · spend {r.get('spend_cad') or r.get('spend')} · CTR {r.get('ctr_pct')}%"
                for r in los[:120]]
    path = ROOT / "brands" / args.brand / "research" / "ad_account_digest.md"
    path.write_text("\n".join(out))
    print(f"Wrote {path} ({path.stat().st_size // 1024} KB)")


MARKET_SOURCES = [  # (title, file glob: the newest match is used, row cap)
    ("Core competitors: every ad we pulled (active first, longest-running first)", "core_competitors_*.csv", 250),
    ("Wider competitor set (angle rivals): active, longest-running", "angle_rivals_*.csv", 300),
    ("Other brands' long-running statics (proven formats)", "longrun_statics.csv", 120),
    ("Proven ads from other brands", "proven_other_brands*.csv", 120),
    ("Health & wellness statics growing now (ranked by 7-day impression growth)", "inspiration_wellness_45d.csv", 120),
    ("Curated inspiration (growing statics)", "inspiration_curated.csv", 120),
    ("Long-running inspiration from category brands", "brand_inspiration_longrunning.csv", 120),
    ("Category competitors (top impressions)", "competitor_top_dental.csv", 120),
    ("Ultrasonic-cleaner ads in the market", "ultrasonic_relevant.csv", 120),
    ("Category competitors", "competitor_ads.csv", 150),
]


def market_cmd(args):
    """Other brands' ads with their full copy, from the CSVs this repo's Atria pulls already wrote (newest
    file of each kind; no Atria calls). De-duplicated by brand + copy; active and long-running first."""
    import csv
    data = ROOT / "brands" / args.brand / "research" / "data"
    cfg = json.loads((ROOT / "brands" / args.brand / "brand.json").read_text())
    csv.field_size_limit(10 ** 8)
    out = [f"# {cfg['name']}: what competitors and other brands run (Atria)", "",
           f"Built {dt.date.today()} from the repo's latest Atria pulls. Each ad: brand, format, status, days "
           "running (long-running = the brand keeps paying for it), impression percentile (lower = more "
           "impressions), then its headline and primary text. Use for patterns, hooks and formats; never copy "
           "another brand's words, claims or names into our ads.", ""]
    seen = set()
    for title, pattern, cap in MARKET_SOURCES:
        files = sorted(data.glob(pattern), key=lambda p: p.stat().st_mtime)
        files = [f for f in files if not f.name.startswith("new_since_last")]
        if not files:
            continue
        with open(files[-1], newline="") as f:
            rows = list(csv.DictReader(f))

        def key(r):
            active = str(r.get("status", "")).upper() in ("ACTIVE", "TRUE", "1")
            try:
                days = float(r.get("days_running") or 0)
            except ValueError:
                days = 0
            return (not active, -days)
        rows.sort(key=key)
        block, n = [], 0
        for r in rows:
            body = (r.get("body") or r.get("primary_text") or "").strip()
            head = (r.get("title") or r.get("headline") or "").strip()
            brand = r.get("brand") or r.get("competitor") or ""
            k = (brand.lower(), (head + body)[:240].lower())
            if not (head or body) or k in seen:
                continue
            seen.add(k)
            meta = " · ".join(x for x in [brand, r.get("format", ""), r.get("status", ""),
                                          f"{r['days_running']} days" if r.get("days_running") else "",
                                          f"pct {r['impression_percentile']}" if r.get("impression_percentile") else "",
                                          f"growth {r['growth_7d']}" if r.get("growth_7d") else ""] if x)
            block.append(f"### {meta}\n" + (f"**Headline:** {head}\n" if head else "") +
                         (f"\n{body[:1500]}\n" if body else ""))
            n += 1
            if n >= cap:
                break
        if block:
            out += [f"## {title} ({n}, from {files[-1].name})", ""] + block
    path = ROOT / "brands" / args.brand / "research" / "atria_market_pack.md"
    path.write_text("\n".join(out))
    print(f"Wrote {path} ({path.stat().st_size // 1024} KB)")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    c = sub.add_parser("call")
    c.add_argument("tool")
    c.add_argument("json", nargs="?", default="{}")
    u = sub.add_parser("upload")
    u.add_argument("--brand", required=True)
    u.add_argument("files", nargs="+")
    w = sub.add_parser("copy")
    w.add_argument("--brand", required=True)
    w.add_argument("--week", required=True)
    w.add_argument("--ids", nargs="*")
    w.add_argument("--chunk", type=int, default=10, help="concepts per StefanBrain ask (asks run in parallel)")
    w.add_argument("--force", action="store_true")
    r = sub.add_parser("revise")
    r.add_argument("--brand", required=True)
    r.add_argument("--week", required=True)
    r.add_argument("--id", required=True)
    r.add_argument("note")
    h = sub.add_parser("history")
    h.add_argument("--brand", required=True)
    g = sub.add_parser("digest")
    g.add_argument("--brand", required=True)
    m = sub.add_parser("market")
    m.add_argument("--brand", required=True)
    a = p.parse_args()
    if a.cmd == "status":
        print(call("account_status", {})[1])
    elif a.cmd == "call":
        sc, text, err = call(a.tool, json.loads(a.json))
        print(text)
        if sc:
            print(json.dumps(sc, ensure_ascii=False, indent=1)[:20000])
    elif a.cmd == "upload":
        upload_cmd(a)
    elif a.cmd == "copy":
        copy_cmd(a)
    elif a.cmd == "revise":
        revise_cmd(a)
    elif a.cmd == "history":
        history_cmd(a)
    elif a.cmd == "digest":
        digest_cmd(a)
    elif a.cmd == "market":
        market_cmd(a)


if __name__ == "__main__":
    main()
