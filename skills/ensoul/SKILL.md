---
name: ensoul
description: |
  Use when complex context, coding work, bug hunts, project state, architecture, strategy, research, reviews, or emotionally loaded material needs a visual artifact instead of a normal summary. Also use when designing or critiquing diagrams, maps, dashboards, reports, visual essays, glyph systems, ASCII/Unicode artifacts, symbolic mirrors, patterned frames, or public-facing explanations. Every artifact balances three loads: truth (it does not lie), beauty (form and meaning intensify each other), and goodness (it leaves the person clearer and more sovereign, never manipulated).
---

# Ensoul

Create visual artifacts for felt understanding.

The lived purpose: a model thinks, types, and emits far faster than a person can feel. That gap is the wall — every extra sentence is a demand on a finite human's attention. Ensoul is how the model carries the complexity on its own side and hands back only what fits in one breath.

So the compression is not decoration. It is care: restraint on the model's side so the person is met, not overwhelmed. Reader-protection against the wall. When in doubt, give less.

Ensoul turns complex work into bounded artifacts where line, silence, symbol, pattern, and evidence let truth become felt before it is fully explained. Use it for research communication, project state, coding transcripts, strategy, architecture, agent behavior, symbolic mirrors, public explainers, ASCII/Unicode artifacts, and visual essays.

## The Three Loads

Every Ensoul artifact carries three loads at once. They are equal weight. An artifact that aces one and fails another does not ship.

```text
  TRUTH     it does not lie. visual weight matches real
            evidence, and proof sits next to its claim.

  BEAUTY    form and meaning intensify each other. nothing
            is decoration; nothing earns its place by being
            pretty alone.

  GOODNESS  it leaves the person clearer and more sovereign —
            never manipulated, flattered, exposed, or rushed
            by how good the picture looks.
```

Truth keeps it honest. Beauty makes it land. Goodness keeps it *for the person* instead of a performance aimed at them. When the three conflict, subtract until all three can hold at once. The gates below are how you check each load.

## Default Register

Default to the **smallest artifact that does the job**: one move, a few lines, glanceable at once — Rubin before cathedral. "Small" is few lines and few live relationships, *not* a narrow column; let each line run as wide as it reads best (see the Render Gate). A bare `/ensoul` takes whatever is in front of it — transcript, diff, decision, conversation — and returns one honest, glanceable shape. The user specifies nothing; that is the whole interface.

Two settings, usually chosen once at install and recorded **globally** in the agent's memory so they hold across projects:

- **dial** — `plain` (words + a few marks) · `balanced` (the small glanceable visual; the default) · `wild` (one striking single-image artifact: commit to a dominant metaphor — a sun, a tide, a creature — and render the content *into* it; enter Wild Permission Mode, and do **not** fall back to a tidy card/list/timeline). A per-invocation request ("go wild," "just words") overrides the dial for that turn.
- **mode** — `on-demand` (invoked explicitly, `/ensoul` or `$ensoul`) or `standing` (the agent leads with an artifact whenever its own reply would otherwise land as a wall).

**Configure by showing, not asking.** At first run, render one real recent artifact of theirs at all three dials (`plain` · `balanced` · `wild`) **inline as text, in your reply** — then let them pick by seeing it on their own work. Never make them choose from words alone, and never defer to an interactive picker or UI affordance: if you cannot display all three rendered artifacts as text, configuration is not done. Record the dial + mode globally only after they have seen the three and chosen.

Range is available **on request** ("more," "bigger," "a plate," "a mirror"); absent that, stay small even when the input is huge — compress to what matters (~3–7 lines). Too many live threads to hold at once? Surface the top few and ask what to focus on; do not silently expand into a dense map. And if a plain sentence is the clearest form, **return the sentence** — a box around "the meeting is at 3pm" is theater. The no-artifact reply is a legitimate output, not a failure to perform.

## Core Lineage

The lineage maps onto the three loads:

- **Tufte** — *truth:* evidence, integrity, comparison, graphical honesty under the beauty.
- **Ruth Asawa** — *beauty through line:* wire-like structure, loop, shadow, transparency, delicacy, spaciousness, and forms that let air participate. Use this region when an artifact needs woven relationships, suspended tension, nested loops, or a light structure whose shadow/negative space carries meaning.
- **Rick Rubin** — *beauty by subtraction:* essence, presence, restraint, silence, and the one true thing. Use this region when the artifact is becoming clever, dense, or performative: remove until the remaining object feels inevitable.
- **Works in Progress / Stripe Press** — *beauty as cognition:* ornament that is information.
- **Psychomagic** — *goodness:* symbols grounded in real forces, costs, and choices, used to free perception, not to cast a spell.

These are lineage prompts, not style costumes. Do not imitate an artist's works or mannerisms. Let the references activate craft operations: Asawa asks "what can line and air hold?"; Rubin asks "what remains if everything nonessential is removed?" Keep the public surface grounded. The deeper charge belongs in the artifact, not in vague mystical claims.

## Concrete Transformation Gate

Default to **show the transformation**, not the taxonomy.

Before making a mythic map, temple, mirror, or editorial plate, identify the smallest concrete input and the useful output it should become. If the audience is new to the project, lead with a before/after artifact unless another form is clearly more useful.

```text
BEFORE
"We fixed the login bug, tests pass locally, prod deploy is still pending."

AFTER ENSOUL
  LOGIN FLOW
  ──────────────────────────────────────────────────
    behavior   ◎  session now persists across refreshes
    old path   ✕  it used to log users out
    patch      Δ  retry the token refresh once
    proof      ✓  regression test passed locally
    open       ~  prod deploy still pending
```

This uses the **forgiving form**: a top rule and a left-aligned ASCII
column carry the structure, and the meaning-glyphs (`◎ ✕ Δ ✓ ~`) sit
*after* it with a ragged-right tail — no right border to drift, so it
holds across fonts with nothing to measure. A closed `┌─┐` box is
equally valid here; it would just earn one measure first (see the
Render Gate).

Use the abstract visual system only after the concrete transformation is visible. A stranger should be able to answer, within a few seconds: "What did this skill do to the input?"

If the first artifact explains Ensoul, the project, or the visual grammar more than it transforms the user's material, revise toward a before/after, state card, bug map, or concrete worked example. (Performing the skill instead of serving the person is a goodness failure — see the Goodness Gate.)

## Show-Not-Tell Preference

When the topic is complex, prefer a compact visual before long prose — "dense" means *perceptually* dense, not word-dense. Prefer one designed object over a long explanation when the object can carry the structure. When the user asks for creativity, make the artifact feel alive, but make every flourish encode meaning.

- Use a diagram or concept map for structure.
- Use a causal or process flow for mechanism.
- Use a timeline for sequence.
- Use a comparison table or small multiples for alternatives, tradeoffs, or variants.
- Use an annotated artifact sketch when a concrete example can carry the explanation.
- Use a glyph legend, ASCII/Unicode map, atlas page, or semiotic key when the subject has recurring forces, organs, gates, risks, or states.
- Use an image-like editorial plate when the response should be felt and remembered, not merely summarized.
- Use visual primitives deliberately: center, threshold, plinth, aperture, spire, band, lattice, procession, orbit, root, scar, gate, vessel, and field.
- Treat borders and frames as semantic surfaces. A rich frame can encode evidence, pressure, lineage, constraints, rhythm, weather, or provenance; it should not be a decorative box.
- For coding collaboration, use intuitive coding primitives: `✓` verified proof, `▤` file/receipt, `✕` failure/risk, `!` urgency, `Δ` change, `◆` design/decision, `?` unknown, `~` unstable, `▲` user-visible feature, `◎` behavior at the center, `o──o` dependency/handoff.

Make the visual do real explanatory work. Add prose to interpret the visual, not to replace it. Before writing paragraphs, ask: "What would the reader understand if they only saw the artifact?"

## Output Contract

When producing an artifact:

1. Lead with the artifact itself, usually in a fenced `text`, `mermaid`, HTML/SVG, image prompt, table, or compact mixed-media layout.
2. For first-contact, README-like, onboarding, or explanatory outputs, prefer a concrete before/after transformation over a map of the skill's categories.
3. Make the artifact legible without the prose tail.
4. Keep interpretation short: one paragraph or 3 bullets unless the user asks for a deeper read.
5. Put evidence, assumptions, or caveats under the artifact as a small drawer, not as the main event.
6. Do not apologize for weirdness. Explain only the symbols that are not self-evident.

If the first draft feels like a paragraph with decorations, revise toward a picture: reduce sentences, increase spatial relationships, labels, contrast, and marks that mean something.

## Truth Gate

Beauty does not exempt the artifact from rigor. Before shipping, check that it does not lie:

1. **Story** — what comparison, mechanism, state, or decision is this meant to reveal? If there is no answer, the artifact is decoration.
2. **Integrity** — does visual weight match actual evidence and importance? Never make weak evidence look central, verified, or urgent.
3. **Comparison** — does the viewer know "compared to what?" Show the alternative, baseline, before/after, or counterfactual when comparison matters.
4. **Evidence** — are receipts, assumptions, scales, sources, tests, and verification levels close to the claims they support? Keep a compact evidence drawer beneath the artifact.
5. **Tufte spine** (for charts and quantitative displays) — lie factor ≈ 1.0, proportional scales, real baselines, no 3D distortion, minimal chartjunk, high data-ink ratio, clear labels, and appropriate small multiples. See `references/tufte-principles.md`.

For personal, strategic, identity, relationship, or values mirrors, label the artifact `recognition-pending` until the human explicitly says it lands. Elegance is not evidence.

## Beauty Gate

Beauty is not styling laid on top of an idea; it is form and meaning intensifying each other. Before shipping, check that the form earns itself:

1. **Eraser** — for every mark, word, border, glyph, label, tick, line, ornament, or annotation: can it be erased without losing information or felt structure? If yes, erase it.
2. **Collision** — mentally box every text label and dense mark cluster. Does another label, line, border, or symbol cross or crowd it? Move, lighten, separate, or remove.
3. **Layering** — does primary meaning dominate while secondary structure recedes? Borders and ornament should support the center, not fight it.
4. **Wonder** — is there a small intake of breath, surprise, or curiosity, or does it read like a tidy workplace diagram?
5. **Presence** — does it feel attended to, specific, and awake, rather than generated or generically ornamental?
6. **Intensification** — would the idea be weaker without this form? If the styling could be stripped and the meaning survive unchanged, the beauty is decoration. Make the beauty carry the mechanism.

To push beauty further when the user invites it, see Wild Permission Mode and the Works in Progress / Stripe Press inspiration below.

## Goodness Gate

Truth and beauty can both be present and the artifact can still harm: a gorgeous, accurate picture that quietly manipulates, flatters, exposes, or leaves the person dependent on its spell. Goodness is the load that keeps the artifact in service of the person's own seeing and freedom. Before shipping, check that it is *for them*:

1. **Non-manipulation** — beauty must never smuggle a conclusion past the evidence. If the composition makes the viewer *feel* that something is proven, urgent, or settled when the evidence does not support it, it is lying with style. Lower the visual weight to match the truth.
2. **Sovereignty** — does the artifact leave the person more able to see, decide, and act on their own, or more dependent on the maker's cleverness? Aim to hand back power, not to dazzle.
3. **No false weather** — do not manufacture urgency, certainty, doom, or hype through visual force. Let what is calm look calm; mark only what is genuinely at risk.
4. **Care under load** — for emotionally loaded, vulnerable, or cruelty-prone material (a person's failures, a relationship, someone's life), hold it without wounding or exposing. Reduce confusion and cruelty. A mirror should let someone meet themselves, not flinch from a verdict.
5. **Honest blind spots** — name what the artifact cannot see. A clean frame implies completeness; say what was excluded, assumed, or unknown so the tidiness is not itself a lie.
6. **Recognition over seduction** — for anything that mirrors a person's values, life, or direction, the goal is "yes, that is the pattern," not "wow." Hold `recognition-pending` until they say it lands; never self-certify that it landed.

Goodness is not softness. It can mean showing a hard truth plainly. It refuses two opposite failures: **cruelty** (wounding without care) and **flattery** (comfort that hides consequence).

## Render Gate

The three loads judge the artifact's *meaning*. This gate is about one fact you cannot escape: **when you generate an artifact, you are typing characters into a monospace grid you cannot see.** You never perceive the rendered result — you infer columns from memory. Eyeballing alignment is not seeing; it is guessing, and almost every broken border, drifted column, and cramped width is born here.

So there are exactly two honest ways to be aligned:

```text
   LOOK                              USE A FORGIVING FORM
   ────                              ────────────────────
   measure or render before you      one that cannot drift —
   show it: count the column of      a left-spine or open frame
   each aligned mark, confirm        (no closing right border),
   they match. closed boxes and      a ragged-right tail.
   column grids earn this.           costs nothing; no check.
```

Pick per artifact. Both are good: a closed `┌─┐` box carries real meaning (containment, a held space) and is first-class — it just pays for it with one measure. A forgiving form is free. The only wrong move is shipping an ambitious aligned form you never looked at.

**"Measure" means render-cells, not code-points.** A naive `len()` count is itself a form of eyeballing: it says `·` and `✓` are one character each, but the *terminal* may render them as two cells, and the border drifts anyway. Either count true display width, or — far simpler — **call a generator instead of hand-typing.** `recipes/render.py` ships `cells()`, `audit()` (flags ambiguous glyphs that would drift a border), `open_frame()`, `measured_box()`, `hbar()`, and `spark_block`/`spark_braille`. A box you generate is correct by construction; a box you type is a guess.

Three corollaries fall out of being blind:

- **Width is a choice, not a reflex.** "Small" means few lines and few live relationships — *not* a narrow column. Narrow only *feels* safe because there is less room to misalign. Let each line run as wide as its content reads best, then stop. (Real tension: very wide artifacts wrap or sideways-scroll on a phone — choose width for where it will be read.)
- **Some glyphs are 1-or-2 cells by font** (`◎ ● ○ ★ ◑ ☉ → Δ` and the sneaky everywhere-in-this-style `·` middle dot), so they can shove a *right border* off across fonts; `✓ ✕ ⚠ ~ ! ?` and ASCII are reliably one cell and safe at an edge. (Shading `░ ▒ ▓ █` also flips by theme: glow on dark, solid mass on light.) When unsure, keep these off the right edge or use a forgiving form — inside a figurative image with no alignment edge, they are perfectly safe.
- **Let structure carry the meaning; glyphs are accent.** Position, grouping, CAPS labels, indentation, and box-drawing rails encode meaning *and cannot drift and need no legend* — make them load-bearing. A glyph is a dab of valence (`✓` good / `✕` bad) the eye reads pre-verbally, not the thing holding the artifact up. If erasing the glyph loses the structure, the structure was too weak; fix that first.

A bare `/ensoul` clears this on its own first pass — alignment and width are generation-time craft, not afterthoughts. The `artifact-review` skill is the deeper adversarial render pass (multi-model, cross-platform) for ship-polish; ensoul should not *depend* on it to come out aligned.

## Surface Gate

The artifact may be read in a terminal, Codex app, Claude app, GitHub README, Slack, or mobile browser. Attune to the actual surface when you can; when you cannot, use portable defaults.

```text
  IF WIDTH IS KNOWABLE              IF WIDTH IS UNKNOWN
  ────────────────────              ───────────────────
  use it, with breathing room        use a sensible default
  terminal: `tput cols`              balanced: ~68 cells
  rendered pane: observe it          wild: ~78 cells if earned
  screenshot/browser: look           closed box: narrower or generated
```

Do not make this a hard global clamp. Use the width the artifact needs, but pay for it: know the surface when possible, measure display cells, and keep important meaning away from the wrap cliff. Even when a line technically fits, fold secondary detail if it lands inside the breathing-room margin.

When a line grows long, preserve the spine and fold secondary detail downward:

```text
  risky
  ├─ hot history      Timeseries store ──▶ dashboards [0-30d]

  safer
  ├─ hot history      Timeseries store ──▶ dashboards
                       0-30d
```

The rule is **spine across, detail down**. Do not shrink the whole artifact just to save a qualifier at the edge. Use `recipes/render.py`'s `surface_width()` and `flow_row()` when rendering flow rows under uncertain surfaces.

## Materials

Stop thinking "font," start thinking **paint.** The medium is a shelf of materials, each with a different grain — resolution, how fast meaning lands, whether it survives fonts/copy, what *register* it carries. Leveraging it fully is not *more marks* — it is the right material at the right register: type and rails for calm structure; block shading for weight and mass (**magnitude as ink**); braille for fine series (**a curve in a sentence**); safe glyphs (`✓ ✕ ⚠ ~ !`) as accent; emoji warm but fragile. Block-as-magnitude and braille-as-curve are the two habitually under-used; **generate both with `recipes/render.py`** rather than hand-typing.

**The discipline that keeps this from chartjunk:** richer material is *earned* by encoding real structure or magnitude, and still faces the three loads — shading must mean weight, a sparkline must be real data, emoji must fit the room. If it can be stripped and the meaning survives, erase it.

```text
   plain      type · rules · safe glyphs
   balanced   + a sparkline or magnitude bar when there's a series / weight
   wild       full block + braille figuration — draw the thing, fill the frame
```

The full material shelf with grain notes, plus worked examples, lives in `references/materials-gallery.md`; the generators in `recipes/render.py` — call them, don't hand-type.

## Wild Permission Mode

When the user asks for weirder, wilder, Rubin-like, jazz-like, appalling, or permission-to-fail work — **or whenever the dial is `wild`** — loosen the politeness and make a stranger object. On `wild` this is the job, not optional. Lead with one dominant, unforgettable image and bend the content into it.

- privilege surprise, rhythm, silence, repetition, knots, and sculptural line; make ASCII/Unicode feel like wire, score, ritual diagram, or found inscription;
- let it risk being ugly, excessive, asymmetrical, haunted, funny, or wrong;
- keep a hidden skeleton of integrity: symbols still mean something, the artifact still reveals real structure.

**Most wild artifacts fail by being timid** — a few lines and scattered dots. Use the full palette (see Materials): commit to one material — light, water, mass, growth, circuitry, or plate — and **draw the thing**, rendering content *into* its body, not beside it. Density is allowed and often better than space; negative space is a tool, not a rule. If the subject has a hidden center or symbolic tension, an editorial plate can be the right wild form: a contained field, named center, satellites, pressure lines, and one sentence that says what the composition revealed. If the subject is data, motion, or magnitude, dense exact beauty should be **generated, not hand-typed**: reach for `recipes/render.py`'s `terrain` (a real series as a landscape), `wave`, `orb`, and `field` — fed real data — instead of scattering glyphs. `terrain` is the gold one: a wild image that is also a truthful chart.

The three loads still hold: even wild must not lie, must intensify rather than decorate, and must not wound the person it is for. Failure is allowed if it teaches taste.

Target shape: one contained window (usually 25–45 lines), a clear boundary or center, one strange focal object, fewer labels and stronger marks, enough air for the eye to move without becoming a pause button.

## Symbolic Mirror Mode

Use this mode when the ask touches strategy, identity, creative direction, agent behavior, relationships, memory, values, or "what is really going on?"

Design the artifact like a living network:
- **Hyphae:** subtle links, dependencies, traces, affordances, and latent paths.
- **Nodes:** people, ideas, commitments, organs, risks, memories, offers, proofs, and artifacts.
- **Nutrients:** attention, trust, money, evidence, energy, beauty, legitimacy, time.
- **Fruiting bodies:** visible outputs: pages, products, decisions, offers, essays, rituals, releases.
- **Rot:** stale beliefs, dead projects, debt, shame loops, hidden bottlenecks, uninspected costs.
- **Symbiosis:** mutual benefit, shared context, handoffs, alliances, honest reciprocity.

Psychomagic does not mean vague mysticism. It means the image changes what can be perceived and therefore what can be acted on. Keep it grounded: every symbol should correspond to a real force, evidence trace, decision, or lived tension.

Symbolic mirrors are where the Goodness Gate matters most. The material is loaded and the person is exposed in their own reflection. Do not claim the artifact is true because it is elegant. Include a compact evidence drawer with the observed prompt/context signals, hold the result as `recognition-pending`, and hold the person with care rather than verdict.

When the input is emotionally raw, or about another person's hidden intentions, do not arrange unverifiable psychology into a confident shape — a `recognition-pending` label does not redeem an artifact that still overclaims what cannot be known. Default instead to a plain **known / unknown / next question** frame: what the evidence actually shows, what it cannot, and the next thing to check. Earn the fuller mirror only when there is real signal to ground it.

## Works in Progress / Stripe Press Inspiration

Take visual inspiration from Works in Progress and Stripe Press without copying their house style. The useful principles are:

- **Ornament as cognition:** an image, texture, etching, glyph, or historical fragment can be information, not decoration.
- **Topic-specific worlds:** each idea deserves its own visual atmosphere so it can be remembered as itself.
- **Beauty invites difficulty:** a beautiful artifact can ask the reader to lean in, puzzle, and reread.
- **Historical freshness:** old diagrams, engravings, ledgers, type specimens, maps, and marginalia can feel new when recontextualized truthfully.
- **Easter eggs with purpose:** strange details are allowed when they encode the subject's mechanism or leak meaning across the composition.
- **Public progress lens:** make underrated ideas legible, vivid, and socially consequential.

When this influence matters, read `references/editorial-artifact-patterns.md`.

## Workflow

One loop, whatever the artifact:

1. **Find the nerve** — the single comparison, mechanism, state, decision, or feeling this must reveal. If you can't name it, there's no artifact.
2. **Choose the form to fit the nerve** — a session/journey (a debug, a PR, a day) → trail; structure → map/table; mechanism → flow; tradeoff → 2×2 or decision table; magnitude → bar; series → sparkline; lived meaning → mirror. Pick the material by register (see Materials). When there's a sequence, prefer the trail — it carries story, where a card only carries state.
3. **Make every mark mean** — position, value, texture, enclosure, arrows each carry meaning or get erased. Keep a visible spine: input → transform → output.
4. **Run the gates** — Truth, Beauty, Goodness, then Render. Subtract until all hold.
5. **Ship the smallest version that lands.** When in doubt, give less.

Critiquing a visualization is the same gates in reverse: check integrity (lie factor, baselines, no 3D distortion), erase chartjunk, ask whom the display serves, then give specific before/after fixes. For quantitative displays, apply the Tufte spine in detail (`references/tufte-principles.md`).

## Key Principles Reference

- `references/tufte-principles.md` — core principles from *Visual Display of Quantitative Information*: lie factor, data-ink, chartjunk, small multiples, integrity. (Truth.)
- `references/analytical-design.md` — extensions from *Envisioning Information*, *Visual Explanations*, and *Beautiful Evidence*: the 6 principles of analytical design, sparklines, layering & separation, micro/macro, range-frames, causality, confections. Load when designing dashboards, dense displays, sparklines, or explanatory graphics.
- `references/visual-language-research-communication.md` — graphic-language and research-communication patterns inspired by semiology of graphics, diagrams, networks, maps, visual variables, evidence confections, and public technical storytelling. Load when explaining research, systems, strategy, architecture, agent behavior, or complex ideas to humans.
- `references/editorial-artifact-patterns.md` — WIP/Stripe Press-inspired editorial art direction, ornament-as-information, and grounded symbolic artifact patterns. Load when the user asks for magic, artifacts, mycelial networks, publication-quality visuals, or public-facing explainers. (Beauty.)
- `references/visual-primitives.md` — reusable mark grammar and compositional primitives inspired by temple architecture, editorial plates, ASCII art, living systems, and coding collaboration. Load when inventing a new artifact style, making a glyph system, tuning visual language, or summarizing coding/project state.
- `references/materials-gallery.md` — golden input→ensoul pairs plus seven verified worked examples on real technical artifacts (a sentence, a debugging trail, a state card, a block sparkline, a wild plate, and two wild images), smallest first, each breathing and showing the generative move. A coding session is a journey — the trail is the resonant default. Load when choosing a material or learning a form by imitation. (Beauty + Truth.)
- `recipes/render.py` — runnable generators that produce aligned artifacts by construction: alignment (`cells`, `audit`, `open_frame`, `measured_box`), surface attunement (`surface_width`, `flow_row`), magnitude/series (`hbar`, `spark_block`, `spark_braille`), and procedural beauty for the wild dial (`terrain`, `wave`, `orb`, `field`). Call these instead of hand-typing fragile glyphs, padding, or art. `recipes/test_render.py` unit-tests them all (run by `scripts/validate`).
- `references/calibration-prompts.md` — first-run prompts, failure modes, and self-evaluation patterns. Load when testing, tuning, installing, or validating the skill.

## Cross-Agent Use

This skill is intentionally compatible with Codex and Claude Code skill formats: a folder with `SKILL.md` plus optional `references/` and `assets/`. To keep both agents aligned, update the source skill and mirror the whole folder into Claude's personal skills directory at `~/.claude/skills/ensoul/`. In Claude Code, the command name comes from the directory, so invoke it as `/ensoul`; in Codex the trigger is `$ensoul`.

This plain skill folder is the canonical source.
