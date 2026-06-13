#!/usr/bin/env python3
"""
AI QA Wiki LLM — Ingest raw sources → wiki articles + Q&A via Groq

Usage:
    python3 wiki_llm.py --ingest <raw_file>              — Process one raw file → wiki
    python3 wiki_llm.py --ingest-all                     — All unprocessed raw files
    python3 wiki_llm.py --missing                        — List raw files without wiki
    python3 wiki_llm.py --ask "question"                 — Q&A from wiki
    python3 wiki_llm.py --ask "question" --save          — Q&A + save to outputs/
    python3 wiki_llm.py --ingest <file> --model groq/llama-3.3-70b  — Use specific model
    python3 wiki_llm.py --update-index                   — Regenerate wiki-topics.json
    python3 wiki_llm.py --update-index --git-push        — Regenerate + push to GitHub

Models (cost per 1M tokens):
  openai/gpt-oss-120b     $0.15/$0.60 — cheap, good for ingest (DEFAULT)
  llama-3.3-70b-versatile $0.59/$0.79 — best quality, use for Q&A
  openai/gpt-oss-20b      $0.075/$0.30 — fastest, cheapest
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "openai/gpt-oss-120b"

PROJECT_DIR = Path(__file__).parent
RAW_DIR = PROJECT_DIR / "raw"
WIKI_DIR = PROJECT_DIR / "wiki"
OUTPUTS_DIR = PROJECT_DIR / "outputs"
LOG_FILE = PROJECT_DIR / "wiki_llm.log"

SYSTEM_PROMPT_INGEST = """You are a knowledge curator for an AI Testing and QA wiki.
Read the source material and produce a well-structured wiki article.
Write in the same language as the source.
Include: summary, key concepts, practical applications, related topics.
Format: clean markdown with sections. Max 500 words.
Do not repeat content verbatim — synthesize and organize."""

SYSTEM_PROMPT_ASK = """You are an expert in AI Testing and QA.
Answer based on the provided wiki context.
If information is not in context, say so honestly.
Answer concisely (3-5 sentences)."""


def log_run(mode: str, topic: str, status: str, output: str = ""):
    line = f"[{datetime.now().isoformat()}] {mode} | {topic[:80]} | {status} | {output[:80]}"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def get_groq_key():
    key = os.environ.get("GROQ_API_KEY")
    if key:
        return key
    raise ValueError("GROQ_API_KEY not set. Run: export GROQ_API_KEY=$(cat ~/1.groq_ke)")


def ask_llm(prompt: str, system_prompt: str = SYSTEM_PROMPT_INGEST, temperature: float = 0.5, max_tokens: int = 1200, model: str = "") -> str:
    import requests
    headers = {"Authorization": f"Bearer {get_groq_key()}", "Content-Type": "application/json"}
    data = {
        "model": model or GROQ_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    resp = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=120)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def find_relevant_files(query: str, top_n: int = 3) -> list:
    keywords = query.lower().split()
    scores = {}
    for f in list(WIKI_DIR.glob("*.md")):
        try:
            content = f.read_text(encoding="utf-8").lower()
            score = sum(1 for kw in keywords if kw in content)
            if score > 0:
                scores[f] = score
        except:
            pass
    sorted_files = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [f for f, _ in sorted_files[:top_n]]


def build_context(files: list, max_chars: int = 4000) -> str:
    parts = ["# Wiki Context\n"]
    total = 0
    for f in files:
        if total >= max_chars:
            break
        try:
            content = f.read_text(encoding="utf-8")[:max_chars // len(files)]
            parts.append(f"## {f.name}\n{content}\n")
            total += len(content)
        except:
            pass
    return "\n\n".join(parts)


def get_existing_wiki_names() -> set:
    return {f.stem.lower() for f in WIKI_DIR.glob("*.md")}


def raw_to_wiki_name(raw_path: Path) -> str:
    name = raw_path.stem.lower()
    name = re.sub(r'[^a-zа-я0-9_-]', '', name)
    return name


def missing_raw_files() -> list:
    existing = get_existing_wiki_names()
    missing = []
    for f in sorted(RAW_DIR.glob("*")):
        if f.suffix not in (".md", ".txt"):
            continue
        stem = raw_to_wiki_name(f)
        if stem not in existing and stem not in ("sources",):
            missing.append(f)
    return missing


def ingest_file(raw_path: Path, model: str = ""):
    print(f"\n📄 Processing: {raw_path.name}")
    try:
        source_text = raw_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"❌ Failed to read: {e}")
        log_run("ingest", raw_path.name, "error", str(e))
        return None

    wiki_name = raw_to_wiki_name(raw_path) + ".md"
    wiki_path = WIKI_DIR / wiki_name
    if wiki_path.exists():
        print(f"⏭️  Already exists: wiki/{wiki_name}")
        return wiki_path

    if len(source_text) > 8000:
        source_text = source_text[:8000] + "\n\n[...truncated]"

    prompt = f"""Transform the following source material into a well-structured wiki article.

Source: {raw_path.name}

Content:
{source_text}

Produce: summary, key concepts, practical applications, related topics.
Format as clean markdown."""

    import time
    for attempt in range(3):
        print(f"🤖 Generating wiki article...")
        try:
            result = ask_llm(prompt, model=model)
            break
        except Exception as e:
            if "429" in str(e) and attempt < 2:
                wait = 10 * (attempt + 1)
                print(f"⏳ Rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"❌ LLM error: {e}")
                log_run("ingest", raw_path.name, "error", str(e))
                return None

    wiki_name = raw_to_wiki_name(raw_path) + ".md"
    wiki_path = WIKI_DIR / wiki_name

    # Add frontmatter
    content = f"""---
source: "{raw_path.name}"
ingested: "{datetime.now().strftime('%Y-%m-%d')}"
---

{result}

---
*Generated by wiki_llm.py (Groq) — ingested from `raw/{raw_path.name}`*
"""

    wiki_path.write_text(content, encoding="utf-8")
    print(f"✅ Saved to: wiki/{wiki_name}")
    log_run("ingest", raw_path.name, "ok", f"wiki/{wiki_name}")
    return wiki_path


def ask_question(question: str, save: bool = False, model: str = ""):
    relevant = find_relevant_files(question)
    context = ""
    if relevant:
        print(f"📄 Found: {[f.name for f in relevant]}")
        context = build_context(relevant)
    else:
        print("📄 No relevant files found — answering without context")

    prompt = f"""## Wiki Context
{context}

## Question
{question}

Answer concisely (3-5 sentences) using the wiki context."""
    answer = ask_llm(prompt, SYSTEM_PROMPT_ASK, temperature=0.3, max_tokens=500, model=model)
    print(f"\n## Answer\n\n{answer}\n")

    log_run("ask", question, "ok")

    if save:
        OUTPUTS_DIR.mkdir(exist_ok=True)
        fname = f"qa_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.md"
        (OUTPUTS_DIR / fname).write_text(
            f"""---
question: "{question}"
date: "{datetime.now().isoformat()}"
---

# Q: {question}

## A

{answer}

---
*Generated by wiki_llm.py (Groq)*
""", encoding="utf-8")
        print(f"💾 Saved to: outputs/{fname}")
        log_run("ask", question, "saved", f"outputs/{fname}")


def list_missing():
    missing = missing_raw_files()
    if not missing:
        print("✅ All raw files have wiki counterparts")
        return

    print(f"\n📋 Raw files without wiki articles ({len(missing)}):\n")
    for f in missing:
        size = len(f.read_text(encoding="utf-8")) if f.suffix == ".md" else 0
        print(f"  • {f.name}  ({size:,} chars)")
    print(f"\n  → python3 wiki_llm.py --ingest <file>   to process one")
    print(f"  → python3 wiki_llm.py --ingest-all         to process all")


def ingest_all(model: str = ""):
    missing = missing_raw_files()
    if not missing:
        print("✅ All raw files already processed")
        return

    print(f"\n🔄 Processing {len(missing)} raw files...")
    ok, fail = 0, 0
    for f in missing:
        if ingest_file(f, model):
            ok += 1
        else:
            fail += 1
    print(f"\n✅ {ok} ingested, ❌ {fail} failed")


def update_index():
    """Scan wiki/ and raw/ → generate wiki-topics.json for index.html"""
    import json

    topics = []
    for f in sorted(WIKI_DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8", errors="ignore")
        lines = content.split("\n")

        title = ""
        desc = ""
        tag = ""
        for line in lines:
            if line.startswith("# ") and not title:
                title = line.lstrip("# ").strip()
        if not title:
            title = f.stem.replace("-", " ").replace("_", " ").title()
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith("---") and not stripped.startswith("**Last"):
                desc = stripped[:120]
                break

        if f.parent.name != "wiki" and f.parent.name != WIKI_DIR.name:
            tag = f.parent.name.replace("-", " ").title()
        topics.append({
            "file": str(f.relative_to(PROJECT_DIR)).replace(".md", ".html"),
            "title": title,
            "desc": desc or f"{len(content.split())} words",
            "tag": tag or "Wiki"
        })

    raw_count = len(list(RAW_DIR.glob("*")))
    data = {
        "topics": topics,
        "raw_count": raw_count,
        "updated": datetime.now().strftime("%Y-%m-%d")
    }
    dst = PROJECT_DIR / "wiki-topics.json"
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"📋 wiki-topics.json: {len(topics)} topics, {raw_count} raw sources")
    log_run("update-index", f"{len(topics)} topics", "ok")


def git_push(files: list, message: str = ""):
    """Commit and push changes to GitHub"""
    import subprocess
    try:
        subprocess.run(["git", "add"] + files, cwd=PROJECT_DIR, check=True, capture_output=True)
        msg = message or "feat(wiki): ingest raw sources"
        subprocess.run(["git", "commit", "-m", msg], cwd=PROJECT_DIR, check=True, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_DIR, check=True, capture_output=True)
        print(f"🚀 Pushed to GitHub: {msg}")
        log_run("git-push", msg, "ok")
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stderr.decode():
            print("📭 Nothing to commit")
        else:
            print(f"❌ Git error: {e}")
            log_run("git-push", message or "", "error", str(e))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    args = sys.argv[1:]
    git_push_flag = "--git-push" in args
    args = [a for a in args if a != "--git-push"]

    model = ""
    if "--model" in args:
        idx = args.index("--model")
        if idx + 1 < len(args):
            model = args[idx + 1]
        args = [a for a in args if a not in ("--model", model)]

    print(f"🤖 Model: {model or GROQ_MODEL}")

    if args[0] == "--missing":
        list_missing()
        return

    if args[0] == "--ingest-all":
        ingest_all(model)
        if git_push_flag:
            update_index()
            git_push(["wiki/", "wiki-topics.json"], "feat(wiki): ingest all raw sources")
        return

    if args[0] == "--ingest":
        if len(args) < 2:
            print("❌ Specify file: --ingest <raw/filename.md>")
            sys.exit(1)
        path = Path(args[1])
        if not path.is_absolute():
            path = RAW_DIR / path.name
        if not path.exists():
            print(f"❌ File not found: {path}")
            sys.exit(1)
        ingest_file(path, model)
        if git_push_flag:
            update_index()
            git_push(["wiki/", "wiki-topics.json"], f"feat(wiki): ingest {path.name}")
        return

    if args[0] == "--update-index":
        update_index()
        if git_push_flag:
            git_push(["wiki-topics.json"], "chore(wiki): update index")
        return

    if args[0] == "--ask":
        save = "--save" in args
        question = " ".join(a for a in args[1:] if a != "--save")
        if not question:
            print("❌ Enter a question after --ask")
            sys.exit(1)
        print(f"❓ {question}\n")
        ask_question(question, save, model)
        return

    print(__doc__)
    sys.exit(1)


if __name__ == "__main__":
    main()
