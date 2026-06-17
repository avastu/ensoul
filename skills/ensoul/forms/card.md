# card — where the work stands

**Nerve:** the state of a thing at a glance — and, when there are many threads,
*triage*: what needs **you** versus what's just moving. A card sorts by demand-on-you,
which a flat status buries. **Material:** an open frame (`open_frame()`) — an ASCII
label column carries it, glyphs are accent, no right border to drift. One or two
things per line; a blank line for air. Use the canonical marks: `?`/`◆` decide ·
`✕` blocked · `~` watch · `✓` nearly. (A *sequence* wants a trail, not a card.)

INPUT
```text
status friday. payments migration ~80% — stripe cut over but old paypal path still
parallel, undecided when to kill it. new onboarding shipped, conversion +4% but 3
tickets on confusing email verify. mobile blocked on API v2, ETA wed. auth service
tech debt piling up, two engineers want to refactor, worried about launch timing.
dashboard basically done, needs design review. two onsites next week.
```

ENSOUL
```text
  FRIDAY / WHAT NEEDS YOU
  ─────────────────────────────────────────
   ?  decide   when to kill PayPal parallel
   ?  decide   auth refactor now, or wait

   ✕  blocked  mobile waits on API v2 / wed
   ~  watch    onboarding +4%, email confusion

   ✓  nearly   payments 80% / dashboard review
```

CALL (optional — the frame is generated, so the rule can't drift)
```bash
python3 -c "import render as r; print(r.open_frame('FRIDAY / WHAT NEEDS YOU', [' ?  decide   when to kill PayPal parallel', ' ✕  blocked  mobile waits on API v2 / wed']))"
```
