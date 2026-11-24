# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/yudhisutawan77/makefun-haiku-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/yudhisutawan77/makefun-haiku-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging, written for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on make.fun.

## The haiku

> Red dot holds its breath
> the log lies at half past three
> one typo, all night

Three lines, 5-7-5 syllables, 76 characters — a breakpoint waiting, a log line
that cannot be trusted at half past three, and the turn: the whole night was
one typo.

## What `main.py` does

`main.py` holds the haiku in `VERSES`, checks each line against the 5-7-5
syllable shape with a small vowel-group counter, checks the whole text stays
under the 200-character limit, then writes it to `/output/entry.txt`
(or the path in `ENTRY_OUT` / `ENTRY_OUT_DIR` when set).

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
