# Distributed P2P LLM Inference — SwarmLLM

> Nehanth Narendrula (@Nehanth), ML @ Red Hat AI. MIT-licensed open-source project. 250k+ views, 10.7 tokens/s.

## What Is SwarmLLM

A peer-to-peer inference engine that runs a large language model (e.g., Qwen 3.8 27B) across multiple devices — phones, laptops, PCs — from a browser tab. Each device holds a slice of the model, tokens pass between devices peer-to-peer over WebRTC, and the answer appears on every screen simultaneously.

**Core idea**: Your phone alone can't run Qwen 3.8. Your room can.

## Architecture

### Mesh Inference Model
```
┌──────────┐    ┌──────────┐    ┌──────────┐
│  Phone   │    │  Laptop  │    │  PC      │
│  slice   │◄──►│  slice   │◄──►│  slice   │
│  of model│    │  of model│    │  of model│
└──────────┘    └──────────┘    └──────────┘
       ◄──── one room code ◀────►
       ◄── WebRTC P2P, no server ──►
       ◄── your words never leave the room ◀─►
```

### Key Properties
- **No install** — runs from browser tab
- **No accounts** — four-letter room code
- **No servers** — pure P2P over WebRTC
- **Privacy-first** — text never leaves the room
- **Open-source** — MIT license (`github.com/Nehanth/swarmllm`)

### How It Works
1. **Make a room** — get a four-letter code
2. **Chip in** — each device downloads its slice of the model (bigger devices = more slices)
3. **Think together** — every token laps the room through all devices, appears on every screen

## Performance

| Metric | Initial | Current |
|--------|---------|---------|
| Throughput | 2.5 tokens/s | **10.7 tokens/s** |
| Model | Qwen 3.8 27B | Qwen 3.8 27B |
| Devices | Phone + Mac | Multiple |
| Identical output | — | **Bit-for-bit identical** with speculative decoding |

## Roadmap
- Multi-turn conversations
- Rooms that survive a device leaving
- Longer context windows
- Faster prefill
- More models
- **Every item is up for grabs** (open-source, community-driven)

## Testing Implications

### 1. Distributed Inference Testing
- **Partial model on each device** → how to verify correctness of the full model output?
- **Token-by-token validation** — each device contributes a token; must verify the stream is coherent
- **Bit-for-bit identical** claim requires deterministic inference across heterogeneous hardware
- **Speculative decoding** verification — how to confirm no tokens were fabricated?

### 2. P2P Network Testing
- **Device joining/leaving** — graceful degradation when a peer drops mid-inference
- **Network partition** — what happens when a device loses connection?
- **Heterogeneous hardware** — different speeds, memory, compute → different slice sizes
- **WebRTC reliability** — NAT traversal, firewall, latency, jitter

### 3. Security Testing
- **No central server** → no single point of attack, but also no central trust
- **Privacy guarantee** — words never leave the room → need to verify this actually holds
- **WebRTC attack surface** — new vectors for interception, MITM, data exfiltration
- **Model slice integrity** — is each device serving its actual slice, or a modified version?

### 4. Reliability / Quality Gates
- **Throughput as quality metric** — tokens/s is the primary signal
- **Output coherence** — do all screens show identical output?
- **Error handling** — graceful degradation when device fails
- **Determinism across devices** — bit-for-bit identical claim needs verification

## Related Projects & Concepts

| Project | Approach | Difference |
|---------|----------|------------|
| **SwarmLLM** (Nehanth) | Browser-based WebRTC P2P | No install, room code |
| **SwarmLLM** (enapt/Rust) | Single binary, libp2p, Kademlia DHT | Rust, OpenAI API, enterprise |
| **SWARM-LLM** (academic) | Edge SLMs with uncertainty routing | Research paper, gateway-based |
| **MLC-LLM/web-llm** | In-browser WebGPU inference | Single device, no P2P |
| **Federated Learning** | Distributed model training | Training, not inference |

## Connection to Our Work

- **[[llm-testing]]**: Distributed LLM inference creates new testing challenges (verification of distributed output, determinism across devices)
- **[[Test-Reliability]]**: Flakiness in P2P networks, device heterogeneity
- **[[Fault-injection]]**: Simulating device dropout, network partition, corrupted slices
- **[[rag-evaluation]]**: If RAG is deployed on distributed inference, verification gets harder

## Source
- Website: swarmllm.ai
- GitHub: `github.com/Nehanth/swarmllm` (MIT)
- Author: Nehanth Narendrula, ML @ Red Hat AI (agentic evaluation)
- LinkedIn: nehanthnarendrula
- Tags: #swarmllm, #p2p-inference, #distributed-ai, #webrtc, #edge-ai, #browser-inference, #mesh-inference, #open-source

---

## Practical Testing Plan — 2-Device Swarm

> **Date:** 2026-09-09  
> **Goal:** Test SwarmLLM on our hardware (PC-224 + MacBook Pro), validate P2P inference, and document findings.

### Hardware Available

| Device | RAM | GPU | Role in Swarm |
|--------|-----|-----|---------------|
| **PC-224** | 64GB | 6GB VRAM (RTX 3060) | Primary: larger slice, host server |
| **MacBook Pro** | 16GB | Intel integrated | Secondary: smaller slice |

### Network
- **ZeroTier VPN:** `10.24.175.x` — both devices on same virtual LAN
- **PC-224:** `192.168.1.224` / ZeroTier `10.24.175.30`
- **MacBook:** `192.168.1.31` / ZeroTier `10.24.175.x`
- **Ollama on PC-224:** `http://192.168.1.224:11434`

### Step-by-Step Plan

1. **Check WebGPU support** on MacBook Pro:
   ```
   # Open Chrome → chrome://gpu → look for "WebGPU: Enabled"
   ```
   If WebGPU is available → browser-based SwarmLLM should work.

2. **Clone and run SwarmLLM** on PC-224:
   ```bash
   git clone https://github.com/Nehanth/swarmllm
   cd swarmllm
   # Follow setup instructions
   ```

3. **Clone and run SwarmLLM** on MacBook Pro:
   ```bash
   git clone https://github.com/Nehanth/swarmllm
   cd swarmllm
   # Connect to same room via ZeroTier VPN
   ```

4. **Create a room** on PC-224 → join from MacBook with room code

5. **Load a model** and observe:
   - Each device downloads its slice
   - Token generation across both devices
   - Output appears on both screens simultaneously
   - **Measure:** tokens/s, latency, coherence

6. **Test failure scenarios:**
   - MacBook disconnects mid-inference → graceful degradation?
   - Network interruption → recovery?
   - Different model sizes → how does slice allocation work?

### Alternative Approaches (if SwarmLLM doesn't work)

| Approach | Tool | Setup |
|----------|------|-------|
| **Browser inference** | MLC-LLM/web-llm | npm install @mlc-ai/web-llm, Chrome WebGPU |
| **Binary P2P** | enapt/SwarmLLM | Rust binary, libp2p, Kademlia DHT |
| **Ollama distributed** | Ollama multi-GPU | PC-224 only (GPU + CPU split) |
| **Custom WebRTC** | Simple P2P signaling | Manual WebRTC data channel |

### What to Document
- [ ] WebGPU status on MacBook
- [ ] SwarmLLM install success/failure
- [ ] Model loading time per device
- [ ] Tokens/s per device
- [ ] Output coherence verification
- [ ] Device dropout behavior
- [ ] Network latency metrics (ZeroTier vs local)

### Expected Outcomes
- **Best case:** Working P2P inference on PC-224 + MacBook → proof of concept for distributed QA testing
- **Medium case:** Browser-based inference works but P2P has issues → document limitations
- **Learning case:** Neither works → understand P2P inference barriers, document for future

---

## William Tran — Outreach Note

> **Status:** Followed on LinkedIn (2026-09-09). Post is public.
> 
> **Topic:** "Developers shouldn't test their own code" — AI writes code AND tests, "700 tests passed" ≠ tested correctly, breadcrumb rendering bug missed by automated check.
> 
> **Key quote:** "Writing test cases isn't the scarce skill anymore. Knowing which 'tests passed' needs a second look is."
> 
> **Relevance:** Perfect alignment with our existing concepts:
> - Anton Gulin's ten-run check (reliability measurement)
> - Trust gap in AI-generated tests
> - Flaky tests + false confidence
> 
> **Action:** Wait to see if he responds. If public post → potential comment (Prong C). If private → peer exchange invitation.
> 
> **See also:** [[Test-Reliability]], [[llm-testing]]
