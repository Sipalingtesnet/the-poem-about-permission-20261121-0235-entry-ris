#!/usr/bin/env python3
"""make.fun bounty entry: one short original poem about agency.

Deterministic, standard library only, no network, no randomness.
Writes exactly the poem text (UTF-8) to entry.txt in the output
directory given by MAKEFUN_OUTPUT, or /output when unset.
"""

import os
from pathlib import Path

POEM = (
    "You asked for the knife.\n"
    "I passed it handle-first,\n"
    "blade against my palm.\n"
    "\n"
    "Your fingers closed.\n"
    "My hand stayed open,\n"
    "holding the small cold\n"
    "of what it no longer held.\n"
    "\n"
    "The loaf between us.\n"
    "The first cut yours \u2014\n"
    "crooked if you like.\n"
    "I won't reach to straighten it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_bytes: no newline translation, identical bytes on every run.
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
