# Pi Image Generation via OpenRouter

**Source:** https://openrouter.ai/api/v1/models (424 models, 18 :free) + pi-subagents
**Date:** 2026-09-03
**Fetched:** via webfetch openrouter models + pi-subagents README

---

Pi worker can call image generator via OpenRouter and return file.

Example:
```
Ask worker to generate image via openrouter model google/gemini-3.1-flash-image with prompt "LinkedIn cover 1200x644" and save to outputs/cover.png, then show it.
```

Pricing 1024x1024:
- gemini-3.1-flash-image ~$0.002-0.003
- flux-1.1-pro ~$0.055
- stable-diffusion-xl ~$0.02
- recraft ~$0.04
- ideogram ~$0.08

No :free for images — always paid, counts against 1$/day, 0.5$/session.

[Full content in wiki/pi-image-generation-2026.md]

