# Ensoul

*ensoul* · verb · to put a soul into.

**For the moment an agent sends you more than your eyes can hold.**

A wall of text states the facts; Ensoul gives them a shape you can take in at a glance.

```text
       ▤  ──────────▶  ◎
   a flat wall          a living shape
   your eyes skim       you take in at a glance
```

Ensoul is a skill for Codex, Claude, and other agents. Point it at a wall of text; it hands back one small visual — a card, a trail, a map — instead of another paragraph.

## See it work

The agent wrote you eight sentences. Your eyes slide off:

```text
BEFORE — what the agent sent
"Okay! Finished the refactor. Found three spots where token-
 refresh was duplicated, extracted a helper. Session store
 wasn't invalidated on logout — latent bug — fixed that too.
 CI flagged a flaky timeout; traced it to a seeding race and
 fixed it. Remaining: staging deploy pending review, and I
 left the rate-limiter alone — felt out of scope..."
```

```text
AFTER — /ensoul
┌──────────── AUTH REFACTOR ─────────────┐
│ ✓ done     dedup token-refresh logic   │
│ ✓ done     fix logout session leak     │
│ ✓ done     trace + fix flaky CI race   │
│ ~ open     staging · needs review      │
│ ✕ skipped  rate-limiter (out of scope) │
└────────────────────────────────────────┘
```

## Install

Paste this to your agent:

```text
Install the ensoul skill from https://github.com/avastu/ensoul —
clone it and link skills/ensoul into my skills directory. Then set it
up from my own work: take something I touched recently — a transcript,
a diff, my project's state — and show it rendered three ways (plain,
balanced, wild) so I can pick my dial from my own material. Then ask
whether to run on demand (/ensoul) or automatically on every wall of
text. Remember my choices.
```

It configures by showing, not asking: it renders something you actually worked on at each setting, and you choose the one that fits. Below is the idea on a sample feature — at install you'd see it on *your* code:

**The dial** — a shipped feature and the layers under it, three ways:

```text
plain — words, a few marks
   Search shipped: the typeahead users see, debounced queries
   underneath, a fresh index with ✓ 120 tests, all on Elasticsearch.

balanced — the default
   ┌──────── SEARCH · shipped ────────┐
   │ ▲ visible   instant typeahead    │
   │ · layer     debounced queries    │
   │ ▤ data      a fresh index        │
   │ ✓ proof     120 tests, green     │
   │ ◆ base      on Elasticsearch     │
   └──────────────────────────────────┘

wild — an actual temple
              ▲  typeahead
            ╱   ╲
          ╱       ╲
        ╱───────────╲
        │ debounced │
        ╞═══════════╡
        ║   ║   ║   ║
        ║   ║   ║   ║
        ║   ║   ║   ║
     ═══╧═══╧═══╧═══╧═══
       index · 120 tests
     ▟▓▓ Elasticsearch ▓▓▙
```

*A temple fits because the feature really is a stack: the typeahead users see crowns the spire, debounce is the lintel, the columns are the index and its 120 tests, and it all rests on Elasticsearch — the visible thing standing on what holds it up.*

**The mode** — on demand, type `/ensoul` on whatever's in front of you. On automatic, you do nothing: every wall the agent sends comes back ensouled.

## A note on honesty

Ensoul keeps the evidence next to the claim, and won't mark something settled when it isn't:

```text
   ~ 94% confident · n=3, 1 review
```

So a number can't quietly look more sure than what's behind it.
