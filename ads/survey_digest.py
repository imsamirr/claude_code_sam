"""Customer survey digest: post-purchase Google Form answers -> anonymous aggregates + short verbatim quotes.

    python ads/survey_digest.py --brand comfortwear            # writes research/customer_survey_latest.md

(research/customer_survey_digest.md is the full hand analysis from 2026-11-18; this script keeps the numbers and
quotes current.)

Reads brand.json -> survey {sheet_id, gid}. Downloads with the GDRIVE_CLIENT_ID / GDRIVE_CLIENT_SECRET /
GDRIVE_REFRESH_TOKEN environment variables (raw rows go to a temp file only, never into the repo).
Drops the order/email column, scrubs emails, phone and order numbers and family-member names from quotes.
Column positions are matched by question text, so new form questions don't break it.
"""
import argparse, collections, csv, datetime as dt, io, json, os, random, re, tempfile
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
PII = re.compile(r"[\w.+-]+@[\w-]+\.\w+|\b\d{5,}\b|#\s?\d{3,}|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b")
NAMEFAM = re.compile(r"\b(my )?(wife|husband|daughter|son|mom|mother|dad|father|friend|sister|brother)\s+[A-Z][a-z]+", re.I)
Q = {"comfort": "how comfortable", "source": "where did you find", "problem": "foot problem", "reason": "#1 reason",
     "job": "your job", "looking": "looking for when buying", "fit": "size you received", "size": "shoe size do you typically",
     "solution": "current solution", "age": "your age"}


def download(sheet_id, gid):
    tok = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": os.environ["GDRIVE_CLIENT_ID"], "client_secret": os.environ["GDRIVE_CLIENT_SECRET"],
        "refresh_token": os.environ["GDRIVE_REFRESH_TOKEN"], "grant_type": "refresh_token"}, timeout=60).json()["access_token"]
    r = requests.get(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}",
                     headers={"Authorization": f"Bearer {tok}"}, timeout=300)
    r.raise_for_status()
    return list(csv.reader(io.StringIO(r.content.decode("utf-8"))))


def pct(n, t):
    return f"{round(100 * n / t)}%" if t else "n/a"


def clean(s):
    s = " ".join(s.split())
    return None if PII.search(s) else NAMEFAM.sub(lambda m: (m.group(1) or "") + m.group(2), s)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--brand", default="comfortwear")
    p.add_argument("--csv", help="use a local export instead of downloading")
    a = p.parse_args()
    bdir = ROOT / "brands" / a.brand
    cfg = json.loads((bdir / "brand.json").read_text()).get("survey") or {}
    rows = list(csv.reader(open(a.csv, encoding="utf-8"))) if a.csv else download(cfg["sheet_id"], cfg.get("gid", 0))
    hdr, data = rows[0], rows[1:]
    col = {k: next((i for i, h in enumerate(hdr) if v in h.lower()), None) for k, v in Q.items()}
    if [i for i, h in enumerate(hdr) if "size do you typically" in h.lower()][1:]:
        col["size"] = [i for i, h in enumerate(hdr) if "size do you typically" in h.lower()][-1]
    g = lambda r, k: r[col[k]].strip() if col[k] is not None and col[k] < len(r) else ""
    N = len(data)

    def date(r):
        try:
            return dt.datetime.strptime(r[0].split()[0], "%m/%d/%Y").date()
        except (ValueError, IndexError):
            return None
    dates = [x for x in map(date, data) if x]
    fp = lambda v: [x.strip() for x in re.split(r",\s(?=[A-Z])", v.replace("No Foot Pain, Only Need for Comfort",
                                                                             "No foot pain (only need comfort)")) if x.strip()]
    out = [f"# {a.brand}: post-purchase survey digest", "",
           f"Source: post-purchase Google Form, {N:,} responses, {min(dates)} to {max(dates)}. Aggregates and anonymous "
           f"short quotes only (no names, emails or order numbers). Built {dt.date.today()} by ads/survey_digest.py.", "",
           "## Who buys"]
    age = collections.Counter(g(r, "age") for r in data if g(r, "age")); ta = sum(age.values())
    out.append(f"- Age ({ta:,} answered): " + ", ".join(f"{k} {pct(n, ta)}" for k, n in age.most_common()))
    jobs = collections.Counter(g(r, "job").lower() for r in data if g(r, "job"))
    out.append("- Top job answers: " + ", ".join(f"{k} {n}" for k, n in jobs.most_common(15)))
    f = collections.Counter(x for r in data for x in fp(g(r, "problem"))); tf = sum(1 for r in data if g(r, "problem"))
    out.append(f"- Foot problem ({tf:,}): " + ", ".join(f"{k} {pct(n, tf)}" for k, n in f.most_common(9)))
    src = collections.Counter(g(r, "source").title() for r in data if g(r, "source"))
    out.append("- Found us: " + ", ".join(f"{k} {pct(n, N)}" for k, n in src.most_common(5)))
    fit = collections.Counter(g(r, "fit") for r in data if g(r, "fit")); tft = sum(fit.values())
    out.append("- Size received: " + ", ".join(f"{k} {pct(n, tft)}" for k, n in fit.most_common()))
    cr = collections.Counter(g(r, "comfort")[:1] for r in data if g(r, "comfort"))
    out.append("- Comfort rating 1-5: " + ", ".join(f"{k} = {pct(cr[k], N)}" for k in "12345"))
    recent = [r for r in data if date(r) and date(r) >= dt.date.today() - dt.timedelta(days=90)]
    if recent:
        ra = collections.Counter(g(r, "age") for r in recent if g(r, "age")); t = sum(ra.values())
        rf = collections.Counter(x for r in recent for x in fp(g(r, "problem")))
        out.append(f"- Last 90 days ({len(recent)}): age " + ", ".join(f"{k} {pct(n, t)}" for k, n in ra.most_common()) +
                   "; problems " + ", ".join(f"{k} {n}" for k, n in rf.most_common(5)))
    out += ["", "## In their own words (anonymous, short, verbatim)", ""]
    for title, keys, pat, rat in [
            ("Why they bought", ["reason"], r"(nurse|shift|stand|on my feet|work|plantar|neuropath|bunion|heel|arthrit|swell|walk|disney|travel|wide)", None),
            ("The pain and what it costs them", ["reason", "solution"], r"(pain|hurt|ache|can't|cannot|limp|swollen|burn|numb|throb)", None),
            ("What they tried before", ["solution"], r"(insole|insert|orthotic|sketcher|skecher|hoka|brooks|massage|stretch|tylenol|ibuprofen|\bice\b|surgery|podiatrist|slipper|barefoot)", None),
            ("What they want in a shoe", ["looking"], r"(support|wide|cushion|style|cute|light|slip|toe|arch|all day|stand)", None),
            ("When it worked (4-5 star respondents)", ["reason", "looking", "solution"], r"(love|best|great|finally|amazing|so comfortable|recommend|no more|help)", "45"),
            ("When it didn't (1-2 star respondents; design around these)", ["reason", "looking", "solution"], r"(thought|supposed|expected|disappoint|small|tight|narrow|return|hurt|flimsy|no support|slide)", "12")]:
        rx, pool = re.compile(pat, re.I), []
        for r in data:
            if rat and g(r, "comfort")[:1] not in rat:
                continue
            for k in keys:
                t = g(r, k)
                if 35 <= len(t) <= 230 and rx.search(t) and (c := clean(t)):
                    pool.append(c)
        pool = list(dict.fromkeys(pool)); random.seed(len(title)); random.shuffle(pool)
        out += [f"### {title}", ""] + [f"- \"{q}\"" for q in pool[:22]] + [""]
    path = bdir / "research" / "customer_survey_latest.md"
    path.write_text("\n".join(out))
    print(f"Wrote {path} ({N:,} responses)")


if __name__ == "__main__":
    main()
