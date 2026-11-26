"""python3 add.py <brand>  < lines 'ad_id suffix days'  -> appends 'ad_id url days' to candidates/<brand>.txt"""
import sys
b = sys.argv[1]
with open(f"candidates/{b}.txt", "a") as f:
    for l in sys.stdin:
        if l.strip():
            a, s, d = l.split()
            f.write(f"{a} https://cdn.tryatria.com/adfiles/{a}_{s}.jpeg {d}\n")
