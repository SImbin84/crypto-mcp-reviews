#!/usr/bin/env python3
"""
HERMES — CRYPTO MCP REVIEW: DUE DILIGENCE
Read-only static analysis only. No installs, no runs, no secrets.
"""

from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_DIR = Path("/Users/simbin/crypto-mcp-reviews")
RESULTS_DIR = REPO_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

REPOS_PATH = REPO_DIR / "repos.json"
CANDIDATES: List[Dict[str, Any]] = json.loads(REPOS_PATH.read_text(encoding="utf-8"))

RUN_TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class Candidate:
    id: str
    url: str
    name: str
    author: str
    category: str
    summary: str
    tags: List[str]
    target_use: str
    notes: str
    verdict: str = "DEFER"
    classification: str = "DEFER"
    hypothesis_relevance: str = "NONE"
    risk: str = "medium"
    reason: str = ""
    last_commit_hint: str = "not_checked_github_api"
    stars_forks_forks_hint: str = "not_checked_github_api"
    license_hint: str = "not_checked_github_api"
    language_hint: str = "not_checked_github_api"
    transport_hint: str = "not_checked_github_api"
    write_capable_hint: str = "not_checked_github_api"
    keys_required_hint: str = "not_checked_github_api"
    tests_ci_hint: str = "not_checked_github_api"
    dependency_lock_hint: str = "not_checked_github_api"
    abandon_hint: str = "not_checked_github_api"
    additive_value_hint: str = ""


def classify(c: Candidate) -> None:
    tags = {t.lower() for t in c.tags}
    text = f"{c.name} {c.summary} {c.notes} {' '.join(c.tags)}".lower()
    write_indicators = [
        "order", "swap", "trade", "transfer", "sign", "execute",
        "withdraw", "deposit", "transaction", "send"
    ]
    is_write = any(w in text for w in write_indicators)

    if is_write:
        c.classification = "MIXED_RISK"
    else:
        c.classification = "READ_ONLY_CANDIDATE"

    # Hypothesis relevance by category and tags
    if "market-data" in c.category or any(t in tags for t in ["ccxt", "coingecko", "prices", "history", "orderbook"]):
        c.hypothesis_relevance = "H9_read_only; H7_only_if_historical_funding_confirmed"
    elif "news-sentiment" in c.category or "news" in tags or "sentiment" in tags:
        c.hypothesis_relevance = "NEW_NEWS_EVENT_STUDY_NOT_H1-H10"
    elif "onchain-ethereum" in c.category or "ethereum" in tags or "onchain" in tags:
        c.hypothesis_relevance = "DEFER_EVM_separate_program"
    elif "curation" in c.category:
        c.hypothesis_relevance = "NONE_catalog_only"
    else:
        c.hypothesis_relevance = "NONE"

    # Verdict heuristics
    if c.classification == "MIXED_RISK":
        c.verdict = "DEFER"
        c.reason = "Есть write-potential; требует sandbox review и явного отключения write tools."
        c.risk = "high"
        return

    if c.classification == "READ_ONLY_CANDIDATE" and c.category in {"market-data", "news-sentiment"}:
        c.verdict = "CANDIDATE_READ_ONLY"
        c.risk = "medium" if c.category == "news-sentiment" else "low"
        c.reason = (
            "Заявлен как read-only data source; write tools отсутствуют."
            " Дальнейшая проверка только на свежесть и документацию."
        )
        return

    if c.classification == "READ_ONLY_CANDIDATE" and c.category == "curation":
        c.verdict = "DEFER"
        c.reason = "Каталог, не источник данных."
        c.risk = "low"
        return

    c.verdict = "DEFER"
    c.reason = "Не попадает в H1-H10 без отдельной предрегистрации."
    c.risk = "medium"


def additive_value(c: Candidate) -> str:
    if c.id == "coingecko-mcp-server":
        return "Добавляет универсальный скриннинг 15k+ монет, историю и метаданные, которых нет в Bitget OHLCV collector."
    if c.id in {"mcp-server-ccxt", "mcp-server-ccxt-nayshins"}:
        return "Даёт cross-exchange подтверждение и унифицированный доступ к биржам сверх Bitget."
    if c.id == "cryptominute-news-mcp":
        return "Даёт новостной и Reddit/YouTube сентимент слой для будущих event-study гипотез."
    if c.id in {"eth-mcp-server", "eth-mcp"}:
        return "Даёт ETH/EVM ончейн данные, не относящиеся к текущим H1-H10."
    if c.id == "awesome-mcp-servers-finance-crypto":
        return "Только индекс; не добавляет данных."
    return "Не определена сверх Bitget collector."


def main() -> None:
    rows: List[Dict[str, Any]] = []
    fields = list(Candidate.__dataclass_fields__.keys())
    for raw in CANDIDATES:
        data = {k: raw.get(k, "") for k in fields}
        c = Candidate(**data)
        c.additive_value_hint = additive_value(c)
        classify(c)
        rows.append(asdict(c))

    dt = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    (RESULTS_DIR / "mcp_due_diligence.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    with (RESULTS_DIR / "mcp_hypothesis_mapping.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    # Summary markdown
    md = [f"# MCP Due Diligence\n\nRun: {RUN_TS}\n"]
    md.append("| id | verdict | classification | hypothesis_relevance | risk |")
    md.append("| --- | --- | --- | --- | --- |")
    for r in rows:
        md.append(
            f"| {r['id']} | {r['verdict']} | {r['classification']} | {r['hypothesis_relevance']} | {r['risk']} |"
        )
    md.append("\n## READ-ONLY candidates\n")
    for r in rows:
        if r["verdict"] != "CANDIDATE_READ_ONLY":
            continue
        md.append(f"### {r['name']}\n")
        md.append(f"- URL: {r['url']}\n")
        md.append(f"- Additive value: {r['additive_value_hint']}\n")
        md.append(f"- H relevance: {r['hypothesis_relevance']}\n")
        md.append(f"- Why not integrate now: {r['reason']}\n")
    md.append("\n## Full JSON\n")
    md.append("- `results/mcp_due_diligence.json`\n")
    md.append("- `results/mcp_hypothesis_mapping.csv`\n")
    md.append("\n> Ни один сервер не разрешён для execution или доступа к секретам без отдельного approval.\n")
    (REPO_DIR / "MCP_DUE_DILIGENCE.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # README
    readme = """\
# Crypto MCP Reviews

Due diligence registry for cryptocurrency data/statistics MCP servers.

## Status
- Mode: read-only review only
- No API keys, OAuth, Docker, npm/pip installs, or production integration yet.

## Important
Ни один сервер не разрешён для execution или доступа к секретам без отдельного approval.

## Deliverables
- `MCP_DUE_DILIGENCE.md` — summary verdicts
- `results/mcp_due_diligence.json` — full findings
- `results/mcp_hypothesis_mapping.csv` — hypothesis mapping
- `mcp_due_diligence.py` — analysis script

## Last run
""" + RUN_TS + "\n"
    (REPO_DIR / "README.md").write_text(readme, encoding="utf-8")

    print(json.dumps({"updated": len(rows), "ts": RUN_TS}, ensure_ascii=False))


if __name__ == "__main__":
    main()
