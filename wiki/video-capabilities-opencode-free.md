# Video Capabilities in OpenCode Free

**Status:** Verified (Jun 2026)
**Model:** MiMo-V2.5 (310B/15B Sparse MoE, 1M context)
**Interface:** TUI (terminal), Desktop (GUI, partial), WebUI (no), CLI (headless, no)

---

## 1. Executive Summary

MiMo-V2.5 is a native omnimodal model — video is not an API add-on but part of the core architecture.

**Important distinction:** OpenCode has three interfaces, not one:
- **TUI** — runs inside your terminal (iTerm2/Terminal.app via `opencode` command). Video works via `read` tool (PR #18005).
- **Desktop** — native GUI app (Tauri v2, separate window). Video is **blocked** by bug #18143.
- **WebUI** — browser interface (`opencode serve`). Video blocked by bug #21273.

**Bottom line:** Video only works in **TUI** (terminal). If you use Desktop or WebUI, video upload is blocked until bugs are fixed.

---

## 2. Architecture

MiMo-V2.5 processes video through its Vision Transformer (729M params, 28 layers with sliding-window attention). The same encoder handles images, video frames, and audio spectrograms — no separate pipeline.

| Component | Spec |
|-----------|------|
| Total Parameters | 310B (Sparse MoE) |
| Active Parameters | 15B |
| Context Window | 1M tokens |
| Vision Encoder | 729M ViT (24 SWA + 4 Full layers) |
| Audio Encoder | 261M Audio Transformer |
| Input | Text, Image, Video, Audio |
| Output | Text only |

---

## 3. Interface Architecture

OpenCode has three separate interfaces with different code paths:

| Interface | Type | Tech Stack | Video | Limit | Bug |
|-----------|------|------------|-------|-------|-----|
| **TUI** | Terminal (iTerm2) | SolidJS in terminal | 🟢 Yes | 20-256 MB | — |
| **Desktop** | Native GUI app | Tauri v2 (Rust + SolidJS) | 🔴 No | — | #18143 |
| **WebUI** | Browser | SolidJS + Vite | 🔴 No | — | #21273 |
| **CLI `--file`** | Headless | Node.js/Bun | 🔴 No | — | #24698 |

**Why Desktop and TUI differ:** Desktop is a Tauri v2 native app that embeds CLI as a sidecar process. File handling goes through Tauri's native dialog system, which has a separate allowlist — and video types are not included. TUI handles files directly via the `read` tool, which has video MIME detection (PR #18005).

**TUI path:** `read /path/to/video.mp4` → base64 encode → model processes via ViT → text description.

---

## 4. Usage

> **Note:** Video input only works in **TUI** (terminal). Desktop and WebUI users cannot attach video directly. See workaround below.

### Files < 20 MB

```
read /path/to/bug-reproduction.mp4
"Analyze this UI glitch and find the CSS class causing the flickering"
```

### Files > 20 MB — video-frames Skill

```bash
npx skills add mugnimaestra/video-frames-skill
ffmpeg -i large-video.mp4 -vf "fps=1" /tmp/frames/frame_%04d.jpg
read /tmp/frames/frame_0001.jpg  # model analyzes frame sequence
```

### Desktop Workaround (No Direct Video)

Since Desktop blocks video drag-and-drop, use ffmpeg to extract frames first, then attach the frames as images:

```bash
# Extract key frames from video
ffmpeg -i screen-recording.mov -vf "fps=1" /tmp/frames/frame_%04d.jpg

# Attach frames one by one in Desktop chat
# "Analyze these frames from a bug reproduction..."
```

The model will analyze the frame sequence, though you lose audio and motion analysis compared to TUI.

---

### Metadata Extraction

```bash
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
```

---

## 5. Known Bugs

| Bug | Issue | Status | Workaround |
|-----|-------|--------|------------|
| WebUI rejects video | #21273 | Open (Apr 2026) | Use TUI |
| Desktop fewer types | #18143 | Open (Mar 2026) | Use TUI |
| CLI wrong MIME | #24698 | Open (Apr 2026) | Use TUI |
| No vision fallback | #31936 | Open (Jun 2026) | Configure `vision_model` |

**Vision sub-model fallback** (Issue #31936): When primary model lacks video support, configure:
```json
{ "vision_model": "xiaomi/mimo-v2.5" }
```

---

## 6. QA Use Cases

| Use Case | Workflow |
|----------|----------|
| Bug reproduction | Record screen → attach → "What's causing this?" |
| Test failure analysis | Attach CI video → "Why did this E2E test fail?" |
| Regression detection | Compare two recordings → "What changed?" |
| Performance analysis | Attach load video → "Where's the bottleneck?" |
| Demo review | Attach demo → extract feature list |

---

## 7. Token Cost

Video files consume input tokens proportional to base64 size:

| Video Size | Base64 Size | Approx Tokens | Cost ($0.14/1M) |
|------------|-------------|---------------|------------------|
| 1 MB | 1.3 MB | ~330K | $0.046 |
| 5 MB | 6.7 MB | ~1.7M | $0.238 |
| 10 MB | 13.3 MB | ~3.3M | $0.462 |
| 20 MB | 26.7 MB | ~6.7M | $0.938 |

---

## 8. Comparison

| Tool | Video Support | Method |
|------|---------------|--------|
| OpenCode TUI + MiMo-V2.5 | Yes | Native read tool |
| OpenCode Desktop + MiMo-V2.5 | No (bug #18143) | Use ffmpeg frames workaround |
| Gemini CLI | Yes | Native multimodal |
| Kimi CLI | Yes | Native multimodal |
| Claude Code | No | Text + images only |
| Cursor | No | Text + images only |

---

## 9. All OpenCode Go Models — Video Support Matrix

OpenCode Go includes 19 models (as of Jun 2026). 8 support video input.

### Video-Capable Models (8)

| Model | Input Modalities | Context | Price (in/out per 1M) | Notes |
|-------|------------------|---------|----------------------|-------|
| **MiMo-V2.5** | text, image, **audio**, **video** | 1M | $0.14/$0.28 | Best value — cheapest + audio + video |
| **MiniMax M3** | text, image, video | 512K | $0.10/$0.40 | Cheapest video, 3x usage promo |
| **Qwen3.7 Plus** | text, image, video | 1M | $0.40/$1.60 | Best Qwen video, 1M context |
| **Qwen3.6 Plus** | text, image, video | 1M | $0.50/$3.00 | Long context video |
| **Kimi K2.5** | text, image, video | 262K | $0.60/$3.00 | Frontend dev |
| **Kimi K2.6** | text, image, video | 262K | $0.95/$4.00 | Improved K2.5 |
| **Kimi K2.7 Code** | text, image, video | 262K | $0.95/$4.00 | Code-focused |
| **Qwen3.5 Plus** | text, image, video | 262K | $0.20/$1.20 | Deprecated |

### Text-Only Models (11)

| Model | Input | Context | Price (in/out per 1M) |
|-------|-------|---------|----------------------|
| MiMo-V2.5-Pro | text | 1M | $1.74/$3.48 |
| MiMo-V2-Pro | text | 1M | $1.00/$3.00 |
| DeepSeek V4 Flash | text | 1M | $0.14/$0.28 |
| DeepSeek V4 Pro | text | 1M | $1.74/$3.48 |
| GLM-5 | text | 202K | $1.00/$3.20 |
| GLM-5.1 | text | 202K | $1.40/$4.40 |
| GLM-5.2 | text | 1M | $1.40/$4.40 |
| MiniMax M2.5 | text | 204K | $0.30/$1.20 |
| MiniMax M2.7 | text | 204K | $0.30/$1.20 |
| Qwen3.7 Max | text | 1M | $2.50/$7.50 |

### Special Case

| Model | Input | Note |
|-------|-------|------|
| MiMo-V2-Omni | text, image, audio, pdf | No video — deprecated, replaced by V2.5 |

### Video Model Ranking (by value)

1. **MiMo-V2.5** — cheapest, most modalities (audio+video), 1M context
2. **MiniMax M3** — cheapest video-only, 512K, 3x promo
3. **Qwen3.7 Plus** — good balance, 1M context
4. **Kimi K2.7 Code** — code-specific video analysis

### Key Insight

**MiMo-V2.5 is the only model with text + image + audio + video** — full omnimodal. All other video models support text + image + video (no audio).

---

## 10. Sources

- PR #18005 — native video/audio reading (merged Mar 2026)
- Issue #22258 — media attachments in read tool
- Issue #21273 — WebUI video upload bug
- Issue #18143 — Desktop file type gap
- Issue #24698 — CLI MIME type bug
- Issue #31936 — vision sub-model fallback
- Issue #10531 — original feature request (7 upvotes, Jan 2026)
- Xiaomi MiMo-V2.5 docs — https://mimo.xiaomi.com/mimo-v2-5/
- OpenCode Go pricing — https://whichllm.io/models/opencode-go-mimo-v2-5
