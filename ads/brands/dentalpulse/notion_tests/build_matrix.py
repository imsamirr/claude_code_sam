import json, os, csv, collections, sys
D = os.path.dirname(os.path.abspath(__file__))
FILES = ['legacy.json', 'native.json', 'apr_may.json', 'jun.json', 'jul.json', 'aug.json', 'sep.json', 'oct.json', 'nov.json']
SOURCE = {'legacy.json': None, 'native.json': 'Native Ads'}
rows, seen = [], set()
for name in FILES:
    data = json.load(open(os.path.join(D, name), encoding='utf-8'))
    for r in data:
        u = r.get('url') or (name + str(len(rows)))
        key = u.split('?')[0].rstrip('/').split('/')[-1].replace('-', '')[-32:]
        if key in seen: continue
        seen.add(key)
        src = r.get('source') or SOURCE.get(name) or 'Monthly scripts'
        if name not in SOURCE: src = 'Monthly scripts'
        if src.startswith('Native Ads'): src = 'Native Ads'
        r['source'] = src
        r['written'] = bool(r.get('written'))
        r['primary_angle'] = r.get('primary_angle') or ('(not classified)' if r['written'] else '—')
        r['format'] = r.get('format') or ('(not classified)' if r['written'] else '—')
        if r['format'] == 'Other: Song / musical ad': r['format'] = 'Other: Song / music video'
        r['appliance'] = r.get('appliance') or 'Broad/unspecified'
        r['month'] = (r.get('month') or (r.get('created') or '')[:7]) or 'unknown'
        rows.append(r)
monthly_codes = {(r.get('code') or '').strip().upper() for r in rows if r['source'] == 'Monthly scripts'}
before = len(rows)
rows = [r for r in rows if not (r['source'] == 'Creative Tracker' and (r.get('code') or '').strip().upper() in monthly_codes)]
print('dropped tracker copies of monthly codes:', before - len(rows))
cc = collections.Counter((r.get('code') or '').strip().upper() for r in rows if r.get('code'))
for r in rows:
    k = (r.get('code') or '').strip().upper()
    if k and cc[k] > 1: r['code_reused'] = True
print('reused codes:', len([k for k, v in cc.items() if v > 1]))
os.makedirs(os.path.join(D, 'site'), exist_ok=True)
meta = {'asof': f"Read from Notion on {sys.argv[1] if len(sys.argv) > 1 else ''}: {len(rows)} task pages from the Apr–Nov 2026 monthly script boards, the earlier Creative Tracker (Nov 2025–Apr 2026) and the Native Ads advertorial tracker."}
json.dump({'meta': meta, 'briefs': rows}, open(os.path.join(D, 'site', 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False)
cols = ['month', 'source', 'code', 'title', 'status', 'nn_it', 'written', 'word_count', 'appliance', 'primary_angle', 'secondary_angles', 'format', 'format_detail', 'persona', 'awareness', 'angle_summary', 'hooks', 'competitors_named', 'offer_in_script', 'iteration_of', 'notion_angle', 'notes', 'url']
with open(os.path.join(D, 'dentalpulse_tested_matrix.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(cols)
    for r in sorted(rows, key=lambda r: (r['month'], r.get('created') or '')):
        w.writerow(['; '.join(map(str, r.get(c) or [])) if isinstance(r.get(c), list) else r.get(c) for c in cols])
W = [r for r in rows if r['written']]
print('total', len(rows), 'written', len(W), collections.Counter(r['source'] for r in rows))
bym = collections.Counter(r['month'] for r in rows); bymw = collections.Counter(r['month'] for r in W)
srcm = collections.Counter((r['month'], r['source']) for r in W)
for m in sorted(bym): print(m, 'written', bymw[m], 'of', bym[m], {s: srcm[(m, s)] for s in ['Monthly scripts', 'Creative Tracker', 'Native Ads'] if srcm[(m, s)]})
print('\nANGLES'); [print(f'{n:4} {a}') for a, n in collections.Counter(r['primary_angle'] for r in W).most_common(14)]
print('\nFORMATS'); [print(f'{n:4} {a}') for a, n in collections.Counter(r['format'] for r in W).most_common(12)]
print('\nAPPLIANCE'); [print(f'{n:4} {a}') for a, n in collections.Counter(r['appliance'] for r in W).most_common()]
