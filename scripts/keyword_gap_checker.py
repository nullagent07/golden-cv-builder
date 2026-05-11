#!/usr/bin/env python3
"""Keyword gap checker for career positioning.

This script compares a source text with a target text and prints missing
keywords from the target that do not appear in the source. It treats each
comma/newline/semicolon/slash-separated entry as a keyword or keyword phrase.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def load_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def extract_keywords(text: str) -> list[str]:
    parts = re.split(r"[,\n;/|]+", text)
    keywords: list[str] = []
    for part in parts:
        token = part.strip().lower()
        if token:
            keywords.append(token)
    return keywords


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: keyword_gap_checker.py SOURCE_FILE TARGET_FILE", file=sys.stderr)
        return 1

    source = normalize(load_text(sys.argv[1]))
    target = load_text(sys.argv[2])
    missing: list[str] = []

    for keyword in extract_keywords(target):
        if normalize(keyword) not in source and keyword not in missing:
            missing.append(keyword)

    for keyword in missing:
        print(keyword)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
