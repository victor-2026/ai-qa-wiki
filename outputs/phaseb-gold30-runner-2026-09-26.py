#!/usr/bin/env python3
"""Phase B: gold-30 judge runs (W3 execution, frozen plan).
Arms: L0 qwen2.5:3b x3 (temp 0) + binding routing (T1 UNPARSEABLE->L1,
T2 split->L0 third+majority, persistent split->L1; T3-CAL6 literal check,
T4 N/A in severity space — both documented) + cloud Jev x1.
Incremental save after every row. Raw only, no interpretation."""
import json, re, time, urllib.request, os

HOSTS = ["http://192.168.1.209:11434", "http://10.24.175.30:11434"]
L0 = "qwen2.5:3b"
L1 = "gemma3:4b"
L2 = "qwen3:4b"
SEVS = ("P0", "P1", "P2", "NOISE")
OUT = "/Users/victor/Projects/ai-qa-wiki/outputs/phaseb-gold30-raw-2026-09-26.json"
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
        return ("UNPARSEABLE", "?")
    return (m.group(1).upper(), m.group(2).lower())

def gen(host, model, text, timeout, think=None):
    t0 = time.time()
    p = {"model": model, "prompt": PROMPT.format(f=text), "stream": False,
         "options": {"temperature": 0}}
    if think is not None:
        p["think"] = think
    try:
        r = api(host, p, timeout)
        return parse(r.get("response", "")), round(time.time() - t0, 2)
    except Exception as e:
        return ((f"ERROR:{type(e).__name__}", "?"), round(time.time() - t0, 2))

def save(rows):
    json.dump({"rows": rows, "partial": True}, open(OUT, "w"), indent=1)

items = [(i["id"], i["title"] + ". " + i["description"]) for i in json.load(open(GOLD))["items"]]
host = pick_host()
print(f"host={host} items={len(items)}")
rows = []
if os.path.exists(OUT):
    try:
        rows = json.load(open(OUT)).get("rows", [])
    except Exception:
        rows = []
done = set((r["id"], r["arm"], r.get("run", 1)) for r in rows)
for iid, text in items:
    # L0 x3
    l0outs = []
    for run in (1, 2, 3):
        if (iid, "L0", run) in done:
            continue
        (s, f), lat = gen(host, L0, text, 120)
        r = {"id": iid, "arm": "L0", "run": run, "latency_s": lat, "got_sev": s, "got_fp": f}
        rows.append(r)
        l0outs.append(r)
        save(rows)
        print(iid, "L0", run, s, f, lat, flush=True)
print("L0 done, rows:", len(rows))
