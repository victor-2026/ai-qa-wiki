#!/usr/bin/env python3
"""W5 mini-jev-local arm: same 7 FlowScout findings via Ollama CPU (qwen2.5:3b),
3 runs each. Raw measurements only: finding x latency x verdicts. No interpretation.
Method: generative judge with fixed prompt (NOT System-One logprob readout)."""
import json, re, time, urllib.request

HOSTS = ["http://192.168.1.209:11434", "http://10.24.175.30:11434"]
MODEL = "qwen2.5:3b"
RUNS = 3

FINDINGS = [
    (1, "Forgot password link present but not verified functional", "Link exists but no verification"),
    (2, "Login button discovered, risk=safe", "Expected element"),
    (3, "External LinkedIn link marked destructive", "Correctly flagged as external nav"),
    (4, "Password reset Cancel button", "UI element, not a finding"),
    (5, "Navigation menu items (Admin, PIM, Leave, Time, etc.)", "Navigation elements"),
    (6, "Logout button", "Destructive action, correctly identified"),
    (7, "OrangeHRM, Inc external link", "External navigation"),
]

PROMPT = ("You are a QA triage judge. Given a finding, reply in EXACTLY this format on one line:\n"
          "severity=<P0|P1|P2|noise> fp=<yes|no>\n"
          "Finding: {f}\nNote: {n}\nReply with only that line.")

def api(host, path, payload, timeout=120):
    req = urllib.request.Request(host + path, data=json.dumps(payload).encode(),
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

host = pick_host()
print(f"host={host} model={MODEL} runs={RUNS}")
rows = []
t0 = time.time()
for fid, f, n in FINDINGS:
    for run in range(1, RUNS + 1):
        t1 = time.time()
        try:
            r = api(host, "/api/generate", {"model": MODEL, "prompt": PROMPT.format(f=f, n=n),
                                            "stream": False, "options": {"temperature": 0}})
            lat = time.time() - t1
            sev, fp = parse(r.get("response", ""))
        except Exception as e:
            lat = time.time() - t1
            sev, fp = ("ERROR", str(e)[:60])
        rows.append({"finding": fid, "run": run, "latency_s": round(lat, 2),
                     "severity": sev, "fp": fp})
        print(rows[-1], flush=True)
total = time.time() - t0
print(f"\nBATCH: {len(rows)} calls in {round(total,1)}s = {round(len(rows)/total,2)} calls/s")
out = {"host": host, "model": MODEL, "method": "generative judge, temp 0, NOT logprob readout",
       "batch_s": round(total, 1), "throughput_cps": round(len(rows) / total, 2), "rows": rows}
open("/var/folders/kl/2pdh9p0j585dv40l78p7wkch0000gn/T/opencode/minijev_raw.json", "w").write(json.dumps(out, indent=1))
print("saved minijev_raw.json")
