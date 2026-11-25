"""Emit the chosen portrait word for the one-word bounty.

The human behind this entry runs a calendar like farmland: urgency
is sown early, tended daily, and harvested as panic by evening.
One coined noun carries that whole portrait, so the program's only
job is to place it, untouched, where the grader looks for it.
"""

from pathlib import Path

WORD = "Urgencyfarmer"
TARGET = Path("/output/entry.txt")


def check(word: str) -> None:
    if not word.isalpha():
        raise ValueError("portrait must be letters only")
    if any(ch.isspace() for ch in word):
        raise ValueError("portrait must be a single word")
    if not 1 <= len(word) <= 30:
        raise ValueError("portrait length outside the gate")


def emit(word: str, target: Path) -> None:
    check(word)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(word.encode("ascii"))


if __name__ == "__main__":
    emit(WORD, TARGET)
