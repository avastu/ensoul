# Recipe API — call, don't read

`recipes/render.py` is ~4k tokens of source. **You don't need to read it.** This
sheet is the whole calling surface — glance here, then run the generator. Output
is correct by construction; never hand-type what a recipe emits.

```python
python3 -c "import render as r; print(r.<fn>(...))"
```

## Measure (so a closed box can't drift)
- `cells(s) -> int` — render-cell width (NOT len; CJK=2, combining=0).
- `audit(s) -> [chars]` — ambiguous-width glyphs in `s`; `[]` == safe to close a box.

## Magnitude & series
- `hbar(frac, width=24) -> str` — proportional bar, `█`+`░` track. Safe light/dark.
- `spark_block(data, lo=None, hi=None) -> str` — 1 cell/point, 8 levels.
- `spark_braille(data) -> str` — 2 points/cell; dense, turns to noise when small.

## Frames
- `open_frame(title, rows) -> str` — top rule + left rows, NO right border. Cannot
  drift; ship this when any row holds an ambiguous glyph.
- `measured_box(title, lines) -> (str, warns)` — closed `┌─┐`, padded by cells.
  `warns` is non-empty if a glyph may drift → fix it or use `open_frame`.

## Surface
- `surface_width(dial="balanced", surface_cols=None) -> int` — target width; pass
  `tput cols` when known, else conservative default.
- `flow_row(label, path, qualifier=None, width=None) -> str` — flow row that folds
  a crowding qualifier downward instead of running past the edge.

## Wild (one dominant GENERATED image; the facts go in a caption beneath)
- `terrain(series, width=56, height=9) -> str` — value-as-elevation landscape; a
  real series that is ALSO a truthful area chart. Tuned dark-terminal (more ink = deeper).
- `wave(width=56, height=9, envelope="decay") -> str` — shaded waveform; `decay` |
  `crescendo` | `steady`.
- `orb(radius=7, rays=12) -> str` — luminous radial body. Pure beauty (no data).
- `field(fn, width=56, height=12) -> str` — shade any scalar field.
  `fn(nx, ny) -> 0..1` over normalized coords (ripples, gradients, blobs).
- `calligram(gradient, fn, width=74, height=31) -> str` — word-field shaded by
  MEANING. `gradient` = low→high words `["seeing",…,"KNOW"]`. `fn(nx, ny) ->
  intensity 0..1 (which word) or None (blank/void)` — same contract as `field`.
  Blank edge rows auto-cropped. Figures (each returns an `fn`):
  - `fig_eye(pupil=0.30, squash=1.7)` — almond + void pupil; peak rings the pupil.
  - `fig_ring(inner=0.46, outer=1.0)` — annulus; peak rings a hollow center.
  - `fig_spire(base=0.95)` — solid triangle; peak crowns the apex.
  - custom (rightward arrow, tip = peak): `lambda nx,ny: (lambda u=(nx-.5)*2,
    v=(ny-.5)*2: ((u+1)/2) if (u<=.28 and abs(v)<=.20) or (.28<u<=1 and
    abs(v)<=.8*(1-u)/.72) else None)()`
- `exponential_backoff_spiral() -> str` — the fixed golden spiral (widening gaps).

All generators are deterministic (same input → same image; no clock, no random).
Read the source only to change a recipe — not to call one.
