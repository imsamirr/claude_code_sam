"""Usage: python3 -I reddit_pull.py <out.json> <queries.txt (one search per line)>"""
import json, sys, time, urllib.parse, urllib.request, datetime, os
out = sys.argv[1]
Q=[l.strip() for l in open(sys.argv[2]) if l.strip()]
seen=set(); rows=[]
for q in Q:
    for kind in ("comment","submission"):
        url=f"https://api.pullpush.io/reddit/search/{kind}/?q={urllib.parse.quote(q)}&size=100"
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"research-script"}),timeout=40) as r:
                data=json.load(r).get("data",[])
        except Exception as e:
            print("ERR",q,kind,e,file=sys.stderr); time.sleep(2); continue
        for d in data:
            if d["id"] in seen: continue
            seen.add(d["id"])
            ts=datetime.datetime.utcfromtimestamp(int(d.get("created_utc",0)))
            text=(d.get("body") or ((d.get("title") or "")+" — "+(d.get("selftext") or ""))).replace("\n"," ").strip()
            if len(text)<40 or text.startswith("[removed]") or text.startswith("[deleted]"): continue
            rows.append({"q":q,"kind":kind,"sub":d.get("subreddit"),"score":d.get("score",0),"date":ts.strftime("%Y-%m-%d"),"month":ts.month,"text":text[:700],"link":"https://reddit.com"+(d.get("permalink") or "")})
        time.sleep(1.2)
    print(q, len(rows), file=sys.stderr)
json.dump(rows,open(out,"w"))
print("total",len(rows),"decjan",sum(1 for r in rows if r["month"] in (11,12,1,2)))
