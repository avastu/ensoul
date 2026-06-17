# Resonance Gate

**Glance at this before shipping a change to ensoul.** The validator proves the code
is correct; this proves the *feel* is intact. Each panel below is ensoul on a real
wall of text, produced by a **cold agent reading the skill** — install once, then one
form per `/ensoul`. If they still land in one look, breathe, and feel alive, ship. If
one went dense, generic, or wrong-formed, the soul slipped.

Only Utsav marks this passed. The machine cannot certify resonance.

Last refreshed: 2026-06-16 — against the **per-form library** (`forms/<name>.md`,
loaded one at a time at runtime; the whole library read at install). Every artifact
below came from a fresh cold agent that navigated `SKILL.md` → the right form file.

To refresh: re-run the golden walls in `references/calibration-prompts.md` by hand
(one cold agent per form, fresh input, no coaching), or `scripts/e2e`. Replace the
panel, run `recipes/token_cost.py`, then judge.

---

## plain — restraint

### 0 · clean status → the sentence (no artifact is a real output)
```text
  tests green. migration clean. the flaky test is the story.
```

---

## balanced — the everyday forms

### 1 · a debug session → the trail
```text
  MEMORY LEAK / THE OBVIOUS SUSPECT

  image cache  ──●  cleared it. heap unchanged. no.
                │
  ws handlers  ──●  added counters. detaching fine. no.
                │
  modal mount  ──●  subscribes to store, never unsubscribes on close
                │
  cleanup      ──●  unsubscribe on unmount
                ╰─ heap flattened

  lesson: the "obvious" theory held the chair too long
```

### 2 · a 7-thread standup → a card that keeps only what needs you
```text
  MONDAY / WHAT NEEDS YOU
  ──────────────────────────────────────────────────────────
   ?  decide   API redesign — version it, or break clients
   ◆  hold     mobile port — premature; want to wait

   ✕  blocked  QA stalled on staging credentials
   ~  watch    API redesign 60%, no contract decided

   ✓  shipped  data export live, feedback good
```

### 3 · a tradeoff across options → a table ("compared to what?")
```text
  option              durable   ops burden   scale ceiling   lock-in
  ──────────────────────────────────────────────────────────────────
  Redis               ✕         low          high            low
  SQS                 ✓         none          high            HIGH
  Postgres-backed     ✓         low          ~few k/min      none
```

### 4 · several workstreams → progress, magnitude as ink
```text
  year-end goals

  revenue             ██████████████████  110% +
  hiring              ███████████░░░░░░░  60%
  platform migration  █████░░░░░░░░░░░░░  30%
  customer health     ██░░░░░░░░░░░░░░░░  10%
```

### 5 · a series → a generated sparkline
```text
  daily active users — finally catching

  wk-start  ▁▁▁▂▄▅█  now          3.5× in 7 days
            1200          4200
```

### 6 · a system → a braided flow
```text
  WEBHOOK
      │
      ▼
  edge ──▶ queue ──▶ worker ──▶ postgres
  sig verify    SQS/etc   validate + write
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
                  email                  slack
                                │
                    bad payload │
                                ▼
                          dead-letter
                          inspect /day
```

---

## wild — one striking image, the rare exception

### 7 · a felt arc → a generated terrain
```text
  THE QUARTER / IT BUILT AND BUILT, THEN LANDED AND WENT QUIET

                                                 ░
                                               ░░▒░
                                             ░░▒▒▓▒
                                        ░░░░░▒▒▓▓█▓░
                                      ░░▒▒▒▒▒▓▓████▒
                               ░░░░░░░▒▒▓▓▓▓▓██████▓░
                             ░░▒▒▒▒▒▒▒▓▓████████████▒░
                     ░░░░░░░░▒▒▓▓▓▓▓▓▓██████████████▓▒░
               ░░░░░░▒▒▒▒▒▒▒▒▓▓██████████████████████▓▒░░░
░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓█████████████████████████▓▒▒▒░░░░░░
  oct · slow start    nov · overdrive    DEC ▲ close    holidays · quiet
  the surface is the quarter's effort · darkest = December's weight (dark-terminal)
```

### 8 · a day/week with a center → a plate
```text
  +-- PLATE / THE WEEK HAS A CENTER --------------------+
  |   MON    TUE     WED        THU                     |
  |   prep   deck    rehearsal  lock numbers            |
  |     \      \       | \          /                   |
  |      `---.  `---.  dentist `----'                   |
  |           +------------------+                      |
  |           |   BOARD MEETING  |                      |
  |           |     FRIDAY       |                      |
  |           +------------------+                      |
  |   the dentist is wednesday. it just happens.        |
  +-----------------------------------------------------+
```

### 9 · a mechanism → geometry that IS the algorithm
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

### 10 · an act intensifying inward → a calligram (words as paint, void at center)
```text
                      waiting waiting waiting
               waiting hearing hearing hearing hearing
          waiting hearing words words words words hearing
       waiting hearing words meaning meaning meaning words hearing
    waiting hearing meaning FEELING FEELING FEELING meaning hearing
   waiting hearing meaning FEELING PRESENCE PRESENCE meaning words
 waiting hearing meaning                    PRESENCE FEELING words
 waiting words meaning                         PRESENCE meaning words
waiting hearing meaning                         PRESENCE meaning hearing
 waiting words meaning                         PRESENCE meaning words
 waiting hearing meaning                    PRESENCE FEELING words
   waiting hearing meaning FEELING PRESENCE PRESENCE meaning words
    waiting hearing meaning FEELING FEELING FEELING meaning hearing
       waiting hearing words meaning meaning meaning words hearing
          waiting hearing words words words words hearing
               waiting hearing hearing hearing hearing
                      waiting waiting waiting

         an ear built from the act of listening — empty at its own center
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
   recognition-passed-by-Utsav   ☑    (Utsav, 2026-06-16 — "lgtm")
   panel                         2026-06-16 · post per-form-library migration
   gate evidence                 11 cold agents, fresh inputs, each navigated
                                 SKILL → the right forms/ file; plate routing
                                 fixed; render suite green (56 checks).
```
