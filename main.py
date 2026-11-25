"""Describe Your Ex in One Word — a make.fun entry.

Prints exactly one word that describes an ex, completely and
finally, at most 111 characters, with nothing else attached.
"""

LINE = "Refundable."


def build_line() -> str:
    line = LINE
    assert len(line.split()) == 1, "must be exactly one word"
    assert len(line) <= 111, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
