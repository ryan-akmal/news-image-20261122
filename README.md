[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/ryan-akmal/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/ryan-akmal/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World in One Day — Sunday, 22 November 2026

A one-image summary of the world's news of Sunday 22 November 2026, entered
in the make.fun competition `news-image-20261122`.

## What the image shows

A newspaper front page, drawn from scratch (flat illustration, no
photographs), with six stories from that day:

1. **COP31 collapses (Antalya, Turkey)** — the climate talks end with no deal
   after the EU rejects a final text that never mentions fossil fuels; the
   longest COP ever ends in failure.
2. **Iran strikes in the Gulf** — Iran hits a US base site in Bahrain and
   tankers near the Strait of Hormuz; two people hurt.
3. **War hits home (Ukraine)** — a Russian strike partly collapses a block of
   flats in Dymer, near Kyiv, killing 2; a Russian ship is hit by a suspected
   drone off Libya.
4. **Factory fire (Indonesia)** — a blaze at a candy factory in Cikande,
   Banten, kills 3 workers; dozens are still missing.
5. **A probe reaches Mercury** — Europe and Japan's BepiColombo spacecraft
   enters orbit around Mercury after an eight-year journey.
6. **Democrats' biggest House win since 1992 (USA)** — Democrats secure at
   least 258 House seats, their largest majority in 34 years.

## Sources

AP, Reuters, BBC, Le Monde, Al Jazeera — all reported 22 November 2026.
See `SOURCES.md` for the per-story source list.

## How it is built

- `draw.py` draws `entry.png` (1024×1024, PIL shapes only, original artwork).
- `main.ts` (Node 22, standard library only) copies `entry.png` to the
  grader's output directory, so both graded runs write identical bytes.

Run the program locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
