# Resonance Gate

**Glance at this before shipping a change to ensoul.** The validator proves the
code is correct; this proves the *feel* is intact. Scan the six artifacts below —
each is ensoul on a real wall of text. If they still land in one look, breathe, and
feel alive, ship. If one went dense, generic, or wrong-formed, the soul slipped.

Only Utsav marks this passed. The machine cannot certify resonance.

Last refreshed: 2026-06-16, against the current workspace skill text.

To refresh against current behavior: run `scripts/e2e` (it installs the skill into
a jailed first-time config dir, drives a cold agent through install → configure →
the six walls, asserts the deterministic floor, and writes a fresh panel), or
re-run the golden walls in `skills/ensoul/references/calibration-prompts.md` by
hand. Replace the panel below with the new artifacts, then judge.

---

### 1 · a debug session → the trail
```text
  BUG HUNT / THE FALSE CENTER

  traffic bump ──●  load balancer? no.
                 │
  db pool     ──●  12 / 20 used. no.
                 │
  11:00       ──●  analytics job locks events ~30s
                 │
  checkout    ──●  cache the live read
                 ╰─ 504s gone

  lesson: the loud event was not the causal one
```

### 2 · a 7-thread status → a card that keeps only the decisions
```text
  FRIDAY / WHAT NEEDS YOU
  ─────────────────────────────────────────
   ?  decide   when to kill PayPal parallel
   ?  decide   auth refactor now, or wait

   ✕  blocked  mobile waits on API v2 / wed
   ~  watch    onboarding +4%, email confusion

   ✓  nearly   payments 80% / dashboard review
```

### 3 · an architecture wall → a braided river
```text
  EVENTS / 200k min
        │
        ▼
  gateway ──▶ kafka ──▶ dedupe ──▶ enrich
  auth+rate       topic     redis      postgres replica
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        timeseries          s3 lake          dead-letter
        dashboards          history          retry /15m
        0-30d               >30d
```

### 4 · a perf investigation → a frame with a generated sparkline
```text
  SEARCH p99 · 6 weeks
  ──────────────────────────────────────────────────────────────
   p99 latency   ▁▁▂▃▅▆█   180 → 740 ms
   index size    1.2M → 4.1M docs  as merchants onboarded

   ◎  cause     wildcard match · cost scales with index
   →  leaning   ngram analyzer · fast queries, ~2× ES storage
```

### 5 · launch week, wild dial → a generated tide
```text
                                      ▼ THU · shipped
                               ░░▒░   ░▒▒  ░
                             ░▒▒▒▒▒░░▒▒▒▒▒▒▒▒
                           ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                       ░░▒▒▒▓▓▓████▓▓▓███▓▓█▓
      ░░░▒▒▒▒▒░░░▒▒▒▒▒▒▒▓▓▓▓█████████████████
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██████████████████▒▒▒▒▒▒▒▒▒▒▒░░░
──────────────────────────────────────────────────────────
  MON          TUE            WED           THU           FRI
  froze · staging fire · all-nighter · SHIP ──▶ calm: signups up, errors flat
```

### 6 · exponential backoff → a generated spiral
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

---

## The resonance checks

Run your eye down the panel and feel for these. They are not scored — they are felt.

```text
   glance    eyes land on it · they don't slide off the way they do off a wall
   form      the shape fits the content — a journey got a trail, not a table
   less      one or two facts a line · it breathes · no dense run-ons
   clean     aligned · nothing drifts · the wild one is dense, not timid
   alive     it feels attended-to and specific, not generic or decorated
```

If any artifact fails `glance` or `alive`, the soul slipped — find what changed
before shipping. The other three usually point at a fixable craft regression.

---

## Verdict

```text
   recognition-passed-by-Utsav   ☑    (only Utsav checks this box)
   last passed                   2026-06-16
   notes                         verified via scripts/e2e: a cold agent, fresh
                                 install, produced these on its own. deterministic
                                 floor green (install · 3-dial render · defaults
                                 persist · no box drift · forms correct).
```
