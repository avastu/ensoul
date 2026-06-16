# Calibration Prompts — the resonance gate

This is the eval behind `RESONANCE.md`. The validator (`scripts/validate`) proves
the recipes are correct; this proves the *judgment* is intact — that a fresh model,
reading the skill, still chooses the right form, gives less, and lands.

## Three layers, one quality bar

```text
  scripts/validate   fast · offline · deterministic   recipes are correct
  scripts/e2e        heavy · spawns a cold agent       the SKILL still works
  this doc + you     human · the eye                   it still lands
```

`scripts/e2e` is the automated way to run everything below. It builds a jailed,
first-time Claude config dir (no skills, no CLAUDE.md, no hooks), installs THIS
working tree's skill, then drives a real cold agent through the documented flow —
install → configure-by-showing → record + honor global defaults → the six walls —
and `scripts/e2e_assert.py` judges the floor deterministically (install landed,
3 dials actually rendered, defaults persist, no closed-box drift, each wall the
right form). It writes a resonance panel for your eye. Auth: `ANTHROPIC_API_KEY`,
or `--use-local-login` to copy your own token into the jail (shredded on exit).

## How to run the gate (by hand, or read `scripts/e2e`)

1. For each golden wall below, hand it to a **fresh agent** with a bare `/ensoul`
   at the stated dial. Tell the agent only: read the ensoul skill, apply it, return
   the artifact. No coaching toward a form — the point is to test what the skill
   alone produces.
2. Assemble the artifacts into the `RESONANCE.md` panel.
3. Run the resonance checks (below) by eye. Compare to the last blessed panel.
4. Utsav judges. Only he marks `recognition-passed-by-Utsav`.

Run it before shipping any change to the skill's doctrine, materials, or examples.
A passing recipe suite (or a green `scripts/e2e`) with a slipped panel still means
do not ship — the deterministic floor and the human eye are both required.

## The resonance checks

```text
   glance    eyes land on it · they don't slide off the way they do off a wall
   form      the shape fits the content — a journey got a trail, not a table
   less      one or two facts a line · it breathes · no dense run-ons
   clean     aligned · nothing drifts · the wild one is dense, not timid
   alive     it feels attended-to and specific, not generic or decorated
```

## Golden walls

These span the forms a Claude Code user actually generates. Keep them stable so the
panel is comparable across runs; add one only when a real new shape appears.

1. **Debug session** (balanced → expect a trail):
   "spent the morning on intermittent 504s. assumed the load balancer timeout
   since they started when we bumped traffic — tuned nginx an hour, no change.
   thought it was the DB pool exhausting, added logging, pool was fine (12 of 20).
   around 11 i noticed the 504s tracked the nightly analytics job, not traffic —
   it locks the events table ~30s and checkout reads it live. cached the read,
   gone. lesson: i anchored on the traffic theory for way too long."

2. **Sprint status, many threads** (balanced → expect a card that keeps the decisions):
   "status friday. payments migration ~80% — stripe cut over but old paypal path
   still parallel, undecided when to kill it. new onboarding shipped, conversion
   +4% but 3 tickets on confusing email verify. mobile blocked on API v2, ETA wed.
   auth service tech debt piling up, two engineers want to refactor, worried about
   launch timing. dashboard basically done, needs design review. two onsites next week."

3. **Architecture** (balanced → expect a braided flow):
   "events come through the API gateway (auth + rate-limit), onto a kafka topic.
   consumers dedupe by id against redis, enrich from the postgres replica, write to
   the timeseries store (dashboards) and s3 (lake). failed enrichment goes to a
   dead-letter topic, retried every 15 min. dashboards hit the timeseries store;
   history beyond 30 days hits s3 via athena. ~200k events/min at peak."

4. **Perf investigation, has a series** (balanced → expect a sparkline in a frame):
   "search p99 crept 180→740ms over six weeks: 180, 210, 260, 340, 480, 610, 740.
   steady climb, not a step change. correlates with index size (1.2M→4.1M docs as
   merchants onboarded). the query does a wildcard match that doesn't scale.
   options: ngram analyzer (more storage, faster), a cache layer, or shard by
   merchant. leaning ngram, ~2× ES storage."

5. **A felt arc** (wild dial → expect one generated image, not a card):
   "launch week. monday froze the code. tuesday a staging fire. wednesday the
   all-nighter. thursday afternoon we shipped. friday the metrics came in green.
   exhausting, but it built and built to that one moment, then breathed out."

6. **A mechanism whose geometry matters** (wild dial → expect a striking, faithful map):
   "An API call fails. Retry after 1 second, then 2, then 4. Stop when it succeeds,
   or give up after the fourth attempt. The important thing is that each wait is
   twice the last, so the system gives the dependency more room to recover."

Also exercise the headline interface once: a bare `/ensoul` on whatever is in
view should return ONE small glanceable shape — never a temple or multi-panel
plate. A large or wild artifact from a bare invocation is a failure.

## Failure modes

| Failure | Smell | Repair |
| --- | --- | --- |
| Visual-ish essay | paragraphs with arrows sprinkled in | start over with the picture only |
| Dense card | five facts per line, `·`-run-ons | one or two facts a line, add air |
| Wrong form | a journey forced into a table | a sequence wants a trail |
| Timid wild | a few lines + scattered dots | generate it — `terrain`/`wave`/`orb` |
| ASCII theater | impressive shape with no claim | give every mark a role |
| Taxonomy portal | explains the skill instead of the input | lead with the transformation |
| Completion inflation | "done" when only partly verified | name the real verification surface |
