#!/bin/sh
# poll_kie.sh tasks.txt  (lines: name taskId) -> downloads <name>.mp4 when done
while read n t; do
  until s=$(curl -sS -m 30 -H "Authorization: Bearer $KIE_AI" "https://api.kie.ai/api/v1/jobs/recordInfo?taskId=$t" | tee rec_$t.json | python3 -I -c "import json,sys; print(json.load(sys.stdin)['data']['state'])"); [ "$s" = success ] || [ "$s" = fail ]; do sleep 10; done
  u=$(python3 -I -c "import json; d=json.load(open('rec_$t.json'))['data']; print(json.loads(d['resultJson'])['resultUrls'][0] if d.get('resultJson') else '')")
  [ -n "$u" ] && curl -sS -o $n.mp4 "$u"; echo "$n $s $u"
done < "$1"
echo ALLDONE
