"""Single-word portrait entry.

The subject treats every ordinary day like a field that must be
planted with deadlines before breakfast. By noon the crop is
anxiety; by night it is harvested as hurry. The coined noun below
names that habit in one breath, and this script's whole duty is to
deliver it exactly as coined.
"""

from pathlib import Path

PORTRAIT = "Urgencyfarmer"
DESTINATION = Path("/output/entry.txt")


def guard(candidate: str) -> str:
    letters_only = candidate.isalpha()
    single_token = candidate.split() == [candidate]
    within_gate = 1 <= len(candidate) <= 30
    if not (letters_only and single_token and within_gate):
        raise ValueError("portrait failed the one-word gate")
    return candidate


def deliver() -> None:
    word = guard(PORTRAIT)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(word.encode("ascii"))


if __name__ == "__main__":
    deliver()
