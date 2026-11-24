"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt (or the path named
by ENTRY_OUT / ENTRY_OUT_DIR when those are set).
"""

import os

VERSES = [
    "Red dot holds its breath",
    "the log lies at half past three",
    "one typo, all night",
]

EXPECTED_SHAPE = (5, 7, 5)
MAX_CHARS = 200

VOWELS = "aeiouy"


def syllables_in_word(word):
    """Count vowel groups in one word, dropping a trailing silent e."""
    cleaned = word.strip(",.").lower()
    groups = 0
    prev_was_vowel = False
    for ch in cleaned:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_was_vowel:
            groups += 1
        prev_was_vowel = is_vowel
    if cleaned.endswith("e") and groups > 1:
        groups -= 1
    return max(groups, 1)


def syllables_in_line(line):
    """Sum the per-word counts across one line of the haiku."""
    return sum(syllables_in_word(w) for w in line.split())


def build_entry():
    if len(VERSES) != 3:
        raise ValueError(f"haiku needs 3 lines, got {len(VERSES)}")
    for verse, want in zip(VERSES, EXPECTED_SHAPE):
        if not verse.strip():
            raise ValueError("haiku line must not be blank")
        got = syllables_in_line(verse)
        if got != want:
            raise ValueError(f"line {verse!r} has {got} syllables, want {want}")
    text = "\n".join(VERSES)
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over {MAX_CHARS}")
    return text


def resolve_output_path():
    if os.environ.get("ENTRY_OUT"):
        return os.environ["ENTRY_OUT"]
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = build_entry()
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
