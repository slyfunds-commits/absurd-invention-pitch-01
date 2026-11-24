"""One-Sentence Absurd Invention Pitch — entry program.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt, then verifies the file
immediately (the grader runs python:3.13-slim, stdlib only).

Craft: the laugh lives in the invention's own mechanism (a lamp that
dims when you lie), the last word does the work ("dessert" reframes
the whole family meal as a sequence of lies), and the reader completes
the step the sentence leaves out. One concrete act, one hidden fact.
"""

import os

ENTRY = "A lamp that dims a little every time you lie, so the room goes dark by dessert."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes do not match"
    assert written == ENTRY, "entry.txt does not match the entry"
    assert 1 <= len(written) <= 220, "entry must be 1-220 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert written.count(".") == 1 and written.endswith("."), "entry must be one sentence"


if __name__ == "__main__":
    main()
