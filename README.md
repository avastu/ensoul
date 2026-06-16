# ensoul

*ensoul* · verb · to imbue with soul

**for the moment an agent sends you a wall of text and your eyes start to glaze over**

text states the facts; *ensoul* breathes them into being.

```text
   ▤▤▤▤▤▤▤▤▤▤▤▤▤
   ▤▤▤▤▤▤▤▤▤▤▤
   ▤▤▤▤▤▤▤▤▤▤▤▤▤▤    ─────▶      ◎
   ▤▤▤▤▤▤▤▤▤▤▤▤              ╶───┴───╴
   ▤▤▤▤▤▤▤▤▤▤▤
your eyes slide off           it lands
```

ensoul is a skill for Codex, Claude, and other agents. when you see a wall of text, type */ensoul*; it creates a visual you can intuit, rather than another paragraph you have to read

## see it work

you asked for a weekend in Lisbon. the assistant sent back a wall:

```text
before — what the assistant sent
"sure! so for a weekend in Lisbon there's honestly a lot you
 could do. friday evening i'd just get settled — Alfama is a
 lovely old neighborhood, full of character, and there are
 tascas right there for dinner. saturday, start with pastéis
 de nata (the famous egg tarts!), walk up to São Jorge castle
 for the views, then ride tram 28 — touristy but worth it.
 saturday night you have to do fado, the traditional music —
 but book ahead or you won't get in. sunday, Belém for the
 tower and monastery, lunch by the river, then the airport.
 oh, and rain's likely saturday, so bring a layer!"
```

```text
after — /ensoul

   lisbon · a weekend

   fri ──●  arrive · alfama · tasca dinner
         │
   sat ──●  pastéis · são jorge · tram 28
         │   ◎ fado at night — ⚠ book ahead
         │
   sun ──●  belém · tower + monastery → lunch → airport

   ⚠ rain likely saturday · bring a layer
```

or a system you're trying to hold in your head:

```text
before — a spec you keep re-reading
"events enter via the API gateway (auth + rate-limit) onto a Kafka
 topic. consumers dedupe by id against Redis, enrich from the Postgres
 replica, then write to both the timeseries store (dashboards) and S3
 (the lake). failed enrichment goes to a dead-letter topic, retried
 every 15 min. dashboards read recent from timeseries; history older
 than 30 days comes from S3 via Athena. peak ~200k events/min."
```

```text
after — /ensoul

   events · 200k/min
         │
         ▼
   gateway ──▶ kafka ──▶ dedupe ──▶ enrich
   auth+rate      topic     redis     postgres replica
                                 │
               ┌─────────────────┼─────────────────┐
               ▼                 ▼                 ▼
         timeseries          s3 lake          dead-letter
         dashboards          history          retry /15m
         0–30d               >30d

   the fork into two stores · the 30-day hot/cold seam
```

## install

paste this to your agent:

```text
set up the ensoul skill from https://github.com/avastu/ensoul.

then help me configure it:
 • show me something I made recently, rendered three ways
   (plain, balanced, wild) — so I can pick how I like mine
 • ask whether to run when I type /ensoul, or automatically
 • remember my answers globally, so they hold across all my projects
```

it configures by showing, not asking — it renders something you actually made at each setting, and you keep the one that fits. here's the idea on a memory leak; at install you'd see it on *your* own work:

**the dial** — a memory leak, three ways:

```text
plain — words, a few marks
   heap climbs ~180MB/hr ↑ and GC can't reclaim it — pauses stretch
   40→900ms, then OOM-kill at 6.2GB ✗ every ~31h, climbs again ↺

balanced — the default
   HEAP · leaking ~180MB/hr
   ──────────────────────────────────────
    climb  ▁▂▃▄▅▆▇█  0.8 → 6.2 GB
    gc     runs, but the floor keeps rising
    wall   OOM-kill at 6.2 GB · ~every 31h
    cycle  restart → climb → die → repeat

wild — looser, stranger
   HEAP · a slow leak, until it dies

   6.2 ┤┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄✗┄ OOM-kill
       │                                  ▓   ▓▓▓
       │                             ▓   ▓▓  ▓▓▓▓
       │                   ▓   ▓▓  ▓▓▓  ▓▓▓ ▓▓▓▓▓
       │              ▓   ▓▓  ▓▓▓ ▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓
       │        ▓▓  ▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
       │  ▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
       │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   1.0 ┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
       └─────────────────────────────────────────
        0h                                ~31h
   GC keeps cutting it back — never to the floor it began at
```

**the mode** — on demand, type `/ensoul` on whatever's in front of you. on automatic, you do nothing: every wall the agent sends comes back ensouled.

## what it balances

```text
               truth
                 △
                ╱ ╲
               ╱ ◎ ╲
              ╱     ╲
       beauty ─────── goodness
```

every ensoul stands on all three. drop one and it tips: pretty but false, true but unreadable, or true but misleading.
