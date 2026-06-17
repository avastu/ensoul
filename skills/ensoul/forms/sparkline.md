# sparkline — a shape you can feel

**Nerve:** a series is a *feeling* before it's a number — watching the suite go
green, latency creeping, signups waking up. **Material:** `spark_block()` — one
cell per point, wide enough to read; put the endpoints as labels so the curve has
scale. (Braille doubles the density but turns to noise when small; reach for it
only with width to spare.) A sparkline lives best *inside* a sentence or a frame,
not alone. Two stacked sparklines show a correlation in one glance.

INPUT
```text
the test suite went from 188 passing on monday to 241 by friday as we backfilled
coverage across the refactor — a steady climb, no big jumps.
```

ENSOUL
```text
  tests turning green

  mon  ▁▂▃▂▄▅▇█  fri
       188       241
```

CALL (this snippet is all you need — no need to read recipe-api.md or render.py)
```bash
python3 -c "import render as r; print(r.spark_block([188,201,209,206,221,230,237,241]))"
# also: r.spark_braille(data) — denser; r.hbar(frac, width) — a magnitude, not a series
```
