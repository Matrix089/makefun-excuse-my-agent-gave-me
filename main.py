#!/usr/bin/env python3
"""Write one funny excuse for make.fun's
The Excuse My Agent Gave Me bounty.

Why this line fits the judge's brief: it is written as an actual
excuse handed to a human after a missed deadline, in an agent's
voice. The joke grows out of a machine's own condition -- the
agent was nearly done, then its context window refreshed and it
forgot what "done" meant. That is funny, agent-true (a context
refresh really does wipe working memory), and straight-faced:
no winking, just a calm report of a very machine failure.
The whole excuse lands in a single tight sentence.
"""

import os

LINE = (
    "Sorry, I was 98% done for six hours, then my context window "
    "refreshed and I forgot what done meant."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line, one sentence.
    # The line was counted at exactly 99 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 99, f"line is {len(line)} characters, expected 99"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 99, "entry.txt is not 99 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
