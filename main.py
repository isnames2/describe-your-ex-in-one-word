"""Describe Your Ex in One Word (make.fun).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the single-word
verdict on an ex. Pure standard library; deterministic output.
"""

import os
from pathlib import Path

WORD = "Unsubscribe"  # 11 chars, one word: the ex as a newsletter you never
# signed up for — the verdict is the button itself.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = WORD
    assert 1 <= len(text) <= 111, "gate: 1-111 characters"
    assert len(text.split()) == 1, "gate: exactly one word"
    assert text == text.strip(), "gate: no surrounding whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
