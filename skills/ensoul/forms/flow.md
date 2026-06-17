# flow — a system you're trying to hold in your head

**Nerve:** a pipeline or architecture — where things enter, branch, and land.
**Material:** rails + arrows (`──▶ │ ┌─┴─┐`), reliably 1 cell, no right border to
drift. Let the **spine run top-to-bottom or left-to-right**; fan out at the branch
points; hang the qualifier (rate, latency, retention) under each node. Don't draw
every box — draw the path. If a row crowds the edge, fold the qualifier downward
(`flow_row()` helps).

INPUT
```text
events come through the API gateway (auth + rate-limit), onto a kafka topic.
consumers dedupe by id against redis, enrich from the postgres replica, write to the
timeseries store (dashboards) and s3 (the lake). failed enrichment goes to a
dead-letter topic, retried every 15 min. dashboards hit the timeseries store; history
beyond 30 days hits s3 via athena. ~200k events/min at peak.
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
