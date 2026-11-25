"""One-word portrait, second planting.

Some managers water the calendar until the whole team wilts.
Every quiet week gets seeded with a fresh alarm, and by Friday
the harvest is a room full of people sprinting in place.
The noun below is that grower, named in a single breath.
This program's only job is to set the word down exactly.
"""

from pathlib import Path

WORD = "Panicfarmer"
TARGET = Path("/output/entry.txt")


def check(word: str) -> bytes:
    if word.split() != [word]:
        raise ValueError("entry must be a single word")
    if not word.isalpha():
        raise ValueError("entry must be letters only")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry outside the 1-30 character gate")
    return word.encode("ascii")


def main() -> None:
    payload = check(WORD)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(payload)


if __name__ == "__main__":
    main()
