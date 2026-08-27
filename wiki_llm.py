#!/usr/bin/env python3
"""
AI QA Wiki LLM — Ingest raw sources → wiki articles + Q&A

Usage:
    python3 wiki_llm.py --ingest <raw_file>              — Process one raw file → wiki
    python3 wiki_llm.py --ingest-all                     — All unprocessed raw files
    python3 wiki_llm.py --missing                        — List raw files without wiki
    python3 wiki_llm.py --ask "question"                 — Q&A from wiki
    python3 wiki_llm.py --ask "question" --save          — Q&A + save to outputs/
    python3 wiki_llm.py --ingest <file> --model groq/llama-3.3-70b  — Use specific model
    python3 wiki_llm.py --update-index                   — Regenerate wiki-topics.json
    python3 wiki_llm.py --update-index --git-push        — Regenerate + push to GitHub
    python3 wiki_llm.py --sync-links                     — Rebuild all backlinks across wiki
    python3 wiki_llm.py --sync-links --git-push          — Sync links + push

Models (cost per 1M tokens):
  openai/gpt-oss-120b     $0.15/$0.60 — cheap, good for ingest (DEFAULT)
  openai/gpt-oss-120b — recommended (llama-3.3 decommissioned Aug 2026)
  openai/gpt-oss-20b      $0.075/$0.30 — fastest, cheapest
"""

import os
import sys
import re
import json
import time
from pathlib import Path
from datetime import datetime

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-oss-120b"

PROJECT_DIR = Path(__file__).parent
RAW_DIR = PROJECT_DIR / "raw"
WIKI_DIR = PROJECT_DIR / "wiki"
OUTPUTS_DIR = PROJECT_DIR / "outputs"
LOG_FILE = PROJECT_DIR / "wiki_llm.log"

# Backlinks section markers (managed by script, do not edit manually)
BACKLINK_HEADING = "### Backlinks"
BACKLINK_MARKER_START = "<!-- backlinks-start -->"
BACKLINK_MARKER_END = "<!-- backlinks-end -->"

SYSTEM_PROMPT_INGEST = """You are a knowledge curator for an AI Testing and QA wiki.
Read the source material and produce a well-structured wiki article.
Write in the same language as the source.
Include: summary, key concepts, practical applications.
Format: clean markdown with sections. Max 500 words.
Do not repeat content verbatim — synthesize and organize.
At the end, add a "### See also" section with wiki-style links to related pages if any are provided below."""

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
        "model": model or DEFAULT_MODEL,
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


def find_relevant_files(query: str, top_n: int = 5) -> list:
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


def wiki_page_summary(path: Path) -> dict:
    """Extract title and short description from a wiki page."""
    content = path.read_text(encoding="utf-8", errors="ignore")
    title = ""
    desc = ""
    for line in content.split("\n"):
        s = line.strip()
        if line.startswith("# ") and not title:
            title = line.lstrip("# ").strip()
        if not desc and s and not s.startswith("#") and not s.startswith("---") and not s.startswith("*"):
            desc = s[:150]
    if not title:
        title = path.stem.replace("-", " ").replace("_", " ").title()
    return {"path": path, "stem": path.stem, "title": title, "desc": desc}


def find_related_wiki_pages(source_text: str, exclude_stem: str = "", max_n: int = 5) -> list:
    """Find existing wiki pages related to source text by keyword matching."""
    words = re.findall(r'\b[a-zа-яё]{4,}\b', source_text.lower())
    stop_words = {
        "this", "that", "with", "from", "have", "been", "will", "they", "their",
        "what", "which", "when", "where", "about", "into", "than", "then",
        "also", "more", "some", "such", "only", "other", "over", "very", "just",
        "these", "those", "after", "before", "should", "could", "would",
        "there", "them", "each", "much", "many", "most", "your", "like",
    }
    word_freq = {}
    for w in words:
        if w not in stop_words:
            word_freq[w] = word_freq.get(w, 0) + 1

    top_keywords = [w for w, _ in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:20]]
    if not top_keywords:
        return []

    query = " ".join(top_keywords)
    relevant = find_relevant_files(query, top_n=max_n)

    result = []
    for f in relevant:
        if exclude_stem and f.stem.lower() == exclude_stem.lower():
            continue
        result.append(wiki_page_summary(f))

    return result


def get_backlinks_content(page_path: Path) -> str:
    """Generate the backlinks section content for a page, scanning all other wiki pages for links to it."""
    links = []
    page_ref = f"(wiki/{page_path.name})"
    for f in sorted(WIKI_DIR.glob("*.md")):
        if f.name == page_path.name:
            continue
        content = f.read_text(encoding="utf-8", errors="ignore")
        if page_ref in content:
            info = wiki_page_summary(f)
            links.append(f"- [{info['title']}](wiki/{f.name})")
    if not links:
        return ""
    return f"\n\n{BACKLINK_MARKER_START}\n{BACKLINK_HEADING}\n" + "\n".join(sorted(links)) + f"\n{BACKLINK_MARKER_END}\n"


def update_backlinks_for_page(page_path: Path):
    """Rebuild the backlinks section for a single page."""
    content = page_path.read_text(encoding="utf-8")
    new_backlinks = get_backlinks_content(page_path)

    # Remove existing backlinks section
    cleaned = content
    if BACKLINK_MARKER_START in cleaned:
        before = cleaned[:cleaned.index(BACKLINK_MARKER_START)]
        after_idx = cleaned.index(BACKLINK_MARKER_END) + len(BACKLINK_MARKER_END)
        after = cleaned[after_idx:]
        cleaned = before + after

    if new_backlinks:
        # Insert before the generated footer
        gen_footer = "\n---\n*Generated by"
        if gen_footer in cleaned:
            insert_pos = cleaned.rfind(gen_footer)
            cleaned = cleaned[:insert_pos] + new_backlinks + cleaned[insert_pos:]
        else:
            cleaned += new_backlinks

    page_path.write_text(cleaned, encoding="utf-8")


def sync_all_backlinks():
    """Rebuild backlinks for all wiki pages."""
    pages = sorted(WIKI_DIR.glob("*.md"))
    print(f"🔗 Syncing backlinks for {len(pages)} pages...")
    count = 0
    for p in pages:
        update_backlinks_for_page(p)
        count += 1
    print(f"✅ Backlinks synced for {count} pages")
    log_run("sync-links", f"{count} pages", "ok")


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

    # Find related wiki pages for cross-linking context
    exclude_stem = raw_to_wiki_name(raw_path)
    related = find_related_wiki_pages(source_text, exclude_stem=exclude_stem)
    crosslink_context = ""
    if related:
        crosslink_context = "\n### Related wiki pages — link to them in a 'See also' section:\n"
        for r in related:
            crosslink_context += f"- `wiki/{r['stem']}.md` — {r['title']}: {r['desc'][:100]}\n"
        print(f"🔗 Found {len(related)} related pages for cross-linking")
    else:
        print("🔗 No related wiki pages found")

    prompt = f"""Transform the following source material into a well-structured wiki article.

Source: {raw_path.name}

Content:
{source_text}

Produce: summary, key concepts, practical applications.
Format as clean markdown with sections.
At the end, add a "### See also" section with wiki-style links to related pages listed below.{crosslink_context}"""

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

    content = f"""---
source: "{raw_path.name}"
ingested: "{datetime.now().strftime('%Y-%m-%d')}"
---

{result}

---
*Source: [raw/{raw_path.name}](../raw/{raw_path.name}) · Generated by wiki_llm.py (Groq)*
"""

    wiki_path.write_text(content, encoding="utf-8")
    print(f"✅ Saved to: wiki/{wiki_name}")
    log_run("ingest", raw_path.name, "ok", f"wiki/{wiki_name}")

    # Add backlinks to related pages
    if related:
        update_backlinks_for_page(wiki_path)
        for r in related:
            update_backlinks_for_page(r["path"])
        print(f"🔗 Backlinks updated for {len(related)} related page(s)")

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
    ingested_paths = []
    for f in missing:
        result = ingest_file(f, model)
        if result:
            ok += 1
            ingested_paths.append(result)
        else:
            fail += 1
    print(f"\n✅ {ok} ingested, ❌ {fail} failed")
    log_run("ingest-all", f"{ok} ok, {fail} fail", "ok")


def update_index():
    """Scan wiki/ and raw/ → generate wiki-topics.json for index.html"""
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

    print(f"🤖 Model: {model or DEFAULT_MODEL}")

    if args[0] == "--missing":
        list_missing()
        return

    if args[0] == "--sync-links":
        sync_all_backlinks()
        if git_push_flag:
            update_index()
            git_push(["wiki/", "wiki-topics.json"], "chore(wiki): sync backlinks")
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
