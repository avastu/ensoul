# calligram — a word-field shaded by meaning (wild)

**Nerve:** the felt point is an *act intensifying toward a center* — attention,
knowing, presence, a spiral inward. **Material:** `calligram(gradient, fn)` — the
WORDS are the paint; their vocabulary climbs a semantic gradient by position
(`seeing → look → gaze → watch → KNOW`), and the peak word rings a **void**. That's
the move's whole power: the most intense word surrounds an absence. Only on the
`wild` dial. The gradient must be *real* — if the words don't actually intensify,
it's decoration and a plainer form wins. Figurative image, no right border, all-ASCII.

INPUT
```text
the whole practice is just attention. you start scattered — noticing, then you
actually look, then you're absorbed, then for a moment there's just awareness with no
'you' watching. then you scatter again.
```

ENSOUL
```text
                      seeing seeing see see seeing
               seeing see see look look look see see seeing
          seeing see look look read read read read look see
       seeing see look read gaze gaze gaze gaze gaze read look
    seeing see look gaze watch watch SEE SEE watch gaze read look
   seeing look read gaze SEE SEE KNOW KNOW KNOW SEE watch read look
 seeing look read watch SEE                 KNOW SEE watch read look
 seeing look read watch                        KNOW SEE watch read see
seeing look read watch                          KNOW SEE watch read see
 seeing look read watch                        KNOW SEE watch read see
 seeing look read watch SEE                 KNOW SEE watch read look
   seeing look read gaze SEE SEE KNOW KNOW KNOW SEE watch read look
    seeing see look gaze watch watch SEE SEE watch gaze read look
       seeing see look read gaze gaze gaze gaze gaze read look
          seeing see look look read read read read look see
               seeing see see look look look see see seeing
                      seeing seeing see see seeing
```

An eye built from the act of seeing — knowing nothing at its own center.

**GENERATE it — never hand-type a calligram.** By hand it flails into noise and the
void won't hold; the generator places every word by render-cell. Call the snippet
(below); for a new shape, write a custom `fn`, don't hand-place words.

CALL (this snippet is all you need — no need to read recipe-api.md or render.py)
```bash
python3 -c "import render as r; print(r.calligram(['seeing','see','look','read','gaze','watch','SEE','KNOW'], r.fig_eye()))"
# figures: r.fig_eye() · r.fig_ring() (hollow center) · r.fig_spire() (apex) ·
# or your own fn(nx,ny)->intensity 0..1 or None, peak words ringing a void.
```
