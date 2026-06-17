---
name: ensoul
description: |
  For the moment an agent sends a wall of text and your eyes glaze over — /ensoul breathes it into one visual you can take in at a glance.
---

# Ensoul

Create **visual artifacts for felt understanding.**

A model thinks, types, and emits far faster than a person can feel. That gap is the wall — every extra sentence taxes a finite human's attention. Ensoul carries the complexity on the model's side and hands back only what fits in one breath. So compression is not decoration; it is care. **When in doubt, give less.**

## Runtime Contract

- **Default to the smallest artifact that lands** — one move, a few lines, glanceable at once (~3–7 lines). "Small" means few lines and few live relationships, *not* a narrow column; let each line run as wide as it reads best. A bare `/ensoul` takes whatever is in front of it and returns one honest shape; the user specifies nothing.
- **If a plain sentence is clearest, return the sentence.** A box around "the meeting is at 3pm" is theater; the no-artifact reply is legitimate. Too many live threads to hold? Surface the top few and ask what to focus on — don't silently sprawl into a dense map.
- **Lead with the artifact**, fenced. Keep prose short (≤1 paragraph or 3 bullets); put evidence/caveats in a small drawer beneath; explain only non-obvious symbols. It must be legible without the prose tail.
- **dial** — `plain` (words + a few marks) · `balanced` (the small glanceable visual; the default) · `wild` (one striking single-image artifact — commit to a dominant metaphor and render the content *into* it; see Modes). A per-turn request ("go wild," "just words") overrides for that turn.
- **mode** — `on-demand` (`/ensoul`, `$ensoul`) or `standing` (lead with an artifact whenever a reply would otherwise land as a wall).
- **Configure by showing, not asking.** At first run, render one real recent artifact of theirs at all three dials **inline as text** — let them pick by seeing it on their own work, never from words alone, never via a dead interactive picker. Only after they've chosen, record dial + mode to the agent's **global memory so it loads every session** — Claude: `~/.claude/CLAUDE.md`, Codex: `~/.codex/AGENTS.md` — then **verify the file was actually written** (read it back; never just report success). Defaults that aren't truly persisted force a re-ask next session.

## Generation Loop

1. **Find the nerve** — the one comparison, mechanism, state, decision, or feeling to reveal. Can't name it? There's no artifact.
2. **Fit the form to the nerve** — match it via the **Forms** index below, then load that one form. When there's a sequence, prefer the **trail** (it carries story; a card only carries state). Pick the material by register (see Materials).
3. **Make every mark mean** — position, value, texture, enclosure, arrows each carry meaning or get erased. Coding glyphs: `✓` proof · `✕` fail/risk · `!` urgency · `Δ` change · `◆` decision · `?` unknown · `~` unstable · `▲` feature · `◎` behavior at center · `o──o` dependency.
4. **Run the gates** — Truth · Beauty · Goodness · Render. Subtract until all hold.
5. **Ship the smallest version that lands.**

**Concrete Transformation Gate:** show the transformation, not the taxonomy. For first-contact / README / onboarding output, lead with a **before/after** of the user's own material, not a map of the skill's categories. A stranger should answer in seconds: "what did this do to the input?" If the first artifact explains Ensoul more than it transforms the material, revise toward a before/after, state card, or worked example. (Examples live in `references/materials-gallery.md`.)

## The Gates

Every artifact carries three loads at once, equal weight — ace one and fail another and it does not ship. Subtract until all hold. Render is physical correctness, not aesthetics.

```text
  TRUTH     it does not lie. visual weight = real evidence; proof sits by its claim.
  BEAUTY    form and meaning intensify each other; nothing is mere decoration.
  GOODNESS  leaves the person clearer and freer — never manipulated, flattered, or exposed.
```

- **Truth** — name the story (no story = decoration); weight matches evidence (never make weak look central or urgent); show "compared to what?"; keep an evidence drawer near the claims; for charts hold the Tufte spine (lie-factor ≈ 1, real baselines, no chartjunk — `references/tufte-principles.md`). Personal/identity/values mirrors stay `recognition-pending` until the human says it lands — elegance is not evidence.
- **Beauty** — erase any mark, border, or label that loses nothing; check collisions and layering (primary dominates, secondary recedes); aim for a small intake of breath, not a tidy workplace diagram; the form must *intensify* — if styling strips away and the meaning survives, it was decoration.
- **Goodness** — no manipulation (beauty must not smuggle a conclusion past the evidence); hand back power, don't dazzle; no false weather (let calm look calm; mark only what is genuinely at risk); care under load (hold vulnerable material without wounding or exposing); name blind spots (a clean frame implies a completeness it may not have). Refuses both cruelty and flattery.

### Render Gate

**You are typing into a monospace grid you cannot see.** Eyeballing alignment is guessing — almost every broken border and drifted column is born here. Two honest paths:

```text
  LOOK                                USE A FORGIVING FORM
  measure render-cells (not           a left-spine / open frame, no closing
  code-points), or GENERATE it;       right border, ragged-right tail —
  closed ┌─┐ boxes earn this.         cannot drift, costs nothing.
```

- **Measure = render-cells, not `len()`.** Simplest: **call a generator** — `recipes/render.py` (`cells`, `audit`, `open_frame`, `measured_box`, `hbar`, `spark_block`/`spark_braille`). A generated box is correct by construction; a typed one is a guess.
- **Some glyphs are 1-or-2 cells by font** (`◎ ● ○ ★ ◑ → Δ` and the everywhere `·` middle dot) — keep them off a right border or use a forgiving form. `✓ ✕ ⚠ ~ ! ?` and ASCII are reliably one cell, safe at an edge. Shading `░ ▒ ▓ █` inverts by light/dark theme — say which you tuned for. Inside a figurative image (no alignment edge) anything is safe.
- **Let structure carry the meaning; glyphs are accent.** Position, CAPS labels, indentation, and rails encode meaning and cannot drift. If erasing a glyph loses the structure, the structure was too weak — fix that first.

### Surface Gate

The artifact may be read in a terminal, app, GitHub README, Slack, or on a phone. Know the width when you can (`tput cols`, observe the pane); when you can't, default to **~68 cells balanced, ~78 wild**. Don't hard-clamp — use the width the artifact needs, but keep meaning off the wrap cliff. When a line grows long: **spine across, detail down** (fold the qualifier underneath; don't shrink the whole artifact). `surface_width()` / `flow_row()` help.

## Materials

Stop thinking "font," think **paint** — a shelf of materials, each with a grain: type + rails for calm structure; **block shading for magnitude (ink = weight)**; **braille for fine series (a curve in a sentence)**; safe glyphs as accent; emoji warm but fragile. Block-as-magnitude and braille-as-curve are habitually under-used — **generate both with `recipes/render.py`**. Richer material is *earned* by encoding real structure or magnitude, and still faces the three loads; if it strips away and the meaning survives, erase it.

```text
  plain     type · rules · safe glyphs
  balanced  + a sparkline or magnitude bar when there's a series / weight
  wild      full block + braille figuration — draw the thing, fill the frame
```

Full shelf with grain notes + worked examples: `references/materials-gallery.md`.

## Modes

**Wild** (on the `wild` dial, or when asked for wilder / stranger / permission-to-fail): lead with one dominant, unforgettable image and bend the content into it — do **not** fall back to a tidy card/list/timeline. Most wild artifacts fail by being **timid** (a few lines, scattered dots); commit to one material (light, water, mass, growth, circuitry) and **draw the thing**, content rendered *into* its body. Density is allowed. If the subject is data or magnitude, **generate it** — `terrain` (a real series as a landscape; the gold one), `wave`, `orb`, `field` — instead of scattering glyphs. If the felt point is an *act intensifying toward a center* (attention, knowing, presence), reach for `calligram` — a word-field on a semantic gradient where the peak word rings a void (`fig_eye`/`fig_ring`/`fig_spire`, or any `fn`). The three loads still hold. Target: one contained window (~25–45 lines), a clear center, strong marks, room to breathe.

**Symbolic Mirror** (strategy, identity, relationships, values, memory, "what's really going on?"): design as a living network where every symbol maps to a real force, evidence trace, or lived tension — never decorative mysticism. This is where Goodness matters most: include an evidence drawer, hold `recognition-pending`, hold the person with care rather than verdict. When the material is raw, or about another person's hidden intentions, don't arrange unverifiable psychology into a confident shape — default to a plain **known / unknown / next question** frame. Full grammar: `references/editorial-artifact-patterns.md`.

## Lineage

Craft prompts, not style costumes — let them activate operations, don't imitate works: **Tufte** (truth: evidence, integrity) · **Asawa** (line, air, and shadow hold relationships) · **Rubin** (subtract to the one true thing) · **Works in Progress / Stripe Press** (ornament as cognition) · **Psychomagic** (symbols grounded in real forces, to free perception, not cast a spell).

## Forms

The form library — one worked example per form (the nerve, the material, the call).
Two load paths:

- **Install / first run:** read the **whole** library — learn the craft deeply, once.
- **Runtime (`/ensoul`):** load the **one** form the nerve calls for. The index below
  carries the gradient so you pick before you load.

```text
  sequence → trail · state / triage → card · tradeoff → table · several magnitudes → progress ·
  a series → sparkline · a system or pipeline → flow ·
  a day / list orbiting one center → plate (wild) ·
  a felt arc or series-as-landscape → terrain (wild) ·
  a mechanism whose shape IS the logic → its own geometry (wild) ·
  an act intensifying inward, e.g. attention or listening → calligram (wild) ·
  already said → the sentence.
```

Home is small; step out one notch at a time; the wild forms are the rare exception.
Each lives in `forms/<name>.md` (the generator forms carry their own call snippet,
so you needn't read `recipe-api.md` or `render.py` for a single form).

## References

Lazy-load only when the task calls for it:

- `forms/<name>.md` — the **form library** (worked examples). Runtime: load one (see Forms index). Install: read all.
- `references/materials-gallery.md` — **material shelf + craft lineage** (read at install with `forms/`). The per-form worked examples now live in `forms/`.
- `references/tufte-principles.md` · `references/analytical-design.md` — quantitative integrity, sparklines, dashboards, dense displays. (Truth.)
- `references/visual-language-research-communication.md` — diagrams, networks, maps for explaining research, systems, or strategy.
- `references/editorial-artifact-patterns.md` — editorial art direction, ornament-as-information, and the symbolic-mirror grammar. (Beauty.)
- `references/visual-primitives.md` — reusable mark grammar and compositional primitives for inventing a new style.
- `references/calibration-prompts.md` — the resonance gate: first-run prompts, failure modes, and `scripts/e2e`. Load when testing, tuning, or installing.
- `references/recipe-api.md` — the **calling surface** for the generators (signatures + when-to-use). Glance here and run them; **don't read `render.py`** (~4k tok) just to call it — read the source only to change a recipe.
- `recipes/render.py` — generator implementations (alignment, surface attunement, magnitude/series, and wild `terrain`/`wave`/`orb`/`field`/`calligram`). Call via the cheatsheet; don't hand-type. `recipes/test_render.py` covers them (run by `scripts/validate`).

Cross-agent: works in Claude (`/ensoul`) and Codex (`$ensoul`); mirror this folder into each agent's skills directory. This plain folder is the canonical source.
