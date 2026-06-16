# Materials Gallery

Worked examples are how a model learns ensoul: at generation time you reach for
the nearest example you have seen and imitate it. So each one here is **verified**
(generated with `recipes/render.py`, not hand-typed), shows **the move** (the
nerve, the material, why), and breathes.

These render what a Claude Code user actually has in front of them — a debugging
session, a diff, project state, a coding day — with the warmth and shape of the
README's life examples. The trick: **a coding session is already a journey.** That
is why the trail lands; lean into it. Read top-down — the home is small (a
sentence, a card), each entry steps one notch out, and the wild plates/images
are the *rare* exception. Stop at the first form that lands. When in doubt, give
less.

Lineage to keep alive while imitating these examples:

- **Rick Rubin:** subtract until one true thing remains. A small sentence, a trail
  with one lesson, or a card with only the decisions is often stronger than a
  clever plate.
- **Ruth Asawa:** let line, loop, air, and shadow carry relationships. When a
  structure wants delicacy, use rails, loops, nested paths, and negative space
  instead of heavier labels.

---

## Golden pairs — input → ensoul

These are the clearest teaching examples. Read them as transformations, not just
forms: the output keeps the truth, removes the wall, and lets line/air carry what
paragraphs were carrying.

### Debug wall → trail

INPUT
```text
Sure — I dug into the intermittent 504s from this morning. My first guess was
that the load balancer timeout had become too aggressive, especially because the
errors appeared around the same time as the traffic bump, so I spent about an
hour tuning nginx and rechecking the gateway, but that did not change the error
rate. I then suspected the DB pool was exhausting, so I added some logging around
checkout and the pool looked healthy, around 12 of 20 connections in use. The
actual pattern showed up around 11: the 504s line up with the nightly analytics
job, not traffic. That job locks the events table for about 30 seconds, and
checkout was reading that table live. I cached that read and the 504s disappeared.
Main lesson: I anchored too hard on the traffic theory because it was the loudest
event, but it was not the causal one.
```

ENSOUL
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

### Status wall → decision card

INPUT
```text
Here is the Friday status. The payments migration is roughly 80% complete: Stripe
is cut over, but the old PayPal path is still running in parallel and we have not
decided when to remove it. The new onboarding flow shipped and looks positive so
far, with conversion up about 4%, though there are three support tickets about
the email verification step being confusing. Mobile is currently blocked on the
API v2 endpoints, with an ETA of Wednesday. The auth service tech debt is also
piling up; two engineers want to refactor it now, but I am worried about doing
that this close to launch. The dashboard is basically done but still needs design
review. Also noting that we have two onsite interviews next week.
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

### Architecture wall → braided flow

INPUT
```text
At a high level, the event ingestion system works like this. Events enter through
the API gateway, which handles auth and rate limiting, and then they are placed
onto a Kafka topic. A fleet of consumers reads from Kafka, dedupes events by id
against Redis, enriches them from the Postgres replica, and writes the results to
two destinations: the timeseries store for dashboards and S3 for the lake. If
enrichment fails, the event goes to a dead-letter topic and is retried every 15
minutes. Dashboards read recent data from the timeseries store, while history
older than 30 days is queried from S3 through Athena. Peak volume is around
200k events per minute.
```

ENSOUL
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

---

## The shelf

Each material has a grain — resolution, robustness, register. Match it to the job;
generate the fragile ones rather than hand-typing.

| material | res | robust | register | best at |
| --- | --- | --- | --- | --- |
| **type + whitespace** CAPS · indent · air | low | total | calm, editorial | structure, hierarchy, the spine |
| **rules + rails** `─ │ ├ └` | low | high¹ | architectural | grouping, frames, flow |
| **block shading** `░ ▒ ▓ █ ▀ ▄ ▌ ◢ ◣` | med | high² | weight, mass, light | **magnitude as ink**, gradient, the wild image |
| **braille field** `⠀ … ⣿` | high | high | precise, delicate | **sparklines, curves, micro-charts**, drawn figures |
| **safe glyphs** `✓ ✕ ⚠ ~ !` | point | high | valence | a dab of good/bad — accent only |
| **fragile glyphs** `◎ ● → · Δ` | point | low | ornament | sparingly, never at an edge |
| **emoji** `🔥 ✅ 💸` | picto | low³ | warm, casual | register-matched valence (a chat ping, not a board card) |

¹ box-drawing renders 1 cell in every real terminal. ² but `░ ▒ ▓` invert by light/dark theme. ³ ~2 cells, platform-variant render, no copy guarantee — breaks alignment; deploy by deliberate register choice, never reflex.

---

## 0 · The sentence — plain words

The clearest form is often a sentence; a frame around it is theater. The
no-artifact reply is a real ensoul output — usually the most caring one.

```text
  tests green. migration clean. the flaky test is the story.
```

---

## 1 · The trail — a journey down the work

The resonant centerpiece. A bug hunt has dead ends, a catch, a lesson — a
**story**, not a status. **Material:** an open trail (`●──● │`, no right border),
so the `◎ ⚠ ●` glyphs are safe. One beat per stop; air between them.

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

---

## 2 · The card — where the work stands

**Nerve:** the state of a refactor at a glance. **Material:** open frame
(`open_frame()`) — an ASCII label column carries it, glyphs are accent, no right
border to drift. One or two things per line; a blank line for air.

```text
  AUTH REFACTOR
  ─────────────────────────────
   ✓  held    sessions / login / logout
   ◑  now     token refresh
   ~  next    delete old middleware

   ⚠  watch   3 old callers
```

---

## 3 · The curve — a shape you can feel

**Nerve:** watching the suite go green across a refactor is a *feeling*, not a
metric. **Material:** `spark_block()` — wide enough to read. (Braille doubles the
density but turns to noise small; reach for it only with width to spare.)

```text
  tests turning green

  mon  ▁▂▃▂▄▅▇█  fri
       188       241
```

---

## 4 · The hunt, as an image — one wild form (the rare exception)

**Nerve:** the felt shape of the debug — a tangle of dead ends resolving into the
one clean line. Only on the `wild` dial, and only when the facts live elsewhere.
**Material:** procedural block shading (`░ ▒ ▓ █`) — a turbulent waveform whose
amplitude decays left→right, so chaos literally settles into calm. Dense and
exact because it is *generated*, not hand-scattered; a figurative image has no
alignment edge, so it cannot drift.

```text
          ░░
         ░▓▓▒░
        ░▓███▓░    ░▒▒▒░░       ░░░░      ░░░░░░
        ▓█▒▒▓█▓▒▒▒▒▓████▓▒░  ░░▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒
       ▒█░   ▒██████▓▓▓▓██▓▒▒▓▓█████████████████████████████
  ▒   ░█▒     ░▓▓▓▓▒░░░░▒▓████▓▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒
  █▒░░▓▓       ░░░       ░▒▒▒▒░░      ░░░        ░░░░░
  ▒█▓▓█░
   ▓██▒
   ░▒▒
  the tangle on the left · the one clean line on the right
```

## 5 · The plate — a composed wild object with a center

**Nerve:** an ordinary day is not a list; it has a center of gravity. **Material:**
ASCII plate grammar — a contained field, a named center, satellites arranged by
felt relation. This is the useful `wild` move when the input is small but wants
more presence: do not make it a timeline with costume jewelry; compose the actual
forces so the reader can feel what pulls what.

```text
  +-- PLATE / THE DAY HAS A CENTER ----------------------+
  |                                                      |
  |        gym                         call mom          |
  |          \                           /               |
  |           \                         /                |
  |            \      THE REPORT       /                 |
  |             \    +------------+   /                  |
  |              ----| focus now  |----                  |
  |                  +------------+                      |
  |                /                \                    |
  |        lunch with sam        groceries               |
  |             noon             way home                |
  |                                                      |
  |   one center; the rest becomes orbit                 |
  +------------------------------------------------------+
```

## 6 · The mechanism, as geometry — striking but still lossless

**Nerve:** exponential backoff is not "retry a few times"; it is a widening gap.
**Material:** generated block spiral (`exponential_backoff_spiral()`) — the
distance between attempts carries the algorithm, so the beauty is the truth.
This is the golden pair for **striking + faithful**: the picture is memorable
because it is the mechanism, not because it decorates the mechanism.

INPUT
```text
An API call fails. Retry after 1 second, then 2, then 4. Stop when it succeeds,
or give up after the fourth attempt. The important thing is that each wait is
twice the last, so the system gives the dependency more room to recover.
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

---

## Using these

- **A session is a journey** — when there's a sequence (a debug, a PR, a day),
  reach for the trail before a card. It carries story; a card only carries state.
- **Match material to the job:** a state → a card · a magnitude → a bar · a series
  → a sparkline · an ordinary thing with a hidden center → a plate · a felt shape
  → an image · a mechanism → its own geometry. A sentence beats all of them when
  it already says it.
- **Generate, don't hand-type:** call `render.py`. Correct by construction.
- **One or two facts per line.** Density is the enemy of landing.
- **Stop early.** The first honest form that lands wins.
