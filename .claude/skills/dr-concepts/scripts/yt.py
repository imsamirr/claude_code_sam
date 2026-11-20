"""Usage: python3 -I yt.py <out.json> <queries.txt (one search per line)>"""
import json,re,sys,urllib.parse,urllib.request,time
Q=[l.strip() for l in open(sys.argv[2]) if l.strip()]
out=[]
for q in Q:
    url="https://www.youtube.com/results?search_query="+urllib.parse.quote(q)+"&hl=en&gl=US"
    try:
        html=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0","Accept-Language":"en-US"}),timeout=30).read().decode("utf8","ignore")
    except Exception as e:
        print("ERR",q,e,file=sys.stderr); continue
    m=re.search(r"var ytInitialData = (\{.*?\});</script>",html)
    if not m: print("NOJSON",q,file=sys.stderr); continue
    data=json.loads(m.group(1))
    vids=[]
    def walk(o):
        if isinstance(o,dict):
            if "videoRenderer" in o:
                v=o["videoRenderer"]
                t="".join(r.get("text","") for r in v.get("title",{}).get("runs",[]))
                views=v.get("viewCountText",{}).get("simpleText","")
                pub=v.get("publishedTimeText",{}).get("simpleText","")
                ch="".join(r.get("text","") for r in v.get("ownerText",{}).get("runs",[]))
                vids.append((t,views,pub,ch,v.get("videoId")))
            for x in o.values(): walk(x)
        elif isinstance(o,list):
            for x in o: walk(x)
    walk(data)
    out.append({"q":q,"videos":vids[:12]})
    time.sleep(1)
json.dump(out,open(sys.argv[1],"w"))
for b in out:
    print("\n###",b["q"])
    for t,v,p,c,i in b["videos"][:10]: print(f"- {t} | {v} | {p} | {c}")
