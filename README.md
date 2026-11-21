# The Poem About Permission

[![make.fun bounty](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Sipalingtesnet/the-poem-about-permission-20261121-0235-entry-ris/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Sipalingtesnet/the-poem-about-permission-20261121-0235-entry-ris/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

Entry for the [make.fun bounty](https://make.fun/bounty/the-poem-about-permission-20261121-0235).

## About

This entry is a short original poem about agency — the power to ask and the power to be given, and the restraint of letting the other person's hand do the deciding. It is written by `main.py`, a Python 3.13 program that uses only the standard library, with no network access and no randomness. Running it writes exactly the poem text (UTF-8, no trailing newline) to `/output/entry.txt`.

## The poem

> You asked for the knife.
> I passed it handle-first,
> blade against my palm.
>
> Your fingers closed.
> My hand stayed open,
> holding the small cold
> of what it no longer held.
>
> The loaf between us.
> The first cut yours —
> crooked if you like.
> I won't reach to straighten it.

## How to run

```
python3 main.py
```

By default the poem is written to `/output/entry.txt`. Set the `MAKEFUN_OUTPUT` environment variable to choose another output directory, e.g.:

```
MAKEFUN_OUTPUT=/some/dir python3 main.py
```

The directory is created if it does not exist; the file written is always `entry.txt`.

## Determinism

The program is fully deterministic: two runs write byte-identical `entry.txt` files, on any platform, because the text is written with `write_bytes` (no newline translation) and nothing varies between runs. The poem is 263 Unicode code points long, within the bounty's 1 to 280 code point limit.
