#!/usr/bin/env python3
"""Phase B cloud arm: Jev x1 on gold-30 (W3). Incremental save, verbatim reasoning."""
import json, os, sys, time
sys.path.insert(0, "/Users/victor/Private/Positions-CV-CL/company/pilots/FlowScout/FlowScout")
from flowscout.jev_client import JEVClient

OUT = "/Users/victor/Projects/ai-qa-wiki/outputs/phaseb-gold30-cloud-2026-09-26.json"
GOLD = "/Users/victor/Private/Positions-CV-CL/company/pilots/Jev/gold-n30.json"

items = [(i["id"], i["title"] + ". " + i["description"]) for i in json.load(open(GOLD))["items"]]
rows = []
if os.path.exists(OUT):
    try:
        rows = json.load(open(OUT)).get("rows", [])
    except Exception:
        rows = []
done = set(r["id"] for r in rows)
c = JEVClient()
for iid, text in items:
    if iid in done:
        continue
    t0 = time.time()
    try:
        r = c.classify_finding(text, context="Phase B gold-30 cloud arm")
        rows.append({"id": iid, "arm": "cloud", "latency_s": round(time.time() - t0, 2),
                     "got_sev": r.severity, "fp_bool": bool(r.is_fp),
                     "conf": r.confidence, "raw": str(r.reasoning)[:500]})
    except Exception as e:
        rows.append({"id": iid, "arm": "cloud", "error": f"{type(e).__name__}: {e}"})
    json.dump({"rows": rows, "partial": True}, open(OUT, "w"), indent=1)
    print(iid, rows[-1].get("got_sev"), rows[-1].get("fp_bool"), flush=True)
print("done, rows:", len(rows))
