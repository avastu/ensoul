# table — a tradeoff across options ("compared to what?")

**Nerve:** a decision across options weighed on a few axes — the honest home for
"compared to what?", because the eye reads *down* a column. **Material:** aligned
columns + one header rule. **Measure the columns** (`cells()`, render-cells not
`len`) or the rule and rows drift; keep to ≤4–5 columns. Visual weight matches
evidence — let the loud marks (a CAPS `HIGH`, an `✕`) fall only on the real risk,
not on every cell.

INPUT
```text
we've got three ways to kill the 504s. cache the read — cheap, low-risk, fully
reversible. rewrite the query — more effort, medium risk, still reversible. or drop
the nightly analytics job — easy, but high-risk and basically not reversible since
downstream reports depend on it.
```

ENSOUL
```text
  fix path           effort   risk   reversible
  ─────────────────────────────────────────────
  cache the read     low      low    ✓
  rewrite query      high     med    ✓
  drop nightly job   low      HIGH   ✕
```

VERIFY (so columns and rule hold)
```bash
python3 -c "import render as r; print([r.cells(c) for c in ['cache the read','rewrite query','drop nightly job']])"
# align each column to its widest cell; one header rule spanning the row.
```
