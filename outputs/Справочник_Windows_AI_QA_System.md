# Справочник: Windows-based AI QA System

**Дата:** 2026-04-21  
**Статус:** Планируется

---

## Архитектура после развертывания

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows ПК (мощный)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │   Ollama    │    │  BGE-M3    │    │   Qdrant    │      │
│  │  (K2.6)    │    │ (embedding)│    │ (vector DB) │      │
│  └─────┬───────┘    └──────┬─────┘    └──────┬─────┘      │
│        │                   │                   │            │
│        └───────────────────┴───────────────────┘            │
│                         │                                │
│                    API: localhost:11434                  │
│                    API: localhost:8080                   │
│                    API: localhost:6333                   │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                      MacBook                               │
│                                                             │
│  wiki_qa.py ──http──> Windows ПК API                         │
│                     (Groq fallback)                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Компоненты

### 1. Ollama — Локальные LLM

**Установка:**
```powershell
# Скачать с https://ollama.com/download
# Windows: ollama-windows-amd64.exe
```

**Модели для установки:**

| Модель            | Размер | Назначение                   | RAM    |
| ----------------- | ------ | ---------------------------- | ------ |
| `kimi-k2.6:cloud` | ~? GB  | Agentic coding, long-horizon | 32+ GB |
| `llama3.3:70b`    | ~40 GB | Q&A, русский                 | 64 GB  |
| `qwen2.5:14b`     | ~9 GB  | Fast tasks                   | 16 GB  |

**Команды:**
```powershell
ollama pull kimi-k2.6:cloud
ollama pull llama3.3:70b
ollama serve  # запуск сервера
ollama list   # список моделей
```

**API:** `http://localhost:11434`

---

### 2. BGE-M3 — Embeddings + RAG

**Установка:**
```powershell
pip install FlagEmbedding fastapi uvicorn pydantic
```

**Server.py:**
```python
# bge_server.py
from fastapi import FastAPI
from pydantic import BaseModel
from FlagEmbedding import BGEM3FlagModel
from typing import List, Union

model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=False)

app = FastAPI()

class EmbeddingRequest(BaseModel):
    input: Union[str, List[str]]
    model: str = "bge-m3"

@app.post("/v1/embeddings")
def embeddings(req: EmbeddingRequest):
    texts = [req.input] if isinstance(req.input, str) else req.input
    vectors = model.encode(texts, batch_size=8, max_length=8192)['dense_vecs']
    return {
        "object": "list",
        "model": req.model,
        "data": [{"object": "embedding", "index": i, "embedding": v.tolist()} 
                 for i, v in enumerate(vectors)],
        "usage": {"prompt_tokens": 0, "total_tokens": 0},
    }

@app.get("/health")
def health():
    return {"status": "ok", "model": "BAAI/bge-m3"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
```

**Запуск:**
```powershell
python bge_server.py
# или через systemd (см. ниже)
```

**API:** `http://localhost:8080/v1/embeddings`

---

### 3. Qdrant — Vector Database

**Установка:**
```powershell
# Скачать https://github.com/qdrant/qdrant/releases
# Windows: qdrant-x86_64-pc-windows-msvc.zip
```

**Запуск:**
```powershell
./qdrant.exe --data-dir ./qdrant_storage
```

**API:** `http://localhost:6333`

**Dashboard:** `http://localhost:6333/dashboard`

---

## Systemd Unit (опционально)

```ini
# C:\ProgramData\systemd\units\bge-m3.service
[Unit]
Description=BGE-M3 Embeddings Server
After=network.target

[Service]
Type=simple
WorkingDirectory=C:\ai-qa
ExecStart=C:\ai-qa\.venv\Scripts\python.exe bge_server.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

---

## Интеграция с wiki_qa.py

**Текущий код (Groq):**
```python
# wiki_qa.py - текущий
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
```

**Новый код (Ollama):**
```python
# Добавить выбор провайдера
import os

LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "groq")  # "ollama" или "groq"

if LLM_PROVIDER == "ollama":
    url = "http://WINDOWS_PC_IP:11434/api/chat"
    headers = {"Content-Type": "application/json"}
else:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

EMBEDDING_URL = "http://WINDOWS_PC_IP:8080/v1/embeddings"
```

**Environment variables:**
```bash
# .env
LLM_PROVIDER=ollama
OLLAMA_HOST=192.168.1.100  # IP Windows ПК
OLLAMA_MODEL=kimi-k2.6:cloud

EMBEDDING_HOST=192.168.1.100
```

---

## Сколько RAM нужно?

| Конфигурация | Ollama | BGE-M3 | Qdrant | Итого |
|--------------|-------|--------|--------|-------|
| **Минимальная** | 16 GB | 1 GB | 1 GB | **18 GB** |
| **Рекомендуемая** | 32 GB | 1 GB | 2 GB | **35 GB** |
| **Оптимальная** | 64 GB | 2 GB | 4 GB | **70 GB** |

---

## Checklist развертывания

- [ ] Установить Ollama на Windows
- [ ] `ollama pull llama3.3:70b` (или kimi-k2.6)
- [ ] `pip install FlagEmbedding fastapi uvicorn pydantic`
- [ ] Скачать Qdrant для Windows
- [ ] Запустить Qdrant: `./qdrant.exe`
- [ ] Запустить BGE-M3: `python bge_server.py`
- [ ] Проверить: `curl http://localhost:8080/health`
- [ ] Запустить Ollama: `ollama serve`
- [ ] Проверить: `curl http://localhost:11434/api/tags`
- [ ] Обновить wiki_qa.py с выбором провайдера
- [ ] Заполнить .env файл
- [ ] Протестировать RAG pipeline

---

## Тестирование

```powershell
# 1. Ollama
curl http://localhost:11434/api/chat -d '{"model":"llama3.3:70b","messages":[{"role":"user","content":"Привет"}]}'

# 2. BGE-M3
curl -X POST http://localhost:8080/v1/embeddings -H "Content-Type: application/json" -d '{"input":"Привет, мир"}'

# 3. Qdrant
curl http://localhost:6333/collections
```

---

## Troubleshooting

| Проблема | Решение |
|----------|---------|
| Ollama не видит GPU | `ollama run llama3.3:70b --gpu` |
| BGE-M3 медленный | Убрать `use_fp16=True` на CPU |
| Qdrant OOM | Уменьшить `max_workers` в config |
| Нет соединения с Mac | Проверить firewall, открыть порты |

---

## Порты

| Сервис | Порт | Протокол |
|--------|------|---------|
| Ollama | 11434 | HTTP |
| BGE-M3 | 8080 | HTTP (OpenAI-compatible) |
| Qdrant | 6333 | HTTP + gRPC |

---

## Полезные команды

```powershell
# Ollama
ollama list                    # список моделей
ollama ps                      # запущенные
ollama stop llama3.3:70b       # остановить
ollama rm llama3.3:70b         # удалить

# Система
tasklist /FI "MEMTHRESH 10000" # процессы > 10MB RAM
wmic OS get FreePhysicalMemory  # свободная RAM
```

---

## Альтернативы

| Компонент | Альтернатива |
|----------|-------------|
| Ollama | LM Studio, vLLM |
| BGE-M3 | text-embedding-3-large (OpenAI) |
| Qdrant | Chroma, Pinecone |

---

## 🚀 План перспективных установок

### Фаза 1: Минимальная (RAM ~16 GB)

```
Ollama (qwen2.5:14b) + BGE-M3 + Qdrant (in-memory)
```

1. [ ] `ollama pull qwen2.5:14b`
2. [ ] Запустить BGE-M3 server
3. [ ] Qdrant в Docker/in-memory
4. [ ] Настроить wiki_qa.py

**Результат:** Рабочий RAG pipeline на локальном железе

---

### Фаза 2: Средняя (RAM ~32 GB)

```
Ollama (llama3.3:70b) + BGE-M3 + Qdrant (persistent)
```

1. [ ] `ollama pull llama3.3:70b`
2. [ ] Qdrant в persistent mode
3. [ ] Создать коллекцию `ai-qa-wiki`
4. [ ] Индексировать wiki/ файлы
5. [ ] Настроить автозапуск через Scheduled Task

**Результат:** Полноценная база знаний с русским RAG

---

### Фаза 3: Максимальная (RAM ~64 GB)

```
Ollama (kimi-k2.6:cloud) + Agent Swarm
```

1. [ ] `ollama pull kimi-k2.6:cloud`
2. [ ] Настроить Agent Swarm (300 agents)
3. [ ] Подключить MAS-Pipeline (Generator/Critic/Fixer)
4. [ ] Интеграция с Mutation Testing
5. [ ] Prometheus + Grafana мониторинг

**Результат:** Agentic TDD pipeline, 12h coding sessions

---

### Фаза 4: Продакшен (future)

```
Kubernetes cluster + Multi-node RAG + Distributed Training
```

1. [ ] Ollama cluster
2. [ ] Qdrant distributed
3. [ ] Fine-tuning pipeline
4. [ ] CI/CD integration

---

## ⚙️ Настройки для оптимальной производительности

### Ollama

```powershell
# environment variables для Ollama
$env:OLLAMA_NUM_PARALLEL = "4"
$env:OLLAMA_MAX_LOADED_MODELS = "2"
$env:OLLAMA_GPU_OVERHEAD = "1024"
```

```powershell
# config.toml (C:\Users\username\.ollama\config.toml)
numa = true
gpu = true
swap = 4
```

### BGE-M3

```python
# bge_server.py optimizations
vectors = model.encode(
    texts, 
    batch_size=16,          # больше на мощном ПК
    max_length=8192,
    convert_to_numpy=True,
    normalize_embeddings=True
)
```

### Qdrant

```yaml
# config.yaml
storage:
  storage_path: ./qdrant_storage
  snapshots_path: ./snapshots
  
service:
  host: 0.0.0.0
  http_port: 6333
  grpc_port: 6334
  
cluster:
  enabled: false  # включить для distributed
```

### Windows optimizations

```powershell
# PowerShell (Admin)
# 1. Отключить Hyper-V если используется много RAM
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All

# 2. Увеличить page file
# System Properties → Advanced → Performance Settings → Advanced → Virtual Memory

# 3. GPU drivers для Ollama
# Установить CUDA Toolkit если Nvidia
nvidia-smi  # проверить
```

---

## 📊 Ожидаемая производительность

| Конфигурация | Модель | Tokens/sec | RAM | Latency |
|--------------|--------|-----------|-----|---------|
| Минимальная | qwen2.5:14b | ~30 | 16 GB | ~500ms |
| Средняя | llama3.3:70b | ~15 | 32 GB | ~1s |
| Максимальная | kimi-k2.6 | ~50 | 64 GB | ~200ms |

### Embeddings speed

| Режим | CPU | GPU |
|-------|-----|-----|
| Dense | ~120ms | ~12ms |
| Sparse | ~150ms | ~15ms |
| Multi-vector | ~200ms | ~20ms |

---

## 🔗 Следующие шаги

1. [ ] Проверить RAM на Windows ПК
2. [ ] Скачать Ollama для Windows
3. [ ] Скачать Qdrant
4. [ ] Установить Python зависимости
5. [ ] Первый запуск BGE-M3
6. [ ] Протестировать Ollama
7. [ ] Запустить Qdrant
8. [ ] Индексировать wiki
9. [ ] Обновить wiki_qa.py

---

## 📞 Quick Reference

```powershell
# Быстрый старт
ollama serve
python bge_server.py
./qdrant.exe --data-dir ./qdrant_storage

# Проверка
curl http://localhost:11434/api/tags
curl http://localhost:8080/health
curl http://localhost:6333/collections
```

---

## Ресурсы

- [Ollama](https://ollama.com/)
- [BGE-M3 на HuggingFace](https://huggingface.co/BAAI/bge-m3)
- [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)
- [Qdrant](https://qdrant.tech/)

---

*Обновлено: 2026-04-21*