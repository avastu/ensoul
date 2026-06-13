# ensoul

*ensoul* · verb · to put a soul into.

**for the moment an agent sends you more than your eyes can hold.**

a wall of text states the facts; *ensoul* breathes them into being.

```text
       ▤  ──────────▶  ◎
   a flat wall          a living shape
   your eyes skim       you take in at a glance
```

ensoul is a skill for Codex, Claude, and other agents. point it at a wall of text; it hands back one small visual — a card, a trail, a map — instead of another paragraph.

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

## install

paste this to your agent:

```text
set up the ensoul skill from https://github.com/avastu/ensoul.

then help me configure it:
 • show me something I made recently, rendered three ways
   (plain, balanced, wild) — so I can pick how I like mine
 • ask whether to run when I type /ensoul, or automatically
 • remember my answers
```

it configures by showing, not asking — it renders something you actually made at each setting, and you keep the one that fits. here's the idea on an ordinary day; at install you'd see it on *your* own work:

**the dial** — your day, three ways:

```text
plain — words, a few marks
   today: gym, then the report, lunch with sam, groceries
   on the way home, and call mom tonight.

balanced — the default
   ┌─────── today ────────┐
   │ ✓ gym               │
   │ ◑ the report   (now) │
   │ · lunch with sam     │
   │ · groceries         │
   │ · call mom          │
   └──────────────────────┘

wild — looser, stranger
   morning
      ●  gym
       ╲
        ●  the report
       ╱
      ●  lunch · sam
       ╲
        ●  groceries
       ╱
      ●  call mom
   night
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

every ensoul stands on all three. drop one and it tips: pretty but false, true but unreadable, or true but manipulative.
