#!/usr/bin/env python3
"""Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (program/v1 harness).

The excuse is one line, under 200 characters, built as a 3-beat joke:
setup (a 'quick 5-minute fix'), escalation (a function with 47 callers),
punchline (the only guard was a comment that says 'do not touch') —
the warning was in the code all along, and the developer ignored it.
"""
import os
from pathlib import Path

EXCUSE = "My 'quick 5-minute fix' touched a function with 47 callers and a comment that just says 'do not touch'."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    target.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
