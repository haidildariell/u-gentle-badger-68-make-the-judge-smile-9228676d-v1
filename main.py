"""Make the Judge Smile — one warm, surprising line about a small good thing today."""

import os

LINE = "The stray cat that hissed at me all month left a wet leaf on my doormat this morning, like rent paid in full."

MAX_CHARS = 200


def validate_line(text):
    """A line only counts if it is real text inside the 200-character cap."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only white space")
    if len(cleaned) > MAX_CHARS:
        raise ValueError("line exceeds 200 characters")
    return cleaned


def write_entry(text, output_dir):
    """Write one validated line to entry.txt inside output_dir."""
    line = validate_line(text)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(LINE, output_dir)


if __name__ == "__main__":
    main()
