# trail — a journey down the work

The resonant centerpiece. A sequence — a bug hunt, a PR, a day — has dead ends, a
catch, a lesson: a **story**, not a status. When there's a sequence, reach for the
trail before a card; a card only carries state. **Material:** an open trail
(`●──● │`, no right border) so `◎ ⚠ ●` glyphs are safe. One beat per stop; air
between them. Lesson at the foot, where the eye lands last.

INPUT
```text
spent the morning on intermittent 504s. assumed the load balancer timeout since
they started when we bumped traffic — tuned nginx an hour, no change. thought it
was the DB pool exhausting, added logging, pool was fine (12 of 20). around 11 i
noticed the 504s tracked the nightly analytics job, not traffic — it locks the
events table ~30s and checkout reads it live. cached the read, gone. lesson: i
anchored on the traffic theory for way too long.
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
