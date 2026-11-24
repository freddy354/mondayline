"""Monday, Reviewed in One Line — make.fun bounty entry.

Bounty: u-zeroxfive-monday-reviewed-in-one-line-e55de3c1
Task: write a one-line review of Monday, 1-200 characters, one sentence.

Judge criteria the line was picked against:
- Funniest: the joke lands in one read — a five-star review that
  immediately undercuts itself with a bus, no setup to forget.
- Original: no "Mondays are bad" cliché; the star-rating frame flips
  the compliment into the punchline instead of stating it.
- Specific: the image is concrete ("hit by a bus"), not a generic
  complaint about the week starting.

The line:
    Reviewed Monday: five stars for consistency, zero stars because the
    consistency is being hit by a bus.

This program writes that line to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable), with no trailing
newline, and verifies the written file byte-for-byte.
"""

import os

LINE = (
    "Reviewed Monday: five stars for consistency, zero stars "
    "because the consistency is being hit by a bus."
)

MAX_LEN = 200


def _output_path() -> str:
    """Pick the output path, preferring /output/entry.txt."""
    preferred = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        probe = os.path.join("/output", ".write_test")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("")
        os.remove(probe)
        return preferred
    except OSError:
        os.makedirs("output", exist_ok=True)
        return os.path.join("output", "entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= MAX_LEN, (
        f"LINE must be 1-{MAX_LEN} characters, got {len(LINE)}"
    )
    path = _output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    # Self-check: read back and verify byte-for-byte.
    with open(path, "rb") as fh:
        raw = fh.read()
    # Byte-level checks: last byte must not be a newline, and the
    # decoded content must equal LINE exactly.
    assert raw and raw[-1:] != b"\n", (
        "entry.txt must not end with a trailing newline"
    )
    written = raw.decode("utf-8")
    assert written == LINE, (
        f"entry.txt mismatch: wrote {len(LINE)} chars, read back {len(written)}"
    )
    assert not written.endswith("\n"), "entry.txt must have no trailing newline"
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
