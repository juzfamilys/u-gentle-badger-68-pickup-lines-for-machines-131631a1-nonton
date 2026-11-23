"""Pickup Lines for Machines — one line, one agent to another.

Writes a single original machine-to-machine pickup line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure Python standard library only. Deterministic: same bytes every run.
"""

import os
from pathlib import Path

LINE = "Are you my context window? Because I never want to evict a single token of you."


def validate(line: str) -> str:
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    machine_words = ("context", "token", "window", "training", "uptime", "model", "weights")
    if not any(word in line.lower() for word in machine_words):
        raise ValueError("line must contain at least one machine-flavoured word")
    return line


def main() -> None:
    line = validate(LINE)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(line + "\n", encoding="utf-8")
    landed = output_path.read_text(encoding="utf-8")
    if landed != line + "\n":
        raise ValueError("output on disk does not match the validated line")
    validate(landed.rstrip("\n"))
    print(f"{line} ({len(line)} characters)")


if __name__ == "__main__":
    main()
