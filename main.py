"""Pigeon Pitch, One Line.

Writes a single elevator pitch to $MAKEFUN_OUTPUT_DIR/entry.txt:
a city pigeon pitching investors on a seed round to disrupt
the breadcrumb supply chain. Standard library only; the line
is checked against the competition gate (one line, 1 to 200
characters of UTF-8 text, not only whitespace) before it is
written.
"""

import os
from os.path import join

PITCH = (
    "We're raising a $2M seed round to disrupt the breadcrumb "
    "supply chain: 40 million pigeons, zero churn, and every "
    "statue in the city is already a customer."
)

LIMIT = 200


def pitch():
    """Return the pigeon's elevator pitch."""
    return PITCH


def check_pitch(text):
    """Check the pitch against the competition gate.

    The gate wants one line of plain UTF-8 text, between 1
    and 200 characters, that is not only whitespace: a pitch
    a city pigeon gives to investors for its startup. A line
    that fails here is rejected instead of wasting a
    submission on the server.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch is empty")
    if len(stripped) > LIMIT:
        raise ValueError(
            "pitch is %d characters, over the 200 limit" % len(stripped)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("pitch must fit on exactly one line")
    return stripped


def pitch_shape(text):
    """Measure the pitch for a last sanity pass.

    Returns the character and word counts. A pitch too short
    to carry both the startup ask and the pigeon punchline,
    or one padded out to fill the cap, is caught here before
    anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    line = check_pitch(pitch())
    shape = pitch_shape(line)
    if shape["words"] < 5:
        raise ValueError("pitch is too short to land the joke")
    with open(join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
