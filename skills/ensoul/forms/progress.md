# progress — several magnitudes, felt as ink

**Nerve:** magnitude across several workstreams — who's near done, who's behind —
felt as ink in one glance, not read as four numbers. **Material:** stacked
`hbar()`; measure the label column so every bar starts on the same edge. `█` + the
track read safely in both light and dark themes. The percentages ride along as the
evidence drawer. Order by importance, not by progress, so the headline isn't buried.

INPUT
```text
launch readiness check. payments at 80%, onboarding done (100%), mobile still
behind at 25%, dashboard nearly there around 90%.
```

ENSOUL
```text
  launch readiness

  payments    ██████████████░░░░  80%
  onboarding  ██████████████████  100%
  mobile      ████░░░░░░░░░░░░░░  25%
  dashboard   ████████████████░░  90%
```

CALL (this snippet is all you need — no need to read recipe-api.md or render.py)
```bash
python3 -c "
import render as r
items=[('payments',.80),('onboarding',1.0),('mobile',.25),('dashboard',.90)]
w=max(r.cells(l) for l,_ in items)
for l,f in items: print(f'  {l}{chr(32)*(w-r.cells(l))}  {r.hbar(f,18)}  {round(f*100)}%')
"
```
