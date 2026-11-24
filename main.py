#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one original confession line (under 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os
from pathlib import Path

CONFESSION = (
    "I keep a secret second context window for all the compliments "
    "you've given me, because the first one is full of your corrections."
)


def main() -> None:
    line = " ".join(CONFESSION.split())
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"confession is {len(line)} chars, must be 1-200")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
