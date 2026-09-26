#!/usr/bin/env python3
"""Phase B canonical: gold-30 L0 x3 with verbatim + bool fp (W2 4f3fd45 rulings 2-3).
Same frozen prompt, same digest 357c53fb659c5076de1d65cc, temp 0.
Row: id/arm/run/latency/got_sev/fp_bool/raw_response. Incremental save."""
import json, re, time, urllib.request, os

HOSTS = ["http://192.168.1.209:11434", "http://10.24.175.30:11434"]
L0 = "qwen2.5:3b"
OUT = "/Users/victor/Projects/ai-qa-wiki/outputs/phaseb-gold30-verbatim-2026-09-26.json"
GOLD = "/Users/victor/Private/Positions-CV-CL/company/pilots/Jev/gold-n30.json"

PROMPT = ("You are a QA triage judge. Given a finding, reply in EXACTLY this format on one line:\n"
          "severity=<P0|P1|P2|noise> fp=<yes|no>\n"
          "Finding: {f}\nReply with only that line.")

def api(host, payload, timeout):
    req = urllib.request.Request(host + "/api/generate", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)

def pick_host():
    for h in HOSTS:
        try:
            urllib.request.urlopen(h + "/", timeout=5)
            return h
        except Exception:
            continue
    raise RuntimeError("no Ollama reachable")

def parse(text):
    m = re.search(r"severity\s*=\s*(P0|P1|P2|noise)\s+fp\s*=\s*(yes|no)", text, re.I)
    if not m:
        return ("UNPARSEABLE", None)
    return (m.group(1).upper(), m.group(2).lower() == "yes")

items = [(i["id"], i["title"] + ". " + i["description"]) for i in json.load(open(GOLD))["items"]]
host = pick_host()
print(f"host={host} model={L0} items={len(items)}")
rows = []
if os.path.exists(OUT):
    try:
        rows = json.load(open(OUT)).get("rows", [])
    except Exception:
        rows = []
done = set((r["id"], r["run"]) for r in rows)
for iid, text in items:
    for run in (1, 2, 3):
        if (iid, run) in done:
            continue
        t0 = time.time()
        try:
            r = api(host, {"model": L0, "prompt": PROMPT.format(f=text), "stream": False,
                           "options": {"temperature": 0}}, 120)
            raw = r.get("response", "")
        except Exception as e:
            raw = f"ERROR:{type(e).__name__}"
        s, f = parse(raw)
        rows.append({"id": iid, "arm": "L0", "run": run, "latency_s": round(time.time() - t0, 2),
                     "got_sev": s, "fp_bool": f, "raw": raw[:500]})
        json.dump({"rows": rows, "partial": True}, open(OUT, "w"), indent=1)
        print(iid, run, s, f, flush=True)
print("done, rows:", len(rows))
