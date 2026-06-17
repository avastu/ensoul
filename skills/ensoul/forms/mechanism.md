# mechanism — geometry that IS the algorithm (wild)

**Nerve:** a mechanism isn't "a few steps" — its *shape* carries why it works.
Exponential backoff is a *widening gap*; a rate limiter is a *vessel that refills*.
**Material:** a generated image whose geometry is the truth, not decoration — the
gold pair for **striking + faithful**. Only on the `wild` dial; the picture is
memorable because it is the mechanism. Facts in a caption beneath; figurative image,
no right border, can't drift.

INPUT
```text
an API call fails. retry after 1 second, then 2, then 4. stop when it succeeds, or
give up after the fourth attempt. each wait is twice the last, so the system gives
the dependency more room to recover.
```

ENSOUL
```text
  EXPONENTIAL BACKOFF

               ▓▓▓▓▓▓▓▓▓▓▓
           ▓▓ 4          ▓▓▓▓
         ███                ▓▓▓
       ███                    ▓▓▓
      ██            ░░░         ▓
     ██         ░░◂░░ ░░░░       ▓
     █         ▒░   .... ░░      ▓
    ██         ▒   ..  .. ░      ▓
    █          ▒   :    1 :      ▓
    █          3   :: 2 :::     ▓▓
    █          ▒▒              ▓▓
    ██          ▒▒▒         ▒▒▒
     █            ▒▒▒▒▒▒▒▒▒▒▒
     ██
      ██
       ███
         ███
           ███
              ████                >
                  ██████>█████████

  fail 1      retry 2      retry 3      retry 4
     │           │            │            │
     └─ wait 1s ─┴─ wait 2s ──┴─ wait 4s ──┴─> success or give up
        the gaps widen; that widening is the backoff
```

CALL (this snippet is all you need — no need to read recipe-api.md or render.py)
```bash
python3 -c "import render as r; print(r.exponential_backoff_spiral())"
# for a NEW mechanism, write its geometry as r.field(fn) or r.calligram(...);
# the rule is the same — make the shape BE the algorithm, not a label on it.
```
