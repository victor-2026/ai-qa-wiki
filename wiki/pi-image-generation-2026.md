# Pi Image Generation via OpenRouter (and Gamma)

**Source:** https://openrouter.ai/models (424 models, 18 `:free`; image pricing via `google/gemini-*-image` etc.) + `pi-subagents` (worker delegation)
**Date:** 2026-09-03
**Tags:** #pi #openrouter #image-generation #gamma #subagents
**Raw:** [pi-image-generation-2026.md](../raw/pi-image-generation-2026.md)

---

## What It Is

Pi subagent (`worker`) can call any image generator exposed via **OpenRouter** (or directly) and return the file. No special `Gamma` subagent needed — `worker` with `bash` + `curl` + `write` is enough. Pi displays image if terminal supports (`terminal.showImages:true`, Kitty/iTerm2), otherwise returns path for preview.

## How Pi Calls It

**OpenRouter path (recommended, uses your `OPENROUTER_API_KEY` + `1$/день, 0.5$/сессию` guard):**

```bash
# Pi worker runs this bash (inside delegation):
curl -s https://openrouter.ai/api/v1/chat/completions \
 -H "Authorization: Bearer $OPENROUTER_API_KEY" \
 -H "Content-Type: application/json" \
 -d '{"model":"google/gemini-3.1-flash-image","messages":[{"role":"user","content":"LinkedIn cover 1200x644, QA automation, flat minimal, no text"}]}' \
 | python3 -c "import json,base64,sys; d=json.load(sys.stdin); b64=d['choices'][0]['message']['images'][0]['image_url']['url'].split(',')[1]; open('/tmp/out.png','wb').write(base64.b64decode(b64))"

# Or dedicated image endpoint (where supported):
curl -s https://openrouter.ai/api/v1/images/generations \
 -H "Authorization: Bearer $OPENROUTER_API_KEY" \
 -d '{"model":"black-forest-labs/flux-1.1-pro","prompt":"cover 1200x644 QA","size":"1024x1024"}' \
 | jq -r '.data[0].b64_json' | base64 -d > /tmp/out.png
```

Pi then `read /tmp/out.png` (shows inline if `terminal.showImages:true`) or `write outputs/cover.png`.

**Prompt for Pi (copy to OpenCode Desktop chat):**
```
Ask worker to generate image via openrouter model google/gemini-3.1-flash-image with prompt "LinkedIn cover 1200x644, QA automation, flat minimal" and save to outputs/cover.png, then show it.
```
Pi decides to call `subagent` tool, picks `worker`, composes `bash` + `write`.

**Gamma (gamma.app) path:** same delegation, different endpoint:
```bash
curl -s https://api.gamma.app/v1/generate -H "Authorization: Bearer $GAMMA_API_KEY" -d '{"prompt":"...","format":"pptx"}' > /tmp/deck.pptx
```
Worker saves `pptx/png`, returns path. Gamma is not via OpenRouter — direct API, billed separately.

## Pricing (OpenRouter, 1024×1024, 2026-09-03 via `GET /api/v1/models`)

| Model | Prompt | Image | Total / 1 img |
|-------|--------|-------|---------------|
| `google/gemini-3.1-flash-image` | $0.0000005/1k | — | **~$0.002-0.003** |
| `google/gemini-3.1-flash-lite-image` | $0.00000025/1k | — | ~$0.0015 |
| `google/gemini-3-pro-image` | $0.000002/1k | $0.000012/1k | ~$0.012 |
| `black-forest-labs/flux-1.1-pro` | — | — | **~$0.055** |
| `stability-ai/stable-diffusion-xl` | — | — | ~$0.02 |
| `recraft-ai/recraft-v3` | — | — | ~$0.04 |
| `ideogram-ai/ideogram-v2` | — | — | ~$0.08 |

- Free `:free` variants do **not** include image generation — always paid, counts against `1$/день` limit (0.5$/сессию). Free RPM (20/1000д) not applicable.
- Cost is per image, not per token. 10 covers via `gemini-flash-image` ≈ $0.03, via `flux-pro` ≈ $0.55.

## Can Subagent Return Image?

Yes. Worker saves to `outputs/` or `/tmp/` and Pi brings result back:
- Foreground: streams in conversation, image inline if terminal supports.
- Background: FleetView shows run, `/subagents-fleet` to inspect, machine-readable artifact in `~/.pi/agent/sessions/.../subagent-artifacts/`.
- Bounded: `maxSubagentSpawnsPerRun=3` (now limited for paid intensity) — image gen counts as 1 spawn.

**Relevance to QA/QE:**

| Use Case | Pi Agent | Prompt |
|----------|----------|--------|
| Cover 1200×644 for LinkedIn article | `worker` | Generate cover via `gemini-3.1-flash-image`, flat, QA automation |
| Gamma deck for client pitch | `worker` | Generate pptx via gamma.app, 5 slides, QA strategy |
| Visual test baseline | `worker` | Generate baseline png via flux, compare vs screenshot |

Gamma cost separate (Gamma Pro $10/mo unlimited or per-deck $0.20) — not OpenRouter.

## Where to Start

1. Enable `terminal.showImages:true` in `~/.pi/agent/settings.json` (already `true`).
2. Try free text first: `pi --provider openrouter --model openrouter/free --print "Use worker to generate..."` — will fallback to paid image model automatically (image models have no `:free`).
3. Keep `0.5$/сессию` guard: one cover = $0.003, well within; 100 covers = $0.30 < 0.5.

## Cross-links

- Related: [pi-subagents](pi-subagents-2026.md) (scout/worker/reviewer/oracle, FleetView, 64→3)
- Related: [pi-opencode-integration](pi-opencode-integration-2026.md) (3 layers AGENTS.md/MCP/CLI, loop)
- Related: [ruvnet agentic stack](ruvnet-agentic-stack-2026.md) (harness evolution)
- Guard: `~/.pi/agent/scripts/openrouter-guard.sh --report`

---

*Ingested: 2026-09-03 · Via openrouter.ai/api/v1/models (424, 18 free) + pi-subagents README + openrouter-guard 1$/0.5$*
