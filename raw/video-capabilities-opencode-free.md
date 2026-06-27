# Video Capabilities in OpenCode Free

**Source:** GitHub Issues #10531, #18005, #21273, #22258, #24698, #31936 + Xiaomi MiMo-V2.5 docs
**Date:** 2026-06-24
**Model:** MiMo-V2.5 (310B total / 15B active, Sparse MoE)

---

## Overview: Three Interfaces

OpenCode has three separate interfaces with different video support:

| Interface | Type | Video | Bug |
|-----------|------|-------|-----|
| **TUI** | Terminal (iTerm2) | 🟢 Yes | — |
| **Desktop** | Native GUI (Tauri v2) | 🔴 No | #18143 |
| **WebUI** | Browser | 🔴 No | #21273 |
| **CLI `--file`** | Headless | 🔴 No | #24698 |

**Why they differ:** Desktop is a Tauri app that wraps CLI as a sidecar. File dialogs go through Tauri's native allowlist, which excludes video. TUI uses the `read` tool directly with video MIME detection (PR #18005).

**Desktop workaround:** Extract frames via ffmpeg → attach as images.

---

## 1. Model Architecture

MiMo-V2.5 is a native omnimodal model. Not bolted-on — designed from scratch with video in the architecture.

| Component | Spec |
|-----------|------|
| Total Parameters | 310B (Sparse MoE) |
| Active Parameters | 15B per inference |
| Context Window | 1M tokens |
| Vision Encoder | 729M-param ViT (28 layers: 24 SWA + 4 Full) |
| Audio Encoder | 261M-param Audio Transformer (24 layers) |
| Input Modalities | Text, Image, Video, Audio |
| Output Modalities | Text only |
| Training | SFT → Agentic RL → Multi-Teacher On-Policy Distillation |

Key insight: Video is not an API add-on. It's processed natively through the Vision Transformer with sliding-window attention — the same encoder handles images, video frames, and audio spectrograms.

---

## 2. Interface Support Matrix

| Interface | Video Files | Limit | Status |
|-----------|-------------|-------|--------|
| **TUI** | Yes (read tool) | 20-256 MB | PR #18005 merged |
| **Desktop** | Partial | 20 MB | Bug #18143 open |
| **WebUI** | No | — | Bug #21273 open |
| **CLI `--file`** | No | — | Bug #24698 open |

### TUI (Primary Path)

The `read` tool detects `video/*` MIME types on binary files and returns them as base64-encoded file attachments — same pattern as existing PDF/image support.

```
User: read /path/to/bug-reproduction.mp4
→ Tool detects video/mp4 MIME type
→ Base64-encodes file (20MB cap)
→ Returns as file attachment
→ MiMo-V2.5 processes via Vision Transformer
→ Model describes video content
```

**Size Limits:**
- Default: 20 MB (base64 safety cap)
- Configurable: up to 256 MB via `OPENCODE_READ_MAX_ATTACHMENT_BYTES`
- Workaround for >20 MB: `video-frames-skill` (extracts key frames via ffmpeg)

### Desktop

Bug #18143: Desktop accepts fewer dropped file types than TUI. Dragging a video shows "Unsupported attachment — Only images, PDFs, or text files can be attached here."

Status: Open since March 2026. PR #18139 was merged but gap remains for video specifically.

### WebUI

Bug #21273: Clicking "+" to select a video returns "Only images, PDFs, or text files can be attached here."

Status: Open since April 2026. Assigned to @iamdavidhill.

### CLI `--file` Flag

Bug #24698: The `--file` flag hardcodes MIME type to `text/plain` regardless of extension. A video file is sent as text, not as multimodal input.

Status: Open since April 2026. Multiple fix PRs submitted (#24933, #26152).

---

## 3. How to Use Video (TUI Only)

> **Desktop users:** Video upload is blocked by bug #18143. Use the ffmpeg frames workaround below.

### Direct Read (files < 20 MB)

```
# Simple case — model analyzes the video
read /path/to/screen-recording.mp4

# With question
"Analyze this 30-second bug reproduction. What CSS class might be causing the flickering?"
```

### Large Files (> 20 MB) — video-frames Skill

```bash
# Install the skill
npx skills add mugnimaestra/video-frames-skill

# Extract key frames
ffmpeg -i large-video.mp4 -vf "fps=1" /tmp/frames/frame_%04d.jpg

# Read extracted frames
read /tmp/frames/frame_0001.jpg
read /tmp/frames/frame_0002.jpg
# ... model analyzes frame sequence
```

### Desktop Workaround (ffmpeg Frames)

Since Desktop blocks video, extract frames and attach as images:

```bash
ffmpeg -i screen-recording.mov -vf "fps=1" /tmp/frames/frame_%04d.jpg
```

Then attach frame_0001.jpg, frame_0002.jpg etc. in Desktop chat. The model analyzes the frame sequence, though audio and motion are lost.

---

### Using ffmpeg via Bash Tool

```bash
# Extract frames at 1fps
ffmpeg -i input.mp4 -vf fps=1 frame_%04d.jpg

# Extract audio for transcription
ffmpeg -i input.mp4 -vn -acodec pcm_s16le audio.wav

# Get video metadata
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
```

---

## 4. Known Bugs and Workarounds

| Bug | Description | Workaround |
|-----|-------------|------------|
| #21273 | WebUI rejects video uploads | Use TUI `read` tool |
| #18143 | Desktop fewer file types than TUI | Use TUI directly |
| #24698 | CLI `--file` wrong MIME type | Use TUI `read` tool |
| #31936 | No vision sub-model fallback | Configure `vision_model` in opencode.json |

### Vision Sub-Model Fallback (Issue #31936)

When the primary model doesn't support images/video (e.g., `mimo-v2.5-pro`), you can configure a fallback:

```json
{
  "model": "xiaomi/mimo-v2.5-pro",
  "vision_model": "xiaomi/mimo-v2.5"
}
```

Status: Open. Referenced by similar issues #24948, #22828, #26160.

---

## 5. Practical Use Cases for QA

| Use Case | How | Example |
|----------|-----|---------|
| Bug reproduction analysis | Record screen → attach video → ask model to identify issue | "Analyze this UI glitch" |
| Test failure investigation | Attach CI video log → ask for root cause | "Why did this E2E test fail?" |
| Demo recording analysis | Attach product demo → extract feature list | "What features are shown?" |
| Regression detection | Compare before/after screen recordings | "What changed between these two?" |
| Performance analysis | Attach page load video → identify bottlenecks | "Where's the slowest render?" |

---

## 6. Pricing

| Metric | Cost |
|--------|------|
| Input | $0.14 / 1M tokens |
| Output | $0.28 / 1M tokens |
| Cached Input | $0.00 |
| Context Window | 1M tokens |
| Max Output | 128K tokens |

Video files consume input tokens proportional to their base64 size. A 5 MB MP4 ≈ 6.7M base64 characters ≈ ~1.7M tokens.

---

## 7. Comparison with Alternatives

| Tool | Video Support | How |
|------|---------------|-----|
| OpenCode TUI + MiMo-V2.5 | Yes | Native read tool, base64 |
| OpenCode Desktop + MiMo-V2.5 | No (bug #18143) | ffmpeg frames workaround |
| Gemini CLI | Yes | Native multimodal |
| Kimi CLI | Yes | Native multimodal |
| Claude Code | No | Text + images only |
| Cursor | No | Text + images only |

---

## 8. All OpenCode Go Models — Video Support Matrix

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

## 9. Sources

1. PR #18005 — `feat(opencode): add native video and audio file reading support` (Mar 2026)
2. Issue #22258 — `feat(tool): Add media attachments to read tool`
3. Issue #21273 — `The WebUI is unable to upload video files to models that support video` (Apr 2026)
4. Issue #18143 — `Desktop should accept more dropped file types in prompt input` (Mar 2026)
5. Issue #24698 — `CLI: --file flag attaches images with incorrect MIME type` (Apr 2026)
6. Issue #31936 — `feat: vision sub-model fallback for non-multimodal models` (Jun 2026)
7. Issue #10531 — `Native Multimodal Context Support (Video/Audio)` (Jan 2026)
8. Xiaomi MiMo-V2.5 docs — https://mimo.xiaomi.com/mimo-v2-5/
9. OpenCode Go pricing — https://whichllm.io/models/opencode-go-mimo-v2-5
